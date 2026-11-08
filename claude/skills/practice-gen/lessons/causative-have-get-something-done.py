TITLE = 'Causative: have/get something done'
AUX = (['have', 'had', 'get', 'got'], None, 'had')
NEXT = ('Passive Reporting Structures', '/grammar/passive-voice/passive-reporting-structures/')
BODY = r'''
## How to form the causative

| Structure | Example |
|---|---|
| have + **object** + past participle | I **had my hair cut**. |
| get + **object** + past participle | I **got my hair cut**. |

The causative means **someone else does it for you** — usually because you pay or ask them. The word order is important: the **object comes before** the participle.

| Sentence | Meaning |
|---|---|
| I **cut my hair**. | I did it myself. |
| I **had my hair cut**. | A hairdresser did it for me. |

## Tenses

Only *have* / *get* changes. The object and the participle stay the same.

| Tense | Example |
|---|---|
| present simple | She **has** her nails **done** every month. |
| present continuous | We**'re having** the kitchen **painted**. |
| past simple | I **had** my car **repaired** yesterday. |
| present perfect | They**'ve had** the house **cleaned**. |
| future | I**'ll get** my eyes **tested** next week. |
| *going to* | He**'s going to have** his teeth **checked**. |
| modal | You **should get** your bike **fixed**. |

## When to use the causative

### 1. Services we pay for

- I **have** my car **serviced** once a year.
- She **got** her photo **taken** for her passport.

> ⚠️ Typical error: ~~I had cut my hair.~~ → That's past perfect (you did it). Causative: *I had my hair cut.*

### 2. *Get* is more informal

- I **got** my phone **fixed**. (informal)
- I **had** my phone **fixed**. (neutral)

### 3. Bad experiences

The causative can also describe something bad that **happened to** you (not a service).

- He **had** his wallet **stolen** on the train.
- We **had** our windows **broken** in the storm.

> ⚠️ Typical error: ~~He stole his wallet on the train.~~ → That means he stole it! *He had his wallet stolen.*

## Questions and negatives

*Have* and *get* are normal verbs here: use **do / does / did**.

| Question | Negative |
|---|---|
| **Did** you **have** your hair **cut**? | I **didn't have** it **cut**. |
| **Do** you **get** your car **washed**? | She **doesn't get** it **washed**. |
| Where **do** you **have** your nails **done**? | They **haven't had** the roof **fixed**. |

> ⚠️ Typical error: ~~Had you your hair cut?~~ → *Did you have your hair cut?*

## Word order

| ✗ | ✓ |
|---|---|
| ~~I had cut my hair.~~ | I had **my hair cut**. |
| ~~She got repaired her car.~~ | She got **her car repaired**. |

## Common mistakes

**1. Wrong word order.** *~~I had repaired my bike~~* (= I repaired it before) → **I had my bike repaired.**

**2. Base verb instead of participle.** *~~I had my hair cutted / cutting~~* → **I had my hair cut.**

**3. Questions without *do/did*.** *~~Had you your eyes tested?~~* → **Did you have your eyes tested?**

**4. Forgetting the causative.** *~~I painted my house last week~~* (when painters did it) → **I had my house painted.**

**Pro tip:** remember the order **have + THING + done** — "have the thing done".
'''

