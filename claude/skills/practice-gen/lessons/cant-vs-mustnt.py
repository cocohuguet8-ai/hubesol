TITLE = 'Can’t vs Mustn’t'
AUX = (['can’t', 'mustn’t', 'don’t'], None, 'mustn’t')
NEXT = ('Need & Needn’t', '/grammar/modal-verbs/need-neednt/')
BODY = r'''
## How the forms compare

| Form | Main meaning | Example |
|---|---|---|
| **can't** + base verb | it isn't allowed (a rule) · it isn't possible · I'm sure it isn't true | You **can't** park here. |
| **mustn't** + base verb | it's forbidden — strong prohibition, often from the speaker | You **mustn't** touch that! |
| **don't have to** + base verb | it isn't necessary | You **don't have to** come. |

*Can't* and *mustn't* are both modals: base verb after them, no *-s*, no *to*.

## When *can't* and *mustn't* are similar

For **rules and prohibitions**, both are possible and the meaning is very close.

- You **can't** / **mustn't** smoke in the hospital.
- Students **can't** / **mustn't** use phones in the exam.

The difference is in **tone**:

| | Sounds like… |
|---|---|
| **can't** | a fact about the rules: it's not permitted |
| **mustn't** | a strong order or warning from the speaker |

## When to use *can't*

### 1. Reporting a rule

- In Spain you **can't** vote until you're 18.
- We **can't** wear trainers at school.

> ⚠️ Typical error: ~~We don't can wear trainers.~~ → The negative of *can* is *can't*.

### 2. Impossibility (no ability)

*Mustn't* is never used for ability.

- I **can't** swim. (✓) — not ~~I mustn't swim~~ (= swimming is forbidden for me)
- She **can't** come — she's ill.

> ⚠️ Typical error: ~~I mustn't open this jar — it's too tight.~~ → It's impossible, not forbidden: *I can't open this jar.*

### 3. Logical deduction

*Can't* = I'm sure it isn't true.

- That **can't** be Laia — she's in London.

See [Deduction: must, might & can't](/grammar/modal-verbs/deduction-must-might-cant/).

## When to use *mustn't*

### 1. Strong warnings

- You **mustn't** play with matches!
- You **mustn't** cross the road here — it's dangerous.

### 2. The speaker's own rules and promises

- I **mustn't** forget Mum's birthday again.
- We **mustn't** tell anyone the secret.

> ⚠️ Typical error: ~~I mustn't to forget.~~ → No *to*: *I mustn't forget.*

## *Mustn't* ≠ *don't have to*

The biggest trap: these negatives mean different things.

| Sentence | Meaning |
|---|---|
| You **mustn't** wear jeans. | Jeans are forbidden. |
| You **don't have to** wear jeans. | Jeans are optional — wear what you like. |

## Past forms

*Mustn't* has no past. Use **couldn't** or **wasn't/weren't allowed to**.

- When I was ten, I **couldn't** stay up late.
- We **weren't allowed to** use calculators.

## Common mistakes

**1. *Mustn't* for ability.** *~~I mustn't ride a bike~~* (you never learnt) → **I can't ride a bike.**

**2. *Mustn't* for "not necessary".** *~~You mustn't pay — it's free~~* → **You don't have to pay.**

**3. *Mustn't* in the past.** *~~Yesterday we mustn't go out~~* → **Yesterday we couldn't / weren't allowed to go out.**

**4. *To* after the modal.** *~~You can't to enter~~* → **You can't enter.**

**Pro tip:** ask "Is it forbidden, impossible or unnecessary?" Forbidden → *can't/mustn't*; impossible → *can't*; unnecessary → *don't have to*.
'''

