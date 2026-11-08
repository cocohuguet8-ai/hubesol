TITLE = 'Must vs Have to'
AUX = (['must', 'have', 'has', 'to'], None, 'must')
NEXT = ('Can’t vs Mustn’t', '/grammar/modal-verbs/cant-vs-mustnt/')
BODY = r'''
## How the two forms compare

| | *must* | *have to* |
|---|---|---|
| Type of verb | modal (no -s, no do) | normal verb (has to, do/does/did) |
| Who decides? | the **speaker** | someone **else**: rules, laws, situation |
| Past | — | **had to** |
| Future | — | **will have to** |
| Negative meaning | **mustn't** = forbidden | **don't have to** = not necessary |

In the present affirmative, both mean "it's necessary". The choice depends on **where the obligation comes from**.

## When to use *must*

### 1. The speaker's own feeling or decision

- I **must** stop eating so much sugar. (my decision)
- I **must** remember to call Laia. (a note to myself)

> ⚠️ Typical error: ~~I have to remember to call Laia.~~ → Possible, but for a personal reminder *must* sounds more natural.

### 2. Strong advice or recommendations

- You **must** come and visit us!
- You **must** read this book — it's fantastic.

> ⚠️ Typical error: ~~You have to see this film!~~ → Not wrong in speech, but *must* is the classic choice for an enthusiastic recommendation.

### 3. Formal written rules

Signs, notices and instructions often use *must* because the writer is the authority.

- Passengers **must** keep their luggage with them.
- Answers **must** be written in pen.

## When to use *have to*

### 1. Rules and laws from outside

- I **have to** wear a uniform. (the school's rule)
- In Spain, you **have to** be 18 to vote. (the law)

> ⚠️ Typical error: ~~I must wear a uniform at my school.~~ → Not wrong, but when you report a rule someone else made, *have to* is more natural.

### 2. Talking about other people's obligations

- My sister **has to** work on Sundays.
- Do doctors **have to** work at night?

### 3. Past, future and other forms

| Tense | Example |
|---|---|
| past | I **had to** get up at six yesterday. |
| future | You**'ll have to** wait. |
| after *might / may* | We **might have to** cancel. |
| -ing / infinitive | I hate **having to** queue. |

## The negatives: a big difference

| Sentence | Meaning |
|---|---|
| You **mustn't** tell her. | Don't tell her! It's forbidden. |
| You **don't have to** tell her. | You can tell her or not — it's your choice. |

## Questions

*Must I…?* exists but is rare and formal. In everyday English we ask with *have to*.

- **Do** I **have to** finish this today?
- **Does** he **have to** come?

## Common mistakes

**1. *Must* for the past.** *~~I must work yesterday~~* → **I had to work yesterday.**

**2. *Mustn't* for "not necessary".** *~~You mustn't bring anything~~* (when it's optional) → **You don't have to bring anything.**

**3. *Have to* without *do* in questions.** *~~Have you to go?~~* → **Do you have to go?**

**4. *Will must*.** *~~I will must study~~* → **I will have to study.**

**Pro tip:** *must* = "I say so"; *have to* = "the rules say so".
'''

