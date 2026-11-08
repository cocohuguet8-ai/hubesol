TITLE = 'Should & Ought to'
AUX = (['should', 'shouldn’t', 'ought'], None, 'should')
NEXT = ('Must & Have to', '/grammar/modal-verbs/must-have-to-obligation/')
BODY = r'''
## How to form should and ought to

| Form | Structure | Example |
|---|---|---|
| Affirmative | should + base verb | You **should rest**. |
| Affirmative | ought to + base verb | You **ought to rest**. |
| Negative | shouldn't + base verb | You **shouldn't worry**. |
| Question | Should + subject + base verb? | **Should** I **call** her? |

*Should* is a modal verb: no *-s*, no *to* after it, no *do* in questions. *Ought* is the only modal that **always** takes *to*.

| ✗ | ✓ |
|---|---|
| ~~She shoulds go.~~ | She **should** go. |
| ~~You should to study.~~ | You **should study**. |
| ~~You ought study.~~ | You **ought to study**. |
| ~~Do I should call?~~ | **Should** I call? |

## When to use *should* and *ought to*

### 1. Giving advice

We say what we think is the best thing to do.

- You **should** see a doctor about that cough.
- You **ought to** wear a helmet when you cycle.

> ⚠️ Typical error: ~~You should to see a doctor.~~ → No *to* after *should*: *You should see a doctor.*

### 2. Saying what is right or wrong

- People **should** recycle their rubbish.
- You **shouldn't** talk with your mouth full.

> ⚠️ Typical error: ~~You don't should talk with your mouth full.~~ → The negative is *shouldn't*.

### 3. Asking for advice

- **Should** I tell the teacher?
- What **should** I wear to the party?

> ⚠️ Typical error: ~~What I should wear?~~ → Question order: *What should I wear?*

### 4. Expectation (it's probably true)

*Should* can also mean we expect something.

- The bus **should** be here in five minutes.
- The exam **shouldn't** be too difficult.

## *Should* or *ought to*?

They mean almost the same. *Should* is much more common, especially in questions and negatives. *Ought to* is a bit more formal and sounds stronger.

| | *should* | *ought to* |
|---|---|---|
| frequency | very common | less common |
| negative | shouldn't | ought not to (rare) |
| question | Should I…? | Ought I to…? (very rare) |

## Other ways to give advice

| Phrase | Followed by | Example |
|---|---|---|
| If I were you, I'd… | base verb | **If I were you, I'd** apologise. |
| You'd better… | base verb | **You'd better** hurry. (strong: or there's a problem) |
| Why don't you…? | base verb | **Why don't you** ask for help? |

*Had better* is stronger than *should*: it suggests a bad result if you don't do it.

## *Should* vs *must*

| *should* | *must* |
|---|---|
| advice, opinion | obligation, necessity |
| You **should** go to bed early. | You **must** wear a seatbelt. |

See [Must & Have to](/grammar/modal-verbs/must-have-to-obligation/).

## Common mistakes

**1. *To* after *should*.** *~~You should to rest~~* → **You should rest.**

**2. Forgetting *to* after *ought*.** *~~You ought go~~* → **You ought to go.**

**3. *-s* or *-ed* after *should*.** *~~He should studies~~* → **He should study.**

**4. Wrong question order.** *~~I should go?~~* → **Should I go?**

**Pro tip:** *should* is your opinion; *must* is a rule. If you're giving a friend tips, *should* is almost always right.
'''

