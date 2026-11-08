TITLE = 'First Conditional'
AUX = (['will', 'won’t', '’ll'], None, 'will')
NEXT = ('Second Conditional', '/grammar/conditionals/second-conditional/')
BODY = r'''
## How to form the first conditional

| Clause | Verb form | Example |
|---|---|---|
| If-clause (the condition) | if + present simple | **If it rains** tomorrow, |
| Main clause (the result) | will / won't + base verb | we**'ll stay** at home. |

The if-clause uses the **present simple**, even though it talks about the future. The result uses **will** (*'ll*) or **won't** + the base verb. If the if-clause comes first, put a **comma** after it; if it comes second, no comma.

| Form | Example |
|---|---|
| Affirmative | If you study, you**'ll pass**. |
| Negative | If you don't hurry, you **won't catch** the bus. |
| Question | What **will** you **do** if she **says** no? |
| Result first | You'll pass **if you study**. |

## When to use the first conditional

### 1. A real, likely future situation

The condition is possible and we think the result will probably happen.

- **If it's sunny** on Saturday, we**'ll go** to the beach.
- **If I see** Marta, I**'ll give** her your message.

> ⚠️ Typical error: ~~If it will rain, we'll stay home.~~ → No *will* in the if-clause: *If it rains, we'll stay home.*

### 2. Warnings and threats

- **If you touch** that, you**'ll burn** yourself.
- **If you don't stop** shouting, I**'ll call** your parents.

> ⚠️ Typical error: ~~If you don't stop, I call your parents.~~ → A future result needs *will*: *I'll call your parents.*

### 3. Promises and offers

- **If you help** me with this, I**'ll buy** you lunch.
- I**'ll drive** you to the station **if you want**.

> ⚠️ Typical error: ~~If you will help me, I'll buy you lunch.~~ → Promise or not, the if-clause takes the present simple: *If you help me…*

## Other forms in the result clause

*Will* is the most common, but the result can also use other verbs.

| Result | Meaning | Example |
|---|---|---|
| be going to | a plan or clear result | If he's late again, he**'s going to lose** his job. |
| can / could | possibility, ability | If you finish early, you **can leave**. |
| might / may | less certain | If we hurry, we **might catch** the train. |
| should / must | advice, obligation | If you feel ill, you **should stay** in bed. |
| imperative | instruction | If you see Tom, **tell** him to call me. |

## Unless and other linkers

*Unless* means **if … not**. The verb after *unless* is affirmative.

- **Unless you hurry**, you'll miss the bus. = **If you don't hurry**, you'll miss the bus.

Other future linkers work the same way: **when, as soon as, before, after, until** + present simple.

- I'll call you **as soon as I arrive**. (not ~~as soon as I will arrive~~)

More in [Unless, as long as, provided that](/grammar/conditionals/unless-as-long-as-provided/).

## First or second conditional?

| | First conditional | Second conditional |
|---|---|---|
| Meaning | real, likely future | imaginary or unlikely |
| Form | if + present, will + verb | if + past, would + verb |
| Example | If I **have** time, I**'ll help** you. | If I **had** time, I**'d help** you. |

## Common mistakes

**1. Using *will* in the if-clause.** The most frequent first-conditional error. *If* already shows the future, so the condition stays in the present simple. *~~If I will see her, I'll tell her~~* → **If I see her, I'll tell her.**

**2. Using the present simple in the result.** A future result needs *will* (or a modal). *~~If it rains, we stay at home tomorrow~~* → **If it rains, we'll stay at home tomorrow.**

**3. Using *unless* with a negative.** *Unless* already means *if not*. *~~Unless you don't hurry, you'll be late~~* → **Unless you hurry, you'll be late.**

**4. Forgetting the comma (or adding it in the wrong place).** *~~If you call me I'll come~~* → **If you call me, I'll come.** No comma when the result comes first: **I'll come if you call me.**

**Pro tip:** think "if + now, will + later" — the condition looks like the present, the result looks like the future.
'''

GAP = ('Fill in the gaps',
  'Type the correct form of the verb in brackets: present simple after if, will / won’t + base verb in the result. Twenty original sentences.',
  [
  ('Likely future', 'If it rains tomorrow, we [[will stay|’ll stay|’ll stay]] at home.', '(stay)', 'The result of a likely future condition takes will + base verb: ‘will stay’.'),
  ('Likely future', 'If you [[study]] hard, you’ll pass the exam.', '(study)', 'After ‘if’ use the present simple, even for the future: ‘you study’, not ‘will study’.'),
  ('Likely future', 'If Marta [[calls]], I’ll tell her the news.', '(call)', 'The if-clause takes the present simple with -s for ‘she’: ‘calls’.'),
  ('Likely future', 'We [[will miss|’ll miss]] the train if we don’t leave now.', '(miss)', 'The result clause comes first here, but it still takes will + base verb.'),
  ('Likely future', 'If the weather [[is]] nice, we’ll have a picnic.', '(be)', 'Present simple of ‘be’ with ‘the weather’ (it): ‘is’, not ‘will be’.'),
  ('Negative', 'If you don’t hurry, you [[won’t catch]] the bus.', '(not catch)', 'A negative future result: won’t + base verb, ‘won’t catch’.'),
  ('Negative', 'If he [[doesn’t come]], we’ll start without him.', '(not come)', 'Negative present simple in the if-clause with ‘he’: doesn’t + base verb.'),
  ('Negative', 'If they don’t invite us, we [[won’t go]] to the party.', '(not go)', 'The negative result uses won’t + base verb: ‘won’t go’.'),
  ('Warning', 'If you touch that plate, you [[will burn|’ll burn]] your fingers.', '(burn)', 'A warning about a likely result: will + base verb.'),
  ('Warning', 'If you [[eat]] all those sweets, you’ll feel sick.', '(eat)', 'A warning: the condition stays in the present simple, ‘you eat’.'),
  ('Promise', 'If you help me with the dishes, I [[will make|’ll make]] dessert.', '(make)', 'A promise: will + base verb in the result, ‘I’ll make’.'),
  ('Promise', 'I’ll lend you my bike if you [[promise]] to be careful.', '(promise)', 'The if-clause is second here, but it still takes the present simple.'),
  ('Offer', 'If you’re cold, I [[will close|’ll close]] the window.', '(close)', 'An offer made now about a future action: ‘I’ll close’.'),
  ('Question', 'What will you do if you [[fail]] the test?', '(fail)', 'In a question the if-clause still takes the present simple: ‘if you fail’.'),
  ('Question', 'If it snows, [[will they cancel]] the match?', '(they / cancel)', 'A future question: will + subject + base verb, ‘will they cancel’.'),
  ('Modal', 'If you finish your homework, you [[can watch]] TV.', '(can / watch)', 'The result can use a modal instead of will: can + base verb.'),
  ('Modal', 'If we leave now, we [[might arrive]] on time.', '(might / arrive)', 'Might shows a less certain result: might + base verb, ‘might arrive’.'),
  ('Imperative', 'If you see Leo, [[tell]] him to call me.', '(tell)', 'The result can be an instruction: the imperative ‘tell’, with no subject.'),
  ('Unless', 'Unless you [[leave]] now, you’ll be late.', '(leave)', '‘Unless’ means ‘if not’, so the verb after it is affirmative: ‘unless you leave’.'),
  ('Time linker', 'I’ll text you as soon as I [[arrive]].', '(arrive)', 'After ‘as soon as’ (like ‘if’) use the present simple for the future.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with likely futures, warnings, promises, negatives and questions. If the if-clause goes first, it needs a comma.',
  [
  ('Likely future', 'If it rains, we’ll stay at home.', ['we’ll stay at home if it rains.']),
  ('Likely future', 'If I see Anna, I’ll give her the book.', ['I’ll give Anna the book if I see her.']),
  ('Likely future', 'You’ll pass the exam if you study.', ['if you study, you’ll pass the exam.']),
  ('Likely future', 'If we leave now, we’ll catch the train.', ['we’ll catch the train if we leave now.']),
  ('Likely future', 'If the shop is open, I’ll buy some bread.', ['I’ll buy some bread if the shop is open.']),
  ('Negative', 'If you don’t hurry, you’ll be late.', ['you’ll be late if you don’t hurry.']),
  ('Negative', 'We won’t go out if it’s cold.', ['if it’s cold, we won’t go out.']),
  ('Negative', 'If she doesn’t call, I won’t wait.', ['I won’t wait if she doesn’t call.']),
  ('Warning', 'If you touch the oven, you’ll burn yourself.', ['you’ll burn yourself if you touch the oven.']),
  ('Warning', 'If you shout, you’ll wake the baby.', ['you’ll wake the baby if you shout.']),
  ('Promise', 'If you help me, I’ll buy you lunch.', ['I’ll buy you lunch if you help me.']),
  ('Offer', 'I’ll drive you home if you want.', ['if you want, I’ll drive you home.']),
  ('Question', 'What will you do if it rains?', ['if it rains, what will you do?']),
  ('Question', 'Will you come if I invite you?', ['if I invite you, will you come?']),
  ('Question', 'Where will you stay if the hotel is full?', ['if the hotel is full, where will you stay?']),
  ('Modal', 'If you finish early, you can go home.', ['you can go home if you finish early.']),
  ('Modal', 'If we hurry, we might get seats.', ['we might get seats if we hurry.']),
  ('Imperative', 'If you see Tom, say hello.', ['say hello if you see Tom.']),
  ('Unless', 'Unless you hurry, you’ll miss the bus.', ['you’ll miss the bus unless you hurry.']),
  ('Time linker', 'I’ll call you when I get home.', ['when I get home, I’ll call you.']),
  ])

MATCH = {'title': 'Match the condition and result', 'subtitle': 'Tap an if-clause, then tap its most likely future result. The if-clause uses the present simple; the result uses will.',
  'leftLabel': 'If-clause', 'rightLabel': 'Result', 'rightLabelSub': '(will + verb)', 'reviewArrowPrefix': '',
  'pairs': [
  ('If it rains tomorrow,', 'we’ll stay at home.'), ('If you study every day,', 'you’ll pass the exam.'), ('If you touch the hot pan,', 'you’ll burn yourself.'),
  ('If we leave right now,', 'we’ll catch the bus.'), ('If you don’t wear a coat,', 'you’ll get cold.'), ('If I see Marta,', 'I’ll give her your message.'),
  ('If you help me tidy up,', 'I’ll make you a cake.'), ('If the tickets are cheap,', 'we’ll buy four.'), ('If you eat all that chocolate,', 'you’ll feel sick.'),
  ('If my team wins,', 'I’ll be really happy.'), ('If you don’t water the plants,', 'they’ll die.'), ('If you go to bed late,', 'you’ll be tired tomorrow.'),
  ('If she misses the train,', 'she’ll take a taxi.'), ('If you lend me your notes,', 'I’ll give them back on Monday.'), ('If the café is closed,', 'we’ll go to the park.'),
  ('If you shout,', 'you’ll wake the baby.'), ('If it’s sunny on Saturday,', 'we’ll go to the beach.'), ('If I get the job,', 'I’ll move to Barcelona.'),
  ('If you don’t charge your phone,', 'the battery will die.'), ('If we practise more,', 'we’ll play better.'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Present simple after if, will in the result — and watch for unless.',
  [
  ('Likely future', 'If it ___ tomorrow, we’ll stay at home.', ['rains', 'will rain', 'rained', 'would rain'],
   ['Never use ‘will’ in the if-clause: the condition takes the present simple.', '‘Rained’ is past; it belongs to the second conditional (imaginary).', '‘Would’ belongs to the result of the second conditional, not the if-clause.'],
   'First conditional: if + present simple. ‘It’ needs -s: ‘rains’.'),
  ('Likely future', 'If you study, you ___ the exam.', ['will pass', 'pass', 'passed', 'would pass'],
   ['A future result needs ‘will’; the present simple here sounds like a general truth.', '‘Passed’ is past, but the exam is in the future.', '‘Would pass’ is second conditional: imaginary, not a likely future.'],
   'The result of a likely future condition: will + base verb.'),
  ('Likely future', 'I’ll give her the message if I ___ her.', ['see', 'will see', 'saw', 'seeing'],
   ['No ‘will’ after ‘if’, even when the if-clause comes second.', '‘Saw’ is past simple; this is about the future.', '‘Seeing’ needs an auxiliary; after ‘if I’ use the present simple.'],
   'The if-clause takes the present simple, even when it comes second: ‘if I see her’.'),
  ('Negative', 'If you don’t hurry, you ___ the bus.', ['won’t catch', 'don’t catch', 'didn’t catch', 'wouldn’t catch'],
   ['A future result needs ‘won’t’, not the present simple.', '‘Didn’t catch’ is past; the bus hasn’t gone yet.', '‘Wouldn’t’ makes it imaginary (second conditional).'],
   'A negative future result: won’t + base verb.'),
  ('Negative', 'If Leo ___ soon, we’ll start without him.', ['doesn’t arrive', 'won’t arrive', 'don’t arrive', 'didn’t arrive'],
   ['No ‘will’/‘won’t’ in the if-clause: use the present simple.', '‘Leo’ is he, so use ‘doesn’t’, not ‘don’t’.', '‘Didn’t’ is past; this is about the future.'],
   'Negative present simple with ‘he’ in the if-clause: ‘doesn’t arrive’.'),
  ('Warning', 'If you touch that wire, you ___ a shock.', ['’ll get', 'get', 'got', '’d get'],
   ['A warning about the future needs ‘will’: ‘you’ll get’.', '‘Got’ is past; the danger is in the future.', '’d get’ (would) is for imaginary situations, not a real warning.'],
   'A warning: will (’ll) + base verb.'),
  ('Promise', 'If you lend me £10, I ___ you back tomorrow.', ['’ll pay', 'pay', 'paid', 'am paying'],
   ['A promise about the future needs ‘will’, not the present simple.', '‘Paid’ is past; the payment hasn’t happened.', 'The present continuous is for fixed plans, not a promise that depends on a condition.'],
   'A promise: I’ll + base verb.'),
  ('Offer', 'If you’re thirsty, I ___ you some water.', ['’ll get', 'get', 'got', 'getting'],
   ['An offer about the next moment needs ‘will’.', '‘Got’ is past; the offer is for the future.', '‘Getting’ needs an auxiliary and doesn’t make an offer.'],
   'Offers decided at the moment of speaking use will: ‘I’ll get’.'),
  ('Question', 'What ___ if you miss the last train?', ['will you do', 'do you do', 'you will do', 'did you do'],
   ['This asks about one future situation, so ‘will’ is needed.', 'Question order is will + subject + verb: ‘will you do’.', '‘Did you do’ asks about the past.'],
   'A future question: What will you do…?'),
  ('Question', 'If it snows, ___ the school close?', ['will', 'does', 'is', 'did'],
   ['‘Does’ asks about a general truth; this is one future situation.', '‘Is close’ isn’t a correct form.', '‘Did’ asks about the past.'],
   'A future question needs will + subject + base verb.'),
  ('Modal', 'If you finish early, you ___ go home.', ['can', 'will can', 'could have', 'must to'],
   ['‘Will can’ is impossible: two modals can’t go together. Use ‘can’ or ‘will be able to’.', '‘Could have’ is for the past.', '‘Must’ is never followed by ‘to’.'],
   'The result can use a modal: can + base verb.'),
  ('Modal', 'If we run, we ___ catch the train — but I’m not sure.', ['might', 'will', 'did', 'would have'],
   ['‘Will’ sounds certain, but the speaker is not sure.', '‘Did’ is past; this is future.', '‘Would have’ is third conditional (the past).'],
   '‘Might’ shows a less certain result.'),
  ('Imperative', 'If you see Ana, ___ her I said hi.', ['tell', 'you tell', 'will tell', 'told'],
   ['An instruction is an imperative with no subject: ‘tell her’.', '‘Will tell’ needs a subject and isn’t an instruction.', '‘Told’ is past.'],
   'The result can be an imperative (an instruction).'),
  ('Unless', '___ you leave now, you’ll be late.', ['Unless', 'If', 'When', 'As long as'],
   ['‘If you leave now, you’ll be late’ is the opposite meaning.', '‘When you leave now’ doesn’t make sense: leaving makes you late?', '‘As long as’ means ‘only if’, which reverses the meaning.'],
   '‘Unless’ = ‘if not’: if you don’t leave now, you’ll be late.'),
  ('Unless', 'You won’t get in unless you ___ a ticket.', ['have', 'don’t have', 'will have', 'had'],
   ['‘Unless’ already means ‘if not’, so the verb after it is affirmative.', 'No ‘will’ after ‘unless’ — it works like ‘if’.', '‘Had’ is past; this is the future.'],
   'After ‘unless’ use an affirmative present simple: ‘unless you have’.'),
  ('Time linker', 'I’ll call you as soon as I ___ home.', ['get', 'will get', 'got', 'getting'],
   ['Like ‘if’, ‘as soon as’ takes the present simple, not ‘will’.', '‘Got’ is past; you aren’t home yet.', '‘Getting’ needs an auxiliary.'],
   'Future time linkers (when, as soon as, before) take the present simple.'),
  ('First or second', 'If I ___ time this weekend, I’ll visit you.', ['have', 'had', 'would have', 'will have'],
   ['‘Had’ is the second conditional, but the result here is ‘I’ll’ (real future).', '‘Would’ never goes in the if-clause.', 'No ‘will’ after ‘if’.'],
   'A real possibility with ‘I’ll’ in the result: present simple ‘have’.'),
  ('First or second', 'If she ___ the bus, she’ll be here at six.', ['catches', 'caught', 'catch', 'will catch'],
   ['‘Caught’ is second conditional; the result is ‘she’ll’, so it’s a real future.', '‘She’ needs -es: ‘catches’.', 'No ‘will’ in the if-clause.'],
   'Present simple with -es for ‘she’: ‘catches’.'),
  ('Likely future', 'If the price ___ down, I’ll buy a new phone.', ['goes', 'will go', 'go', 'went'],
   ['Never ‘will’ after ‘if’.', '‘The price’ is it, so add -es: ‘goes’.', '‘Went’ is past or second conditional.'],
   'If + present simple with -es for ‘it’: ‘goes’.'),
  ('Negative', 'If it doesn’t rain, the plants ___ grow.', ['won’t', 'don’t', 'didn’t', 'wouldn’t'],
   ['This is about this season’s future, so use ‘won’t’, not the present simple.', '‘Didn’t’ is past.', '‘Wouldn’t’ is for imaginary situations.'],
   'A negative future result: won’t + base verb.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('Will after if', 'If it *will rain*, we’ll stay home.', 'rains', 'No ‘will’ after ‘if’: ‘If it rains…’.'),
  ('Will after if', 'If you *will call* me, I’ll come.', 'call', 'The if-clause takes the present simple: ‘If you call me…’.'),
  ('Will after if', 'I’ll tell her if I *will see* her.', 'see', 'Even when it comes second, the if-clause has no ‘will’: ‘if I see her’.'),
  ('Missing will', 'If you study, you *pass* the exam next week.', 'will pass', 'A future result needs ‘will’: ‘you will pass the exam next week’.'),
  ('Missing will', 'If it rains, *I stay* at home tomorrow.', 'I’ll stay', 'Tomorrow’s result needs ‘will’: ‘I’ll stay at home tomorrow’.'),
  ('Missing -s', 'If Tom *call*, I’ll tell him.', 'calls', '‘Tom’ is he, so add -s: ‘If Tom calls…’.'),
  ('Wrong tense', 'If I *had* time tomorrow, I’ll help you.', 'have', 'With ‘I’ll’ in the result, the if-clause takes the present simple: ‘have’.'),
  ('Wrong tense', 'If you hurry, you *would* catch the bus.', 'will', 'A real future takes ‘will’; ‘would’ is for imaginary situations.'),
  ('Won’t + verb', 'If you don’t hurry, you won’t *caught* the train.', 'catch', 'After ‘won’t’ use the base verb: ‘won’t catch’.'),
  ('Won’t + verb', 'If it’s cold, we will not *going* out.', 'go', 'After ‘will not’ use the base verb: ‘will not go’.'),
  ('Don’t or doesn’t', 'If she *don’t* come, we’ll leave.', 'doesn’t', '‘She’ takes ‘doesn’t’: ‘If she doesn’t come…’.'),
  ('Base verb after doesn’t', 'If he doesn’t *wakes* up, he’ll be late.', 'wake', 'After ‘doesn’t’ the verb is the base form: ‘doesn’t wake’.'),
  ('Unless + not', 'Unless you *don’t hurry*, you’ll miss it.', 'hurry', '‘Unless’ already means ‘if not’: ‘Unless you hurry…’.'),
  ('Will after linker', 'I’ll call you when I *will arrive*.', 'arrive', 'After ‘when’ (future) use the present simple: ‘when I arrive’.'),
  ('Will after linker', 'We’ll start as soon as she *will get* here.', 'gets', 'After ‘as soon as’ use the present simple: ‘as soon as she gets here’.'),
  ('Two modals', 'If you finish, you *will can* go out.', 'can', 'Two modals can’t go together: ‘you can go out’.'),
  ('Question', 'What *do* you do if it rains tomorrow?', 'will', 'A question about one future situation needs will: ‘What will you do…?’.'),
  ('Imperative', 'If you see Ana, *tells* her I called.', 'tell', 'An imperative has no -s: ‘tell her’.'),
  ('Will + base verb', 'If you eat that, you’ll *feels* sick.', 'feel', 'After ‘will’ use the base verb: ‘you’ll feel’.'),
  ('Wrong word', 'If you *helps* me, I’ll make dinner.', 'help', 'With ‘you’ there is no -s: ‘If you help me…’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, result-clause choices, multiple choice and spot-the-mistake. In the typing questions write the present simple after if and will / won’t + verb in the result. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('result', 'Result clause'),
 'fill': [
  ('Likely future', 'If you [[leave]] now, you’ll arrive on time.', 'leave', 'After ‘if’ use the present simple: ‘you leave’.', 'No ‘will’ after ‘if’: ‘If you leave…’.'),
  ('Likely future', 'If it’s sunny, we [[will go|’ll go]] to the beach.', 'go', 'The result takes will + base verb: ‘will go’.', 'Use will + base verb: ‘will go’.'),
  ('Negative', 'If you don’t wear a coat, you [[won’t be]] warm.', 'not be', 'A negative future result: won’t + base verb.', 'Use won’t + base verb: ‘won’t be’.'),
  ('Unless', 'Unless she [[runs]], she’ll miss the bus.', 'run', 'After ‘unless’ use an affirmative present simple, with -s for ‘she’.', '‘Unless’ = if not; write ‘runs’ (affirmative).'),
  ],
 'order': [
  ('Likely future', 'If we win, we’ll celebrate.', ['we’ll celebrate if we win.']),
  ('Negative', 'If you don’t study, you won’t pass.', ['you won’t pass if you don’t study.']),
  ('Question', 'What will you do if you lose?', ['if you lose, what will you do?']),
  ('Unless', 'Unless it rains, we’ll play outside.', ['we’ll play outside unless it rains.']),
  ],
 'customItems': [
  ('Modal', 'If you feel ill, you ___ see a doctor.', ['should', 'will should', 'should to', 'are should'],
   ['Two modals can’t go together: no ‘will should’.', '‘Should’ is followed by the base verb, not ‘to’.', '‘Are should’ isn’t a possible form.'],
   'Advice in the result clause: should + base verb.'),
  ('Going to', 'If he’s late again, he ___ lose his job.', ['’s going to', '’s go to', 'going to', 'will going to'],
   ['‘Be going to’ needs ‘go’ + -ing: ‘is going to’.', 'It needs ‘be’: ‘he’s going to’.', 'Never mix ‘will’ and ‘going to’.'],
   '‘Be going to’ can replace will in the result clause.'),
  ('Imperative', 'If you get lost, ___ me.', ['call', 'you will calling', 'calls', 'to call'],
   ['Wrong form: after ‘will’ use the base verb; an instruction needs the imperative.', 'An imperative never has -s.', 'An imperative has no ‘to’.'],
   'An instruction in the result: imperative, ‘call me’.'),
  ('Might', 'If we hurry, we ___ get there before it closes.', ['might', 'might to', 'will might', 'mights'],
   ['‘Might’ is followed by the base verb, no ‘to’.', 'Two modals can’t go together.', 'Modals never take -s.'],
   '‘Might’ + base verb shows a possible, less certain result.'),
  ],
 'mc': [
  ('Likely future', 'If you ___ me your email, I’ll send you the photos.', ['give', 'will give', 'gave', 'gives'],
   ['No ‘will’ after ‘if’.', '‘Gave’ belongs to the second conditional.', 'With ‘you’ there is no -s.'],
   'If + present simple: ‘you give’.'),
  ('Warning', 'If you don’t stop, I ___ the teacher.', ['’ll tell', 'tell', 'told', 'telling'],
   ['A warning about the future needs ‘will’.', '‘Told’ is past.', '‘Telling’ needs an auxiliary.'],
   'A warning: I’ll + base verb.'),
  ('Time linker', 'We’ll have dinner when Dad ___ home.', ['gets', 'will get', 'get', 'got'],
   ['No ‘will’ after a future ‘when’.', '‘Dad’ is he, so add -s.', '‘Got’ is past.'],
   'After future ‘when’ use the present simple: ‘gets’.'),
  ('First or second', 'If I ___ the lottery, I’ll buy a house — I’ve got a ticket!', ['win', 'won', 'would win', 'will win'],
   ['The result is ‘I’ll’, a real future, so not the past.', '‘Would’ never goes after ‘if’ here.', 'No ‘will’ after ‘if’.'],
   'A real possibility with ‘I’ll’: present simple ‘win’.'),
  ],
 'error': [
  ('Will after if', 'If she *will ask*, I’ll help.', 'asks', 'No ‘will’ after ‘if’: ‘If she asks…’.'),
  ('Missing will', 'If you come tomorrow, *I show* you the photos.', 'I’ll show', 'A future result needs will: ‘I’ll show you’.'),
  ('Unless + not', 'Unless you *don’t study*, you’ll fail.', 'study', '‘Unless’ already means ‘if not’: ‘Unless you study…’.'),
  ('Will + base verb', 'If it rains, we’ll *stayed* inside.', 'stay', 'After ‘will’ use the base verb: ‘we’ll stay’.'),
  ],
}
