#!/usr/bin/env node
// Validador de fitxers de pràctica HubESOL.
// Ús: npm run validate   (surt amb codi 1 si hi ha ERRORS; els AVISOS no bloquegen)
import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { join, basename } from 'node:path';

const ROOT = new URL('..', import.meta.url).pathname;
const PRACTICE_DIR = join(ROOT, 'src/data/practice');
const LESSONS_DIR = join(ROOT, 'src/content/lessons');
const N = 20;

let errors = 0, warnings = 0;
const err = (f, m) => { errors++; console.log(`  ✗ ERROR  ${f}: ${m}`); };
const warn = (f, m) => { warnings++; console.log(`  ! AVÍS   ${f}: ${m}`); };
const str = (v) => typeof v === 'string' && v.trim().length > 0;
const norm = (s) => String(s).toLowerCase().replace(/<[^>]+>|&nbsp;/g, ' ').replace(/[^a-z0-9' ]/g, ' ').replace(/\s+/g, ' ').trim();

// Tots els slugs de lliçó existents (src/content/lessons/**/<slug>.md)
function lessonSlugs(dir) {
  const out = new Set();
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    if (e.isDirectory()) lessonSlugs(join(dir, e.name)).forEach((s) => out.add(s));
    else if (e.name.endsWith('.md')) out.add(e.name.replace(/\.md$/, ''));
  }
  return out;
}

// 1) Fitxers de pràctica fora de lloc (el web només llegeix src/data/practice)
function findStray(dir, acc = []) {
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    if (['node_modules', '.git', 'dist', '.astro'].includes(e.name)) continue;
    const p = join(dir, e.name);
    if (e.isDirectory()) findStray(p, acc);
    else if (e.name.endsWith('-practice.json') && !p.startsWith(PRACTICE_DIR)) acc.push(p.replace(ROOT, ''));
  }
  return acc;
}
for (const p of findStray(ROOT)) err(p, 'fitxer de pràctica fora de src/data/practice/ — el web NO el llegeix');

function checkChoice(f, where, q) {
  if (!Array.isArray(q.choices) || q.choices.length < 2) return err(f, `${where}: calen opcions (choices)`);
  if (new Set(q.choices.map(norm)).size !== q.choices.length) err(f, `${where}: opcions repetides`);
  if (!Number.isInteger(q.correct) || q.correct < 0 || q.correct >= q.choices.length)
    return err(f, `${where}: "correct"=${q.correct} fora de rang`);
  if (!Array.isArray(q.wrongReasons) || q.wrongReasons.length !== q.choices.length)
    err(f, `${where}: wrongReasons ha de tenir ${q.choices.length} elements`);
  else {
    if (q.wrongReasons[q.correct] !== '') err(f, `${where}: la resposta correcta (${q.choices[q.correct]}) té un motiu d'error — "correct" probablement apunta a l'opció equivocada`);
    q.wrongReasons.forEach((r, i) => { if (i !== q.correct && !str(r)) err(f, `${where}: falta explicació per a l'opció incorrecta "${q.choices[i]}"`); });
  }
}

function checkError(f, where, it) {
  if (!Array.isArray(it.tokens) || it.tokens.length < 2) return err(f, `${where}: tokens massa curts`);
  if (it.tokens.length < 3) warn(f, `${where}: només ${it.tokens.length} blocs clicables — massa fàcil d'endevinar`);
  if (!Number.isInteger(it.errorIndex) || it.errorIndex < 0 || it.errorIndex >= it.tokens.length)
    return err(f, `${where}: errorIndex=${it.errorIndex} fora de la frase`);
  const span = it.errorSpan || [it.errorIndex, it.errorIndex];
  if (it.errorSpan && !(Array.isArray(span) && span.length === 2 && span[0] <= it.errorIndex && it.errorIndex <= span[1] && span[1] < it.tokens.length))
    err(f, `${where}: errorSpan ${JSON.stringify(it.errorSpan)} no conté errorIndex o surt de la frase`);
  const multi = it.tokens.filter((t) => /\s/.test(t));
  if (multi.length) err(f, `${where}: un bloc ha de ser una sola paraula (${multi.join(' | ')})`);
  if (!str(it.correction)) err(f, `${where}: falta correction`);
  else if (norm(it.correction) === norm(it.tokens.slice(span[0], span[1] + 1).join(' '))) err(f, `${where}: la correcció és igual a la paraula "errònia"`);
  if (!str(it.message)) err(f, `${where}: falta message`);
}

function checkFill(f, where, answers, display) {
  if (!Array.isArray(answers) || !answers.length || !answers.every(str)) return err(f, `${where}: answers buit`);
  if (!answers.map(norm).includes(norm(display))) err(f, `${where}: display "${display}" no és entre les respostes acceptades`);
}

function section(f, d, key, listKey) {
  const s = d[key];
  if (!s || typeof s !== 'object') { err(f, `falta la secció ${key}`); return []; }
  if (!str(s.title)) err(f, `${key}: falta title`);
  const list = s[listKey];
  if (!Array.isArray(list)) { err(f, `${key}.${listKey} no és una llista`); return []; }
  if (list.length !== N) err(f, `${key}: té ${list.length} ítems (n'esperàvem ${N})`);
  return list;
}

