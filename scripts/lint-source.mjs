// Source lint: bugs that bit us before (curly quotes inside code, e.g. [data-id=“x”] → CSS selector TypeError).
import fs from 'node:fs';
import path from 'node:path';
const bad = [];
const walk = (d) => fs.readdirSync(d, { withFileTypes: true }).forEach((e) => {
  const p = path.join(d, e.name);
  if (e.isDirectory()) return walk(p);
  if (!/\.(astro|js|mjs|ts)$/.test(e.name)) return;
  fs.readFileSync(p, 'utf8').split('\n').forEach((l, i) => {
    if (/\[[a-z-]+=[“”‘’]/.test(l)) bad.push(`${p}:${i + 1} curly quote inside an attribute selector`);
    if (/querySelector(All)?\(\s*[“”‘’]/.test(l)) bad.push(`${p}:${i + 1} curly quote opening a querySelector string`);
  });
});
walk('src');
if (bad.length) { console.error(bad.join('\n')); process.exit(1); }
console.log('lint-source: ok');
