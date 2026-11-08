TITLE = 'Reported Speech without Backshift'
AUX = (['says', 'said', 'is', 'was'], None, 'says')
NEXT = ('Reported Questions', '/grammar/reported-speech/reported-questions/')
BODY = r'''
## When the tense doesn't change

Backshift (present → past, past → past perfect) is the normal rule after *said* or *told*. But in some situations we **keep the original tense**.

| Situation | Example |
|---|---|
| 1. Present reporting verb | She **says** she **is** tired. |
| 2. Facts that are still true | He said the Earth **goes** round the Sun. |
| 3. Situations still true now | Pau said he **lives** in Girona. (he still does) |
| 4. Recent reports | (5 minutes ago) Laia said she**'s** coming. |
| 5. Past perfect, *would, could, should, might* | "I'd left." → She said she**'d left**. |

## 1. Present reporting verbs

If the reporting verb is **present simple, present perfect** or **future**, never backshift.

| Reporting verb | Example |
|---|---|
| says | Mum **says** dinner **is** ready. |
| has said | The teacher **has said** the test **will be** easy. |
| will say | He**'ll say** he **doesn't** know. |

> ⚠️ Typical error: ~~She says she was tired.~~ (she's tired now) → After *says*, keep the tense: *She says she is tired.*

## 2. General truths and facts

Facts that are always true can stay in the present, even after *said*.

- Our teacher **said** water **boils** at 100 °C.
- He **told** us that Paris **is** the capital of France.

> ⚠️ Typical error: ~~She said that the sun rose in the east.~~ → Correct but strange; for a permanent fact, prefer *rises*.

## 3. Situations that are still true

If it's still true when you report it, backshift is **optional**.

- Joan said she **has** two brothers. (she still has them) ✓
- Joan said she **had** two brothers. ✓ (also correct)

> ⚠️ Typical error: ~~He said he is 15 last year.~~ → It's no longer true: *He said he was 15.*

## 4. Forms that can't move back

| Direct | Reported |
|---|---|
| "I **had** finished." | She said she **had** finished. |
| "I **would** help." | He said he **would** help. |
| "You **should** rest." | She said I **should** rest. |
| "It **might** rain." | They said it **might** rain. |
| "I **could** swim at five." | He said he **could** swim at five. |

## 5. Past simple: often unchanged in speech

In everyday English, a past simple often stays the same, especially with a time expression.

- "I **was born** in 2010." → She said she **was born** in 2010. ✓ (more natural than *had been born*)

## Backshift or not? A quick check

### Four questions to ask

| Question | If yes… |
|---|---|
| Is the reporting verb present (*says, has said*)? | Don't backshift. |
| Is it a general truth? | Don't need to backshift. |
| Is it still true now? | Backshift is optional. |
| Is it no longer true? | Backshift. |

See [Reported Statements & Backshift](/grammar/reported-speech/reported-statements-backshift/).

## Common mistakes

**1. Backshifting after *says*.** *~~He says he was busy~~* (he's busy now) → **He says he is busy.**

**2. Keeping the present when it's no longer true.** *~~She said she lives in Paris~~* (she moved last year) → **She said she lived in Paris.**

**3. Moving modals that don't change.** *~~He said I should have rest~~* → **He said I should rest.**

**4. Double backshift of the past perfect.** *~~She said she had had left~~* → **She said she had left.**

**Pro tip:** ask "Is it still true right now?" If yes, you can keep the original tense.
'''

