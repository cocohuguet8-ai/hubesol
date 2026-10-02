#!/usr/bin/env node
// Validador de quizzes HubESOL (src/data/quizzes/*.json).
// Ús: npm run validate   (surt amb codi 1 si hi ha ERRORS; els AVISOS no bloquegen)
import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { join, basename } from 'node:path';

const ROOT = new URL('..', import.meta.url).pathname;
const QUIZ_DIR = join(ROOT, 'src/data/quizzes');
const PRACTICE_DIR = join(ROOT, 'src/data/practice');
const LESSONS_DIR = join(ROOT, 'src/content/lessons');
const MIN_MC = 10;
const MIN_WRITE = 3;

let errors = 0, warnings = 0;
const err = (f, m) => { errors++; console.log(`  ✗ ERROR  ${f}: ${m}`); };
const warn = (f, m) => { warnings++; console.log(`  ! AVÍS   ${f}: ${m}`); };
const str = (v) => typeof v === 'string' && v.trim().length > 0;
const norm = (s) => String(s).toLowerCase().replace(/[‘’`´]/g, "'").replace(/\s+/g, ' ').trim();

// Lliçons publicades i el quiz que referencien
function lessons(dir, acc = []) {
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) lessons(p, acc);
    else if (e.name.endsWith('.md')) {
      const fm = readFileSync(p, 'utf8').split('\n---\n')[0];
      acc.push({
        slug: e.name.replace(/\.md$/, ''),
        quiz: (fm.match(/^quiz:\s*"?([^"\n]+)"?/m) || [])[1] || null,
        draft: /^draft:\s*true/m.test(fm),
      });
    }
  }
  return acc;
}

const files = existsSync(QUIZ_DIR) ? readdirSync(QUIZ_DIR).filter((x) => x.endsWith('.json')).sort() : [];
const lessonList = existsSync(LESSONS_DIR) ? lessons(LESSONS_DIR) : [];
const practiceSlugs = new Set(existsSync(PRACTICE_DIR) ? readdirSync(PRACTICE_DIR).filter((x) => x.endsWith('-practice.json')).map((x) => x.replace(/-practice\.json$/, '')) : []);
const quizIds = new Set(files.map((x) => x.replace(/\.json$/, '')));

// Cada lliçó publicada ha de tenir quiz
for (const l of lessonList) {
  if (l.draft) continue;
  if (!l.quiz) err(l.slug + '.md', 'la lliçó no referencia cap quiz');
  else if (!quizIds.has(l.quiz)) err(l.slug + '.md', `el quiz "${l.quiz}" no existeix a src/data/quizzes/`);
}

const REWRITE_PROMPT = /^(correct this|fix this|rewrite|transform)\b/i;
const DOUBLE_ARTICLE = /\b(the|a|an)\s+(the|a|an)\b/i;

for (const file of files) {
  const f = file;
  let d;
  try { d = JSON.parse(readFileSync(join(QUIZ_DIR, file), 'utf8')); }
  catch (e) { err(f, `JSON invàlid: ${e.message}`); continue; }

  const id = file.replace(/\.json$/, '');
  if (d.id !== id) err(f, `id "${d.id}" no coincideix amb el nom del fitxer`);
  if (!str(d.title)) err(f, 'falta title');
  if (!str(d.level)) err(f, 'falta level');
  if (!Array.isArray(d.items)) { err(f, 'items no és una llista'); continue; }

  const mc = [], wr = [];
  d.items.forEach((it, i) => (it.type === 'write' ? wr : mc).push([it, i + 1]));
  if (mc.length < MIN_MC) err(f, `només ${mc.length} ítems d'elecció múltiple (mínim ${MIN_MC})`);

  const questions = new Set();
  d.items.forEach((it, i) => {
    const w = `ítem #${i + 1}`;
    if (!str(it.question)) return err(f, `${w}: falta question`);
    const qn = norm(it.question);
    if (questions.has(qn)) warn(f, `${w}: enunciat repetit`);
    questions.add(qn);
  });

  // MC
  for (const [it, n] of mc) {
    const w = `ítem #${n}`;
    if (!Array.isArray(it.options) || it.options.length < 3) { err(f, `${w}: calen almenys 3 opcions`); continue; }
    if (new Set(it.options.map(norm)).size !== it.options.length) err(f, `${w}: opcions repetides`);
    if (!Number.isInteger(it.answer) || it.answer < 0 || it.answer >= it.options.length) { err(f, `${w}: answer fora de rang`); continue; }
    if (!Array.isArray(it.explanations) || it.explanations.length !== it.options.length) err(f, `${w}: explanations ha de tenir ${it.options.length} elements`);
    else it.explanations.forEach((e, j) => { if (!str(e)) err(f, `${w}: falta explicació per a l'opció ${j + 1}`); });
    if (REWRITE_PROMPT.test(it.question)) err(f, `${w}: enunciat "${it.question.slice(0, 40)}…" demana escriure però es respon clicant — reformula'l ("Choose the correct version of: …") o fes-ne un ítem type=write`);
    it.options.forEach((o) => { if (DOUBLE_ARTICLE.test(o)) warn(f, `${w}: opció amb articles dobles ("${o}") — distractor absurd?`); });
  }
  // Posició de la resposta correcta al JSON estàtic (el web a més barreja en viu)
  if (mc.length >= 5) {
    const counts = [0, 0, 0, 0];
    mc.forEach(([it]) => { if (Number.isInteger(it.answer) && it.answer < 4) counts[it.answer]++; });
    const max = Math.max(...counts);
    if (max >= mc.length * 0.7) err(f, `la resposta correcta és gairebé sempre la mateixa posició (${counts.join('/')})`);
    else if (max > Math.ceil(mc.length * 0.4)) warn(f, `posicions de la resposta correcta desequilibrades (${counts.join('/')})`);
  }

  // Ítems d'escriure
  if (wr.length === 0) err(f, "cap ítem d'escriure (type=write) — el quiz és 100% elecció múltiple");
  else if (wr.length < MIN_WRITE) warn(f, `només ${wr.length} ítems d'escriure (recomanat ${MIN_WRITE})`);
  for (const [it, n] of wr) {
    const w = `ítem #${n} (write)`;
    if (!str(it.kind)) err(f, `${w}: falta kind`);
    if (!Array.isArray(it.answers) || !it.answers.length || !it.answers.every(str)) { err(f, `${w}: answers buit`); continue; }
    if (!str(it.explanation)) err(f, `${w}: falta explanation`);
    if (!/___/.test(it.question) && !/→\s*$/.test(it.question) && !/^correct the mistake$/i.test(it.kind || '')) warn(f, `${w}: l'enunciat no té "___" ni acaba amb "→"`);
    if (it.options || it.answer !== undefined) err(f, `${w}: un ítem write no ha de tenir options/answer`);
    if (it.common !== undefined) {
      if (!Array.isArray(it.common) || !it.common.every((c) => str(c.answer) && str(c.why))) err(f, `${w}: common ha de ser [{answer, why}]`);
      else it.common.forEach((c) => { if (it.answers.map(norm).includes(norm(c.answer))) err(f, `${w}: common "${c.answer}" és també una resposta correcta`); });
    }
    // Pista visible dins l'enunciat que regala la resposta
    if (it.answers.some((a) => norm(it.question).includes(`(${norm(a)})`))) warn(f, `${w}: l'enunciat conté la resposta entre parèntesis`);
  }
}

// Cada lliçó ha de tenir com a mínim una activitat d'escriure (al quiz o a la pràctica)
for (const l of lessonList) {
  if (l.draft || !l.quiz || !quizIds.has(l.quiz)) continue;
  let hasWrite = false;
  try { hasWrite = JSON.parse(readFileSync(join(QUIZ_DIR, l.quiz + '.json'), 'utf8')).items.some((it) => it.type === 'write'); } catch {}
  if (!hasWrite && !practiceSlugs.has(l.slug)) err(l.slug + '.md', "la lliçó no té cap activitat d'escriure (ni al quiz ni a la pràctica)");
}

console.log(`\n${files.length} quizzes revisats · ${errors} errors · ${warnings} avisos`);
process.exit(errors ? 1 : 0);