GAP = ('Fill in the gaps',
  'Type should, shouldn’t, ought to or the base verb that follows. Twenty original sentences.',
  [
  ('Advice', 'You look tired. You [[should]] go to bed earlier.', 'should / shouldn’t', 'Advice about what is best to do: should + base verb.'),
  ('Advice', 'You [[shouldn’t]] eat so many sweets — they’re bad for your teeth.', 'should / shouldn’t', 'Advice not to do something: shouldn’t + base verb.'),
  ('Advice', 'You [[ought to]] wear a coat. It’s freezing outside.', 'ought to', '‘Ought’ always needs ‘to’ before the base verb: ought to wear.'),
  ('Advice', 'If you have a headache, you should [[drink]] more water.', '(drink)', 'After ‘should’ use the base verb, with no ‘to’ and no -s.'),
  ('Advice', 'Marc should [[study]] more if he wants to pass.', '(study)', 'After ‘should’ the verb stays in the base form: study, not studies.'),
  ('Advice', 'You [[shouldn’t]] stay up late before an exam.', 'should / shouldn’t', 'It’s a bad idea, so the advice is negative: shouldn’t.'),
  ('Right and wrong', 'People [[should]] recycle plastic bottles.', 'should / shouldn’t', 'Saying what is the right thing to do: should.'),
  ('Right and wrong', 'Children [[shouldn’t]] play near the road.', 'should / shouldn’t', 'Saying what is wrong or dangerous: shouldn’t.'),
  ('Right and wrong', 'We [[ought to]] help our neighbours more.', 'ought to', 'A moral opinion with ‘ought to’ (a little stronger than should).'),
  ('Asking', '[[Should]] I tell the teacher about it?', 'should / ought', 'Asking for advice: Should + subject + base verb?'),
  ('Asking', 'What [[should]] I buy for my mum’s birthday?', 'should / ought', 'A wh- question asking for advice: What should I…?'),
  ('Asking', 'Where should we [[go]] on holiday this year?', '(go)', 'In the question, the base verb comes after the subject: should we go.'),
  ('Expectation', 'The train [[should]] arrive at ten — it’s usually on time.', 'should / must', '‘Should’ can show what we expect to happen.'),
  ('Expectation', 'The test [[shouldn’t]] be too hard. We’ve practised a lot.', 'should / shouldn’t', 'Expecting something not to happen: shouldn’t be.'),
  ('Had better', 'You’d [[better]] hurry, or you’ll miss the bus.', 'better', '‘Had better’ is strong advice: there’s a problem if you don’t.'),
  ('Had better', 'We’d better not [[make]] any noise — the baby is asleep.', '(make)', '‘Had better not’ + base verb: make.'),
  ('If I were you', 'If I were you, I’d [[apologise]] to her.', '(apologise)', 'Advice with ‘If I were you, I’d’ + base verb.'),
  ('Why don’t you', 'Why don’t you [[ask]] your brother for help?', '(ask)', '‘Why don’t you’ + base verb gives friendly advice.'),
  ('Short answer', '“Should I wear a tie?” “Yes, you [[should]].”', 'should / do', 'Short answers repeat the modal: Yes, you should.'),
  ('Short answer', '“Should we wait for him?” “No, we [[shouldn’t]].”', 'should / shouldn’t', 'Negative short answer: No, we shouldn’t.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples of giving and asking for advice.',
  [
  ('Advice', 'You should see a doctor.', []),
  ('Advice', 'You shouldn’t eat so much sugar.', []),
  ('Advice', 'You ought to call your grandmother.', []),
  ('Advice', 'She should take an umbrella.', []),
  ('Advice', 'We should leave now.', []),
  ('Advice', 'You shouldn’t worry about it.', []),
  ('Right and wrong', 'People should be kind to animals.', []),
  ('Right and wrong', 'We ought to save more water.', []),
  ('Right and wrong', 'You shouldn’t lie to your friends.', []),
  ('Asking', 'Should I tell him the truth?', []),
  ('Asking', 'What should I do now?', []),
  ('Asking', 'Where should we meet?', []),
  ('Asking', 'Should we bring anything?', []),
  ('Expectation', 'The bus should be here soon.', []),
  ('Expectation', 'It shouldn’t take long.', []),
  ('Had better', 'You’d better hurry up.', []),
  ('Had better', 'We’d better not be late.', []),
  ('If I were you', 'If I were you, I’d stay.', ['I’d stay if I were you.']),
  ('Why don’t you', 'Why don’t you try again?', []),
  ('Short answer', 'Yes, you should.', []),
  ])

MATCH = {'title': 'Match the problem and the advice', 'subtitle': 'Tap a problem, then tap the best advice.',
  'leftLabel': 'Problem', 'rightLabel': 'Advice', 'rightLabelSub': '(should / shouldn’t)', 'reviewArrowPrefix': '',
  'pairs': [
  ('I’ve got a toothache.', 'You should see a dentist.'), ('I’m always tired.', 'You should sleep more.'), ('I’m cold.', 'You should put on a jumper.'),
  ('I failed my maths test.', 'You should study harder.'), ('I’m hungry.', 'You should have a snack.'), ('I can’t find my keys.', 'You should look in your bag.'),
  ('I spend too much money.', 'You shouldn’t buy so many clothes.'), ('My eyes hurt.', 'You shouldn’t use your phone so much.'), ('I’m always late.', 'You should get up earlier.'),
  ('I’ve got a cold.', 'You should drink hot tea.'), ('I want to get fit.', 'You should go running.'), ('I’ve had an argument with Pau.', 'You should talk to him.'),
  ('I’m bored.', 'You should read a book.'), ('My room is a mess.', 'You should tidy it.'), ('I feel stressed.', 'You shouldn’t work so hard.'),
  ('I can’t sleep.', 'You shouldn’t drink coffee at night.'), ('I want to learn French.', 'You should take a course.'), ('I’ve lost my wallet.', 'You should tell the police.'),
  ('My plants are dying.', 'You should water them.'), ('I’ve got an exam tomorrow.', 'You shouldn’t go out tonight.'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Should + base verb, ought + to + base verb — and no do in questions.',
  [
  ('Advice', 'You ___ see a doctor about that cough.', ['should', 'should to', 'ought', 'shoulds'],
   ['‘Should’ is never followed by ‘to’ — the base verb comes straight after it.', '‘Ought’ always needs ‘to’: ‘ought to see’.', 'Modal verbs never take -s, whatever the subject.'],
   'Advice: should + base verb. It’s the most common way to say what’s best.'),
  ('Ought to', 'You ___ wear a helmet on your bike.', ['ought to', 'ought', 'should to', 'oughts to'],
   ['‘Ought’ is the one modal that always needs ‘to’.', '‘Should’ never takes ‘to’.', 'Modals never take -s.'],
   '‘Ought to’ + base verb means the same as ‘should’, a little more strongly.'),
  ('Negative', 'You ___ eat so much fast food.', ['shouldn’t', 'don’t should', 'not should', 'shouldn’t to'],
   ['Modals don’t use ‘don’t’: the negative is ‘shouldn’t’.', '‘Not’ goes after the modal: ‘should not’.', 'No ‘to’ after ‘shouldn’t’.'],
   'Negative advice: shouldn’t + base verb.'),
  ('Base verb', 'Lucía should ___ more vegetables.', ['eat', 'eats', 'to eat', 'eating'],
   ['After ‘should’ the verb has no -s, even with ‘she’.', 'No ‘to’ after ‘should’.', 'After ‘should’ we use the base verb, not -ing.'],
   'After ‘should’, always the base verb: should eat.'),
  ('Question', '___ I bring a present to the party?', ['Should', 'Do I should', 'Ought', 'Am I should'],
   ['Modals make questions without ‘do’.', '‘Ought I bring’ is wrong; even ‘Ought I to’ is very rare.', '‘Am I should’ mixes ‘be’ with a modal.'],
   'Asking for advice: Should + subject + base verb?'),
  ('Question order', 'What ___ for the job interview?', ['should I wear', 'I should wear', 'should I to wear', 'do I should wear'],
   ['In a question, the modal comes before the subject.', 'No ‘to’ after ‘should’.', 'No ‘do’ with modals.'],
   'Wh- question with a modal: What + should + subject + base verb?'),
  ('Right and wrong', 'People ___ drop litter in the street.', ['shouldn’t', 'should', 'ought', 'ought not'],
   ['‘Should drop litter’ says it’s a good idea — the opposite.', '‘Ought drop’ needs ‘to’, and the meaning is wrong.', '‘Ought not’ needs ‘to’: ‘ought not to drop’.'],
   'Saying something is wrong: shouldn’t + base verb.'),
  ('Expectation', 'The parcel ___ arrive tomorrow — they sent it yesterday.', ['should', 'must to', 'ought', 'shoulds'],
   ['‘Must’ never takes ‘to’, and it means obligation.', '‘Ought’ needs ‘to’.', 'Modals never take -s.'],
   '‘Should’ can mean ‘I expect this will happen’.'),
  ('Had better', 'You’d ___ leave now or you’ll miss the train.', ['better', 'best', 'better to', 'should'],
   ['The phrase is ‘had better’, not ‘had best’ in everyday English.', 'No ‘to’ after ‘had better’.', '‘You’d should’ is impossible.'],
   '‘You’d better’ + base verb: strong advice with a warning.'),
  ('Had better', 'We’d better ___ make a noise. Grandma is sleeping.', ['not', 'don’t', 'no', 'not to'],
   ['‘Had better don’t’ is wrong: use ‘not’.', '‘No’ can’t make a verb negative.', 'No ‘to’ after ‘had better not’.'],
   'Negative: had better not + base verb.'),
  ('If I were you', 'If I were you, I ___ that phone. It’s too expensive.', ['wouldn’t buy', 'shouldn’t to buy', 'won’t buy', 'don’t buy'],
   ['No ‘to’ after ‘shouldn’t’, and the phrase needs ‘would’.', '‘Won’t’ doesn’t follow ‘If I were you’.', '‘If I were you’ needs ‘would’ in the result.'],
   '‘If I were you, I’d / I wouldn’t…’ is a common way to give advice.'),
  ('Why don’t you', 'Why don’t you ___ to the manager?', ['speak', 'speaking', 'to speak', 'speaks'],
   ['After ‘don’t’ use the base verb, not -ing.', 'No ‘to’ after ‘don’t’.', 'No -s after ‘don’t’.'],
   '‘Why don’t you’ + base verb is friendly advice.'),
  ('Should or must', 'It’s the law: you ___ wear a seatbelt in a car.', ['must', 'should', 'ought', 'had better to'],
   ['‘Should’ is advice; a law is an obligation.', '‘Ought’ needs ‘to’, and it’s advice, not a law.', 'No ‘to’ after ‘had better’.'],
   'A law or rule is an obligation: must. ‘Should’ is only advice.'),
  ('Should or must', 'I think you ___ try the chocolate cake. It’s delicious!', ['should', 'must to', 'have', 'ought'],
   ['No ‘to’ after ‘must’.', '‘Have’ needs ‘to’ and means obligation.', '‘Ought’ needs ‘to’.'],
   '‘I think you should…’ gives an opinion or recommendation.'),
  ('Short answer', '“Should I call him?” “Yes, you ___.”', ['should', 'do', 'ought', 'shall'],
   ['Short answers repeat the modal, not ‘do’.', '‘Yes, you ought’ needs ‘to’.', '‘Shall’ doesn’t answer ‘should’.'],
   'Short answer: Yes, you should.'),
  ('Short answer', '“Should we take a taxi?” “No, we ___. It’s close.”', ['shouldn’t', 'don’t', 'mustn’t to', 'aren’t'],
   ['Repeat the modal, not ‘do’.', 'No ‘to’ after ‘mustn’t’, and the meaning is too strong.', '‘Aren’t’ doesn’t answer ‘should’.'],
   'Negative short answer: No, we shouldn’t.'),
  ('Third person', 'Which sentence is correct?', ['He should practise every day.', 'He shoulds practise every day.', 'He should practises every day.', 'He should to practise every day.'],
   ['Modals never take -s.', 'After ‘should’ use the base verb.', 'No ‘to’ after ‘should’.'],
   'Should + base verb, the same for every subject.'),
  ('Ought to', 'Which sentence is correct?', ['You ought to apologise.', 'You ought apologise.', 'You ought to apologising.', 'You oughts to apologise.'],
   ['‘Ought’ needs ‘to’.', 'After ‘to’ use the base verb.', 'Modals never take -s.'],
   'Ought + to + base verb.'),
  ('Advice', 'It’s raining. You ___ take an umbrella.', ['should', 'shouldn’t', 'ought', 'should to'],
   ['‘Shouldn’t take’ is the opposite advice.', '‘Ought’ needs ‘to’.', 'No ‘to’ after ‘should’.'],
   'Good advice for rain: should take an umbrella.'),
  ('Expectation', 'It ___ be difficult to find the hotel — it’s next to the station.', ['shouldn’t', 'should', 'ought', 'mustn’t'],
   ['‘Should be difficult’ is the opposite of what the context says.', '‘Ought’ needs ‘to’.', '‘Mustn’t’ means it’s forbidden.'],
   'Expecting something easy: shouldn’t be difficult.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('-s after a modal', 'You should *sees* a doctor.', 'see', 'After ‘should’ use the base verb: ‘You should see a doctor’.'),
  ('Missing to', 'You ought *study* for the test.', 'to study', '‘Ought’ always needs ‘to’: ‘ought to study’.'),
  ('-s on a modal', 'She *shoulds* go home.', 'should', 'Modals never take -s: ‘She should go home’.'),
  ('-s after a modal', 'He should *takes* a break.', 'take', 'After ‘should’ use the base verb: ‘take’.'),
  ('-ing after a modal', 'You should *going* to bed.', 'go', 'After ‘should’ use the base verb: ‘go’.'),
  ('Past after a modal', 'You should *called* her.', 'call', 'For present advice, use the base verb: ‘You should call her’.'),
  ('Do with a modal', '*Do* I should tell him?', 'Should', 'No ‘do’ with modals: ‘Should I tell him?’.'),
  ('Wrong negative', 'You *don’t* should worry.', 'shouldn’t', 'The negative is ‘shouldn’t’: ‘You shouldn’t worry’.'),
  ('-ing after a modal', 'What should I *doing* now?', 'do', 'After ‘should’ use the base verb: ‘What should I do?’.'),
  ('Had better', 'You’d better *hurried*.', 'hurry', 'After ‘had better’ use the base verb: ‘You’d better hurry’.'),
  ('Had better', 'We’d better *don’t* be late.', 'not', 'Negative: ‘We’d better not be late’.'),
  ('Had better', 'You *have* better leave now.', 'had', 'The phrase is ‘had better’ (’d better), not ‘have better’.'),
  ('If I were you', 'If I *was* you, I’d rest.', 'were', 'The advice phrase is ‘If I were you’.'),
  ('If I were you', 'If I were you, I *will* apologise.', 'would', '‘If I were you’ needs ‘would’: ‘I would apologise’.'),
  ('Why don’t you', 'Why don’t you *asking* the teacher?', 'ask', '‘Why don’t you’ + base verb: ‘ask’.'),
  ('Short answer', '“Should I go?” “Yes, you *do*.”', 'should', 'Repeat the modal: ‘Yes, you should’.'),
  ('Should or must', 'It’s the law — you *should* stop at a red light.', 'must', 'A law is an obligation: ‘you must stop’.'),
  ('Ought not', 'You ought not *eat* so late.', 'to eat', 'Negative: ‘ought not to eat’.'),
  ('Expectation', 'The bus should *arrives* soon.', 'arrive', 'After ‘should’ use the base verb: ‘arrive’.'),
  ('Wrong modal', 'I think you *will* try this restaurant — it’s great.', 'should', 'A recommendation uses ‘should’: ‘I think you should try…’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, which advice phrase, multiple choice and spot-the-mistake. In the typing questions write should, shouldn’t, ought to or the base verb. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('phrase', 'Advice phrases'),
 'fill': [
  ('Advice', 'You [[should]] drink more water when it’s hot.', 'should / shouldn’t', 'Good advice: should + base verb, no ‘to’.', 'Advice → ‘should’.'),
  ('Negative', 'You [[shouldn’t]] swim straight after lunch.', 'should / shouldn’t', 'Advice not to do something: shouldn’t.', 'Bad idea → ‘shouldn’t’.'),
  ('Ought to', 'We [[ought to]] leave a tip for the waiter.', 'ought to', '‘Ought’ always takes ‘to’: ought to leave.', 'Write ‘ought to’.'),
  ('Asking', 'What [[should]] I say to her?', 'should', 'Asking for advice: What should I…?', 'Question → ‘should’ before the subject.'),
  ],
 'order': [
  ('Advice', 'You should try it.', []),
  ('Asking', 'Should I wear a jacket?', []),
  ('Had better', 'You’d better go now.', []),
  ('Ought to', 'We ought to help her.', []),
  ],
 'customItems': [
  ('Had better', 'There’s a storm coming — you ___ stay inside!', ['’d better', '’d better to', 'better', 'should to'],
   ['No ‘to’ after ‘had better’.', 'It needs ‘had’: ‘you’d better’.', 'No ‘to’ after ‘should’.'],
   '‘Had better’ = strong advice with a warning.'),
  ('If I were you', '___, I’d talk to her.', ['If I were you', 'If I am you', 'When I were you', 'If I would be you'],
   ['‘If I am you’ is impossible.', '‘When’ doesn’t work for imaginary advice.', 'No ‘would’ in the if-clause.'],
   'Fixed phrase: If I were you, I’d…'),
  ('Why don’t you', '___ ask your sister to help you?', ['Why don’t you', 'Why you don’t', 'Why not you', 'Why do you not to'],
   ['Question order: ‘Why don’t you…?’.', '‘Why not you’ is wrong; ‘Why not ask’ is possible.', 'No ‘to’ here.'],
   '‘Why don’t you’ + base verb = friendly advice.'),
  ('Should or must', 'Which is advice, not a rule?', ['You should eat more fruit.', 'You must wear a seatbelt.', 'You mustn’t smoke here.', 'You have to show your ID.'],
   ['That’s a law: obligation.', 'That’s a prohibition.', 'That’s an external rule.'],
   '‘Should’ gives advice or an opinion.'),
  ],
 'mc': [
  ('Base verb', 'My brother should ___ his room.', ['tidy', 'tidies', 'to tidy', 'tidying'],
   ['No -s after ‘should’.', 'No ‘to’ after ‘should’.', 'No -ing after ‘should’.'],
   'Should + base verb.'),
  ('Question', '___ we book a table?', ['Should', 'Do we should', 'Ought', 'Are we should'],
   ['No ‘do’ with modals.', '‘Ought we book’ needs ‘to’ and is rare.', '‘Are we should’ is impossible.'],
   'Question: Should we…?'),
  ('Expectation', 'Don’t worry, it ___ be a problem.', ['shouldn’t', 'mustn’t', 'oughtn’t', 'doesn’t should'],
   ['‘Mustn’t’ means it’s forbidden.', '‘Oughtn’t’ needs ‘to’ and is rare.', 'No ‘do’ with modals.'],
   'Expecting no problem: shouldn’t be.'),
  ('Ought to', 'You ___ thank her for the present.', ['ought to', 'ought', 'should to', 'oughts'],
   ['‘Ought’ needs ‘to’.', 'No ‘to’ after ‘should’.', 'No -s on modals.'],
   'Ought + to + base verb.'),
  ],
 'error': [
  ('Past after should', 'You should *rested*.', 'rest', 'After ‘should’ use the base verb: ‘You should rest’.'),
  ('Missing to', 'We ought *leave* now.', 'to leave', '‘Ought’ needs ‘to’: ‘ought to leave’.'),
  ('-ing after a modal', 'Where should we *going*?', 'go', 'After ‘should’ use the base verb: ‘Where should we go?’.'),
  ('-s after a modal', 'She should *gets* more sleep.', 'get', 'After ‘should’ use the base verb.'),
  ],
}
