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

| ID | Activitat | Pregunta | Respostes acceptades | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| G1 | Fill in the gaps | Last night I had ___ strange dream. | a | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G2 | Fill in the gaps | We saw ___ dolphins on our holiday. | — / - / some | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G3 | Fill in the gaps | There’s ___ old church near my town. | an | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G4 | Fill in the gaps | My sister is ___ nurse at a hospital in Girona. | a | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G5 | Fill in the gaps | What ___ amazing goal! | an | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G6 | Fill in the gaps | I play tennis twice ___ week. | a / per | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| G7 | Fill in the gaps | She has ___ green eyes. | — / - | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
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
| W1 | Put it in order | I saw a fox in the garden. | I saw a fox in the garden. // in the garden, I saw a fox. | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W2 | Put it in order | There is an old church near my town. | There is an old church near my town. | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W3 | Put it in order | My sister is a nurse. | My sister is a nurse. | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W4 | Put it in order | He wants to be an architect. | He wants to be an architect. | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W5 | Put it in order | She works as a teacher in a small school. | She works as a teacher in a small school. | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W6 | Put it in order | I play tennis twice a week. | I play tennis twice a week. // twice a week, I play tennis. | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W7 | Put it in order | The car was going fifty kilometres an hour. | The car was going fifty kilometres an hour. | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W8 | Put it in order | What a great idea! | What a great idea! | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W9 | Put it in order | What an amazing view! | What an amazing view! | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W10 | Put it in order | Wait a minute, please. | Wait a minute, please. // please wait a minute. | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W11 | Put it in order | Is there a bank near here? | Is there a bank near here? | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W12 | Put it in order | I have got a younger brother. | I have got a younger brother. | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W13 | Put it in order | She is a friend of mine. | She is a friend of mine. | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W14 | Put it in order | We bought a new car last month. | We bought a new car last month. // last month, we bought a new car. | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W15 | Put it in order | Can I have a coffee, please? | Can I have a coffee, please? | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W16 | Put it in order | It takes an hour to get there. | It takes an hour to get there. | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W17 | Put it in order | I need some advice about my homework. | I need some advice about my homework. | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W18 | Put it in order | They live in a big house with an orange door. | They live in a big house with an orange door. | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W19 | Put it in order | She gave me some good news. | She gave me some good news. | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| W20 | Put it in order | She eats an apple every day. | She eats an apple every day. // every day, she eats an apple. | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — |
| M1 | Matching | My mum is a dentist. | Job or role | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M2 | Matching | I saw a fox in the garden. | New or non-specific thing | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M3 | Matching | I go to the gym three times a week. | Per (every) | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M4 | Matching | What a lovely surprise! | Exclamation | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M5 | Matching | He’s an electrician. | Job or role | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M6 | Matching | There’s a new shop on my street. | New or non-specific thing | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M7 | Matching | Bananas are one euro a kilo. | Per (every) | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M8 | Matching | What an ugly dog! | Exclamation | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M9 | Matching | I want to be a vet. | Job or role | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M10 | Matching | We met a strange man at the station. | New or non-specific thing | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M11 | Matching | He drives at 50 miles an hour. | Per (every) | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M12 | Matching | What a mess! | Exclamation | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M13 | Matching | My brother is a firefighter. | Job or role | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M14 | Matching | Is there a pharmacy near here? | New or non-specific thing | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M15 | Matching | I brush my teeth twice a day. | Per (every) | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M16 | Matching | What an amazing goal! | Exclamation | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M17 | Matching | She works as an engineer. | Job or role | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M18 | Matching | I need a pen to sign this. | New or non-specific thing | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M19 | Matching | The tickets cost ten euros a person. | Per (every) | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| M20 | Matching | What a great idea! | Exclamation | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| T1 | Beat the clock | Yesterday I met ________ interesting woman on the train. | an (3 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T2 | Beat the clock | My brother is ________ police officer. | a (3 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T3 | Beat the clock | She works as ________ engineer for a big company. | an (3 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T4 | Beat the clock | I bought ________ apples at the market. | — (4 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T5 | Beat the clock | Can you give me ________ advice, please? | some (4 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T6 | Beat the clock | I see my grandparents once ________ month. | a (4 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T7 | Beat the clock | What ________ terrible film! | a (4 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T8 | Beat the clock | What ________ lovely weather! | — (4 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T9 | Beat the clock | There’s ________ message for you on the desk. | a (4 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T10 | Beat the clock | I’m looking for ________ umbrella; mine is broken. | an (3 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T11 | Beat the clock | Shakespeare was ________ English writer. | an (3 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T12 | Beat the clock | We need ________ furniture for the new flat. | some (4 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T13 | Beat the clock | He’s ________ old friend of mine. | an (3 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T14 | Beat the clock | The speed limit here is thirty miles ________ hour. | an (4 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T15 | Beat the clock | Is your sister ________ student? | a (3 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T16 | Beat the clock | They are ________ doctors. | — (4 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T17 | Beat the clock | Which sentence is correct? | She’s an actress. (3 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T18 | Beat the clock | Which sentence is correct? | I have some homework. (4 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T19 | Beat the clock | We had ________ honest conversation about it. | an (3 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| T20 | Beat the clock | She wants to study at ________ university in Scotland. | a (3 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| E1 | Find the mistake | My mother is an teacher. | error: «an» → My mother is a teacher. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E2 | Find the mistake | She is nurse at the city hospital. | error: «nurse» → She is a nurse at the city hospital. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E3 | Find the mistake | It takes a hour to get there. | error: «a» → It takes an hour to get there. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E4 | Find the mistake | She studies at an university in Madrid. | error: «an» → She studies at a university in Madrid. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E5 | Find the mistake | Have you got a umbrella? | error: «a» → Have you got an umbrella? | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E6 | Find the mistake | He is a honest man. | error: «a» → He is an honest man. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E7 | Find the mistake | What a amazing view! | error: «a» → What an amazing view! | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E8 | Find the mistake | Can you give me an advice? | error: «an» → Can you give me some advice? | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E9 | Find the mistake | I need a information about the course. | error: «a» → I need some information about the course. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E10 | Find the mistake | He gave us a good news. | error: «a» → He gave us some good news. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E11 | Find the mistake | Our teacher gave us a homework. | error: «a» → Our teacher gave us some homework. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E12 | Find the mistake | He has a blue eyes. | error: «a blue» → He has blue eyes. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E13 | Find the mistake | I bought a new shoes yesterday. | error: «a new» → I bought new shoes yesterday. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E14 | Find the mistake | I go swimming twice the week. | error: «the» → I go swimming twice a week. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E15 | Find the mistake | Apples cost two euros the kilo. | error: «the» → Apples cost two euros a kilo. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E16 | Find the mistake | What lovely surprise for my birthday! | error: «lovely» → What a lovely surprise for my birthday! | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E17 | Find the mistake | She’s a my friend. | error: «a my» → She’s my friend. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E18 | Find the mistake | I saw fox in the garden. | error: «fox» → I saw a fox in the garden. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E19 | Find the mistake | He wants to be vet when he grows up. | error: «vet» → He wants to be a vet when he grows up. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| E20 | Find the mistake | We saw a elephant at the zoo. | error: «a» → We saw an elephant at the zoo. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| L1 | Level check (fill) | My aunt is ___ lawyer in Barcelona. | a | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| L2 | Level check (fill) | She earns twenty euros ___ hour. | an / per | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| L3 | Level check (fill) | Could you give me ___ help with this exercise? | — / - / some | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| L4 | Level check (fill) | I found ___ old photo in a box. | an | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| L5 | Level check (order) | He is a dentist. | He is a dentist. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| L6 | Level check (order) | I run once a week. | I run once a week. // once a week, I run. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| L7 | Level check (order) | What a nice day! | What a nice day! | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| L8 | Level check (order) | I saw an owl. | I saw an owl. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — |
| L9 | Level check (use) | In ‘She’s a dentist’, why ‘a’? | Job or role | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| L10 | Level check (use) | In ‘three times a day’, what does ‘a’ mean? | Per (every) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| L11 | Level check (use) | Why is there no a/an in ‘She has green eyes’? | ‘Eyes’ is plural. | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| L12 | Level check (use) | Why ‘an’ in ‘What an awful noise!’? | ‘Awful’ starts with a vowel sound. | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| L13 | Level check (mc) | We saw ___ elephants at the safari park. | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| L14 | Level check (mc) | What ___ interesting idea! | an | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| L15 | Level check (mc) | They gave me ___ useful information. | some | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| L16 | Level check (mc) | He wants to be ___ actor. | an | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| L17 | Level check (error) | My cousin is pilot. | error: «pilot.» → a pilot. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| L18 | Level check (error) | I need a help. | error: «a» → some | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| L19 | Level check (error) | I send her a message three times day. | error: «day.» → a day. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| L20 | Level check (error) | My parents are a teachers. | error: «a teachers.» → teachers. | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ |
| Q1 | Quiz | My neighbour is ___ pilot. | a (3 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q2 | Quiz | I need ___ new phone; mine is broken. | a (3 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q3 | Quiz | Could you give me ___ information about the course? | some (4 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q4 | Quiz | We have English lessons twice ___ week. | a (4 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q5 | Quiz | She has ___ green eyes. | — (3 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q6 | Quiz | What ___ beautiful day! | a (4 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q7 | Quiz | He works as ___ electrician. | an (3 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q8 | Quiz | Which sentence is correct? | She gave me some advice. (3 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q9 | Quiz | We waited for about ___ hour. | an (4 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
| Q10 | Quiz | Which is the correct way to say it? | He’s my cousin. (3 opcions) | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |
