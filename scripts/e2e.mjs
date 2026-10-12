// End-to-end contract tests for every unit's activities (HubESOL checklist T-01..T-14 + C-xx that can be automated).
// Usage: npm run build && npm run e2e [-- slug1 slug2]    (env CHROMIUM_PATH to use a pre-installed Chromium)
// Each activity is played from its own JSON (so correct answers are known) and must satisfy the component contract:
//   - no console/page errors
//   - empty Check warns and does not advance
//   - final screen: verdict text, focus on "Play again", review rows show what the learner answered ("You wrote")
//   - restart: activity title visible below the sticky header, keyboard focus inside the activity
//   - Beat the clock: first option focused on every new question
import { chromium } from 'playwright';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve('dist');
const PRACTICE = path.resolve('src/data/practice');
const QUIZ = path.resolve('src/data/quizzes');
const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.pdf': 'application/pdf' };

const server = http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]);
  let f = path.join(ROOT, p);
  if (fs.existsSync(f) && fs.statSync(f).isDirectory()) f = path.join(f, 'index.html');
  if (!fs.existsSync(f)) { res.writeHead(404); res.end('nf'); return; }
  res.writeHead(200, { 'content-type': MIME[path.extname(f)] || 'application/octet-stream' });
  fs.createReadStream(f).pipe(res);
});
await new Promise((r) => server.listen(0, r));
const BASE = `http://localhost:${server.address().port}`;

const args = process.argv.slice(2).filter((a) => !a.startsWith('-'));
const slugs = (args.length ? args : fs.readdirSync(PRACTICE).filter((f) => f.endsWith('-practice.json')).map((f) => f.replace('-practice.json', '')))
  .filter((s) => fs.existsSync(path.join(ROOT, 'grammar/verb-tenses', s, 'index.html')));

const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const failures = [];
let checks = 0;
const norm = (s) => String(s).replace(/[’‘]/g, "'").replace(/[.,?!;:]+$/g, '').trim().toLowerCase();
const VERDICT = /perfect|strong|solid|well done|keep practising|good|great|nice|result|grasp|review|found|mistake/i;