GAP = ('Fill in the gaps',
  'Type can’t, mustn’t or don’t have to. Ask: is it forbidden, impossible or just not necessary? Twenty original sentences.',
  [
  ('Rule', 'You [[can’t|mustn’t]] park in front of the fire station.', 'can’t / mustn’t', 'A rule that forbids something: can’t or mustn’t, both are correct.'),
  ('Warning', 'You [[mustn’t]] touch the iron — it’s really hot!', 'mustn’t / don’t have to', 'A strong warning from the speaker: mustn’t + base verb.'),
  ('Warning', 'Children [[mustn’t]] play with matches.', 'mustn’t / don’t have to', 'A strong prohibition because it’s dangerous: mustn’t.'),
  ('Ability', 'I [[can’t]] swim, so I always stay in the shallow end.', 'can’t / mustn’t', 'No ability is ‘can’t’. ‘Mustn’t’ would mean swimming is forbidden.'),
  ('Ability', 'My grandpa [[can’t]] hear very well any more.', 'can’t / mustn’t', 'A physical impossibility: can’t, never mustn’t.'),
  ('Ability', 'I [[can’t]] open this jar. Can you help me?', 'can’t / mustn’t', 'It’s impossible (too tight), not forbidden: can’t.'),
  ('Rule', 'In Spain you [[can’t]] drive until you’re eighteen.', 'can’t / don’t have to', 'Reporting a law: can’t = it isn’t permitted.'),
  ('Rule', 'We [[can’t]] use our phones in class.', 'can’t / don’t have to', 'Reporting a school rule: can’t.'),
  ('Speaker', 'I [[mustn’t]] forget my keys again!', 'mustn’t / can’t', 'A rule you make for yourself: mustn’t.'),
  ('Speaker', 'We [[mustn’t]] tell anyone about the surprise.', 'mustn’t / don’t have to', 'A strong agreement between speakers: mustn’t.'),
  ('Not necessary', 'You [[don’t have to]] pay — the museum is free on Sundays.', 'mustn’t / don’t have to', 'Not necessary: don’t have to. ‘Mustn’t’ would forbid paying.'),
  ('Not necessary', 'It’s Saturday, so I [[don’t have to]] wear my uniform.', 'mustn’t / don’t have to', 'No obligation: don’t have to.'),
  ('Not necessary', 'You [[don’t have to]] bring anything to the party.', 'mustn’t / don’t have to', 'Optional: don’t have to.'),
  ('Not necessary', 'She [[doesn’t have to]] work tomorrow — it’s a holiday.', 'don’t / doesn’t have to', 'Third person: doesn’t have to.'),
  ('Deduction', 'That [[can’t]] be Marc — he’s on holiday in Italy.', 'can’t / mustn’t', 'I’m sure it isn’t true: can’t (logical deduction).'),
  ('Past', 'When I was little, I [[couldn’t]] watch TV after nine.', 'couldn’t / mustn’t', '‘Mustn’t’ has no past: couldn’t.'),
  ('Past', 'We [[weren’t]] allowed to use calculators in the test.', 'weren’t / mustn’t', 'Past prohibition: weren’t allowed to.'),
  ('Base verb', 'You mustn’t [[run]] near the swimming pool.', '(run)', 'After ‘mustn’t’ use the base verb: run.'),
  ('Base verb', 'Visitors can’t [[take]] photos inside the church.', '(take)', 'After ‘can’t’ use the base verb, no ‘to’: take.'),
  ('Warning', 'You [[mustn’t]] lean out of the train window.', 'mustn’t / don’t have to', 'A safety warning: mustn’t.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with can’t, mustn’t and don’t have to.',
  [
  ('Rule', 'You can’t smoke in here.', []),
  ('Rule', 'We can’t wear jeans at school.', []),
  ('Rule', 'You can’t vote until eighteen.', []),
  ('Warning', 'You mustn’t touch the cooker.', []),
  ('Warning', 'You mustn’t swim after eating.', []),
  ('Warning', 'Children mustn’t play near the road.', []),
  ('Speaker', 'I mustn’t be late again.', []),
  ('Speaker', 'We mustn’t forget the tickets.', []),
  ('Ability', 'I can’t speak Russian.', []),
  ('Ability', 'She can’t come to the party.', []),
  ('Ability', 'My dog can’t climb stairs.', []),
  ('Not necessary', 'You don’t have to wait.', []),
  ('Not necessary', 'We don’t have to get up early.', []),
  ('Not necessary', 'He doesn’t have to pay.', []),
  ('Deduction', 'That can’t be true.', []),
  ('Deduction', 'She can’t be at home now.', []),
  ('Past', 'We couldn’t go out last night.', []),
  ('Past', 'I wasn’t allowed to stay up.', []),
  ('Past', 'They didn’t have to wait long.', []),
  ('Rule', 'Dogs can’t enter the shop.', []),
  ])

MATCH = {'title': 'Forbidden, impossible or not necessary?', 'subtitle': 'Tap a sentence, then tap what it means.',
  'leftLabel': 'Sentence', 'rightLabel': 'Meaning', 'rightLabelSub': '(forbidden / impossible / not necessary)', 'reviewArrowPrefix': '',
  'pairs': [
  ('You mustn’t smoke here.', 'forbidden'), ('I can’t swim.', 'impossible'), ('You don’t have to come.', 'not necessary'),
  ('You can’t park here.', 'forbidden'), ('She can’t hear you.', 'impossible'), ('We don’t have to pay.', 'not necessary'),
  ('You mustn’t tell anyone.', 'forbidden'), ('I can’t lift this box.', 'impossible'), ('He doesn’t have to wear a tie.', 'not necessary'),
  ('Students can’t use phones in exams.', 'forbidden'), ('My baby sister can’t walk yet.', 'impossible'), ('You don’t have to book.', 'not necessary'),
  ('You mustn’t feed the animals.', 'forbidden'), ('I can’t find my keys.', 'impossible'), ('You don’t have to bring food.', 'not necessary'),
  ('You mustn’t run by the pool.', 'forbidden'), ('We can’t see the stage from here.', 'impossible'), ('I don’t have to work tomorrow.', 'not necessary'),
  ('Visitors can’t take photos.', 'forbidden'), ('Penguins can’t fly.', 'impossible'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Forbidden → can’t / mustn’t; impossible → can’t; not necessary → don’t have to.',
  [
  ('Warning', 'You ___ touch that wire — it’s dangerous!', ['mustn’t', 'don’t have to', 'can', 'needn’t'],
   ['‘Don’t have to’ means it’s optional, but touching the wire is dangerous.', '‘Can’ means it’s allowed — the opposite of a warning.', '‘Needn’t’ means it isn’t necessary.'],
   'A strong warning about danger: mustn’t + base verb.'),
  ('Ability', 'I ___ ride a bike. I never learnt.', ['can’t', 'mustn’t', 'don’t have to', 'shouldn’t'],
   ['‘Mustn’t’ would mean riding is forbidden — but this is about ability.', '‘Don’t have to’ means it isn’t necessary.', '‘Shouldn’t’ is advice.'],
   'No ability: can’t. ‘Mustn’t’ is never used for ability.'),
  ('Not necessary', 'You ___ wear a costume — but you can if you want.', ['don’t have to', 'mustn’t', 'can’t', 'couldn’t'],
   ['‘Mustn’t’ means costumes are forbidden.', '‘Can’t’ means it isn’t allowed.', '‘Couldn’t’ is past.'],
   '‘But you can if you want’ shows it’s optional: don’t have to.'),
  ('Rule', 'In this library you ___ eat or drink.', ['can’t', 'don’t have to', 'needn’t', 'couldn’t'],
   ['‘Don’t have to’ makes eating optional.', '‘Needn’t’ means it isn’t necessary.', '‘Couldn’t’ is past.'],
   'Reporting a rule: can’t = it isn’t permitted.'),
  ('Speaker', 'I ___ forget to send that email. It’s really important.', ['mustn’t', 'can’t', 'don’t have to', 'couldn’t'],
   ['‘Can’t forget’ means it’s impossible to forget.', '‘Don’t have to forget’ makes no sense.', '‘Couldn’t’ is past.'],
   'A strong rule you make for yourself: mustn’t.'),
  ('Deduction', 'That ___ be Anna’s car — she sold it last year.', ['can’t', 'mustn’t', 'doesn’t have to', 'needn’t'],
   ['‘Mustn’t’ isn’t used for logical deduction in this way.', '‘Doesn’t have to’ is about necessity.', '‘Needn’t’ is about necessity.'],
   'I’m sure it isn’t true: can’t (deduction).'),
  ('Past', 'When I was young, I ___ go to the park alone.', ['couldn’t', 'mustn’t', 'can’t', 'don’t have to'],
   ['‘Mustn’t’ has no past form.', '‘Can’t’ is present.', '‘Don’t have to’ is present and means optional.'],
   'Past prohibition: couldn’t (or wasn’t allowed to).'),
  ('Past', 'We ___ allowed to talk during the test.', ['weren’t', 'mustn’t', 'can’t', 'didn’t'],
   ['‘Mustn’t allowed’ is wrong.', '‘Can’t allowed’ is wrong.', '‘Didn’t allowed’ is wrong.'],
   'Past prohibition: weren’t allowed to + base verb.'),
  ('Not necessary', 'It’s free! You ___ pay.', ['don’t have to', 'mustn’t', 'can’t', 'couldn’t'],
   ['‘Mustn’t pay’ means paying is forbidden.', '‘Can’t pay’ means it’s impossible or not allowed.', '‘Couldn’t’ is past.'],
   'Free means it isn’t necessary to pay: don’t have to.'),
  ('Ability', 'Sorry, I ___ come tonight. I’ve got a cold.', ['can’t', 'mustn’t', 'don’t have to', 'needn’t'],
   ['‘Mustn’t come’ means coming is forbidden.', '‘Don’t have to’ means it’s optional.', '‘Needn’t’ means it isn’t necessary.'],
   'It isn’t possible because you’re ill: can’t.'),
  ('Rule', 'Which sentence describes a rule correctly?', ['You can’t use calculators in this exam.', 'You don’t have to use calculators in this exam — it’s forbidden.', 'You mustn’t to use calculators.', 'You don’t can use calculators.'],
   ['‘Don’t have to’ means optional, not forbidden.', 'No ‘to’ after ‘mustn’t’.', 'The negative of ‘can’ is ‘can’t’.'],
   'A prohibition: can’t (or mustn’t) + base verb.'),
  ('Mustn’t or don’t have to', 'Which sentence means ‘it’s optional’?', ['You don’t have to stay.', 'You mustn’t stay.', 'You can’t stay.', 'You couldn’t stay.'],
   ['‘Mustn’t’ = forbidden.', '‘Can’t’ = not allowed or not possible.', '‘Couldn’t’ is past.'],
   '‘Don’t have to’ = not necessary; you choose.'),
  ('Mustn’t or don’t have to', 'Which sentence means ‘it’s forbidden’?', ['You mustn’t stay.', 'You don’t have to stay.', 'You needn’t stay.', 'You didn’t have to stay.'],
   ['That means it’s optional.', 'That means it isn’t necessary.', 'That’s past and optional.'],
   '‘Mustn’t’ = it’s not allowed.'),
  ('Base verb', 'You mustn’t ___ in the corridor.', ['run', 'to run', 'running', 'runs'],
   ['No ‘to’ after ‘mustn’t’.', 'After a modal use the base verb, not -ing.', 'No -s after a modal.'],
   'After mustn’t: the base verb.'),
  ('Warning', 'You ___ eat those berries — they’re poisonous!', ['mustn’t', 'don’t have to', 'needn’t', 'won’t'],
   ['‘Don’t have to’ makes it sound optional.', '‘Needn’t’ means it isn’t necessary.', '‘Won’t’ is a prediction.'],
   'Danger → strong prohibition: mustn’t.'),
  ('Ability', 'Penguins ___ fly.', ['can’t', 'mustn’t', 'don’t have to', 'shouldn’t'],
   ['‘Mustn’t’ means flying is forbidden — it’s impossible.', '‘Don’t have to’ is about necessity.', '‘Shouldn’t’ is advice.'],
   'Physical impossibility: can’t.'),
  ('Not necessary', 'Tomorrow is a holiday, so my dad ___ go to work.', ['doesn’t have to', 'mustn’t', 'can’t', 'don’t have to'],
   ['‘Mustn’t’ means work is forbidden.', '‘Can’t’ means it’s impossible.', '‘My dad’ is he: ‘doesn’t’.'],
   'No obligation, third person: doesn’t have to.'),
  ('Rule', 'Passengers ___ smoke on the plane.', ['mustn’t', 'don’t have to', 'needn’t', 'didn’t have to'],
   ['‘Don’t have to’ makes smoking optional.', '‘Needn’t’ means it isn’t necessary.', '‘Didn’t have to’ is past and optional.'],
   'A strict rule: mustn’t (or can’t).'),
  ('Speaker', 'We ___ make a noise — the baby’s asleep.', ['mustn’t', 'don’t have to', 'can’t to', 'needn’t'],
   ['‘Don’t have to’ makes noise optional.', 'No ‘to’ after ‘can’t’.', '‘Needn’t’ means it isn’t necessary.'],
   'An important rule right now: mustn’t.'),
  ('Deduction', 'He ___ be hungry — he’s just eaten a huge pizza!', ['can’t', 'mustn’t', 'doesn’t have to', 'couldn’t to'],
   ['‘Mustn’t’ isn’t used for deduction.', '‘Doesn’t have to’ is about necessity.', 'No ‘to’ after a modal.'],
   'I’m sure it isn’t true: can’t be.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('Mustn’t for ability', 'I *mustn’t* swim — I never learnt.', 'can’t', 'No ability = ‘can’t’: ‘I can’t swim’.'),
  ('Mustn’t for ability', 'My grandma *mustn’t* walk without a stick.', 'can’t', 'It’s about ability: ‘she can’t walk’.'),
  ('Mustn’t for ability', 'I *mustn’t* open this bottle — the lid is stuck.', 'can’t', 'Impossible, not forbidden: ‘I can’t open it’.'),
  ('Mustn’t for not necessary', 'It’s free — you *mustn’t* pay.', 'needn’t', 'Not necessary: ‘you needn’t / don’t have to pay’.'),
  ('Mustn’t for not necessary', 'You *mustn’t* bring a towel — they give you one.', 'needn’t', 'Not necessary: ‘you needn’t bring a towel’.'),
  ('Needn’t for forbidden', 'You *needn’t* touch the fire — it’s dangerous!', 'mustn’t', 'Dangerous = forbidden: ‘you mustn’t touch it’.'),
  ('Needn’t for forbidden', 'Students *needn’t* cheat in exams.', 'mustn’t', 'Cheating is forbidden: ‘students mustn’t cheat’.'),
  ('Past', 'Yesterday we *mustn’t* go out because of the storm.', 'couldn’t', '‘Mustn’t’ has no past: ‘we couldn’t go out’.'),
  ('Past', 'At my old school we *can’t* wear jeans.', 'couldn’t', 'A past rule: ‘we couldn’t wear jeans’.'),
  ('Base verb', 'You mustn’t *running* in the corridors.', 'run', 'After ‘mustn’t’ use the base verb: ‘run’.'),
  ('Base verb', 'You can’t *parks* here.', 'park', 'After ‘can’t’ use the base verb: ‘park’.'),
  ('Base verb', 'We mustn’t *forgot* the tickets.', 'forget', 'After ‘mustn’t’ use the base verb: ‘forget’.'),
  ('Wrong negative', 'You *don’t can* smoke here.', 'can’t', 'The negative is ‘can’t’: ‘You can’t smoke here’.'),
  ('Wrong negative', 'He *don’t* have to wear a uniform.', 'doesn’t', 'He → ‘doesn’t have to’.'),
  ('Mustn’t for deduction', 'That *mustn’t* be Pau — he’s in Paris.', 'can’t', 'Deduction (sure it isn’t true): ‘That can’t be Pau’.'),
  ('Allowed', 'We weren’t *allow* to use our phones.', 'allowed', 'The form is ‘be allowed to’.'),
  ('Allowed', 'They *wasn’t* allowed to leave.', 'weren’t', '‘They’ takes ‘weren’t’.'),
  ('-s on a modal', 'She *mustn’ts* tell anyone.', 'mustn’t', 'Modals never take -s.'),
  ('Wrong modal', 'You *don’t* swim here — sharks!', 'mustn’t', 'A strong warning needs ‘mustn’t’.'),
  ('Spelling', 'You *musn’t* lie to me.', 'mustn’t', 'Spelling: ‘mustn’t’ (with t).'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, which meaning, multiple choice and spot-the-mistake. In the typing questions write can’t, mustn’t or don’t have to. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('meaning', 'Which meaning?'),
 'fill': [
  ('Warning', 'You [[mustn’t]] play with the scissors!', 'mustn’t / don’t have to', 'A strong warning about danger: mustn’t.', 'Danger → ‘mustn’t’.'),
  ('Ability', 'I [[can’t]] whistle. I’ve tried for years!', 'can’t / mustn’t', 'No ability: can’t, never mustn’t.', 'Ability → ‘can’t’.'),
  ('Not necessary', 'You [[don’t have to]] wait for me. Go ahead.', 'mustn’t / don’t have to', 'Not necessary: don’t have to.', 'Optional → ‘don’t have to’.'),
  ('Past', 'We [[couldn’t]] leave until the bell rang.', 'couldn’t / mustn’t', 'Past prohibition: couldn’t.', 'Past → ‘couldn’t’.'),
  ],
 'order': [
  ('Warning', 'You mustn’t touch it.', []),
  ('Ability', 'I can’t drive yet.', []),
  ('Not necessary', 'You don’t have to help.', []),
  ('Rule', 'You can’t eat here.', []),
  ],
 'customItems': [
  ('Meaning', '‘I can’t dance’ means…', ['I’m not able to dance', 'dancing is forbidden', 'dancing isn’t necessary', 'I didn’t dance'],
   ['That’s ‘I mustn’t dance’.', 'That’s ‘I don’t have to dance’.', 'That’s the past simple.'],
   '‘Can’t’ here = no ability.'),
  ('Meaning', '‘You don’t have to dance’ means…', ['dancing is optional', 'dancing is forbidden', 'you aren’t able to dance', 'you danced'],
   ['That’s ‘mustn’t’.', 'That’s ‘can’t’.', 'That’s the past.'],
   '‘Don’t have to’ = not necessary.'),
  ('Meaning', '‘You mustn’t dance’ means…', ['dancing is forbidden', 'dancing is optional', 'you aren’t able to dance', 'you might dance'],
   ['That’s ‘don’t have to’.', 'That’s ‘can’t’ for ability.', 'That’s ‘might’.'],
   '‘Mustn’t’ = it’s not allowed.'),
  ('Meaning', '‘That can’t be true’ means…', ['I’m sure it isn’t true', 'it’s forbidden to be true', 'it isn’t necessary', 'maybe it’s true'],
   ['‘Mustn’t’ is about prohibition, not here.', 'That’s ‘doesn’t have to’.', 'That’s ‘might be’.'],
   '‘Can’t be’ = logical deduction.'),
  ],
 'mc': [
  ('Rule', 'You ___ use the lift during a fire.', ['mustn’t', 'don’t have to', 'needn’t', 'couldn’t'],
   ['Optional — wrong for a safety rule.', 'Not necessary — wrong for a safety rule.', '‘Couldn’t’ is past.'],
   'A safety prohibition: mustn’t.'),
  ('Not necessary', 'I ___ cook tonight — we’re eating out.', ['don’t have to', 'mustn’t', 'can’t', 'couldn’t'],
   ['Cooking isn’t forbidden.', 'It isn’t impossible.', '‘Couldn’t’ is past.'],
   'Not necessary: don’t have to.'),
  ('Ability', 'Babies ___ talk.', ['can’t', 'mustn’t', 'don’t have to', 'needn’t'],
   ['Talking isn’t forbidden for babies.', 'It isn’t about necessity.', 'It isn’t about necessity.'],
   'No ability: can’t.'),
  ('Past', 'Last year we ___ use dictionaries in the exam.', ['weren’t allowed to', 'mustn’t', 'can’t', 'don’t have to'],
   ['‘Mustn’t’ has no past.', '‘Can’t’ is present.', '‘Don’t have to’ is present.'],
   'Past prohibition: weren’t allowed to.'),
  ],
 'error': [
  ('Mustn’t for ability', 'I *mustn’t* read without my glasses.', 'can’t', 'Ability: ‘I can’t read without my glasses’.'),
  ('Mustn’t for not necessary', 'It’s optional — you *mustn’t* come.', 'needn’t', 'Optional: ‘you needn’t come’.'),
  ('Past', 'Last week we *mustn’t* use the gym.', 'couldn’t', 'Past: ‘we couldn’t use the gym’.'),
  ('Base verb', 'You can’t *smoking* here.', 'smoke', 'After ‘can’t’ use the base verb.'),
  ],
}
