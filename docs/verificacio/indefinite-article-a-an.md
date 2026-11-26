# Verificació de les 8 regles: indefinite-article-a-an

Reescrita des de zero el 2026-11-22 (Claude), 5è intent. «✓» = comprovada i compleix; «—» = no aplica a aquest tipus d'exercici. Revisió de l'escriptora, no independent: el retest de Learner Review és la prova real.

## Què s'ha canviat i per què

- **Lliçó:** els 6 usos solapats (first mention / one of a group / meaning “one” / per / jobs / exclamations) passen a 4 d'excloents: cosa nova o no específica, feina o rol, per (every), exclamació. Quick answer, taula, apartats, FAQ i objectius diuen ara el mateix. Afegits news, money, help, homework a la llista d'incomptables, perquè els exercicis els practiquen.
- **Etiquetes `use`:** neutres («Fill the gap», «Choose the answer», «Put it in order», «The mistake»). Abans deien «Job», «Per», «Uncountable»… i donaven la resposta (regla 4).
- **Pistes dels buits:** «Type one word.» (decisió 22/11) en lloc de «a / an / —».
- **Matching:** 4 categories excloents, 5 frases per categoria; cap frase «be + nom» a la categoria «new or non-specific», perquè no es confongui amb «job or role» (regla 8).
- **Distractors:** fora «per a», «in week», «an advices», «one new shoes». «The» només es manté on és un error real d'alumne (twice the week, what the…, a la fila «the hour») i s'ha tret on també seria natural (feina, student, old friend of mine…): aquests ítems tenen 3 opcions (regla 5 + decisió 22/11).
- **Find the mistake:** fora els ítems que admetien dues lectures («He works as the mechanic», «I saw the fox for the first time») i els errors que cap alumne fa («a two children»). Un sol error, una sola correcció, missatges explicatius (regles 2 i 8).
- **Respostes alternatives acceptades (regla 1):** «per» a «twice a week», «100 km an hour» i «twenty euros an hour»; «one» a «Wait a minute»; «some» i «any» als buits sense article quan són naturals.
- **Quiz:** sense absoluts («never», «Jobs need an article»), sense «in week» ni «an advices»; explicacions específiques per opció.
- **Component (GapFill i LevelCheck):** el feedback d'un buit fallat ja no és el genèric «Check the article»: diu si cal a/an pel so, si el nom és plural o incomptable, o per què «the» no hi encaixa.
- **Pack PDF** regenerat des de la lliçó nova; `build_pack.py` accepta ítems de 3 opcions.
- **Provat:** `npm run lint`, `npm run build` (0 errors) i `e2e` copiat a `articles` (64 comprovacions, 0 fallades; l'e2e normal només cobreix verb-tenses), amb mòbil a 390 px sense desbordament ni targetes <44 px.

## Passada del 26/11/2026 (retest de Learner Review a la PR #536)

Learner Review va donar 7,8 i NO APROVAT. En lloc de tocar només els punts que va citar, he repassat tota la lliçó amb les 8 regles i he buscat la mateixa classe d'errors a tot el fitxer:

- **Doble punt (R7):** el missatge del Word order citava la fitxa amb la seva puntuació («not “school.”.»). El component ara cita les paraules sense puntuació final (WordOrder i LevelCheck). Ja no queda cap «..», «?.» ni « ’» als fitxers de la lliçó.
- **Raó gramatical al Word order (R2):** cada frase del Word order i del Level check porta ara un camp `reason` que diu per què l'article va allà (davant de l'adjectiu, davant de la feina, «per», exclamació…).
- **Repeticions (R3/R6):** les 20 frases del Word order s'han tornat a escriure perquè cap no coincideixi amb el Gap-fill (abans n'hi havia 8 de calcades: nurse, architect, bank, friend of mine, wait a minute, twice a week, good news…). També he canviat Matching, Beat the clock, Find the mistake i Level check on una frase o un nom es repetia entre seccions (eyes, ice cream, an hour, old friend, university, elephants, pilot, engineer, amazing goal, strange…).
- **Find the mistake (R8):** s'ha reequilibrat. Passa de 6 de 8 «a/an segons el so» a les posicions 8–15 a 3 de 8, amb errors de feina sense article, singular sense article, plural amb «a», incomptable amb «a», «per» i exclamació sense article. Un sol error i una sola correcció per frase.
- **Find the mistake 18:** el feedback deia «‘a fox’» per a «dog»; ara diu «‘a dog’».
- **Quiz Q8:** el feedback de «She gave me a advice.» ara explica els dos errors (incomptable, i que fins i tot comptable seria «an»).
- **Pack PDF** regenerat.