for (const slug of slugs) {
  const D = JSON.parse(fs.readFileSync(path.join(PRACTICE, `${slug}-practice.json`), 'utf8'));
  const page = await browser.newPage({ viewport: { width: 1000, height: 800 } });
  const errs = [];
  const fail = (act, msg) => failures.push(`${slug} · ${act}: ${msg}`);
  const ok = (cond, act, msg) => { checks++; if (!cond) fail(act, msg); return cond; };
  page.on('pageerror', (e) => errs.push(String(e)));
  page.on('console', (m) => { if (m.type() === 'error' && !/fonts\.g|ERR_TUNNEL|ERR_NAME|ERR_INTERNET|Failed to load resource/.test(m.text())) errs.push(m.text()); });
  await page.goto(`${BASE}/grammar/verb-tenses/${slug}/`);
  await page.waitForLoadState('networkidle');

  const clickText = async (scope, text) => {
    const btns = page.locator(`${scope}:visible`);
    const n = await btns.count();
    for (let i = 0; i < n; i++) {
      const b = btns.nth(i);
      if (!(await b.isEnabled())) continue;
      if (norm(await b.innerText()) === norm(text)) { await b.click(); return true; }
    }
    return false;
  };

  const restartContract = async (act, id, sectionSel) => {
    await page.locator(`#${id}-restartBtn`).click();
    await page.waitForTimeout(1200); // html { scroll-behavior: smooth }
    const top = await page.evaluate((s) => document.querySelector(s).getBoundingClientRect().top, sectionSel);
    ok(top >= 0 && top < 300, act, `after restart the title is not visible (section top = ${Math.round(top)}px)`);
    const inside = await page.evaluate((s) => document.querySelector(s).contains(document.activeElement) && document.activeElement !== document.body, sectionSel);
    ok(inside, act, 'after restart keyboard focus is not inside the activity');
  };
  const finalContract = async (act, id, { review = true, wrote = true } = {}) => {
    const label = await page.locator(`#${id}-finalLabel`).innerText();
    ok(VERDICT.test(label), act, `final screen has no verdict text ("${label}")`);
    const focused = await page.evaluate((i) => document.activeElement && document.activeElement.id === i + '-restartBtn', id);
    ok(focused, act, 'final screen: focus is not on "Play again"');
    if (review) {
      const txt = await page.locator(`#${id}-reviewList`).innerText();
      ok(txt.trim().length > 20, act, 'review list is empty');
      if (wrote) ok(/You wrote|You tapped|Your answer/i.test(txt), act, 'review does not show what the learner answered');
    }
  };

  // ---------- Fill in the gaps
  if (D.gapFill && await page.locator('#gf').count()) {
    const A = 'Fill in the gaps';
    try {
      await page.locator('#gf-blankInput').fill('');
      await page.click('#gf-checkBtn');
      const before = await page.locator('#gf-progressText').innerText();
      ok(/answer|type|write/i.test(await page.locator('#gf-feedback').innerText()), A, 'empty Check shows no warning');
      ok(before === await page.locator('#gf-progressText').innerText(), A, 'empty Check advanced/counted as an answer');
      for (const q of D.gapFill.questions) {
        await page.locator('#gf-blankInput').fill(q.display);
        await page.click('#gf-checkBtn');
        await page.click('#gf-nextBtn');
      }
      ok((await page.locator('#gf-finalScore').innerText()).startsWith(`${D.gapFill.questions.length}/`), A, 'typing every canonical answer did not score full marks');
      await finalContract(A, 'gf');
      await restartContract(A, 'gf', '#gf');
    } catch (e) { fail(A, 'crashed: ' + e.message.split('\n')[0]); }
  }

  // ---------- Put it in order
  if (D.wordOrder && await page.locator('#wo').count()) {
    const A = 'Put it in order';
    try {
      const S = D.wordOrder.sentences;
      for (let k = 0; k < S.length; k++) {
        const seq = (k === 0 && S[k].alts && S[k].alts[0]) || S[k].tokens; // first item via the alternative order (commas)
        for (const w of seq) {
          const done = await clickText('#wo-trayZone button', w);
          if (!done) { fail(A, `item ${k + 1}: tile "${w}" not found`); break; }
        }
        await page.click('#wo-checkBtn');
        await page.click('#wo-nextBtn');
      }
      ok((await page.locator('#wo-finalScore').innerText()).startsWith(`${S.length}/`), A, 'canonical/alternative orders were not all accepted');
      await finalContract(A, 'wo', { wrote: false });
      const txt = await page.locator('#wo-reviewList').innerText();
      ok(/,/.test(txt) || !(S[0].alts || []).some((a) => a.some((w) => /,$/.test(w))), A, 'accepted order with a comma is shown without the comma');
      await restartContract(A, 'wo', '#wo');
    } catch (e) { fail(A, 'crashed: ' + e.message.split('\n')[0]); }
  }

  // ---------- Matching
  if (D.matching && await page.locator('#mt').count()) {
    const A = 'Match the -ing form';
    try {
      // wrong pair first: must not break the board
      const P = D.matching.pairs;
      for (const p of P) {
        const okL = await clickText('#mt-leftCol button:not(.matched)', p.left);
        const okR = await clickText('#mt-rightCol button:not(.matched)', p.right);
        if (!okL || !okR) { fail(A, `pair "${p.left}" → "${p.right}" could not be clicked`); break; }
      }
      await page.waitForTimeout(900);
      ok(await page.locator('#mt-scoreScreen.show').count() === 1, A, 'board does not finish after all correct pairs');
      const focused = await page.evaluate(() => document.activeElement && document.activeElement.id === 'mt-restartBtn');
      ok(focused, A, 'final screen: focus is not on "Play again"');
      ok((await page.locator('#mt-reviewList').innerText()).trim().length > 20, A, 'review list is empty');
      await restartContract(A, 'mt', '#mt');
    } catch (e) { fail(A, 'crashed: ' + e.message.split('\n')[0]); }
  }

  // ---------- Beat the clock
  if (D.timedMC && await page.locator('#tm').count()) {
    const A = 'Beat the clock';
    try {
      await page.click('#tm-startBtn');
      const Q = D.timedMC.questions;
      for (let k = 0; k < Q.length; k++) {
        const hasFocus = await page.evaluate(() => document.activeElement && document.activeElement.classList.contains('timedmc-opt'));
        ok(hasFocus, A, `question ${k + 1}: no option focused (keyboard)`);
        if (!(await clickText('#tm-optionsList button', Q[k].choices[Q[k].correct]))) { fail(A, `question ${k + 1}: correct option not found`); break; }
        await page.click('#tm-nextBtn');
      }
      await finalContract(A, 'tm', { wrote: false });
      await restartContract(A, 'tm', '#tm');
    } catch (e) { fail(A, 'crashed: ' + e.message.split('\n')[0]); }
  }

  // ---------- Find the mistake
  if (D.errorCorrection && await page.locator('#ec').count()) {
    const A = 'Find the mistake';
    try {
      for (const it of D.errorCorrection.items) {
        await page.locator('#ec-sentenceZone .errorcorrection-word').nth(it.errorIndex).click();
        await page.click('#ec-nextBtn');
      }
      await finalContract(A, 'ec', { wrote: false });
      await restartContract(A, 'ec', '#ec');
    } catch (e) { fail(A, 'crashed: ' + e.message.split('\n')[0]); }
  }

  // ---------- Level check
  if (D.levelCheck && await page.locator('#lc').count()) {
    const A = 'Level check';
    try {
      const items = D.levelCheck.items;
      let emptyTested = false;
      for (let k = 0; k < items.length; k++) {
        const it = items[k];
        if (it.type === 'fill') {
          const inp = page.locator('#lc-questionBody input[type=text]');
          if (!emptyTested) {
            emptyTested = true;
            const prog = await page.locator('#lc-progressText').innerText();
            await page.locator('#lc-actionsRow button:has-text("Check")').click();
            ok(/answer|type|write/i.test(await page.locator('#lc-feedback').innerText()) && prog === await page.locator('#lc-progressText').innerText() && await inp.isEnabled(), A, 'empty Check is counted as a wrong answer (no warning)');
          }
          await inp.fill(it.display);
          await page.locator('#lc-actionsRow button:has-text("Check")').click();
        } else if (it.type === 'order') {
          const seq = (it.alts && it.alts[0]) || it.tokens;
          for (const w of seq) if (!(await clickText('#lc-orderTray button', w))) { fail(A, `item ${k + 1}: tile "${w}" not found`); break; }
          await page.locator('#lc-orderCheck').click();
        } else if (it.type === 'error') {
          await page.locator('#lc-errorSentence .errorcorrection-word').nth(it.errorIndex).click();
        } else {
          if (!(await clickText('#lc-questionBody .levelcheck-opt', it.choices[it.correct]))) fail(A, `item ${k + 1}: option not found`);
        }
        await page.locator('#lc-actionsRow button:has-text("→")').click();
      }
      await finalContract(A, 'lc');
      await restartContract(A, 'lc', '#lc');
    } catch (e) { fail(A, 'crashed: ' + e.message.split('\n')[0]); }
  }

  // ---------- Quiz
  const qf = path.join(QUIZ, `${slug}-quiz-1.json`);
  if (fs.existsSync(qf) && await page.locator('#quiz').count()) {
    const A = 'Quiz';
    try {
      const Q = JSON.parse(fs.readFileSync(qf, 'utf8')).items;
      const nodes = page.locator('#quiz .q');
      for (let k = 0; k < Q.length; k++) {
        const q = nodes.nth(k);
        if (Q[k].type === 'write') {
          await q.locator('.write-input').fill(Q[k].answers[0]);
          await q.locator('.write-check').click();
        } else {
          await q.locator(`.opt[data-idx="${Q[k].answer}"]`).click();
        }
      }
      ok((await page.locator('#quiz-score').innerText()).includes(`${Q.length}/${Q.length}`), A, 'answering everything correctly did not give full marks');
      const rev = await page.locator('#quiz-review').innerText();
      ok(rev.includes('Your answer') && (rev.match(/Q\d+\./g) || []).length === Q.length, A, 'final review does not list every question with "Your answer"');
    } catch (e) { fail(A, 'crashed: ' + e.message.split('\n')[0]); }
  }

  ok(errs.length === 0, 'Console', `${errs.length} error(s): ${[...new Set(errs)].slice(0, 3).join(' | ')}`);
  await page.close();
}

await browser.close();
server.close();
console.log(`e2e: ${slugs.length} unit(s), ${checks} checks, ${failures.length} failure(s)`);
failures.forEach((f) => console.log('  ✗ ' + f));
process.exit(failures.length ? 1 : 0);
