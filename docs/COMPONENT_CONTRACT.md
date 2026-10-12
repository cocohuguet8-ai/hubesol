# Contracte dels components d'activitat (HubESOL)

Cada activitat compartida (`src/components/practice/*`, `Quiz.astro`) ha de complir això **sempre**. Ho verifica `npm run e2e` (CI, check «e2e») per a TOTES les units; ho verifica `npm run lint` per al codi. Un bug de component no és «baix»: s'arregla al moment, al component, no lliçó a lliçó.

| # | Requisit | Activitats |
|---|---|---|
| 1 | Consola neta (cap error JS) | totes |
| 2 | Check buit avisa («Type your answer first…») i no compta com a error ni avança | Fill, Level check, Quiz (escriure) |
| 3 | Pantalla final amb **veredicte** (Perfect/Strong/Solid/Keep practising…) | totes |
| 4 | Pantalla final: el focus de teclat va a «Play again» | totes |
| 5 | La revisió mostra **què ha respost l'alumne** («You wrote» / «Your answer»), també a les correctes; a les errònies, la resposta correcta | Quiz, Fill, Level check, Word order |
| 6 | Reiniciar (Try again / Play again): el títol queda visible sota la capçalera fixa i el focus va al primer control | totes |
| 7 | Beat the clock: a cada pregunta nova el focus va a la primera opció | Beat the clock |
| 8 | Ordres acceptades amb coma (ALT) es mostren a la revisió amb la coma | Word order, Level check |
| 9 | Escriure les respostes canòniques del JSON dona puntuació màxima | totes |
| 10 | Cap cometa tipogràfica dins de selectors/codi (`[data-id=“x”]`) | codi (lint) |

Pendent de prova manual (no automatitzable): mòbil real, contrast de colors, mida tàctil 44 px, criteri didàctic (Learner Review).

## Procés per lliçó (actualitzat)
1. Text → Doc → Grok revisa [TEXT] → corregir.
2. Build → `npm run lint && npm run build && npm run e2e` (en verd) → informe adjunt al Doc.
3. Grok fa **una sola passada** (Learner Review + QA) només sobre el que els tests no cobreixen.
4. Publicar a `LIVE_SLUGS` amb LR ≥ 9,5.