**Verificació feta (no independent):** lint, build (114 pàgines), `audit_semantic.py` (0 troballes) i `audit_good.py` (només avisos de camps extra `reason`, que no afecten el render). Script de repeticions: cap frase idèntica entre seccions i cap parell nom+article repetit amb la mateixa estructura. Script de puntuació: 0 hits. **No s'ha pogut executar `npm run e2e`** en aquest entorn (no es pot baixar el navegador de Playwright): depèn del check «e2e» de la PR. La prova amb alumne real és el retest de Learner Review.

| ID | Activitat | Pregunta | Respostes acceptades | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| G1 | Fill in the gaps | Last night I had ___ strange dream. | a | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G2 | Fill in the gaps | We saw ___ dolphins on our holiday. | — / - / some | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G3 | Fill in the gaps | There’s ___ old church near my town. | an | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G4 | Fill in the gaps | My sister is ___ nurse at a hospital in Girona. | a | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G5 | Fill in the gaps | What ___ amazing goal! | an | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G6 | Fill in the gaps | I play tennis twice ___ week. | a / per | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G7 | Fill in the gaps | They sell ___ fresh vegetables at that stall. | — / - / some | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G8 | Fill in the gaps | When he grows up, he wants to be ___ architect. | an | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G9 | Fill in the gaps | Is there ___ bank near here? | a | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G10 | Fill in the gaps | The car was going at 100 kilometres ___ hour. | an / per | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G11 | Fill in the gaps | My teacher gave me ___ good advice. | — / - / some | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G12 | Fill in the gaps | I’ve got ___ younger brother. | a | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G13 | Fill in the gaps | Once upon a time, there was ___ ugly dragon in a cave. | an | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G14 | Fill in the gaps | Wait ___ minute, please. | a / one | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G15 | Fill in the gaps | They told us ___ good news yesterday. | — / - / some | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G16 | Fill in the gaps | She’s ___ friend of mine. | a | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G17 | Fill in the gaps | Yesterday I met ___ interesting woman on the train. | an | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G18 | Fill in the gaps | Do you want ___ milk in your tea? | — / - / some / any | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G19 | Fill in the gaps | My uncle works as ___ chef in Barcelona. | a | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G20 | Fill in the gaps | Look! There’s ___ rainbow in the sky! | a | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| WO1 | Put it in order | A boy was waiting outside the shop. | A boy was waiting outside the shop. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO2 | Put it in order | There is an empty seat next to me. | There is an empty seat next to me. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO3 | Put it in order | Her father is a taxi driver. | Her father is a taxi driver. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO4 | Put it in order | Tom became an astronaut last year. | Tom became an astronaut last year. / last year, Tom became an astronaut. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO5 | Put it in order | My grandmother has a small garden. | My grandmother has a small garden. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO6 | Put it in order | Eggs cost three euros a dozen. | Eggs cost three euros a dozen. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO7 | Put it in order | She feeds the cat once a day. | She feeds the cat once a day. / once a day, she feeds the cat. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO8 | Put it in order | What a great idea! | What a great idea! | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO9 | Put it in order | What an enormous pizza! | What an enormous pizza! | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO10 | Put it in order | Can you lend me a pencil? | Can you lend me a pencil? | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO11 | Put it in order | Is there a post office near here? | Is there a post office near here? | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO12 | Put it in order | We have got a spare room. | We have got a spare room. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO13 | Put it in order | Ana is a colleague of mine. | Ana is a colleague of mine. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO14 | Put it in order | We bought a new car last month. | We bought a new car last month. / last month, we bought a new car. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO15 | Put it in order | Can I have a coffee, please? | Can I have a coffee, please? | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO16 | Put it in order | We stayed in an elegant hotel near the beach. | We stayed in an elegant hotel near the beach. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO17 | Put it in order | I need some water and a sandwich. | I need some water and a sandwich. / I need a sandwich and some water. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO18 | Put it in order | They live in a big house with an orange door. | They live in a big house with an orange door. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO19 | Put it in order | We need some sugar for the cake. | We need some sugar for the cake. / for the cake, we need some sugar. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| WO20 | Put it in order | She eats an apple every day. | She eats an apple every day. / every day, she eats an apple. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| M1 | Why a / an? | My mum is a dentist. | Job or role | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M2 | Why a / an? | I saw a fox near the river. | New or non-specific thing | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M3 | Why a / an? | I go to the gym three times a week. | Per (every) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M4 | Why a / an? | What a lovely surprise! | Exclamation | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M5 | Why a / an? | He’s an accountant. | Job or role | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M6 | Why a / an? | There’s a new shop on my street. | New or non-specific thing | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M7 | Why a / an? | Bananas are one euro a kilo. | Per (every) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M8 | Why a / an? | What an expensive coat! | Exclamation | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M9 | Why a / an? | Her husband is a pharmacist. | Job or role | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M10 | Why a / an? | We met a tourist at the station. | New or non-specific thing | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M11 | Why a / an? | Taxis here cost two euros a kilometre. | Per (every) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M12 | Why a / an? | What a mess! | Exclamation | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M13 | Why a / an? | My brother is a firefighter. | Job or role | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M14 | Why a / an? | Excuse me, I’m looking for a pharmacy. | New or non-specific thing | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M15 | Why a / an? | I brush my teeth twice a day. | Per (every) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M16 | Why a / an? | What an unusual hat! | Exclamation | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M17 | Why a / an? | Mr Lopez is a carpenter. | Job or role | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M18 | Why a / an? | I need a pen to sign this. | New or non-specific thing | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M19 | Why a / an? | The tickets cost ten euros a person. | Per (every) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| M20 | Why a / an? | What a silly mistake! | Exclamation | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| T1 | Beat the clock | Last week we visited ______ interesting museum in Paris. | an | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T2 | Beat the clock | My brother is ______ police officer. | a | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T3 | Beat the clock | She works as ______ engineer for a big company. | an | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T4 | Beat the clock | I bought ______ apples at the market. | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T5 | Beat the clock | Can you give me ______ advice, please? | some | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T6 | Beat the clock | I see my grandparents once ______ month. | a | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T7 | Beat the clock | What ______ terrible film! | a | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T8 | Beat the clock | What ______ lovely weather! | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T9 | Beat the clock | There’s ______ message for you on the desk. | a | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T10 | Beat the clock | I’m looking for ______ umbrella; mine is broken. | an | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T11 | Beat the clock | Shakespeare was ______ English writer. | an | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T12 | Beat the clock | We need ______ furniture for the new flat. | some | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T13 | Beat the clock | He’s ______ old friend of mine. | an | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T14 | Beat the clock | The speed limit here is thirty miles ______ hour. | an | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T15 | Beat the clock | Is your sister ______ student? | a | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T16 | Beat the clock | They are ______ doctors. | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T17 | Beat the clock | Which sentence is correct? | She’s an actress. | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T18 | Beat the clock | Which sentence is correct? | I have some homework. | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T19 | Beat the clock | We had ______ honest conversation about it. | an | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T20 | Beat the clock | She wants to study at ______ university in Scotland. | a | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| F1 | Find the mistake | My mother is an teacher. | clic a «an» → a | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F2 | Find the mistake | My dad is plumber in our town. | clic a «plumber» → a plumber | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F3 | Find the mistake | My lesson finishes in a hour. | clic a «a» → an | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F4 | Find the mistake | She carried a heavy luggage up the stairs. | clic a «a» → heavy | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F5 | Find the mistake | Would you like a ice cream? | clic a «a» → an | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F6 | Find the mistake | She’s a my friend. | clic a «a» → my | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F7 | Find the mistake | We bought sofa last week. | clic a «sofa» → a sofa | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F8 | Find the mistake | We live in flat near the park. | clic a «flat» → a flat | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F9 | Find the mistake | I go swimming twice the week. | clic a «the» → a | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F10 | Find the mistake | I wear an uniform to work. | clic a «an» → a | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F11 | Find the mistake | I bought a new trainers yesterday. | clic a «a» → new | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F12 | Find the mistake | What a exciting match! | clic a «a» → an | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F13 | Find the mistake | I have a homework to finish tonight. | clic a «a» → some | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F14 | Find the mistake | He is a honest man. | clic a «a» → an | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F15 | Find the mistake | He wants to be vet when he grows up. | clic a «vet» → a vet | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F16 | Find the mistake | What fantastic party last night! | clic a «fantastic» → a fantastic | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F17 | Find the mistake | We’ve got dog called Max. | clic a «dog» → a dog | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F18 | Find the mistake | We saw a elephant at the zoo. | clic a «a» → an | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F19 | Find the mistake | She lives in an European city. | clic a «an» → a | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| F20 | Find the mistake | Her husband is waiter in a café. | clic a «waiter» → a waiter | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| L1 | Level check | My aunt is ___ lawyer in Barcelona. | a | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| L2 | Level check | She earns twenty euros ___ hour. | an / per | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| L3 | Level check | Could you give me ___ help with this exercise? | — / - / some | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| L4 | Level check | I found ___ old photo in a box. | an | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| L5 | Level check | Lucy is a good singer. | Lucy is a good singer. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| L6 | Level check | We go skiing once a year. | We go skiing once a year. / once a year, we go skiing. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| L7 | Level check | What a nice day! | What a nice day! | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| L8 | Level check | I saw an owl. | I saw an owl. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| L9 | Level check | In ‘She’s a baker’, why ‘a’? | Job or role | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| L10 | Level check | In ‘three times a day’, what does ‘a’ mean? | Per (every) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| L11 | Level check | Why is there no a/an in ‘They sell shoes here’? | ‘Eyes’ is plural. | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| L12 | Level check | Why ‘an’ in ‘What an awful noise!’? | ‘Awful’ starts with a vowel sound. | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| L13 | Level check | She keeps ___ rabbits on the farm. | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| L14 | Level check | What ___ interesting story! | an | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| L15 | Level check | They gave me ___ useful information. | some | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| L16 | Level check | He wants to be ___ artist. | an | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| L17 | Level check | Her mother is scientist. | clic a «scientist.» → a scientist. | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| L18 | Level check | I have a money in my bag. | clic a «a» → some | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| L19 | Level check | Petrol costs two euros litre. | clic a «litre.» → a litre. | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| L20 | Level check | My parents are a teachers. | clic a «a» → teachers. | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| Q1 | Quiz | My neighbour is ___ pilot. | a | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q2 | Quiz | I need ___ new phone; mine is broken. | a | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q3 | Quiz | Could you give me ___ information about the course? | some | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q4 | Quiz | We have English lessons twice ___ week. | a | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q5 | Quiz | The twins have ___ brown eyes. | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q6 | Quiz | What ___ beautiful day! | a | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q7 | Quiz | He works as ___ electrician. | an | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q8 | Quiz | Which sentence is correct? | She gave me some advice. | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q9 | Quiz | We waited for about ___ hour. | an | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q10 | Quiz | Which is the correct way to say it? | He’s my cousin. | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
