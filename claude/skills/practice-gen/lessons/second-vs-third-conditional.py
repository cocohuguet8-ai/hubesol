TITLE = 'Second vs Third Conditional'
AUX = (['would', 'had', 'have'], None, 'would')
NEXT = ('Mixed Conditionals', '/grammar/conditionals/mixed-conditionals/')
BODY = r'''
## How to form the two conditionals

| | If-clause | Result clause | Example |
|---|---|---|---|
| Second conditional | if + past simple | would + base verb | **If I had** a car, I**'d drive** to work. |
| Third conditional | if + had + past participle | would have + past participle | **If I had had** a car, I**'d have driven** to work. |

Both are **unreal**: they imagine something that isn't true. The difference is **time**.

## The key difference: time

| Conditional | Time | Example |
|---|---|---|
| **Second** | imaginary **present** or unlikely **future** | If I **knew** her number, I**'d call** her. (I don't know it now.) |
| **Third** | imaginary **past** | If I **had known** her number, I**'d have called** her. (I didn't know it then.) |

- **If it were** sunny, we**'d go** to the beach. (It isn't sunny today.)
- **If it had been** sunny, we**'d have gone** to the beach. (It wasn't sunny yesterday.)

## When to use the second conditional

### 1. Something not true now

- **If I lived** in Barcelona, I**'d go** to the beach every weekend.
- **If he were** here, he**'d know** what to do.

> ⚠️ Typical error: ~~If I had lived in Barcelona, I'd go to the beach every weekend.~~ (you don't live there now) → For now, use the past simple: *If I lived…*

### 2. An unlikely future

- **If I won** the competition next month, I**'d buy** a new laptop.

> ⚠️ Typical error: ~~If I had won the competition next month…~~ → The future can't take the past perfect: *If I won…*

## When to use the third conditional

### 1. Something that didn't happen in the past

- **If we had left** on time, we **wouldn't have missed** the plane.
- **If she had studied**, she**'d have passed**.

> ⚠️ Typical error: ~~If we left on time yesterday, we wouldn't have missed the plane.~~ → A past condition needs the past perfect: *If we had left…*

### 2. Past regrets and relief

- **If I hadn't eaten** that fish, I **wouldn't have been** ill.
- **If the lifeguard hadn't seen** him, he **would have drowned**.

## Time clues

| Clue | Usually | Example |
|---|---|---|
| *now, today, these days* | second | If I had more time **these days**, I'd read more. |
| *tomorrow, next week* | second | If it snowed **tomorrow**, the school would close. |
| *yesterday, last year, in 2020* | third | If you'd come **yesterday**, you'd have met her. |
| a fact in the present (*I'm not…*) | second | I'm not tall. If I were taller… |
| a fact in the past (*I didn't…*) | third | I didn't go. If I'd gone… |

## Mixing the two

Sometimes a past condition has a **present** result. Then we mix them — see [Mixed Conditionals](/grammar/conditionals/mixed-conditionals/).

- **If I had taken** the job, I**'d be** rich now.

## Common mistakes

**1. Using the third conditional for the present.** *~~If I had had a dog, I'd walk it every day~~* (you don't have one now) → **If I had a dog, I'd walk it every day.**

**2. Using the second conditional for the past.** *~~If I knew about the party last week, I would go~~* → **If I had known about the party, I would have gone.**

**3. Mismatched results.** Each if-clause has its own result. *~~If I had seen him, I'd tell him~~* (about the past) → **If I had seen him, I'd have told him.**

**4. *Would* in the if-clause.** Neither conditional uses it. *~~If I would have known~~* → **If I had known.**

**Pro tip:** ask "Is this about now or about then?" Now → past simple + *would*. Then → past perfect + *would have*.
'''

