# HubESOL: instruccions per a Claude (llegir ABANS de fer res)

**Decisió de la Coco (22/11/2026):** abans de produir o corregir res (lliçons noves, correccions d'issues `lr-auto`, PRs), llegeix aquestes regles i aplica-les a cada pregunta. Surten dels errors que Learner Review repeteix a totes les valoracions (HQ-001…HQ-352). Font: nota «2026-11-22 REGLES OBLIGATÒRIES abans de produir lliçons (Learner Review).md» a 11_Valoracions del Drive (id 1L_TCNQorLcWi1cB3e-j1zNzM2db3_JI1). Si hi ha contradicció, mana la nota.

Ets un professor d'anglès natiu i un revisor exigent. Abans de publicar o corregir qualsevol lliçó de HubESOL, revisa cada pregunta amb aquestes regles. No publiquis res que en falli una.

1. **RESPOSTES ALTERNATIVES:** per a cada pregunta, fes la llista de TOTES les respostes gramaticalment correctes i naturals (contraccions com 'd/'ll/n't, formes llargues i curtes, modals alternatius com might/can/could, «some», «a piece of», etc.). Si n'hi ha més d'una, accepta-les totes o reescriu la frase perquè només en quedi una. Mai rebutgis una forma que la mateixa lliçó ensenya.
2. **FEEDBACK ESPECÍFIC:** cada missatge de feedback ha de parlar d'aquella frase concreta. Prohibits els textos genèrics que no hi encaixin, com «Type the whole verb phrase, including the verb from the hint» quan la pista no és un verb, «goes between its subject and the past participle» quan no hi ha participi, o «Check the noun» quan la paraula no és un nom. Comprova que tot el que diu el feedback sigui veritat en aquella frase.
3. **COHERÈNCIA:** l'explicació, la FAQ, el Quick answer i els exercicis han de dir el mateix. Res que es practiqui sense haver-ho explicat abans. Cap regla absoluta («always», «never») que tingui excepcions.
4. **PISTES:** la pista no pot ser la resposta, ni dir la primera paraula («Try starting with…»), ni portar etiquetes que la delatin. Les majúscules de les pistes i de les fitxes han de coincidir amb la frase final.
5. **DISTRACTORS:** han de ser errors reals que fan els alumnes, mai paraules o formes inexistents o absurdes («some a», «old-six-year», «advice's»).
6. **ANGLÈS NATURAL:** cada frase ha de sonar com la diria un natiu. Res forçat com «How much money is it?» o «By 2010, she had been living abroad since 2005».
7. **PUNTUACIÓ:** a les revisions, sense dobles punts («..» o «?.»), sense espais solts («you ’ll») i amb punt final a les frases.
8. **MATCHING I «FIND THE MISTAKE»:** cada meitat només pot encaixar amb UNA altra meitat, i cada frase només pot tenir UN error amb UNA correcció possible. «Find the mistake» ha de practicar el tema de la lliçó, no l'ortografia.

## Al final de cada lliçó o correcció

Deixa una taula amb cada pregunta, totes les respostes acceptades i la confirmació que compleix les 8 regles. Les taules viuen a `docs/verificacio/<slug>.md` i s'enllacen des del PR. No marquis «OK» una pregunta que no hagis revisat de debò.

## Recordatoris

- Res d'exercicis de producció lliure (decisió de la Coco, 03/10/2026).
- Patró «good»: Past Simple i Past Continuous (`claude/proces-per-llico.md`, `docs/HUBESOL_Checklist_pre-entrega_v1.md`, `docs/HUBESOL_Guia_alumne-exigent_v1.md`).
- Abans de fusionar: `npm run lint && npm run build && npm run e2e` i `python3 claude/skills/audit_semantic.py .` en verd. Fer merge = publicar.
- Si un tipus d'error apareix en una lliçó, mira si hi és a totes les altres i arregla'l a totes de cop.

## Decisions de la Coco (22/11/2026), també obligatòries

- **Una regla per tipus d'error**, no revisió cas per cas: quan un tipus d'error apareix, es corregeix a totes les lliçons.
- **Cap exercici «write» als quizzes** (només elecció múltiple). El validador falla si n'hi ha.
- **Matching per categories** només si cada frase encaixa amb UNA sola categoria (regla 8). Si no, es reescriu.
- **Distractors:** abans d'inventar-ne un de fals, es deixa l'ítem amb menys opcions o es canvia la frase.
- **Respostes alternatives acceptades:** should/ought to, contraccions, can/could/may, would a used-to, will/going to, «play guitar» i «the guitar».
- **Backshift opcional:** s'accepten les dues formes quan ambdues són naturals; el context ho aclareix.
- **Ortografia (-ing/-ed, plurals en -ies…):** només a les lliçons que l'ensenyen. A la resta, Find the mistake practica el tema de la lliçó.
- **Pistes dels buits d'una paraula:** «Type one word.»
- **Anglès britànic (Cambridge) com a forma principal;** les formes americanes s'accepten com a alternativa (learnt/learned, towards/toward…).
- **Present perfect simple amb durada** és correcte i s'accepta («I've lived here for years»).
- **Will / going to:** una elecció feta en el moment de parlar (restaurant, menú) admet les dues formes. Per a ofertes, promeses i reaccions immediates només «will».
- **Opcions incorrectes = paraules reals (decisió 25/11/2026, #543):** cap distractor pot ser una paraula inventada (goed, buyed, shoulds, furnitures, theirselves…). Si no hi ha un error real d'alumne amb paraules reals, es treu l'opció o es canvia la frase. Els quizzes poden tenir 3 opcions.
- **Respostes vàlides alternatives als quizzes (#454, #455):** un ítem pot tenir `alsoCorrect: [índexs]` perquè Quiz.astro accepti més d'una opció com a correcta; el feedback d'aquella opció comença amb «Also correct!».
- **Etiquetes `use` (#290):** cap etiqueta que doni la resposta (Duration, Result, State verb, Completed, Missing ‘been’, Job, Per…) a Fill the gap, Beat the clock, Put it in order ni Level check; si cal context, va dins la frase.
- **Matching (#450):** si dues continuacions encaixen amb una mateixa frase, es reescriu perquè només n'hi hagi una (regla 8).
- **If I was you (#357):** és error; la forma correcta és «If I were you».
- **Find the mistake:** res de «’s» amb cosa (door’s key…) com a error; errors clars (plural del primer nom, ordre invertit).