GAP = ('Fill in the gaps',
  'Type the causative: have / get in the right tense + object + past participle, or just the missing part. Twenty original sentences.',
  [
  ('Past', 'I [[had my hair cut]] yesterday. Do you like it?', '(have / my hair / cut)', 'Someone else cut it: had + object + past participle.'),
  ('Past', 'She [[had her car repaired]] last week.', '(have / her car / repair)', 'A mechanic did it: had + her car + repaired.'),
  ('Past', 'We [[got our photo taken]] for our passports.', '(get / our photo / take)', 'Informal causative: got + object + taken.'),
  ('Present', 'My mum [[has her nails done]] every month.', '(have / her nails / do)', 'A regular service, present simple: has + her nails + done.'),
  ('Present', 'How often do you [[get your car washed]]?', '(get / your car / wash)', 'After ‘do you’ use the base form ‘get’ + object + participle.'),
  ('Continuous', 'We’re [[having the kitchen painted]] this week.', '(have / the kitchen / paint)', 'In progress now: are having + object + painted.'),
  ('Perfect', 'They’ve just [[had the roof fixed]].', '(have / the roof / fix)', 'Present perfect causative: have had + object + fixed.'),
  ('Future', 'I’ll [[get my eyes tested]] next week.', '(get / my eyes / test)', 'Future causative: will get + object + tested.'),
  ('Going to', 'He’s going to [[have his teeth checked]].', '(have / his teeth / check)', 'Planned future: going to have + object + checked.'),
  ('Modal', 'You should [[get your bike fixed]] before the trip.', '(get / your bike / fix)', 'Advice: should get + object + fixed.'),
  ('Participle', 'I had my laptop [[repaired]] at the shop.', '(repair)', 'After the object use the past participle: repaired.'),
  ('Participle', 'She got her dress [[made]] by a tailor.', '(make)', 'Irregular participle: make → made.'),
  ('Participle', 'We had a new door [[put]] in.', '(put)', '‘Put’ has the same participle: put.'),
  ('Bad experience', 'He [[had his wallet stolen]] on the metro.', '(have / his wallet / steal)', 'A bad thing that happened to him: had + wallet + stolen.'),
  ('Bad experience', 'We had our windows [[broken]] in the storm.', '(break)', 'Causative for a bad experience: had + windows + broken.'),
  ('Question', '[[Did]] you have your hair cut?', 'did / had', 'Causative questions use ‘did’ + have.'),
  ('Question', 'Where do you [[have]] your nails done?', 'have / had', 'After ‘do you’ use the base form ‘have’.'),
  ('Negative', 'I [[didn’t have]] my car cleaned — I did it myself.', '(not have)', 'Negative past causative: didn’t have + object + participle.'),
  ('Negative', 'She [[doesn’t get]] her hair dyed any more.', '(not get)', 'Negative present: doesn’t get + object + participle.'),
  ('Self or service', 'I [[cut]] my own hair yesterday — what a disaster!', '(cut)', 'You did it yourself, so no causative: just ‘cut’.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 causatives with have and get. Remember: have + thing + done.',
  [
  ('Past', 'I had my hair cut.', []),
  ('Past', 'She had her car repaired.', []),
  ('Past', 'We got our house painted.', []),
  ('Past', 'He had his photo taken.', []),
  ('Present', 'I have my car serviced every year.', []),
  ('Present', 'She gets her nails done.', []),
  ('Continuous', 'We are having the kitchen painted.', []),
  ('Perfect', 'They have had the roof fixed.', []),
  ('Future', 'I will get my eyes tested.', []),
  ('Going to', 'He is going to have his teeth cleaned.', []),
  ('Modal', 'You should get your bike checked.', []),
  ('Modal', 'We must have the heating repaired.', []),
  ('Bad experience', 'He had his phone stolen.', []),
  ('Bad experience', 'We had our car broken into.', []),
  ('Question', 'Did you have your hair cut?', []),
  ('Question', 'Where do you get your car washed?', []),
  ('Negative', 'I didn’t have it repaired.', []),
  ('Negative', 'She doesn’t get her hair dyed.', []),
  ('Past', 'I got my dress made.', []),
  ('Past', 'They had a new fence built.', []),
  ])

MATCH = {'title': 'Match the problem and the service', 'subtitle': 'Tap a problem, then tap the causative that solves it.',
  'leftLabel': 'Problem', 'rightLabel': 'Solution', 'rightLabelSub': '(have / get + thing + done)', 'reviewArrowPrefix': '',
  'pairs': [
  ('My hair is too long.', 'I’ll have it cut.'), ('My car is making a strange noise.', 'I’ll get it checked.'), ('My eyes hurt when I read.', 'I’ll have them tested.'),
  ('The walls are dirty.', 'We’ll have them painted.'), ('My phone screen is broken.', 'I’ll get it replaced.'), ('The heating doesn’t work.', 'We’ll have it repaired.'),
  ('My trousers are too long.', 'I’ll get them shortened.'), ('I need a passport photo.', 'I’ll have it taken.'), ('My tooth hurts.', 'I’ll have it looked at.'),
  ('The windows are filthy.', 'We’ll get them cleaned.'), ('My watch has stopped.', 'I’ll have it fixed.'), ('The grass is very long.', 'We’ll get it cut.'),
  ('My bike has a flat tyre.', 'I’ll have it repaired.'), ('The roof is leaking.', 'We’ll have it fixed.'), ('My jacket is stained.', 'I’ll get it dry-cleaned.'),
  ('This document is in German.', 'I’ll have it translated.'), ('My computer has a virus.', 'I’ll get it cleaned.'), ('The lock is broken.', 'We’ll have it changed.'),
  ('My shoes are falling apart.', 'I’ll have them mended.'), ('The piano sounds terrible.', 'We’ll get it tuned.'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Have / get + object + past participle — and check who did the action.',
  [
  ('Word order', 'Which sentence means a hairdresser cut it?', ['I had my hair cut.', 'I had cut my hair.', 'I cut my hair.', 'I have cut my hair.'],
   ['‘I had cut my hair’ is past perfect: you did it yourself, earlier.', '‘I cut my hair’ means you did it yourself.', '‘I have cut my hair’ is present perfect: you did it.'],
   'Causative order is have + object + participle: someone else did it.'),
  ('Past', 'She ___ her car ___ last week.', ['had / repaired', 'had / repair', 'repaired / had', 'has / repairing'],
   ['After the object we need the past participle, not the base verb.', 'The order is have + object + participle.', '‘Has’ is present and ‘repairing’ is the -ing form.'],
   'Past causative: had + her car + repaired.'),
  ('Participle', 'I’m going to have my teeth ___.', ['cleaned', 'clean', 'cleaning', 'to clean'],
   ['After the object use the past participle.', 'The -ing form doesn’t fit the causative.', '‘To clean’ is wrong after the object here.'],
   'Have + object + past participle: cleaned.'),
  ('Participle', 'We had a new kitchen ___ last year.', ['fitted', 'fit', 'fitting', 'to fit'],
   ['After the object use the participle.', '‘Fitting’ is the -ing form.', '‘To fit’ is wrong here.'],
   'Causative: had + a new kitchen + fitted.'),
  ('Question', '___ you have your eyes tested last month?', ['Did', 'Had', 'Were', 'Have'],
   ['‘Had you your eyes tested’ is old-fashioned and not used now.', '‘Were you have’ is wrong.', '‘Have you have’ is wrong.'],
   'Causative questions in the past use ‘did’ + have.'),
  ('Question', 'How often ___ you get your hair cut?', ['do', 'are', 'have', 'did'],
   ['‘Are you get’ is wrong.', '‘Have you get’ is wrong.', '‘Did’ is past, but ‘how often’ asks about habits now.'],
   'Present habit question: do + subject + get…?'),
  ('Continuous', 'We can’t use the bathroom. We’re ___ it redecorated.', ['having', 'have', 'had', 'got'],
   ['After ‘we’re’ use the -ing form: ‘having’.', '‘We’re had’ is wrong.', '‘We’re got’ is wrong.'],
   'Present continuous causative: are having + object + participle.'),
  ('Perfect', 'They’ve just ___ the windows replaced.', ['had', 'have', 'having', 'has'],
   ['‘They’ve have’ is wrong: after ‘have’ use the participle ‘had’.', '‘They’ve having’ is wrong.', '‘They’ve has’ is wrong.'],
   'Present perfect causative: have had + object + participle.'),
  ('Future', 'I’ll ___ my phone fixed tomorrow.', ['get', 'got', 'getting', 'gets'],
   ['After ‘will’ use the base form.', 'After ‘will’ use the base form.', 'After ‘will’ use the base form.'],
   'Future causative: will get + object + participle.'),
  ('Modal', 'You should ___ that cough looked at by a doctor.', ['have', 'had', 'having', 'to have'],
   ['After ‘should’ use the base form.', 'After ‘should’ use the base form.', 'No ‘to’ after ‘should’.'],
   'Advice with a causative: should have + object + participle.'),
  ('Bad experience', 'Poor Joan! She ___ on the bus.', ['had her bag stolen', 'stole her bag', 'had stolen her bag', 'has her bag steal'],
   ['That means Joan stole it!', 'That means Joan stole it earlier.', 'After the object use the participle ‘stolen’.'],
   'A bad experience: had + object + participle.'),
  ('Self or service', 'I ___ the walls myself. It took all weekend!', ['painted', 'had the walls painted', 'got painted the walls', 'had painted the walls by someone'],
   ['‘Had the walls painted’ means someone else did it.', 'Wrong word order.', 'Wrong structure.'],
   '‘Myself’ means you did it: no causative.'),
  ('Get or have', 'Which sentence is more informal?', ['I got my bike fixed.', 'I had my bike fixed.', 'My bike was fixed by a mechanic.', 'A mechanic fixed my bike.'],
   ['‘Had’ is neutral, not especially informal.', 'This passive is neutral or formal.', 'This active sentence is neutral.'],
   '‘Get’ makes the causative more informal.'),
  ('Negative', 'I ___ my car washed — I did it myself.', ['didn’t have', 'hadn’t', 'didn’t had', 'wasn’t'],
   ['‘Hadn’t my car washed’ is old-fashioned.', 'After ‘didn’t’ use the base form ‘have’.', '‘Wasn’t my car washed’ is wrong.'],
   'Negative past causative: didn’t have + object + participle.'),
  ('Participle', 'She had her dress ___ by a famous designer.', ['made', 'make', 'making', 'maked'],
   ['After the object use the participle.', '‘Making’ is the -ing form.', '‘Make’ is irregular: made.'],
   'Irregular participle: make → made.'),
  ('Word order', 'Which sentence is correct?', ['We got our garden designed.', 'We got designed our garden.', 'We got our garden design.', 'We got our designed garden.'],
   ['The object comes before the participle.', 'After the object use the participle ‘designed’.', 'That makes ‘designed’ an adjective — different meaning.'],
   'Order: get + object + past participle.'),
  ('Present', 'My dad ___ his suits dry-cleaned.', ['has', 'have', 'having', 'is have'],
   ['‘My dad’ is he: has.', '‘Having’ needs ‘is’.', '‘Is have’ is wrong.'],
   'Present simple causative: has + object + participle.'),
  ('Bad experience', 'We ___ our car broken into last night.', ['had', 'have', 'got to', 'were'],
   ['‘Have’ is present, but this was last night.', '‘Got to’ means something different.', '‘Were our car’ is wrong.'],
   'A bad past experience: had + object + participle.'),
  ('Going to', 'She’s going to ___ her photo taken for her new ID.', ['have', 'had', 'having', 'has'],
   ['After ‘going to’ use the base form.', 'After ‘going to’ use the base form.', 'After ‘going to’ use the base form.'],
   'Going to + have + object + participle.'),
  ('Participle', 'Have you had your hair ___? It looks great!', ['cut', 'cutted', 'cutting', 'to cut'],
   ['‘Cutted’ doesn’t exist: the participle is ‘cut’.', 'The -ing form doesn’t fit.', '‘To cut’ is wrong here.'],
   'Irregular participle: cut → cut.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('Base verb', 'I had my car *repair* yesterday.', 'repaired', 'After the object use the participle: ‘repaired’.'),
  ('Base verb', 'She got her nails *paint*.', 'painted', 'Participle: ‘painted’.'),
  ('-ing form', 'We had the house *cleaning*.', 'cleaned', 'Participle: ‘cleaned’.'),
  ('Wrong participle', 'I had my hair *cutted*.', 'cut', 'Participle of ‘cut’: ‘cut’.'),
  ('Wrong participle', 'He had his photo *took*.', 'taken', 'Participle of ‘take’: ‘taken’.'),
  ('Wrong participle', 'They had a wall *builded* in the garden.', 'built', 'Participle of ‘build’: ‘built’.'),
  ('Question', 'Where *you* have your nails done?', 'do you', 'Question: ‘Where do you have your nails done?’.'),
  ('Question', 'Did you *had* your bike fixed?', 'have', 'After ‘did’ use ‘have’.'),
  ('Question', '*Are* you get your car washed every week?', 'Do', 'Present question: ‘Do you get your car washed?’.'),
  ('Negative', 'I *hadn’t* my hair cut — I did it myself.', 'didn’t have', 'Negative: ‘I didn’t have my hair cut’.'),
  ('Negative', 'She didn’t *got* her car fixed.', 'get', 'After ‘didn’t’ use ‘get’.'),
  ('Missing -s', 'My mum *have* her hair dyed every month.', 'has', '‘My mum’ is she: ‘has’.'),
  ('Will', 'I will *got* my phone repaired.', 'get', 'After ‘will’ use ‘get’.'),
  ('Continuous', 'We’re *have* the kitchen painted.', 'having', 'Continuous: ‘We’re having…’.'),
  ('Perfect', 'They’ve *have* the roof fixed.', 'had', 'Present perfect: ‘They’ve had…’.'),
  ('Bad experience', 'He had his wallet *stole* on the train.', 'stolen', 'Participle: ‘He had his wallet stolen’.'),
  ('Self or service', 'The painters were great. We had the house *paint* in two days.', 'painted', 'Participle: ‘We had the house painted’.'),
  ('Wrong verb', 'I *made* my hair cut yesterday.', 'had', 'Causative uses ‘have’ or ‘get’: ‘I had my hair cut’.'),
  ('Modal', 'You should *got* your eyes tested.', 'get', 'After ‘should’ use the base form: ‘You should get…’.'),
  ('Spelling', 'I had my jacket *dryclened*.', 'dry-cleaned', 'Spelling: ‘dry-cleaned’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, self or service, multiple choice and spot-the-mistake. In the typing questions write have / get + object + past participle. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('service', 'Self or service'),
 'fill': [
  ('Past', 'I [[had my bike fixed]] at the shop.', 'have / my bike / fix', 'A mechanic did it: had + my bike + fixed.', 'Order: had + thing + participle.'),
  ('Future', 'We’ll [[get the carpet cleaned]] next week.', 'get / the carpet / clean', 'Future causative: will get + object + cleaned.', 'After ‘will’: get + thing + participle.'),
  ('Question', '[[Did]] you have your phone screen replaced?', 'did / had', 'Causative questions in the past use ‘did’ + have.', 'Use ‘did’, not ‘had’.'),
  ('Participle', 'She had her portrait [[painted]] by an artist.', 'paint', 'After the object use the past participle: painted.', 'Use the participle.'),
  ],
 'order': [
  ('Past', 'I had my car washed.', []),
  ('Present', 'She gets her hair cut.', []),
  ('Question', 'Did you have it fixed?', []),
  ('Bad experience', 'He had his bike stolen.', []),
  ],
 'customItems': [
  ('Service', 'A plumber came. We ___ the sink unblocked.', ['had', 'unblocked', 'have unblocked', 'were'],
   ['‘We unblocked the sink’ means we did it ourselves.', '‘Have unblocked’ means we did it.', '‘We were the sink’ makes no sense.'],
   'Someone else did it → causative: had + object + participle.'),
  ('Service', 'I ___ my room myself on Saturday.', ['tidied', 'had my room tidied', 'got tidied my room', 'had tidy my room'],
   ['‘Had my room tidied’ means someone else did it.', 'Wrong word order.', 'Wrong participle and meaning.'],
   '‘Myself’ → you did it: no causative.'),
  ('Service', 'Which sentence means someone else did the work?', ['They had the house painted.', 'They painted the house.', 'They had painted the house.', 'They have painted the house.'],
   ['That means they did it.', 'Past perfect: they did it.', 'Present perfect: they did it.'],
   'have + object + participle = a service.'),
  ('Service', 'Which sentence describes something bad that happened to you?', ['I had my phone stolen.', 'I stole my phone.', 'I had stolen my phone.', 'I have my phone.'],
   ['That means you stole it.', 'That means you stole it earlier.', 'That just means you own it.'],
   'The causative can describe a bad experience.'),
  ],
 'mc': [
  ('Participle', 'He had his car ___ yesterday.', ['serviced', 'service', 'servicing', 'to service'],
   ['After the object use the participle.', 'The -ing form doesn’t fit.', '‘To service’ is wrong here.'],
   'Have + object + participle.'),
  ('Word order', 'Which is correct?', ['I got my watch repaired.', 'I got repaired my watch.', 'I repaired got my watch.', 'I got my watch repair.'],
   ['The object comes before the participle.', 'Wrong order.', 'Use the participle ‘repaired’.'],
   'get + object + participle.'),
  ('Present', 'How often do you ___ your hair cut?', ['have', 'had', 'having', 'has'],
   ['After ‘do you’ use the base form.', 'After ‘do you’ use the base form.', '‘You’ takes ‘have’.'],
   'Do you have + object + participle?'),
  ('Continuous', 'They’re ___ a swimming pool built.', ['having', 'have', 'had', 'got'],
   ['After ‘they’re’ use -ing.', '‘They’re had’ is wrong.', '‘They’re got’ is wrong.'],
   'Continuous causative: are having + object + participle.'),
  ],
 'error': [
  ('Base verb', 'I had my glasses *fix*.', 'fixed', 'Participle: ‘fixed’.'),
  ('Question', 'Where *you* get your car repaired?', 'do you', 'Question: ‘Where do you get your car repaired?’.'),
  ('Wrong participle', 'She had her hair *cutted*.', 'cut', 'Participle: ‘cut’.'),
  ('Self or service', 'The mechanic was quick. I had my car *repair* in an hour.', 'repaired', 'Participle: ‘I had my car repaired’.'),
  ],
}
