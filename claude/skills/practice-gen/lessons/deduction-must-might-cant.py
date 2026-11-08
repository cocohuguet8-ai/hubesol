TITLE = 'Deduction: must, might & can’t'
AUX = (['must', 'might', 'can’t', 'be'], None, 'must')
NEXT = ('Modal Perfects', '/grammar/modal-verbs/modal-perfects/')
BODY = r'''
## How to form deductions in the present

| Certainty | Modal | Example |
|---|---|---|
| I'm sure it's true (about 95%) | **must** + base verb | She **must be** tired. |
| It's possible (about 50%) | **might / may / could** + base verb | She **might be** tired. |
| I'm sure it's not true (about 95%) | **can't** + base verb | She **can't be** tired. |

We use these modals when we **work something out** from evidence, not when we know the fact. They take the base verb — very often **be**.

| ✗ | ✓ |
|---|---|
| ~~He musts be rich.~~ | He **must** be rich. |
| ~~She must to be at home.~~ | She **must be** at home. |
| ~~It mustn't be true.~~ (deduction) | It **can't be** true. |

## When to use *must* (I'm sure it's true)

### 1. Strong evidence

- The lights are on. They **must** be at home.
- You've been running for an hour. You **must** be exhausted!

> ℹ️ *Have to* is also possible for deduction (*You have to be joking!*), especially in American English — but *must* is the normal, safest choice: *They must be at home.*

### 2. With other verbs

- He speaks five languages. He **must** travel a lot.
- She's always smiling. She **must** love her job.

## When to use *can't* (I'm sure it's not true)

### 1. The opposite of *must*

- That **can't** be Marta — she's in Paris this week.
- You **can't** be hungry. You've just had lunch!

> ⚠️ Typical error: ~~That mustn't be Marta.~~ → The negative deduction is *can't*, never *mustn't*: *That can't be Marta.*

### 2. *Couldn't* also works

*Couldn't* is a little softer than *can't*.

- It **couldn't** be the postman — it's Sunday.

## When to use *might / may / could* (it's possible)

### 1. Not enough evidence

- I don't know where Pau is. He **might** be in the library.
- That **could** be the answer, but I'm not sure.

> ⚠️ Typical error: ~~He must be in the library~~ (when you have no evidence) → *He might be in the library.*

### 2. Negative possibility

Use **might not** / **may not** (not *couldn't*).

- She **might not** know about the party.

## Continuous deductions

For an action happening **now**: modal + **be** + -ing.

- Listen! Someone **must be playing** the piano.
- He's not answering. He **might be driving**.
- They **can't be sleeping** — it's only seven.

## Evidence → deduction

| Evidence | Deduction |
|---|---|
| The ground is wet. | It **must** have rained. *(past — see below)* |
| She's wearing a uniform. | She **must** work here. |
| He's yawning. | He **must** be tired. |
| The shop is dark. | It **can't** be open. |
| I'm not sure where she is. | She **might** be at work. |

For deductions about the **past** (*must have done*), see [Modal Perfects](/grammar/modal-verbs/modal-perfects/).

## Common mistakes

**1. *Mustn't* for negative deduction.** *~~It mustn't be true~~* → **It can't be true.**

**2. *Must* + past form.** *~~She must was tired~~* → **She must be tired** (now) / **She must have been tired** (past).

**3. *To* after the modal.** *~~He must to be ill~~* → **He must be ill.**

**4. *Must* without evidence.** If you're only guessing, use *might*.

**Pro tip:** *must* and *can't* are opposites — swap them to change a sure "yes" into a sure "no".
'''