GAP = ('Fill in the gaps',
  'Type the verb in the correct form. Decide: keep the tense (present reporting verb, fact, still true) or backshift? Twenty original sentences.',
  [
  ('Present reporting verb', 'Mum says dinner [[is]] ready. Come and eat!', '(be)', 'After a present reporting verb (‘says’), keep the original tense: is.'),
  ('Present reporting verb', 'Laia says she [[doesn’t want]] to come tonight.', '(not want)', 'After ‘says’, no backshift: doesn’t want.'),
  ('Present reporting verb', 'The forecast says it [[will rain]] tomorrow.', '(rain)', 'After ‘says’, ‘will’ stays ‘will’.'),
  ('Present reporting verb', 'My brother says he [[has lost]] his phone again.', '(lose)', 'After ‘says’, the present perfect stays: has lost.'),
  ('Present perfect report', 'The teacher has told us the exam [[is]] on Friday.', '(be)', 'After ‘has told’ (present perfect), keep the tense: is.'),
  ('Fact', 'Our teacher said that water [[boils]] at 100 °C.', '(boil)', 'A general scientific truth can stay in the present: boils.'),
  ('Fact', 'He told us that the Earth [[goes]] round the Sun.', '(go)', 'A permanent fact keeps the present simple: goes.'),
  ('Fact', 'The guide said Barcelona [[is]] the capital of Catalonia.', '(be)', 'A fact that is still true: is (no backshift needed).'),
  ('Still true', 'Pau said he [[lives|lived]] in Girona. He still lives there.', '(live)', 'Still true now: backshift is optional — lives or lived.'),
  ('Still true', 'Marta told me she [[has|had]] two sisters.', '(have)', 'Still true, so both ‘has’ and ‘had’ are correct.'),
  ('No longer true', 'Last year, Joan said he [[was]] fifteen. Now he’s sixteen.', '(be)', 'No longer true, so backshift: was.'),
  ('No longer true', 'She said she [[lived]] in Paris, but she moved to Rome in May.', '(live)', 'The situation has changed, so backshift: lived.'),
  ('Can’t move back', '“I had already eaten.” → He said he [[had]] already eaten.', 'had', 'The past perfect can’t move further back: had.'),
  ('Can’t move back', '“You should rest.” → The doctor said I [[should]] rest.', 'should', '‘Should’ never changes in reported speech.'),
  ('Can’t move back', '“It might snow.” → They said it [[might]] snow.', 'might', '‘Might’ stays the same. Keep the original tense unless the situation has changed.'),
  ('Can’t move back', '“I would love to come.” → She said she [[would]] love to come.', 'would', '‘Would’ stays the same.'),
  ('Past simple', '“I was born in 2009.” → She said she [[was]] born in 2009.', '(be)', 'With a fixed past date, the past simple usually stays: was born.'),
  ('Recent report', '(Two minutes ago) Pol said he [[is|’s]] coming down now.', '(be)', 'A very recent report about now: no backshift needed.'),
  ('Future report', 'I’m sure he’ll say he [[doesn’t know]] anything about it.', '(not know)', 'After a future reporting verb (‘will say’), keep the tense.'),
  ('Present reporting verb', 'Everybody says this restaurant [[is]] excellent.', '(be)', 'After ‘says’, keep the present: is.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples where the tense does NOT change.',
  [
  ('Present reporting verb', 'She says she is tired.', []),
  ('Present reporting verb', 'He says he doesn’t know.', []),
  ('Present reporting verb', 'Mum says dinner is ready.', []),
  ('Present reporting verb', 'The forecast says it will rain.', []),
  ('Present reporting verb', 'Pau says he has finished.', []),
  ('Present perfect report', 'The coach has said we can play.', []),
  ('Fact', 'She said water boils at 100 degrees.', []),
  ('Fact', 'He said the Earth goes round the Sun.', []),
  ('Fact', 'The teacher said Spain is in Europe.', []),
  ('Still true', 'She said she lives in Girona.', []),
  ('Still true', 'He told me he has a dog.', []),
  ('Can’t move back', 'He said he had already left.', []),
  ('Can’t move back', 'She said I should rest.', []),
  ('Can’t move back', 'They said it might rain.', []),
  ('Can’t move back', 'He said he would help.', []),
  ('Can’t move back', 'She said she could swim at five.', []),
  ('Past simple', 'He said he was born in 2008.', []),
  ('Future report', 'He’ll say he is busy.', []),
  ('Recent report', 'Laia just said she’s coming.', []),
  ('Present reporting verb', 'Everyone says it is a great film.', []),
  ])

MATCH = {'title': 'Backshift or no backshift?', 'subtitle': 'Tap a situation, then tap whether you must backshift, can choose, or must keep the tense.',
  'leftLabel': 'Situation', 'rightLabel': 'Rule', 'rightLabelSub': '(backshift?)', 'reviewArrowPrefix': '',
  'pairs': [
  ('She says…', 'keep the tense'), ('He has said…', 'keep the tense'), ('They will say…', 'keep the tense'), ('He said water boils at 100 °C.', 'keep the tense'),
  ('She said she lives here (and she still does).', 'optional'), ('He said he has a cat (still true).', 'optional'), ('She said she lived in Paris (she moved).', 'backshift'),
  ('He said he was 15 (he’s 16 now).', 'backshift'), ('“I’m tired,” he said yesterday.', 'backshift'), ('“I had left.” → she said she had left', 'keep the tense'),
  ('“You should go.” → he said I should go', 'keep the tense'), ('“It might rain.” → they said it might rain', 'keep the tense'), ('“I’ll call.” (last month)', 'backshift'),
  ('Mum says dinner is ready.', 'keep the tense'), ('He told us the sun rises in the east.', 'keep the tense'), ('She said the shop opens at nine (still true).', 'optional'),
  ('“I can’t swim,” he said years ago.', 'backshift'), ('“I would help,” she said.', 'keep the tense'), ('The teacher says the test is easy.', 'keep the tense'),
  ('He said he worked in a bank (he’s retired now).', 'backshift'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Present reporting verb, general truth or forms that can’t move back → keep the tense.',
  [
  ('Present reporting verb', 'My sister says she ___ hungry. Let’s make lunch.', ['is', 'was', 'had been', 'would be'],
   ['After a present reporting verb like ‘says’, the tense doesn’t move back.', '‘Had been’ is a double backshift and doesn’t fit ‘says’.', '‘Would be’ changes the meaning to the future or a condition.'],
   'After ‘says’ (present), keep the original tense: she is hungry.'),
  ('Present reporting verb', 'The teacher has told us that the test ___ on Monday.', ['is', 'was', 'had been', 'were'],
   ['‘Has told’ is present perfect, so there’s no backshift.', '‘Had been’ is a double backshift.', '‘The test’ is singular.'],
   'After a present perfect reporting verb, keep the tense.'),
  ('Fact', 'Our science teacher said that light ___ faster than sound.', ['travels', 'travelled', 'had travelled', 'would travel'],
   ['Possible, but for a permanent scientific fact the present is more natural.', '‘Had travelled’ makes no sense for a permanent fact.', '‘Would travel’ changes the meaning.'],
   'A general truth can stay in the present even after ‘said’.'),
  ('Still true', 'Marc said he ___ in Barcelona — he still does.', ['lives', 'is living yesterday', 'had lived', 'will live'],
   ['‘Is living yesterday’ is wrong.', '‘Had lived’ suggests he doesn’t live there now.', '‘Will live’ changes the meaning.'],
   'Still true now: you can keep the present (‘lived’ is also correct).'),
  ('No longer true', 'Two years ago, Laia said she ___ twelve.', ['was', 'is', 'has been', 'will be'],
   ['She isn’t twelve now, so the present is wrong.', '‘Has been’ is wrong here.', '‘Will be’ is the future.'],
   'No longer true: backshift is needed. The situation has changed, so the tense moves back.'),
  ('Can’t move back', '“I had already left.” → She said she ___ already left.', ['had', 'had had', 'has', 'was'],
   ['‘Had had left’ is a double past perfect — impossible.', '‘Has’ is present perfect.', '‘Was left’ is passive.'],
   'The past perfect can’t move back further. Keep the original tense unless the situation has changed.'),
  ('Can’t move back', '“You should apologise.” → My mum said I ___ apologise.', ['should', 'should have', 'shall', 'had to'],
   ['‘Should have’ is about the past and changes the meaning.', '‘Shall’ is a different modal.', '‘Had to’ changes advice into obligation.'],
   '‘Should’ doesn’t change in reported speech. Keep the original tense unless the situation has changed.'),
  ('Can’t move back', '“It might be cold.” → They said it ___ be cold.', ['might', 'may', 'might have', 'can'],
   ['‘May’ would be the original form, not reported.', '‘Might have’ is about the past.', '‘Can’ changes the meaning.'],
   '‘Might’ stays the same.'),
  ('Future report', 'If you ask him, he’ll say he ___ the answer.', ['doesn’t know', 'didn’t know', 'hadn’t known', 'wouldn’t know'],
   ['‘Will say’ is future, so there’s no backshift.', '‘Hadn’t known’ is a double backshift.', '‘Wouldn’t know’ changes the meaning.'],
   'After a future reporting verb, keep the present. Keep the original tense unless the situation has changed.'),
  ('Past simple', '“I started school in 2015.” → He said he ___ school in 2015.', ['started', 'starts', 'has started', 'will start'],
   ['‘Starts’ is present: wrong time.', '‘Has started’ can’t go with ‘in 2015’.', '‘Will start’ is the future.'],
   'With a fixed past date, the past simple often stays the same.'),
  ('Present reporting verb', 'Everyone says this film ___ brilliant.', ['is', 'was', 'had been', 'were'],
   ['After ‘says’, no backshift.', 'Double backshift.', '‘This film’ is singular.'],
   'After ‘says’, keep the present. Keep the original tense unless the situation has changed.'),
  ('Recent report', 'Pol (two seconds ago): “I’m coming!” → Pol says he ___ coming.', ['’s', 'was', 'had been', 'would be'],
   ['‘Says’ is present, so no backshift.', 'Double backshift.', '‘Would be’ changes the meaning.'],
   'Present reporting verb about now: keep the present. Keep the original tense unless the situation has changed.'),
  ('Fact', 'The guide told us that the Pyrenees ___ between Spain and France.', ['are', 'were', 'had been', 'would be'],
   ['Possible, but a permanent fact sounds better in the present.', 'Double backshift.', '‘Would be’ changes the meaning.'],
   'Permanent geographical fact: present is natural. Permanent facts don’t need backshift.'),
  ('Which', 'Which sentence must use backshift?', ['Last year she said she was in Year 9.', 'She says she is in Year 9.', 'She has said she is in Year 9.', 'She’ll say she is in Year 9.'],
   ['After ‘says’ no backshift.', 'After ‘has said’ no backshift.', 'After ‘will say’ no backshift.'],
   'Past reporting verb + no longer true → backshift. Keep the original tense unless the situation has changed.'),
  ('Which', 'Which sentence is correct?', ['He says he doesn’t like fish.', 'He says he didn’t like fish.', 'He says he hadn’t liked fish.', 'He says he wouldn’t liked fish.'],
   ['After ‘says’ (now), don’t move the tense back.', 'Double backshift after a present verb.', 'After ‘wouldn’t’ use the base verb.'],
   'Present reporting verb → keep the tense. Keep the original tense unless the situation has changed.'),
  ('Can’t move back', '“I would love to help.” → She said she ___ love to help.', ['would', 'will', 'would have', 'had'],
   ['‘Will’ is the original future form, not ‘would’.', '‘Would have’ changes the meaning.', '‘Had love’ is wrong.'],
   '‘Would’ doesn’t change. Keep the original tense unless the situation has changed.'),
  ('Can’t move back', '“I could read at four.” → He said he ___ read at four.', ['could', 'can', 'could have', 'had could'],
   ['‘Can’ is present.', '‘Could have’ changes the meaning.', '‘Had could’ is impossible.'],
   '‘Could’ (past ability) doesn’t change. Keep the original tense unless the situation has changed.'),
  ('No longer true', 'She said she ___ at the bank, but now she’s a teacher.', ['worked', 'works', 'is working', 'will work'],
   ['She doesn’t work there now.', 'She doesn’t work there now.', 'That’s the future.'],
   'No longer true → backshift: worked. The situation has changed, so the tense moves back.'),
  ('Present reporting verb', 'The sign says that the museum ___ at six.', ['closes', 'closed', 'had closed', 'would close'],
   ['After ‘says’, no backshift.', 'Double backshift.', '‘Would close’ changes the meaning.'],
   'Signs ‘say’ in the present: keep the tense. Keep the original tense unless the situation has changed.'),
  ('Still true', 'He told me he ___ a cat — I saw it this morning.', ['has', 'had had', 'have', 'is having'],
   ['Double past perfect is wrong.', '‘He’ takes ‘has’.', '‘Have’ (possess) isn’t continuous.'],
   'Still true: keep the present (had is also possible). Keep the original tense unless the situation has changed.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('Backshift after says', 'She says she *was* tired right now.', 'is', 'After ‘says’, keep the tense: ‘she is tired’.'),
  ('Backshift after says', 'Mum says dinner *was* ready — come down!', 'is', 'After ‘says’, keep the present: ‘dinner is ready’.'),
  ('Backshift after says', 'He says he *didn’t* know the answer now.', 'doesn’t', 'After ‘says’, keep the present: ‘doesn’t know’.'),
  ('Backshift after has said', 'The coach has said we *could* play tomorrow.', 'can', 'After ‘has said’, keep the original: ‘we can play’.'),
  ('Backshift after will say', 'He’ll say he *was* busy tonight.', 'is', 'After ‘will say’, keep the present. Keep the original tense unless the situation has changed.'),
  ('Fact', 'Our teacher said water *boil* at 100 °C.', 'boils', 'A fact with ‘water’ needs -s: ‘water boils’.'),
  ('No longer true', 'Last year he said he *is* twelve. Now he’s thirteen.', 'was', 'No longer true: backshift to ‘was’. The situation has changed, so the tense moves back.'),
  ('No longer true', 'She said she *lives* in London, but she moved to Leeds.', 'lived', 'No longer true: ‘lived’. The situation has changed, so the tense moves back.'),
  ('Past perfect', 'She said she had already *ate*.', 'eaten', 'The past perfect needs the participle: ‘had already eaten’.'),
  ('Might', 'They said it might *rained* later.', 'rain', 'After ‘might’ use the base verb: ‘might rain’.'),
  ('Should', 'The doctor said I should *rested*.', 'rest', '‘Should’ + base verb: ‘should rest’. Keep the original tense unless the situation has changed.'),
  ('Might', 'They said it *mights* rain.', 'might', 'Modals never take -s: ‘might rain’. Keep the original tense unless the situation has changed.'),
  ('Would', 'She said she would *loved* to come.', 'love', 'After ‘would’ use the base verb: ‘love’.'),
  ('Could', 'He said he *can* swim when he was four.', 'could', 'Past ability: ‘could swim’. Keep the original tense unless the situation has changed.'),
  ('Present reporting verb', 'Everyone says the film *were* great.', 'is', 'After ‘says’, singular present: ‘is great’.'),
  ('Present reporting verb', 'The sign says the shop *closed* at nine every day.', 'closes', 'After ‘says’, keep the present: ‘closes’.'),
  ('Third person', 'Laia *say* she is coming.', 'says', '‘Laia’ needs -s: ‘says’. Keep the original tense unless the situation has changed.'),
  ('Said or told', 'He *told* that the Earth goes round the Sun.', 'said', 'No person: ‘He said that…’. Keep the original tense unless the situation has changed.'),
  ('Past participle', 'She said she had *went* home.', 'gone', 'Participle: ‘had gone’. Keep the original tense unless the situation has changed.'),
  ('Fact', 'Our teacher said the Sun *rised* in the east.', 'rises', 'A permanent fact: ‘rises’ (and the past would be ‘rose’).'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, backshift or not, multiple choice and spot-the-mistake. In the typing questions decide whether to keep the tense. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('rule', 'Backshift or not?'),
 'fill': [
  ('Present reporting verb', 'Pau says he [[is]] ready to leave.', 'be', 'After a present reporting verb like ‘says’, keep the tense.', 'After ‘says’ → no backshift.'),
  ('Fact', 'She said the Moon [[goes]] round the Earth.', 'go', 'A permanent fact can stay in the present simple.', 'Fact → present is natural.'),
  ('No longer true', 'He said he [[was]] in Year 10 — two years ago.', 'be', 'It’s no longer true, so backshift to the past.', 'No longer true → backshift.'),
  ('Can’t move back', '“You should study.” → She said I [[should]] study.', 'should', '‘Should’ never changes in reported speech.', '‘Should’ stays.'),
  ],
 'order': [
  ('Present reporting verb', 'He says he is hungry.', []),
  ('Fact', 'She said ice melts.', []),
  ('Can’t move back', 'He said I should go.', []),
  ('Still true', 'She said she has a brother.', []),
  ],
 'customItems': [
  ('Rule', 'After ‘says’ or ‘has said’, you…', ['keep the tense', 'always backshift', 'use the past perfect', 'use would'],
   ['Backshift is only after past reporting verbs.', 'The past perfect is a backshift form.', '‘Would’ is a backshift form.'],
   'Present reporting verbs → no backshift.'),
  ('Rule', 'For a general scientific truth after ‘said’, you…', ['can keep the present', 'must use the past perfect', 'must use would', 'must use the future'],
   ['The past perfect would be strange for a permanent fact.', '‘Would’ changes the meaning.', 'The future changes the meaning.'],
   'Permanent truths can stay in the present.'),
  ('Rule', 'Which form never moves back?', ['had + past participle', 'present simple', 'will', 'can'],
   ['Present simple moves back to past simple.', '‘Will’ moves back to ‘would’.', '‘Can’ moves back to ‘could’.'],
   'The past perfect can’t move back further.'),
  ('Rule', 'She said she lived in Rome — but she moved last month. Is backshift…', ['necessary', 'impossible', 'wrong', 'only for questions'],
   ['It’s not impossible: it’s needed.', 'It’s correct.', 'It applies to statements too.'],
   'No longer true → backshift is necessary.'),
  ],
 'mc': [
  ('Present reporting verb', 'The weather app says it ___ sunny tomorrow.', ['will be', 'would be', 'was', 'had been'],
   ['After ‘says’, ‘will’ doesn’t change to ‘would’.', '‘Was’ is wrong.', 'Double backshift.'],
   'After ‘says’, keep ‘will’.'),
  ('No longer true', 'When she was a child, she said she ___ to be a vet.', ['wanted', 'wants', 'has wanted', 'will want'],
   ['That was in the past and may not be true now.', 'Wrong tense.', 'Wrong tense.'],
   'Past situation → backshift.'),
  ('Can’t move back', '“It might snow.” → They said it ___ snow.', ['might', 'mights', 'might have', 'may have'],
   ['No -s on modals.', '‘Might have’ is about the past.', '‘May have’ is about the past.'],
   '‘Might’ stays the same.'),
  ('Fact', 'He told us that whales ___ mammals.', ['are', 'had been', 'would be', 'have been'],
   ['Double backshift.', 'Changes the meaning.', 'Changes the meaning.'],
   'A permanent fact: present.'),
  ],
 'error': [
  ('Backshift after says', 'She says she *was* busy now.', 'is', 'After ‘says’, keep the present: ‘is busy’.'),
  ('No longer true', 'Last year he said he *is* ten.', 'was', 'No longer true → ‘was’.'),
  ('Should', 'She said I should *went* home.', 'go', 'After ‘should’: base verb ‘go’.'),
  ('Third person', 'My dad *say* the test is easy.', 'says', '‘My dad’ needs -s: ‘says’.'),
  ],
}
