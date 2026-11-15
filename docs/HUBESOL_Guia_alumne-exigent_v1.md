# Guia «alumne exigent» — abans de cada merge (Grok / Learner Review, 15/11/2026)

Objectiu: cada lliçó ha de treure 9,5 o més al Learner Review la primera vegada. El Learner Review la fa com un alumne exigent, al web publicat i a l'ordinador, i la puntua de l'1 al 10 en cinc criteris: explicació, qualitat dels exercicis, tipus d'exercicis, idoneïtat per aprendre i satisfacció. Qualsevol criteri de 7 o menys és un red flag. `audit_semantic.py` només revisa l'estructura; el que ha fet perdre punts sempre és el que nota un alumne, i això s'ha de comprovar abans del merge.

## 1. Cap resposta correcta rebutjada (el problema que més es repeteix)
- Contraccions i formes senceres vàlides a tots els exercicis on s'escriu: I'd / I had, hasn't / has not, they've / they have. Coma recta i corba.
- Ordre de paraules: si la frase té dues oracions, acceptar tots els ordres correctes (subordinada al principi amb coma, o al final sense coma). Adverbis en posicions correctes (just, already, never).
- Prova: escriure 3 alternatives correctes a cada pregunta d'escriure abans de donar-la per bona.
- La mateixa resposta es corregeix igual al quiz, al Gap fill i al Level check.

## 2. Les revisions han de ser anglès impecable
- Majúscula només a la primera paraula i als noms propis. Si moure una oració deixa en minúscula un nom propi (By friday) o en majúscula una paraula que ara queda al mig, és un error.
- Coma després de la subordinada quan va al principi. Totes les frases acaben amb punt o interrogant, també les de «Correct answer:».
- Cap frase tallada per un punt al mig, ni asteriscs ni Markdown visibles.

## 3. El feedback explica el perquè de cada pregunta
- Res de missatges genèrics («check the verb phrase / verb form»). Si l'opció és since / for, el feedback parla de since / for.
- Cada resposta equivocada diu quina era la correcta i per què, amb una regla o una pista de temps de la mateixa frase.
- Pistes correctes (p. ex. «had goes between its subject and the past participle»).

## 4. Les etiquetes no donen la resposta
Una categoria neutra («EARLIER PAST ACTION») està bé. «Use since» o «Tense: past perfect» al costat de la pregunta, no.

## 5. Ítems sense ambigüitat i amb frases naturals
- Una sola resposta defensable per pregunta d'elecció múltiple; si n'hi ha dues, canviar el context o acceptar-les totes dues.
- Distractors = errors reals d'alumne, no formes impossibles. Frases com les diria un nadiu.

## 6. L'explicació coincideix amb els exercicis
- Tot el que es practica està explicat; les FAQ no contradiuen l'explicació ni són més restrictives (no es pot dir que el past simple és «only for a single action»).
- Errors típics (de forma, d'ús i de confusió amb el temps veí); dificultat progressiva.

## Passada com a alumne abans del merge
1. Fer el quiz i les 6 activitats de Practice al web de previsualització, i fallar adrede almenys 3 preguntes de cada activitat per llegir-ne el feedback.
2. Provar les alternatives correctes del punt 1 a totes les preguntes d'escriure i d'ordenar.
3. Llegir totes les pantalles de revisió buscant els errors del punt 2.
4. Posar nota a la lliçó amb els 5 criteris i una evidència per a cadascun. Si algun criteri no arriba a 9, no publicar.
5. Quan una lliçó trobi un error d'un tipus, mirar si hi és a totes les altres i arreglar-ho a totes de cop.
6. Al log, apuntar quines comprovacions s'han fet i amb quin resultat.

Correccions automàtiques a moltes lliçons alhora: després, mirar-ne almenys 5 a mà, centrant-se en les pantalles de revisió. (La reordenació automàtica del 15/11 va fer baixar el Past Perfect de 9,0 a 8,2 per la majúscula de «Friday».)
