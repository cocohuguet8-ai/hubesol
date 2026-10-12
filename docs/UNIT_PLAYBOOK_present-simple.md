# HubESOL — Unit playbook (prototype: Present Simple, 9.5 on 2026-10-11)

Use this to bring every other unit (lesson + quiz + Practice) to the same standard.
Target: Learner Review mean ≥ 9.5, every criterion ≥ 9.0, from a real retest.
**Don't publish a unit until the HubESOL Learner Review scores 9.5/10.** (Exception: a unit may be temporarily reachable only so Grok/Coco can run that test; it stays "in test" until it passes.)

## 0. Files per unit
- Lesson: `src/content/lessons/verb-tenses/<slug>.md`
- Quiz: `src/data/quizzes/<slug>-quiz-1.json`
- Practice: `src/data/practice/<slug>-practice.json` (keys: gapFill, wordOrder, matching, timedMC, errorCorrection, levelCheck)
- Components: `src/components/practice/*.astro`, styles in `src/styles/global.css`
- Shared state with Grok: Drive `90_Agents` (TASKS, HUBESOL_Estat_Compartit, claude_out/, grok_out/)

## 1. Lesson rules
- One `level` (CEFR) everywhere: frontmatter, quiz `level`, objectives text. Present Simple = A2.
- No remarks about learners' first languages in the text.
- Order of Common mistakes: numbered errors first, **Pro tip at the end** (the callout is rendered by `scripts/rehype-pro-tip.mjs` from "Pro tip:").
- Signal-words table: be explicit about position (before the main verb, after *be*).
- Cover the neighbours learners trip over: questions with *be*, -s pronunciation (/s/ /z/ /ɪz/), adverb after *be*.

## 2. Quiz rules
- Max **one** impossible-by-form option per question; the rest are real forms that fail for context.
- Never leave a second option that is also correct (e.g. "is leaving" for a timetable). Remove it or make the stem unambiguous.
- Write items: list every acceptable answer (`answers: [...]`) — alternative prepositions, contractions, etc. Feedback must read correctly for both right and wrong answers (no "Add -s" when the -s is already there).

## 3. Practice rules (per activity)
**Word order** — tiles are lowercase (capital only for I / names; sentence-initial words lowercased in the tray); add `alts` for every movable time expression; multi-word proper nouns are one tile ("Christmas Day."); hints must match the sentence type (wh- questions: "In a question with 'What time', 'does' comes right after it").
**Fill in the gap** — hint tells the verb or "(do/does)", never "(auxiliary …)"; feedback names the slip ("Missing -s … → boils"); gap + hint stay together on one line (mobile).
**Beat the clock (timedMC)** — 20 items, 4 options, exactly **one** defensible answer:
- every stem needs a present anchor ("usually", "on weekdays", "now", a fact); do **not** use "Nowadays" (it fits the continuous);
- no bare -ing option, no "Is/Are + base verb"; use "is/are + -ing" and "has/have + past participle" as context-wrong real forms; max 1 broken form per item;
- don't stack "usually" with "every …" (redundant);
- timer: starts only on Start, computed from `Date.now()`, pauses off-screen; Play again → Start screen and scrolls to it; after answering the Next button scrolls into view.
**Find the mistake** — spread the error position (not mostly the first word); `errorSpan` when two adjacent words are defensible; wrong taps do not count as "found without help".
**Matching** — matched pair visibly different from a selected tile; tooltip explains "Attempts".
**Level check** — question-by-question review (✓/✗) at the end.

## 4. Mobile / UI checklist (test on a real phone, not only a desktop window)
- Tap targets ≥ 44 px (tiles, inputs, "Reveal the mistake").
- Word order card height must not jump when tiles move (reserved tray + answer zone).
- No text overflowing its box (gap hint); button text uses the ink colour (iOS paints bare buttons blue).
- No horizontal scroll; Beat the clock feedback and Next visible after answering.
- "Teacher mode" only shows/hides the For-teachers block; it never reveals answers.

## 5. Workflow that worked (Claude builds, Grok tests)
1. Claude edits on a branch → build (`npm run build`, 111 pages) → local preview + Playwright smoke test.
2. PR via `gh api` REST → wait for checks `Cloudflare Pages` + `validate` → squash-merge → auto-deploy.
3. Grok retests live and writes to `grok_out/` + the Grok section of HUBESOL_Estat_Compartit; Claude fixes by finding ID (HQ-xxx / G-xxx).
4. Real-device pass by Coco (iPhone) — caught the issues emulation missed (overflow, blue text, Next below the fold).
5. Cut-off: Learner Review ≥ 9.5 on the 5 criteria (grammar explanation, exercise quality, exercise types, suitability for learning, overall satisfaction).

## 6. Per-unit rollout checklist
- [ ] Level decided and unified
- [ ] Lesson: no L1 remarks, Pro tip last, signal table, *be* questions, pronunciation (if relevant)
- [ ] Quiz: one impossible option max, one correct answer, write-item alternatives
- [ ] Word order: lowercase tiles, alts, correct hints
- [ ] Gap fill: hints, specific feedback
- [ ] Beat the clock: 20 items, one defensible answer each, no "Nowadays", no bare -ing
- [ ] Find the mistake: error positions spread
- [ ] Level check review, Matching feedback
- [ ] Local build + smoke test, PR, checks green, merge
- [ ] Grok retest ≥ 9.5, then iPhone pass by Coco
- [ ] Only then: add the slug to the live list (maintenance middleware) / lift maintenance

## 7. While the site is in maintenance
- `related` links in the live lessons may only point to live slugs (see `functions/_middleware.js` LIVE_SLUGS); everything else shows "coming soon" (503). Re-add the full related lists when a unit goes live.

---

## Procés per a cada lliçó nova (revisat 2026-10-12, v2 amb tests automàtics)

Llista de control completa: `docs/HUBESOL_Checklist_pre-entrega_v1.md` (C-01…C-30 contingut + T-01…T-14 tècniques). Contracte dels components: `docs/COMPONENT_CONTRACT.md`.

1. **Text primer.** Frases, opcions, pistes, feedbacks i explicacions en un Doc a `claude_out/`. Grok revisa amb les regles `[TEXT]` (ID de regla per incompliment). Es corregeix el Doc i només llavors es construeix.
2. **Build + proves automàtiques (Claude, obligatori):** `npm run lint && npm run build && npm run e2e` en verd, en local i al CI (checks «validate» + «e2e» + «Cloudflare Pages»). Claude adjunta l'informe (n.º de comprovacions i 0 errors) al Doc. **Mai «llesta» només amb el build.**
3. **Bugs de component:** s'arreglen al moment, al component compartit (no lliçó a lliçó) i s'afegeix el requisit a `COMPONENT_CONTRACT.md` + una comprovació a `scripts/e2e.mjs`. Un bug que ja ha sortit un cop no pot tornar a sortir.
4. **Una sola passada de Grok** (Learner Review + QA) només sobre el que els tests NO cobreixen (vegeu avall). Els retests: només els fallits + regressió.
5. **Publicar** (`LIVE_SLUGS`) només amb Learner Review ≥ 9,5.

### Què cobreix l'automàtic (`npm run e2e`, 610 comprovacions a 10 units)
Consola neta (T-01), activitats de principi a fi amb les respostes del JSON i puntuació màxima (T-04, T-05), Check buit (T-08), pantalla final amb veredicte, focus a «Play again» i focus a cada pregunta de Beat the clock (T-10), títol visible i focus en reiniciar (T-10, T-11), revisions amb «You wrote»/«Your answer» (C-xx revisió), comes a les ordres acceptades (C-24), Matching complet. `npm run lint`: cometes tipogràfiques dins de codi.

### Què NO cobreix (queda per a Grok/Coco)
Enllaços i www→apex en producció (T-02, T-03), Teacher mode en incògnit (T-12), contrast (T-13), mides 44 px i prova al mòbil real (T-14, Coco), anell de focus visual (T-09), Beat the clock amb temps esgotat (T-06), criteri didàctic: dues respostes defensables, naturalitat, nivell (C-xx; Learner Review).