GAP = ('Fill in the gaps',
  'Type the correct form of the verb in brackets. Look for the time clue: now or the future → second conditional; the past → third. Twenty original sentences.',
  [
  ('Second', 'If I [[had]] more free time these days, I’d learn Italian.', '(have)', '‘These days’ is the present: second conditional, past simple ‘had’.'),
  ('Third', 'If I [[had had|’d had]] more time last summer, I’d have learnt Italian.', '(have)', '‘Last summer’ is the past: third conditional, ‘had had’.'),
  ('Second', 'If she lived closer, she [[would visit|’d visit]] us more often.', '(visit)', 'She doesn’t live close now: second conditional, would + base verb.'),
  ('Third', 'If she had lived closer then, she [[would have visited|’d have visited]] us more.', '(visit)', '‘Then’ points to the past: would have + past participle.'),
  ('Second', 'If it [[were|was]] sunny today, we’d go to the beach.', '(be)', '‘Today’ is now: second conditional, ‘were’.'),
  ('Third', 'If it [[had been|’d been]] sunny yesterday, we’d have gone to the beach.', '(be)', '‘Yesterday’ is the past: third conditional, ‘had been’.'),
  ('Second', 'If I knew the answer, I [[would tell|’d tell]] you.', '(tell)', 'I don’t know it now: second conditional, would + tell.'),
  ('Third', 'If I had known the answer, I [[would have told|’d have told]] you.', '(tell)', 'A past situation: would have + told.'),
  ('Second', 'If we [[won]] the match next Saturday, we’d go to the final.', '(win)', 'An unlikely future: second conditional, past simple ‘won’.'),
  ('Third', 'If we [[had won|’d won]] last Saturday, we’d have gone to the final.', '(win)', '‘Last Saturday’ is past: third conditional, ‘had won’.'),
  ('Second', 'If my phone [[worked]], I’d call you right now.', '(work)', '‘Right now’ is the present: second conditional, ‘worked’.'),
  ('Third', 'If you [[had called|’d called]] me, I would have picked you up.', '(call)', 'The result is past (would have), so the condition is past perfect.'),
  ('Second', 'I [[wouldn’t worry]] if I were you.', '(not worry)', 'Advice about now: second conditional, wouldn’t + base verb.'),
  ('Third', 'I [[wouldn’t have worried]] if I had known you were safe.', '(not worry)', 'A past feeling: wouldn’t have + past participle.'),
  ('Second', 'If he [[didn’t snore]], I’d sleep better.', '(not snore)', 'He snores every night (now): second conditional, didn’t + verb.'),
  ('Third', 'If he [[hadn’t snored]] last night, I’d have slept better.', '(not snore)', '‘Last night’ is the past: third conditional, hadn’t + participle.'),
  ('Second', 'What would you do if you [[found]] a wallet in the street?', '(find)', 'An imaginary future situation: second conditional, ‘found’.'),
  ('Third', 'What would you have done if you [[had found|’d found]] that wallet?', '(find)', 'A past event (that wallet): third conditional, ‘had found’.'),
  ('Second', 'If they [[spoke]] English, they could work abroad.', '(speak)', 'They don’t speak it now: second conditional, past simple ‘spoke’.'),
  ('Third', 'If they had spoken English, they [[could have worked]] abroad.', '(can / work)', 'A past ability: could have + past participle.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 10 second conditionals (now) and 10 third conditionals (the past).',
  [
  ('Second', 'If I had a car, I’d drive.', ['I’d drive if I had a car.']),
  ('Second', 'If it were warmer, we’d swim.', ['we’d swim if it were warmer.']),
  ('Second', 'If I knew, I would tell you.', ['I would tell you if I knew.']),
  ('Second', 'She’d be happier if she had a dog.', ['if she had a dog, she’d be happier.']),
  ('Second', 'If we lived nearer, we’d visit more.', ['we’d visit more if we lived nearer.']),
  ('Second', 'What would you do if you were rich?', ['if you were rich, what would you do?']),
  ('Second', 'If he didn’t shout, I’d listen.', ['I’d listen if he didn’t shout.']),
  ('Second', 'If I were you, I’d go home.', ['I’d go home if I were you.']),
  ('Second', 'If we had time, we could help.', ['we could help if we had time.']),
  ('Second', 'I wouldn’t buy it if I were you.', ['if I were you, I wouldn’t buy it.']),
  ('Third', 'If I had known, I would have come.', ['I would have come if I had known.']),
  ('Third', 'If it had rained, we would have stayed in.', ['we would have stayed in if it had rained.']),
  ('Third', 'If she had studied, she would have passed.', ['she would have passed if she had studied.']),
  ('Third', 'We would have won if we had trained.', ['if we had trained, we would have won.']),
  ('Third', 'If you had called, I would have answered.', ['I would have answered if you had called.']),
  ('Third', 'What would you have done if you had lost?', ['if you had lost, what would you have done?']),
  ('Third', 'If he hadn’t fallen, he would have won.', ['he would have won if he hadn’t fallen.']),
  ('Third', 'If we had left earlier, we wouldn’t have missed it.', ['we wouldn’t have missed it if we had left earlier.']),
  ('Third', 'If I had seen you, I’d have said hello.', ['I’d have said hello if I had seen you.']),
  ('Third', 'If they had asked, we could have helped.', ['we could have helped if they had asked.']),
  ])

MATCH = {'title': 'Now or the past?', 'subtitle': 'Tap a sentence, then tap what it imagines: the present (second conditional) or the past (third conditional).',
  'leftLabel': 'Sentence', 'rightLabel': 'It imagines…', 'rightLabelSub': '(now / the past)', 'reviewArrowPrefix': '',
  'pairs': [
  ('If I had a bike, I’d cycle.', 'now'), ('If I’d had a bike, I’d have cycled.', 'the past'), ('If it were sunny, we’d go out.', 'now'),
  ('If it had been sunny, we’d have gone out.', 'the past'), ('If she knew, she’d help.', 'now'), ('If she’d known, she’d have helped.', 'the past'),
  ('If we lived here, we’d be happy.', 'now'), ('If we’d lived there, we’d have been happy.', 'the past'), ('If I were you, I’d rest.', 'now'),
  ('If I’d been you, I’d have rested.', 'the past'), ('If he didn’t smoke, he’d be healthier.', 'now'), ('If he hadn’t smoked, he’d have lived longer.', 'the past'),
  ('If they spoke French, they’d understand.', 'now'), ('If they’d spoken French, they’d have understood.', 'the past'), ('If I had time, I could come.', 'now'),
  ('If I’d had time, I could have come.', 'the past'), ('If you asked, he’d say yes.', 'now'), ('If you’d asked, he’d have said yes.', 'the past'),
  ('If my phone worked, I’d call.', 'now'), ('If my phone had worked, I’d have called.', 'the past'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Now or the future → past simple + would. The past → had + participle + would have.',
  [
  ('Second', 'If I ___ a car now, I’d drive you home.', ['had', 'had had', 'have', 'would have'],
   ['‘Had had’ is third conditional (past), but the clue is ‘now’.', '‘Have’ makes it real; with ‘I’d’ it’s imaginary.', 'No ‘would’ in the if-clause.'],
   '‘Now’ → second conditional: past simple ‘had’.'),
  ('Third', 'If I ___ a car last night, I’d have driven you home.', ['had had', 'had', 'have', 'would have'],
   ['‘Had’ alone is past simple (second conditional); ‘last night’ needs the past perfect.', '‘Have’ is present.', 'No ‘would’ in the if-clause.'],
   '‘Last night’ → third conditional: had had.'),
  ('Second', 'If she were here, she ___ what to do.', ['would know', 'would have known', 'will know', 'knew'],
   ['‘Would have known’ is about the past, but ‘were here’ is now.', '‘Will’ is for a real future.', '‘Knew’ belongs in the if-clause.'],
   'Imaginary present: would + base verb.'),
  ('Third', 'If she had been there, she ___ what to do.', ['would have known', 'would know', 'will know', 'had known'],
   ['‘Would know’ is about now; ‘had been there’ is the past.', '‘Will’ is for a real future.', '‘Had known’ belongs in the if-clause.'],
   'Imaginary past: would have + past participle.'),
  ('Second', 'If it ___ tomorrow, the match would be cancelled.', ['snowed', 'had snowed', 'snows', 'would snow'],
   ['The past perfect can’t talk about tomorrow.', '‘Snows’ is first conditional; the result is ‘would’.', 'No ‘would’ in the if-clause.'],
   'An unlikely future: second conditional, past simple.'),
  ('Third', 'If it ___ last Sunday, the match would have been cancelled.', ['had snowed', 'snowed', 'snows', 'would snow'],
   ['‘Snowed’ is second conditional; ‘would have been’ shows the past.', '‘Snows’ is present.', 'No ‘would’ in the if-clause.'],
   'Past condition: had snowed.'),
  ('Second', 'I’m not rich, but if I ___, I’d help everyone.', ['were', 'had been', 'am', 'would be'],
   ['‘Had been’ is about the past; ‘I’m not rich’ is now.', '‘Am’ is present real.', 'No ‘would’ in the if-clause.'],
   'A present fact → second conditional: were.'),
  ('Third', 'I didn’t go to the party, but if I ___, I’d have danced all night.', ['had gone', 'went', 'go', 'would go'],
   ['‘Went’ is second conditional; ‘didn’t go’ is a past fact.', '‘Go’ is present.', 'No ‘would’ in the if-clause.'],
   'A past fact → third conditional: had gone.'),
  ('Second', 'What ___ if you could speak to animals?', ['would you do', 'would you have done', 'will you do', 'did you do'],
   ['‘Would you have done’ is about the past.', '‘Will’ is for a real future.', '‘Did’ asks about a real past.'],
   'Imaginary present/future question: would + verb.'),
  ('Third', 'What ___ if you had missed the last bus?', ['would you have done', 'would you do', 'will you do', 'had you done'],
   ['‘Would you do’ is about now; ‘had missed’ is past.', '‘Will’ is for a real future.', '‘Had you done’ isn’t a result form.'],
   'Imaginary past question: would + have + participle.'),
  ('Mismatch', 'Which sentence is correct?', ['If I had known, I would have helped.', 'If I had known, I would help yesterday.', 'If I knew, I would have helped yesterday.', 'If I would have known, I would have helped.'],
   ['A past condition needs a past result: ‘would have helped’.', 'A past result needs a past condition: ‘had known’.', 'No ‘would’ in the if-clause.'],
   'Third conditional: had known + would have helped.'),
  ('Mismatch', 'Which sentence is correct?', ['If I lived by the sea, I’d swim every day.', 'If I had lived by the sea, I’d swim every day now.', 'If I lived by the sea, I’d have swum every day.', 'If I would live by the sea, I’d swim every day.'],
   ['A present habit (every day now) needs the past simple in the if-clause.', '‘Would have swum’ is past; ‘lived’ here is about now.', 'No ‘would’ in the if-clause.'],
   'Second conditional: lived + would swim.'),
  ('Third', 'If you had told me earlier, I ___ the tickets.', ['could have bought', 'could buy', 'can buy', 'could bought'],
   ['‘Could buy’ is about now or later; ‘had told’ is past.', '‘Can’ is present real.', 'After ‘could’ use ‘have’ + participle.'],
   'Past possibility: could have + participle.'),
  ('Second', 'If he ___ so much, he’d have more money.', ['didn’t spend', 'hadn’t spent', 'doesn’t spend', 'wouldn’t spend'],
   ['‘Hadn’t spent’ is past; ‘he’d have more money’ is now.', '‘Doesn’t’ is present real.', 'No ‘would’ in the if-clause.'],
   'A present habit → second conditional: didn’t spend.'),
  ('Third', 'If we ___ a map, we wouldn’t have got lost.', ['had taken', 'took', 'take', 'would take'],
   ['‘Took’ is second conditional; ‘wouldn’t have got lost’ is past.', '‘Take’ is present.', 'No ‘would’ in the if-clause.'],
   'Past condition: had taken.'),
  ('Second', 'If I were taller, I ___ basketball.', ['would play', 'would have played', 'will play', 'played'],
   ['‘Would have played’ is about the past; ‘were taller’ is now.', '‘Will’ is for a real future.', '‘Played’ belongs in the if-clause.'],
   'Imaginary present: would play.'),
  ('Third', 'If the alarm had rung, I ___ late.', ['wouldn’t have been', 'wouldn’t be', 'won’t be', 'hadn’t been'],
   ['‘Wouldn’t be’ is about now; the alarm was in the past.', '‘Won’t’ is for a real future.', '‘Hadn’t been’ belongs in the if-clause.'],
   'Past result: wouldn’t have been.'),
  ('Time clue', 'If I had more time ___, I’d read more books.', ['these days', 'last year', 'in 2019', 'yesterday'],
   ['‘Last year’ is past; with ‘had’ + ‘I’d read’ the sentence is about now.', '‘In 2019’ is past.', '‘Yesterday’ is past.'],
   'Second conditional fits a present time clue: these days.'),
  ('Time clue', 'If you had come ___, you’d have met my cousin.', ['yesterday', 'tomorrow', 'now', 'next week'],
   ['‘Tomorrow’ is future; ‘had come’ is past.', '‘Now’ is present.', '‘Next week’ is future.'],
   'Third conditional fits a past time clue: yesterday.'),
  ('Third', 'If they ___ harder, they would have won the cup.', ['had played', 'played', 'play', 'would play'],
   ['‘Played’ is second conditional; ‘would have won’ is past.', '‘Play’ is present.', 'No ‘would’ in the if-clause.'],
   'Past condition: had played.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('Wrong result', 'If I lived near the beach, I *will* swim every day.', 'would', '‘Lived’ (imaginary now) needs ‘would’ in the result: ‘I would swim’.'),
  ('Second for the past', 'If I *knew* about the party last week, I would have gone.', 'had known', 'A past condition needs ‘had known’.'),
  ('Mismatch', 'If I had seen him yesterday, I would *tell* him.', 'have told', 'A past condition needs a past result: ‘would have told’.'),
  ('Mismatch', 'If it were sunny today, we *will* go out.', 'would', '‘Today’ + ‘were’ is imaginary → ‘we would go out’.'),
  ('Would in the if-clause', 'If I *would have* known, I’d have come.', 'had', 'No ‘would’ in the if-clause: ‘If I had known…’.'),
  ('Would in the if-clause', 'If she *would be* here, she’d help.', 'were', 'No ‘would’ in the if-clause: ‘If she were here…’.'),
  ('Past participle', 'If we had left earlier, we would have *catched* the train.', 'caught', '‘Catch’ is irregular: caught.'),
  ('Past participle', 'If you had asked, I would have *went* with you.', 'gone', 'After ‘would have’ use the participle: gone.'),
  ('Base verb', 'If I were rich, I would *bought* a castle.', 'buy', 'After ‘would’ use the base verb: ‘would buy’.'),
  ('Base verb', 'If he had more time, he would *learnt* the piano.', 'learn', 'After ‘would’ use the base verb: ‘would learn’.'),
  ('Time clue', 'If I had studied *tomorrow*, I would have passed.', 'yesterday', 'The past perfect needs a past time: ‘yesterday’, not ‘tomorrow’.'),
  ('Time clue', 'If it snowed *yesterday*, the school would close.', 'tomorrow', 'Second conditional (snowed + would close) fits the future: ‘tomorrow’.'),
  ('Negative', 'If he *didn’t fall* last week, he would have won.', 'hadn’t fallen', 'A past condition: ‘If he hadn’t fallen…’.'),
  ('Negative', 'If I had known, I *won’t* have worried.', 'wouldn’t', 'The result needs ‘wouldn’t have’.'),
  ('Could', 'If I had had a car, I *can* have driven you.', 'could', 'Past possibility: ‘could have driven’.'),
  ('Were', 'If I *was* you, I’d have called him yesterday.', 'had been', 'About the past: ‘If I had been you…’.'),
  ('Question', 'What would you *done* if you had won?', 'have done', 'The past result question is ‘would you have done’.'),
  ('Question', 'If you could fly, where would you *have go*?', 'go', 'Imaginary present: ‘where would you go?’ — no ‘have’.'),
  ('Would of', 'If you’d come, you would *of* loved it.', 'have', 'Write ‘would have’, never ‘would of’.'),
  ('Spelling', 'If we had planned it, we would have *enjoied* it more.', 'enjoyed', 'Vowel + -y keeps the y: enjoy → enjoyed.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, now-or-the-past, multiple choice and spot-the-mistake. In the typing questions check the time first: now → past simple / would; the past → had + participle / would have. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('time', 'Now or the past'),
 'fill': [
  ('Second', 'If I [[spoke]] German, I’d work in Berlin.', 'speak', 'I don’t speak it now: second conditional, past simple ‘spoke’.', 'Now → past simple: ‘spoke’.'),
  ('Third', 'If I [[had spoken|’d spoken]] German, I’d have got that job last year.', 'speak', '‘Last year’ is past: had + spoken.', 'The past → had + past participle.'),
  ('Second', 'If we had a garden, we [[would grow|’d grow]] vegetables.', 'grow', 'Imaginary present: would + base verb.', 'Now → would + base verb.'),
  ('Third', 'If we had planted seeds in spring, we [[would have grown|’d have grown]] tomatoes.', 'grow', 'Imaginary past: would have + grown.', 'The past → would have + participle.'),
  ],
 'order': [
  ('Second', 'If I were you, I’d stay.', ['I’d stay if I were you.']),
  ('Third', 'If I had been you, I’d have stayed.', ['I’d have stayed if I had been you.']),
  ('Second', 'We’d help if we could.', ['if we could, we’d help.']),
  ('Third', 'We’d have helped if we had known.', ['if we had known, we’d have helped.']),
  ],
 'customItems': [
  ('Time', 'I’m tired now. If I ___ more, I wouldn’t be tired.', ['slept', 'had slept', 'sleep', 'would sleep'],
   ['‘Had slept’ is about the past; this is a general present situation.', '‘Sleep’ is present real.', 'No ‘would’ in the if-clause.'],
   'A present habit → second conditional.'),
  ('Time', 'I was tired yesterday. If I ___ more, I wouldn’t have been tired.', ['had slept', 'slept', 'sleep', 'would sleep'],
   ['‘Slept’ is second conditional; ‘yesterday’ needs the past perfect.', '‘Sleep’ is present.', 'No ‘would’ in the if-clause.'],
   'A past situation → third conditional.'),
  ('Time', 'Which sentence is about the past?', ['If she’d asked, I’d have said yes.', 'If she asked, I’d say yes.', 'If she asks, I’ll say yes.', 'If she asks, I say yes.'],
   ['This is second conditional: imaginary present or future.', 'This is first conditional: a real future.', 'This is zero conditional: always true.'],
   '’d asked + ’d have said = third conditional (past).'),
  ('Time', 'Which sentence is about now?', ['If I had a pen, I’d lend it to you.', 'If I’d had a pen, I’d have lent it to you.', 'If I’d had a pen, I’d lent it to you.', 'If I would have a pen, I’d lend it to you.'],
   ['This is third conditional (the past).', 'Wrong form: after ’d (would) we need ‘have lent’.', 'No ‘would’ in the if-clause.'],
   'had + would lend = second conditional (now).'),
  ],
 'mc': [
  ('Second', 'If we ___ in the city, we wouldn’t need a car.', ['lived', 'had lived', 'live', 'would live'],
   ['‘Had lived’ is about the past; ‘wouldn’t need’ is now.', '‘Live’ is present real.', 'No ‘would’ in the if-clause.'],
   'Second conditional: lived.'),
  ('Third', 'If you had worn a coat, you ___ cold.', ['wouldn’t have got', 'wouldn’t get', 'won’t get', 'didn’t get'],
   ['‘Wouldn’t get’ is about now; ‘had worn’ is past.', '‘Won’t’ is for a real future.', '‘Didn’t get’ is a fact, not a result.'],
   'Past result: wouldn’t have got.'),
  ('Mismatch', 'If I had seen the film, I ___ you about it last week.', ['would have told', 'would tell', 'will tell', 'told'],
   ['‘Would tell’ doesn’t fit ‘last week’.', '‘Will’ is for the future.', '‘Told’ is a fact, not an imaginary result.'],
   'Past result: would have told.'),
  ('Second', 'If my brother ___ older, he could drive.', ['were', 'had been', 'is', 'would be'],
   ['‘Had been’ is about the past; ‘could drive’ is now.', '‘Is’ is present real.', 'No ‘would’ in the if-clause.'],
   'Imaginary present: were.'),
  ],
 'error': [
  ('Mismatch', 'If I had known, I would *help* you yesterday.', 'have helped', 'Yesterday + had known → ‘would have helped’.'),
  ('Second for the past', 'If it *rained* last night, the grass would have been wet.', 'had rained', 'A past condition: ‘had rained’.'),
  ('Would in the if-clause', 'If we *would have* money, we’d travel.', 'had', 'No ‘would’ after ‘if’: ‘If we had money…’.'),
  ('Past participle', 'If she had tried, she would have *winned*.', 'won', '‘Win’ is irregular: won.'),
  ],
}