GAP = ('Fill in the gaps',
  'Type must or the correct form of have to. Ask: does the obligation come from the speaker (must) or from outside (have to)? Twenty original sentences.',
  [
  ('Speaker', 'I [[must]] stop biting my nails — it’s a terrible habit.', 'must / have to', 'A personal decision by the speaker: must + base verb.'),
  ('Speaker', 'I [[must]] remember to water the plants before I leave.', 'must / have to', 'A reminder to yourself is typically ‘must’.'),
  ('Speaker', 'You [[must]] come to our house for dinner soon!', 'must / have to', 'An enthusiastic invitation or recommendation: must.'),
  ('Speaker', 'You [[must]] try the croissants at that bakery.', 'must / have to', 'A strong personal recommendation: must + base verb.'),
  ('Written rule', 'All students [[must]] bring their ID card to the exam.', 'must / have to', 'A formal written rule often uses ‘must’.'),
  ('Outside rule', 'At my school we [[have to]] wear a blue jumper.', 'must / have to', 'Reporting a rule made by someone else: have to.'),
  ('Outside rule', 'In the UK, cars [[have to]] drive on the left.', 'must / have to', 'A law of the country (outside obligation): have to.'),
  ('Other people', 'My dad [[has to]] travel to Madrid every week for work.', 'have to / has to', 'Another person’s obligation, third person: has to.'),
  ('Other people', 'Nurses often [[have to]] work at night.', 'must / have to', 'Talking about other people’s duties: have to.'),
  ('Past', 'We [[had to]] stay indoors because of the storm.', 'must / had to', '‘Must’ has no past form: had to.'),
  ('Past', 'I [[had to]] apologise to my teacher yesterday.', 'must / had to', 'Past obligation: had to + base verb.'),
  ('Future', 'You’ll [[have to]] book tickets in advance.', 'must / have to', '‘Will must’ is impossible: will have to.'),
  ('After a modal', 'We might [[have to]] change our plans.', 'must / have to', 'After another modal use ‘have to’.'),
  ('-ing form', 'I hate [[having to]] get up early on Mondays.', 'having to', '‘Hate’ + -ing: having to. ‘Must’ has no -ing form.'),
  ('Mustn’t', 'You [[mustn’t]] tell Ana about the surprise party!', 'mustn’t / don’t have to', 'Don’t do it — forbidden: mustn’t.'),
  ('Don’t have to', 'You [[don’t have to]] bring a towel — the hotel gives you one.', 'mustn’t / don’t have to', 'A casual party means a suit isn’t necessary: ‘don’t have to’ = you can choose.'),
  ('Question', '[[Do]] I have to finish this exercise today?', 'do / must', 'Everyday questions about obligation use ‘Do … have to’.'),
  ('Question', '[[Does]] Marc have to take the exam again?', 'do / does', 'He/she/it: Does + subject + have to?'),
  ('Speaker', 'I really [[must]] go now — it’s getting late.', 'must / had to', 'The speaker decides it’s time to go: must.'),
  ('Outside rule', 'Passengers [[have to]] show their passports at the gate.', 'have to / has to', 'An external rule (the airline): have to.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 10 with must (the speaker decides) and 10 with have to (outside rules and other tenses).',
  [
  ('Speaker', 'I must call my aunt tonight.', []),
  ('Speaker', 'I must eat more vegetables.', []),
  ('Speaker', 'You must visit us in summer.', []),
  ('Speaker', 'We must do this again soon.', []),
  ('Speaker', 'You must see this film.', []),
  ('Speaker', 'I must get some sleep.', []),
  ('Written rule', 'Visitors must leave their bags here.', []),
  ('Written rule', 'All answers must be in English.', []),
  ('Mustn’t', 'You mustn’t forget your passport.', []),
  ('Mustn’t', 'We mustn’t make any noise.', []),
  ('Outside rule', 'I have to wear a uniform.', []),
  ('Outside rule', 'We have to be home by ten.', []),
  ('Other people', 'She has to work on Sundays.', []),
  ('Past', 'I had to walk to school.', []),
  ('Past', 'They had to pay a fine.', []),
  ('Future', 'You’ll have to wait outside.', []),
  ('After a modal', 'We might have to leave early.', []),
  ('Don’t have to', 'You don’t have to come.', []),
  ('Question', 'Do you have to work tomorrow?', []),
  ('Question', 'Does he have to go?', []),
  ])

MATCH = {'title': 'Who decides?', 'subtitle': 'Tap a sentence, then tap where the obligation comes from: the speaker (must) or an outside rule (have to).',
  'leftLabel': 'Sentence', 'rightLabel': 'Who decides?', 'rightLabelSub': '(speaker / outside)', 'reviewArrowPrefix': '',
  'pairs': [
  ('I must lose some weight.', 'the speaker'), ('I have to wear a uniform.', 'an outside rule'), ('I must remember her birthday.', 'the speaker'),
  ('We have to be in class by eight.', 'an outside rule'), ('You must come and see us!', 'the speaker'), ('Drivers have to stop at red lights.', 'an outside rule'),
  ('I must phone Mum.', 'the speaker'), ('My dad has to start at seven.', 'an outside rule'), ('You must try this pizza.', 'the speaker'),
  ('Students have to switch off their phones.', 'an outside rule'), ('I must get fit.', 'the speaker'), ('You have to be 18 to drive here.', 'an outside rule'),
  ('I must stop shouting.', 'the speaker'), ('We have to pay to park.', 'an outside rule'), ('I must tidy my desk.', 'the speaker'),
  ('Pilots have to have a licence.', 'an outside rule'), ('I really must go.', 'the speaker'), ('Players have to wear shin pads.', 'an outside rule'),
  ('We must meet more often.', 'the speaker'), ('You have to queue here.', 'an outside rule'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Must = the speaker decides; have to = outside rules, other people, and every tense must doesn’t have.',
  [
  ('Speaker', 'I ___ go to bed earlier. I’m always tired.', ['must', 'have to', 'had to', 'mustn’t'],
   ['‘Have to’ suggests a rule from outside, but this is your own decision.', '‘Had to’ is past, but the decision is about now.', '‘Mustn’t’ means it’s forbidden — the opposite.'],
   'A personal decision made by the speaker: must + base verb.'),
  ('Outside rule', 'At work, my mum ___ wear a uniform.', ['has to', 'must', 'have to', 'musts'],
   ['‘Must’ sounds like the speaker’s opinion; this is the company’s rule about mum.', '‘Mum’ is she, so ‘have to’ needs -s: ‘has to’.', 'Modals never take -s.'],
   'An outside rule about another person: has to.'),
  ('Speaker', 'You ___ come to the beach with us — it’ll be great fun!', ['must', 'have to', 'mustn’t', 'had to'],
   ['‘Have to’ sounds like a rule; this is an enthusiastic invitation.', '‘Mustn’t’ means it’s forbidden.', '‘Had to’ is past.'],
   'A warm invitation or recommendation: You must…!'),
  ('Outside rule', 'In Spain, you ___ be 18 to get a driving licence.', ['have to', 'must to', 'had to', 'mustn’t'],
   ['‘Must’ never takes ‘to’.', '‘Had to’ is past; the law is still true.', '‘Mustn’t’ means it’s forbidden.'],
   'A law of the country: have to.'),
  ('Past', 'Yesterday we ___ wait an hour for the doctor.', ['had to', 'must', 'have to', 'musted'],
   ['‘Must’ has no past form.', '‘Have to’ is present.', '‘Musted’ doesn’t exist.'],
   '‘Must’ has no past form, so both kinds of obligation become ‘had to’ in the past.'),
  ('Future', 'You ___ show your ticket at the door tonight.', ['’ll have to', '’ll must', 'must to', 'had to'],
   ['‘Will must’ is impossible.', 'No ‘to’ after ‘must’.', '‘Had to’ is past.'],
   '‘Will must’ is impossible, so future obligations are always ‘will have to’.'),
  ('Written rule', 'Sign at the pool: “Swimmers ___ shower before entering.”', ['must', 'must to', 'has to', 'musts'],
   ['No ‘to’ after ‘must’.', '‘Swimmers’ is plural, so not ‘has to’.', 'Modals never take -s.'],
   'Signs and formal written rules usually use ‘must’ because the writer is the authority.'),
  ('Mustn’t', 'You ___ open this door. The alarm will ring.', ['mustn’t', 'don’t have to', 'didn’t have to', 'haven’t to'],
   ['‘Don’t have to’ means it’s optional.', '‘Didn’t have to’ is past and optional.', '‘Haven’t to’ is not correct.'],
   'The alarm shows it’s forbidden, so use ‘mustn’t’ — not ‘don’t have to’ (optional).'),
  ('Don’t have to', 'You ___ wear a suit. It’s a casual party.', ['don’t have to', 'mustn’t', 'must', 'have to'],
   ['‘Mustn’t’ means a suit is forbidden.', '‘Must’ means a suit is necessary.', '‘Have to’ means a suit is necessary.'],
   'Not necessary: don’t have to.'),
  ('Question', '___ we have to bring our own lunch?', ['Do', 'Must', 'Have', 'Are'],
   ['‘Must we have to’ uses two obligation words.', '‘Have we have to’ is wrong.', '‘Are we have to’ is wrong.'],
   'Everyday questions about obligation use ‘have to’ with do: Do + subject + have to?'),
  ('Other people', 'Firefighters ___ be very fit.', ['have to', 'must to', 'has to', 'had'],
   ['No ‘to’ after ‘must’.', '‘Firefighters’ is plural, so ‘have to’.', '‘Had be’ is wrong.'],
   'When we describe what other people’s jobs require, we normally use ‘have to’.'),
  ('-ing form', 'I don’t like ___ get up early.', ['having to', 'must', 'have to', 'to must'],
   ['‘Must’ has no -ing form.', 'After ‘like’ use -ing or ‘to’ + verb: ‘having to’.', '‘To must’ doesn’t exist.'],
   '‘Must’ has no -ing form, so after like / hate / enjoy use ‘having to’.'),
  ('After a modal', 'We may ___ cancel the trip if it rains.', ['have to', 'must', 'has to', 'to have'],
   ['‘May must’ is impossible.', 'No -s after a modal.', 'No ‘to’ after ‘may’.'],
   'After another modal such as ‘may’ or ‘might’, use the base form ‘have to’.'),
  ('Speaker', 'I ___ tidy my room. It’s a disaster! (I’ve decided.)', ['must', 'have to', 'had to', 'don’t have to'],
   ['‘Have to’ would mean someone else told you to.', '‘Had to’ is past.', '‘Don’t have to’ is the opposite.'],
   '‘I’ve decided’ shows the obligation comes from you, the speaker: must.'),
  ('Outside rule', 'I ___ tidy my room — my mum says so.', ['have to', 'must', 'mustn’t', 'had'],
   ['‘Must’ suggests it’s your own decision; here mum decides.', '‘Mustn’t’ means it’s forbidden.', '‘Had tidy’ is wrong.'],
   '‘My mum says so’ shows the obligation comes from outside, so use ‘have to’.'),
  ('Past', 'When I was little, I ___ go to bed at eight.', ['had to', 'must', 'have to', 'musted'],
   ['‘Must’ has no past.', '‘Have to’ is present.', '‘Musted’ doesn’t exist.'],
   'A rule from your childhood is in the past, and ‘must’ has no past: had to.'),
  ('Question', '___ your brother have to do military service?', ['Does', 'Do', 'Must', 'Has'],
   ['‘Your brother’ is he: ‘does’.', '‘Must your brother have to’ is wrong.', '‘Has your brother have to’ is wrong.'],
   '‘Your brother’ is he, so the question is ‘Does your brother have to…?’.'),
  ('Negatives', 'Which sentence means ‘it isn’t necessary’?', ['You don’t have to wait.', 'You mustn’t wait.', 'You must wait.', 'You have to wait.'],
   ['‘Mustn’t’ = forbidden.', '‘Must’ = necessary.', '‘Have to’ = necessary.'],
   '‘Don’t have to’ means it isn’t necessary — you can choose to do it or not.'),
  ('Will must', 'Which sentence is correct?', ['You’ll have to study harder.', 'You’ll must study harder.', 'You must to study harder.', 'You’ll have study harder.'],
   ['Two modals can’t go together.', 'No ‘to’ after ‘must’.', '‘Have’ needs ‘to’.'],
   'For the future we can’t use ‘will must’: the correct form is ‘will have to’.'),
  ('Speaker', 'I ___ write to Granny. I haven’t written for months.', ['must', 'mustn’t', 'had to', 'have'],
   ['‘Mustn’t’ means it’s forbidden.', '‘Had to’ is past.', '‘Have write’ needs ‘to’.'],
   'You feel a personal duty to write — nobody is making you — so ‘must’ is natural.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('Past', 'Yesterday I *must* work late.', 'had to', '‘Must’ has no past: ‘I had to work late’.'),
  ('Past', 'Last summer we *must* wear masks.', 'had to', 'Past obligation: ‘we had to wear…’.'),
  ('Future', 'Next week you will *must* take an exam.', 'have to', 'Future: ‘you’ll have to take an exam’.'),
  ('Base verb', 'You must *trying* this cake!', 'try', 'After ‘must’ use the base verb: ‘You must try…’.'),
  ('-s on must', 'She *musts* finish her essay.', 'must', 'Modals never take -s.'),
  ('Has to', 'My brother *have* to wear braces.', 'has', 'He → ‘has to’.'),
  ('Missing to', 'We have *leave* at six.', 'to leave', '‘Have’ needs ‘to’: ‘have to leave’.'),
  ('Wrong negative', 'It’s free — you *mustn’t* pay.', 'don’t have to', 'Not necessary: ‘you don’t have to pay’.'),
  ('Wrong negative', 'Stop! You *needn’t* cross the road now — a car is coming.', 'mustn’t', 'Dangerous / forbidden: ‘you mustn’t cross’.'),
  ('Wrong negative', 'He *mustn’t* work tomorrow — it’s a holiday.', 'doesn’t have to', 'No obligation: ‘he doesn’t have to work’.'),
  ('Question', 'Do you *has* to go now?', 'have', 'After ‘do’ use ‘have’: ‘Do you have to go now?’.'),
  ('Question', '*Do* she have to work today?', 'Does', 'She → ‘Does she have to…?’.'),
  ('Question', 'Does he *has* to come?', 'have', 'After ‘does’ use ‘have’.'),
  ('Question', 'Did you *had* to queue?', 'have', 'After ‘did’ use ‘have’.'),
  ('-ing form', 'I hate *must* get up early.', 'having to', 'After ‘hate’ use -ing: ‘having to’.'),
  ('After a modal', 'We might *must* cancel.', 'have to', 'After ‘might’ use ‘have to’.'),
  ('Base verb', 'I must *calling* the bank.', 'call', 'After ‘must’ use the base verb: ‘call’.'),
  ('Base verb', 'She has to *works* late.', 'work', 'After ‘has to’ use the base verb: ‘work’.'),
  ('Short answer', '“Do you have to go?” “Yes, I *have*.”', 'do', 'Short answer for ‘do … have to’: ‘Yes, I do’.'),
  ('Wrong form', 'She *had* to go to the dentist tomorrow.', 'has', 'Tomorrow (a fixed appointment) is present/future: ‘has to go’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, who decides, multiple choice and spot-the-mistake. In the typing questions write must or the correct form of have to. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('source', 'Who decides?'),
 'fill': [
  ('Speaker', 'I [[must]] write that email today. I keep forgetting!', 'must / have to', 'Your own decision or reminder: must.', 'Speaker’s decision → ‘must’.'),
  ('Outside rule', 'In our school we [[have to]] speak English in class.', 'must / have to', 'Reporting someone else’s rule: have to.', 'Outside rule → ‘have to’.'),
  ('Past', 'I [[had to]] miss the party because I was ill.', 'must / had to', 'Past obligation: had to.', 'Past → ‘had to’.'),
  ('Other people', 'Our neighbour [[has to]] walk her dog three times a day.', 'have to / has to', 'Another person (she): has to.', 'He/she → ‘has to’.'),
  ],
 'order': [
  ('Speaker', 'I must buy a present.', []),
  ('Outside rule', 'We have to wear helmets.', []),
  ('Future', 'You’ll have to hurry.', []),
  ('Question', 'Do I have to sign here?', []),
  ],
 'customItems': [
  ('Source', '“I ___ start running again. I feel so unfit!”', ['must', 'have to', 'had to', 'mustn’t'],
   ['There’s no outside rule — it’s your own feeling.', '‘Had to’ is past.', '‘Mustn’t’ is the opposite.'],
   'The speaker decides: must.'),
  ('Source', '“The doctor says I ___ rest my knee for two weeks.”', ['have to', 'must to', 'mustn’t', 'had'],
   ['No ‘to’ after ‘must’.', '‘Mustn’t’ means it’s forbidden.', '‘Had rest’ is wrong.'],
   'Someone else (the doctor) decides: have to.'),
  ('Source', 'Notice: “Library books ___ be returned by Friday.”', ['must', 'has to', 'must to', 'musts'],
   ['‘Books’ is plural, so not ‘has to’.', 'No ‘to’ after ‘must’.', 'No -s on modals.'],
   'Formal written rules use ‘must’.'),
  ('Source', '“My sister ___ get up at five — she’s a baker.”', ['has to', 'must', 'have to', 'musts'],
   ['‘Must’ would be your opinion; this is her job’s requirement.', 'She → ‘has to’.', 'No -s on modals.'],
   'Other people’s job obligations: has to.'),
  ],
 'mc': [
  ('Past', 'Last year Joan ___ repeat the exam.', ['had to', 'must', 'has to', 'musted'],
   ['‘Must’ has no past.', '‘Has to’ is present.', '‘Musted’ doesn’t exist.'],
   'Past: had to.'),
  ('Don’t have to', 'We ___ hurry. The film starts at nine.', ['don’t have to', 'mustn’t', 'must', 'have to'],
   ['‘Mustn’t hurry’ means hurrying is forbidden.', '‘Must’ is the opposite.', '‘Have to’ is the opposite.'],
   'There’s time: don’t have to.'),
  ('Speaker', 'You ___ watch this series — it’s amazing!', ['must', 'have to', 'had to', 'mustn’t'],
   ['‘Have to’ sounds like a rule.', '‘Had to’ is past.', '‘Mustn’t’ means it’s forbidden.'],
   'An enthusiastic recommendation: must.'),
  ('Question', '___ you have to work on Saturdays?', ['Do', 'Must', 'Have', 'Are'],
   ['‘Must you have to’ is wrong.', '‘Have you have to’ is wrong.', '‘Are you have to’ is wrong.'],
   'Questions: Do … have to?'),
  ],
 'error': [
  ('Past', 'Yesterday she *must* stay late.', 'had to', '‘Must’ has no past: ‘had to’.'),
  ('Has to', 'He *have* to study tonight.', 'has', 'He → ‘has to’.'),
  ('Wrong negative', 'It’s optional — you *mustn’t* come.', 'don’t have to', 'Optional → ‘don’t have to’.'),
  ('Future', 'Tomorrow I will *must* get up early.', 'have to', '‘I’ll have to get up early’.'),
  ],
}