GAP = ('Fill in the gaps',
  'Type must, might or can’t — or the verb form after it. Use the evidence: sure yes → must; possible → might; sure no → can’t. Twenty original sentences.',
  [
  ('Must', 'The lights are on. They [[must]] be at home.', 'must / might / can’t', 'Strong evidence that it’s true: must + be.'),
  ('Must', 'You’ve walked twenty kilometres! You [[must]] be exhausted.', 'must / might / can’t', 'Clear evidence, so you’re sure: must be exhausted.'),
  ('Must', 'She speaks perfect Italian. She [[must]] have lived in Italy.', 'must / can’t', 'A logical conclusion from the evidence: must.'),
  ('Must', 'He’s wearing a chef’s hat. He [[must]] work in the kitchen.', 'must / might / can’t', 'Evidence (the hat) → sure conclusion: must + base verb.'),
  ('Must', 'Everyone is laughing. The film [[must]] be really funny.', 'must / might / can’t', 'The reaction is strong evidence: must be.'),
  ('Can’t', 'That [[can’t]] be Joan — she’s on holiday in Greece.', 'must / might / can’t', 'You’re sure it isn’t true: can’t + be.'),
  ('Can’t', 'You [[can’t]] be hungry. You’ve just eaten two sandwiches!', 'must / might / can’t', 'Evidence shows it’s impossible: can’t be.'),
  ('Can’t', 'The shop [[can’t]] be open. All the lights are off.', 'must / might / can’t', 'Sure it’s not true: can’t, never mustn’t.'),
  ('Can’t', 'This [[can’t]] be the right road. It’s a dead end!', 'must / might / can’t', 'A negative deduction from evidence: can’t be.'),
  ('Might', 'I don’t know where Laia is. She [[might|may|could]] be at the library.', 'must / might / can’t', 'No real evidence, just a possibility: might be.'),
  ('Might', 'Ask Pol. He [[might|may]] know the answer.', 'must / might / can’t', 'It’s only possible: might + base verb.'),
  ('Might', 'The phone’s ringing. It [[could|might|may]] be Mum.', 'must / could / can’t', 'One possibility among others: could be.'),
  ('Might not', 'She [[might not|may not]] know about the meeting. Let’s tell her.', 'might not / can’t', 'Perhaps she doesn’t know: might not.'),
  ('Base verb', 'He must [[be]] very rich — look at his car!', '(be)', 'After ‘must’ use the base verb ‘be’, not ‘is’.'),
  ('Base verb', 'They must [[love]] animals. They’ve got six dogs.', '(love)', 'After ‘must’ use the base verb: love.'),
  ('Continuous', 'Listen! Someone must be [[playing]] the drums upstairs.', '(play)', 'An action happening now: must be + -ing.'),
  ('Continuous', 'He isn’t answering. He [[might be]] driving.', 'might be / must', 'Perhaps in progress now: might be + -ing.'),
  ('Continuous', 'They can’t be [[sleeping]] — it’s only seven o’clock.', '(sleep)', 'Negative continuous deduction: can’t be + -ing.'),
  ('Couldn’t', 'It [[couldn’t]] be the postman — there’s no post on Sundays.', 'couldn’t / mustn’t', '‘Couldn’t’ is a softer ‘can’t’ for negative deduction.'),
  ('Must', 'Your eyes are red. You [[must]] be tired.', 'must / mustn’t', 'Red eyes are good evidence: must be tired.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 deductions with must, might and can’t.',
  [
  ('Must', 'She must be at work.', []),
  ('Must', 'You must be very tired.', []),
  ('Must', 'He must like football.', []),
  ('Must', 'They must live near here.', []),
  ('Must', 'That must be the new teacher.', []),
  ('Can’t', 'It can’t be true.', []),
  ('Can’t', 'You can’t be serious.', []),
  ('Can’t', 'She can’t be at home.', []),
  ('Can’t', 'That can’t be our bus.', []),
  ('Can’t', 'He can’t be older than me.', []),
  ('Might', 'She might be at the gym.', []),
  ('Might', 'It could be a mistake.', []),
  ('Might', 'They may be lost.', []),
  ('Might not', 'He might not know.', []),
  ('Continuous', 'Someone must be cooking.', []),
  ('Continuous', 'She might be sleeping.', []),
  ('Continuous', 'They can’t be working now.', []),
  ('Continuous', 'He could be waiting outside.', []),
  ('Couldn’t', 'It couldn’t be the postman.', []),
  ('Must', 'This must be your bag.', []),
  ])

MATCH = {'title': 'Match the evidence and the deduction', 'subtitle': 'Tap the evidence, then tap the best deduction.',
  'leftLabel': 'Evidence', 'rightLabel': 'Deduction', 'rightLabelSub': '(must / might / can’t)', 'reviewArrowPrefix': '',
  'pairs': [
  ('He’s yawning all the time.', 'He must be tired.'), ('The house is completely dark.', 'They can’t be at home.'), ('I’m not sure where she is.', 'She might be at work.'),
  ('She’s wearing a nurse’s uniform.', 'She must work at the hospital.'), ('He’s only six.', 'He can’t drive.'), ('The phone’s ringing.', 'It might be Dad.'),
  ('Everyone is wearing coats.', 'It must be cold outside.'), ('You’ve just had lunch.', 'You can’t be hungry.'), ('He hasn’t replied.', 'He may be busy.'),
  ('She’s got a big smile.', 'She must be happy.'), ('Marc is in London.', 'That can’t be Marc.'), ('There’s a noise in the kitchen.', 'It could be the cat.'),
  ('The streets are full of water.', 'It must be raining a lot.'), ('It’s Sunday, and the shop always closes on Sundays.', 'It can’t be open today.'), ('I don’t know the answer.', 'It might be B.'),
  ('He speaks Japanese fluently.', 'He must study a lot.'), ('She’s been asleep all day.', 'She can’t be tired.'), ('Their car isn’t here.', 'They might be on holiday.'),
  ('There’s music upstairs.', 'Someone must be playing the piano.'), ('The answer is 3 + 3 = 7.', 'That can’t be right.'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Must = sure it’s true, can’t = sure it isn’t, might = possible.',
  [
  ('Must', 'She’s been working for twelve hours. She ___ be exhausted.', ['must', 'can’t', 'mustn’t', 'must to'],
   ['‘Can’t be exhausted’ is the opposite of what the evidence shows.', '‘Mustn’t’ is a prohibition, never used for deduction.', '‘Must’ is never followed by ‘to’.'],
   'Twelve hours of work is strong evidence, so you’re sure: must be exhausted.'),
  ('Can’t', 'That ___ be Joan. She’s in Australia.', ['can’t', 'mustn’t', 'must', 'might'],
   ['‘Mustn’t’ is never used for a negative deduction.', '‘Must be Joan’ contradicts the evidence.', '‘Might’ shows doubt, but you’re sure.'],
   'Being in Australia makes it impossible, so the negative deduction is ‘can’t be’.'),
  ('Might', 'I’m not sure who’s at the door. It ___ be the neighbour.', ['might', 'must', 'can’t', 'mustn’t'],
   ['‘Must’ shows you’re sure, but you aren’t.', '‘Can’t’ means you’re sure it isn’t.', '‘Mustn’t’ is a prohibition, not a deduction.'],
   'Without evidence it’s only a possibility, so ‘might be’ is the right choice.'),
  ('Must', 'They’ve got three cars and a pool. They ___ be rich.', ['must', 'can’t', 'might not', 'mustn’t'],
   ['‘Can’t be rich’ contradicts the evidence.', '‘Might not’ is a weak negative possibility.', '‘Mustn’t’ isn’t used for deduction.'],
   'Three cars and a pool are strong evidence, so the deduction is ‘must be rich’.'),
  ('Can’t', 'You ___ be cold. It’s 35 degrees!', ['can’t', 'must', 'mustn’t', 'don’t have to'],
   ['‘Must be cold’ contradicts the evidence.', '‘Mustn’t’ is a prohibition.', '‘Don’t have to’ is about necessity.'],
   'At 35 degrees it’s almost impossible to be cold: can’t be.'),
  ('Base verb', 'He must ___ really tired after the match.', ['be', 'is', 'to be', 'being'],
   ['After a modal use the base verb ‘be’, not ‘is’.', 'No ‘to’ after ‘must’.', '‘Must being’ is wrong; continuous is ‘must be + -ing’.'],
   'After ‘must’ the verb ‘be’ stays in the base form: must be.'),
  ('Continuous', 'Listen! Someone ___ singing in the shower.', ['must be', 'must', 'can’t', 'must to be'],
   ['‘Must singing’ needs ‘be’ before the -ing form.', '‘Can’t singing’ is wrong and contradicts the evidence.', 'No ‘to’ after ‘must’.'],
   'You can hear it now, so it’s a continuous deduction: must be + -ing.'),
  ('Continuous', 'She isn’t answering. She ___ be driving.', ['might', 'must to', 'mights', 'can’t to'],
   ['No ‘to’ after ‘must’.', 'Modals never take -s.', 'No ‘to’ after ‘can’t’.'],
   'Not answering suggests a possibility: she might be driving right now.'),
  ('Mustn’t', 'Which sentence is a correct negative deduction?', ['It can’t be true.', 'It mustn’t be true.', 'It doesn’t must be true.', 'It hasn’t to be true.'],
   ['‘Mustn’t’ means prohibition, not deduction.', 'Modals don’t use ‘doesn’t’.', '‘Hasn’t to’ is not a correct form.'],
   'The opposite of ‘must be’ in deduction is ‘can’t be’.'),
  ('Have to', 'Which sentence is a deduction, not an obligation?', ['He must be at home — his car is outside.', 'He has to be at home by ten.', 'He must be home by ten — it’s the rule.', 'He has to stay at home.'],
   ['That’s an obligation (a time rule).', 'That’s an obligation.', 'That’s an obligation.'],
   'The evidence (his car) shows this ‘must’ is a logical conclusion.'),
  ('Might not', 'She ___ know about the change of plan. Let’s call her.', ['might not', 'couldn’t', 'mustn’t', 'can’t to'],
   ['‘Couldn’t know’ suggests it’s impossible.', '‘Mustn’t’ is a prohibition.', 'No ‘to’ after ‘can’t’.'],
   'Perhaps she doesn’t know: the negative possibility is ‘might not’.'),
  ('Couldn’t', 'It ___ be the postman — it’s a bank holiday.', ['couldn’t', 'mustn’t', 'might', 'must'],
   ['‘Mustn’t’ isn’t used for deduction.', '‘Might’ shows it’s possible, but the holiday rules it out.', '‘Must’ contradicts the evidence.'],
   '‘Couldn’t’ works like a softer ‘can’t’ for negative deduction.'),
  ('Must', 'Your bag is so heavy! What’s in it? It ___ be full of books.', ['must', 'can’t', 'mustn’t', 'needn’t'],
   ['‘Can’t’ contradicts the weight.', '‘Mustn’t’ is a prohibition.', '‘Needn’t’ is about necessity.'],
   'The weight is good evidence, so ‘must be full of books’ is a strong deduction.'),
  ('Can’t', 'He ___ be the manager. He’s only seventeen!', ['can’t', 'must', 'might', 'mustn’t'],
   ['‘Must’ contradicts the evidence.', '‘Might’ shows doubt, but his age rules it out.', '‘Mustn’t’ isn’t used for deduction.'],
   'His age makes it very unlikely, so you’re sure it isn’t true: can’t be.'),
  ('Might', 'Where are my keys? They ___ be in the car — I’m not sure.', ['could', 'must', 'can’t', 'mustn’t'],
   ['‘Must’ means you’re sure, but ‘I’m not sure’.', '‘Can’t’ means you’re sure they aren’t.', '‘Mustn’t’ is a prohibition.'],
   '‘I’m not sure’ shows it’s only possible: could be in the car.'),
  ('Must', 'Pau got 10 out of 10. He ___ have studied a lot.', ['must', 'can’t', 'mustn’t', 'has'],
   ['‘Can’t have studied’ contradicts the evidence.', '‘Mustn’t’ isn’t used for deduction.', '‘Has have’ is wrong.'],
   'A perfect score is strong evidence: must (have studied).'),
  ('Continuous', 'They ___ be having dinner — it’s only four o’clock.', ['can’t', 'must', 'mustn’t', 'must to'],
   ['‘Must be having dinner’ at four contradicts the evidence.', '‘Mustn’t’ isn’t used for deduction.', '‘Must’ is never followed by ‘to’.'],
   'Four o’clock is too early, so the negative continuous deduction is ‘can’t be having’.'),
  ('Certainty', 'Which sentence shows the most certainty?', ['She must be ill.', 'She might be ill.', 'She could be ill.', 'She may be ill.'],
   ['‘Might’ shows doubt.', '‘Could’ shows possibility.', '‘May’ shows possibility.'],
   '‘Must’ shows about 95% certainty; might, may and could show 50% or less.'),
  ('Must', 'Mmm, something smells delicious. Dad ___ be cooking paella.', ['must', 'can’t', 'mustn’t', 'shouldn’t'],
   ['‘Can’t’ contradicts the smell.', '‘Mustn’t’ is a prohibition.', '‘Shouldn’t’ is advice.'],
   'The smell is strong evidence of an action now: must be cooking.'),
  ('Can’t', 'This ___ be my coat. Mine is blue.', ['can’t', 'must', 'mustn’t', 'might'],
   ['‘Must’ contradicts the colour.', '‘Mustn’t’ isn’t used for deduction.', '‘Might’ shows doubt, but the colour is clear evidence.'],
   'The colour proves it isn’t yours: can’t be my coat.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('Mustn’t for deduction', 'That *mustn’t* be Pol — he’s at school.', 'can’t', 'Negative deduction: ‘That can’t be Pol’.'),
  ('Mustn’t for deduction', 'You *mustn’t* be hungry — you’ve just eaten.', 'can’t', 'Negative deduction: ‘You can’t be hungry’.'),
  ('Mustn’t for deduction', 'It *mustn’t* be true!', 'can’t', 'Negative deduction: ‘It can’t be true!’.'),
  ('Must + past form', 'His car is here, so he must *is* at home.', 'be', 'After ‘must’ use the base form: ‘he must be at home’.'),
  ('Mustn’t for deduction', 'Look at their house! They *mustn’t* be poor.', 'can’t', '‘Mustn’t’ is a prohibition; for a sure negative deduction use ‘can’t’: ‘They can’t be poor’.'),
  ('Base verb', 'She must *is* tired after the trip.', 'be', 'After ‘must’ use ‘be’: ‘She must be tired’.'),
  ('Base verb', 'He can’t *knows* the answer.', 'know', 'After ‘can’t’ use the base verb: ‘know’.'),
  ('Base verb', 'They might *are* lost.', 'be', 'After ‘might’ use ‘be’: ‘They might be lost’.'),
  ('-s on a modal', 'He *musts* be the new teacher.', 'must', 'Modals never take -s.'),
  ('Continuous', 'Someone must *playing* the guitar.', 'be playing', 'Continuous deduction: ‘must be playing’.'),
  ('Continuous', 'She might be *sleep* now.', 'sleeping', 'After ‘might be’ use -ing: ‘sleeping’.'),
  ('Wrong certainty', 'I’m not sure where she is. She *must* be at work.', 'might', 'Not sure → ‘She might be at work’.'),
  ('Wrong certainty', 'The lights are off. They *must* be at home.', 'can’t', 'The evidence suggests the opposite: ‘They can’t be at home’.'),
  ('Wrong certainty', 'He’s crying. He *can’t* be sad.', 'must', 'Crying is evidence of sadness: ‘He must be sad’.'),
  ('Wrong certainty', 'Everyone’s wearing shorts. It *can’t* be hot.', 'must', 'The evidence shows ‘It must be hot’.'),
  ('Couldn’t for perhaps not', 'She *couldn’t* know about it — let’s tell her just in case.', 'might not', 'Perhaps not: ‘She might not know’.'),
  ('Wrong modal', 'He’s ten, so he *mustn’t* be a doctor.', 'can’t', 'Negative deduction: ‘He can’t be a doctor’.'),
  ('Mustn’t for deduction', 'It *mustn’t* be the cat — the cat is outside.', 'can’t', 'Negative deduction: ‘It can’t be the cat’.'),
  ('Spelling', 'You *cant* be serious!', 'can’t', 'Spelling: ‘can’t’ with an apostrophe.'),
  ('Wrong form', 'That can’t *been* right.', 'be', 'After ‘can’t’ use ‘be’: ‘That can’t be right’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, how sure, multiple choice and spot-the-mistake. In the typing questions write must, might or can’t, or the verb after them. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('certainty', 'How sure?'),
 'fill': [
  ('Must', 'She’s got a suntan. She [[must]] have been on holiday.', 'must / can’t', 'A suntan is strong evidence, so the deduction is ‘must’.', 'Sure it’s true → ‘must’.'),
  ('Can’t', 'He [[can’t]] be French. He doesn’t speak a word of it.', 'must / can’t', 'Strong evidence it’s not true: ‘can’t be’.', 'Sure it isn’t → ‘can’t’.'),
  ('Might', 'I’m not sure, but the answer [[might|may|could]] be C.', 'must / might', 'Only a guess, no evidence: ‘might be’.', 'Not sure → ‘might’.'),
  ('Continuous', 'Shh! The baby must be [[sleeping]].', 'sleep', 'An action happening now: must be + -ing.', 'After ‘must be’ use -ing.'),
  ],
 'order': [
  ('Must', 'He must be at school.', []),
  ('Can’t', 'That can’t be right.', []),
  ('Might', 'She might be ill.', []),
  ('Continuous', 'They must be joking.', []),
  ],
 'customItems': [
  ('Certainty', 'The evidence is very strong. Which modal fits a sure ‘yes’?', ['must', 'might', 'could', 'may'],
   ['‘Might’ shows only possibility.', '‘Could’ shows only possibility.', '‘May’ shows only possibility.'],
   '‘Must’ = I’m sure it’s true (about 95%).'),
  ('Certainty', 'You’re sure it isn’t true. Which modal do you use?', ['can’t', 'mustn’t', 'might not', 'don’t have to'],
   ['‘Mustn’t’ is a prohibition, not a deduction.', '‘Might not’ only means perhaps not.', '‘Don’t have to’ is about necessity.'],
   '‘Can’t’ = I’m sure it isn’t true.'),
  ('Certainty', '‘She might be at home’ means…', ['perhaps she’s at home', 'I’m sure she’s at home', 'I’m sure she isn’t at home', 'she has to be at home'],
   ['That’s ‘must be’.', 'That’s ‘can’t be’.', 'That’s an obligation.'],
   '‘Might’ = it’s possible, about 50%.'),
  ('Certainty', 'Which word is NOT used for deduction?', ['mustn’t', 'must', 'can’t', 'might'],
   ['‘Must’ is used for a sure deduction.', '‘Can’t’ is used for a sure negative deduction.', '‘Might’ is used for a possible deduction.'],
   '‘Mustn’t’ is only for prohibition — never for deduction.'),
  ],
 'mc': [
  ('Must', 'He’s always at the gym. He ___ love exercise.', ['must', 'can’t', 'mustn’t', 'needn’t'],
   ['‘Can’t’ contradicts the evidence.', '‘Mustn’t’ isn’t used for deduction.', '‘Needn’t’ is about necessity.'],
   'Always at the gym is strong evidence: must love exercise.'),
  ('Can’t', 'You ___ be tired. You slept for ten hours!', ['can’t', 'must', 'mustn’t', 'must to'],
   ['‘Must’ contradicts the evidence.', '‘Mustn’t’ isn’t used for deduction.', '‘Must’ is never followed by ‘to’.'],
   'Ten hours of sleep makes it very unlikely: can’t be tired.'),
  ('Might', 'Where’s Laia? She ___ be in the garden.', ['might', 'must', 'can’t', 'mustn’t'],
   ['‘Must’ needs evidence.', '‘Can’t’ means you’re sure she isn’t.', '‘Mustn’t’ isn’t used for deduction.'],
   'No evidence, just a guess: might be.'),
  ('Base verb', 'That must ___ the new student.', ['be', 'is', 'to be', 'being'],
   ['After a modal use ‘be’, not ‘is’.', 'No ‘to’ after ‘must’.', '‘Must being’ is wrong.'],
   'After ‘must’ the base verb is ‘be’.'),
  ],
 'error': [
  ('Mustn’t for deduction', 'That *mustn’t* be our train — it’s too early.', 'can’t', 'Negative deduction uses ‘can’t’.'),
  ('Must + to', 'She must *to be* at home — her bike is outside.', 'be', '‘Must’ is never followed by ‘to’: ‘She must be at home’.'),
  ('Base verb', 'He must *is* joking.', 'be', 'After ‘must’ use ‘be’: ‘He must be joking’.'),
  ('Wrong certainty', 'I’m not sure. He *must* be in Madrid.', 'might', 'Not sure → ‘might’.'),
  ],
}