function dupes(f, key, texts) {
  const seen = new Map();
  texts.forEach((t, i) => { const k = norm(t); if (!k) return; if (seen.has(k)) warn(f, `${key}: ítems ${seen.get(k) + 1} i ${i + 1} repetits`); else seen.set(k, i); });
}

const slugs = existsSync(LESSONS_DIR) ? lessonSlugs(LESSONS_DIR) : new Set();
const files = existsSync(PRACTICE_DIR) ? readdirSync(PRACTICE_DIR).filter((x) => x.endsWith('.json')).sort() : [];

for (const file of files) {
  const f = file;
  let d;
  try { d = JSON.parse(readFileSync(join(PRACTICE_DIR, file), 'utf8')); }
  catch (e) { err(f, `JSON invàlid: ${e.message}`); continue; }

  const slug = basename(file).replace(/-practice\.json$/, '');
  if (!file.endsWith('-practice.json')) err(f, 'el nom ha d\'acabar en -practice.json');
  else if (!slugs.has(slug)) err(f, `no hi ha cap lliçó ${slug}.md — aquests exercicis no es mostraran enlloc`);
  if (!str(d.tense)) err(f, 'falta tense');
  if (!str(d.lessonTitle)) err(f, 'falta lessonTitle');

  // gapFill
  const gf = section(f, d, 'gapFill', 'questions');
  gf.forEach((q, i) => {
    const w = `gapFill #${i + 1}`;
    if (typeof q.before !== 'string' || typeof q.after !== 'string') err(f, `${w}: falta before/after`);
    checkFill(f, w, q.answers, q.display);
    if (!str(q.explain)) err(f, `${w}: falta explain`);
  });
  dupes(f, 'gapFill', gf.map((q) => `${q.before} ${q.display} ${q.after}`));

  // wordOrder
  const wo = section(f, d, 'wordOrder', 'sentences');
  wo.forEach((s, i) => { if (!Array.isArray(s.tokens) || s.tokens.length < 3 || !s.tokens.every(str)) err(f, `wordOrder #${i + 1}: tokens invàlids`); });
  dupes(f, 'wordOrder', wo.map((s) => (s.tokens || []).join(' ')));

  // matching
  const mp = section(f, d, 'matching', 'pairs');
  mp.forEach((p, i) => { if (!str(p.left) || !str(p.right)) err(f, `matching #${i + 1}: parella incompleta`); });
  const lefts = mp.map((p) => norm(p.left));
  lefts.forEach((l, i) => { if (lefts.indexOf(l) !== i) err(f, `matching #${i + 1}: "${mp[i].left}" repetit (trenca el joc)`); });
  const rights = mp.map((p) => norm(p.right));

  // timedMC (NO es barregen les opcions al web → cal equilibri de posicions)
  const mc = section(f, d, 'timedMC', 'questions');
  mc.forEach((q, i) => { checkChoice(f, `timedMC #${i + 1}`, q); if (!str(q.text)) err(f, `timedMC #${i + 1}: falta text`); });
  if (mc.length) {
    const counts = [0, 0, 0, 0];
    mc.forEach((q) => { if (Number.isInteger(q.correct) && q.correct < 4) counts[q.correct]++; });
    const max = Math.max(...counts);
    if (max >= mc.length * 0.6) err(f, `timedMC: la resposta correcta és gairebé sempre la mateixa posició (${counts.join('/')}) — l'alumne pot endevinar-la`);
    else if (Math.min(...counts) < 3 || max > 7) warn(f, `timedMC: posicions de la resposta correcta desequilibrades (${counts.join('/')}), ideal 5/5/5/5`);
  }

  // errorCorrection
  const ec = section(f, d, 'errorCorrection', 'items');
  ec.forEach((it, i) => checkError(f, `errorCorrection #${i + 1}`, it));
  dupes(f, 'errorCorrection', ec.map((it) => (it.tokens || []).join(' ')));

  // levelCheck
  const lc = section(f, d, 'levelCheck', 'items');
  const order = d.levelCheck?.categoryOrder || [];
  const labels = d.levelCheck?.categoryLabels || {};
  order.forEach((c) => { if (!str(labels[c])) err(f, `levelCheck: categoria "${c}" sense etiqueta`); });
  lc.forEach((it, i) => {
    const w = `levelCheck #${i + 1} (${it.type})`;
    if (!order.includes(it.type)) return err(f, `${w}: tipus no declarat a categoryOrder`);
    if (it.type === 'fill') {
      if (!str(it.sentText) || !it.sentText.includes('{{blank}}')) err(f, `${w}: sentText sense {{blank}}`);
      checkFill(f, w, it.answers, it.display);
    } else if (it.type === 'order') {
      if (!Array.isArray(it.tokens) || it.tokens.length < 3) err(f, `${w}: tokens invàlids`);
    } else if (it.type === 'error') {
      checkError(f, w, it);
    } else {
      if (!str(it.text)) err(f, `${w}: falta text`);
      checkChoice(f, w, it);
    }
  });
  order.forEach((c) => { if (!lc.some((it) => it.type === c)) warn(f, `levelCheck: cap ítem de la categoria "${c}"`); });
}

console.log(`\n${files.length} lliçons revisades · ${errors} errors · ${warnings} avisos`);
process.exit(errors ? 1 : 0);
