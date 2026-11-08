TITLE = 'May, Might & Could'
AUX = (['may', 'might', 'could', 'not'], None, 'might')
NEXT = ('Deduction: must, might & can’t', '/grammar/modal-verbs/deduction-must-might-cant/')
BODY = r'''
## How to form may, might and could for possibility

| Form | Structure | Example |
|---|---|---|
| Affirmative | may / might / could + base verb | It **might rain** later. |
| Negative | may not / might not + base verb | She **may not come**. |
| Continuous | may / might / could + be + -ing | He **might be sleeping**. |
| Question | Do you think…? / Could…? | **Do you think** it'll rain? / **Could** it be true? |

All three are modals: no *-s*, no *to*, no *do*. They mean **"perhaps"** — the speaker isn't sure.

| ✗ | ✓ |
|---|---|
| ~~It mights rain.~~ | It **might** rain. |
| ~~She may to come.~~ | She **may come**. |
| ~~He doesn't might come.~~ | He **might not** come. |

## How sure is the speaker?

| Certainty | Modal | Example |
|---|---|---|
| about 50% | **may** | We **may** go to the beach. |
| a bit less | **might** | We **might** go to the beach. |
| possible | **could** | We **could** go — who knows? |

The difference is small. In everyday English, *might* is the most common; *may* is a little more formal.

## When to use *may* and *might*

### 1. Possible future events

- I **might** go to the party, but I'm not sure.
- It **may** be sunny tomorrow.

> ⚠️ Typical error: ~~Maybe I might go.~~ → Don't use both: *Maybe I'll go.* or *I might go.*

### 2. Possible present situations

- She **might** be at home — her light is on.
- Ask Pol. He **may** know the answer.

### 3. Negatives

- I **may not** have time to call you. (perhaps I won't)
- They **might not** like the film.

> ⚠️ Typical error: ~~He mightn't to come.~~ → No *to*: *He might not come.*

## When to use *could*

### 1. Possibility (affirmative)

- That **could** be the postman at the door.
- Be careful — you **could** fall.

### 2. Not for negative possibility

**Couldn't** doesn't mean "perhaps not". It means "impossible" or "not able".

| Sentence | Meaning |
|---|---|
| She **might not** be at home. | Perhaps she isn't at home. |
| She **couldn't** be at home. | It's impossible that she's at home. |

> ⚠️ Typical error: ~~It couldn't rain tomorrow~~ (meaning perhaps not) → *It might not rain tomorrow.*

## Continuous forms

For actions in progress now:

- Don't call — she **might be studying**.
- They **could be waiting** for us outside.

## *Maybe* and *perhaps*

These adverbs mean the same as *may/might* but use a normal verb.

- **Maybe** she**'s** busy. = She **might** be busy.
- **Perhaps** we**'ll** win. = We **may** win.

## Questions

We don't usually ask questions with *may* or *might* for possibility. Use *Do you think…?* or *Could…?*

- **Do you think** it'll snow? (✓) — not ~~May it snow?~~
- **Could** it be a mistake?

## Common mistakes

**1. *-s* on the modal.** *~~She mights~~* → **She might.**

**2. *To* after the modal.** *~~It may to rain~~* → **It may rain.**

**3. *Couldn't* for "perhaps not".** *~~I couldn't come tomorrow~~* (meaning maybe not) → **I might not come tomorrow.**

**4. *Maybe* + modal.** *~~Maybe it might rain~~* → **It might rain / Maybe it will rain.**

**Pro tip:** when you're 50/50, reach for *might* — it's the safest, most natural choice.
'''

GAP = ('Fill in the gaps',
  'Type may, might, could, may not or might not — or the verb that follows. Twenty original sentences.',
  [
  ('Future', 'Take an umbrella. It [[might|may|could]] rain later.', 'might / must', 'A possible future event: might + base verb.'),
  ('Future', 'I [[might|may]] go to the concert, but I haven’t decided yet.', 'might / will', 'The speaker isn’t sure: might + base verb.'),
  ('Future', 'We [[may|might]] move to Barcelona next year.', 'may / will', 'A possible plan, not certain: may + base verb.'),
  ('Future', 'Joan [[might|may]] be late — the traffic is terrible.', 'might / must', 'A possible situation: might + be.'),
  ('Present', 'Ask Laia. She [[might|may]] know where the keys are.', 'might / must', 'Perhaps she knows now: might + base verb.'),
  ('Present', 'Someone’s at the door. It [[could|might|may]] be the postman.', 'could / can', 'You don’t know who is knocking, so it’s a present possibility: could be.'),
  ('Present', 'He isn’t answering. He [[may|might]] be in the shower.', 'may / will', 'Perhaps he’s in the shower: may be.'),
  ('Negative', 'I [[might not]] have time to call you tonight.', 'might not / couldn’t', 'Perhaps I won’t: might not + base verb.'),
  ('Negative', 'They [[may not]] like the surprise, so let’s ask first.', 'may not / can’t', 'Perhaps they won’t like it: may not + base verb.'),
  ('Negative', 'Don’t wait for me. I [[might not]] finish until nine.', 'might not / couldn’t', 'Negative possibility: might not, never ‘couldn’t’.'),
  ('Base verb', 'It might [[snow]] in the mountains this weekend.', '(snow)', 'After ‘might’ use the base verb, with no ‘to’ and no -s.'),
  ('Base verb', 'She may [[decide]] to stay at home.', '(decide)', 'After ‘may’ use the base verb: decide, not decides.'),
  ('Continuous', 'Don’t phone now — they [[might be]] having dinner.', 'might be / might', 'An action perhaps in progress now: might be + -ing.'),
  ('Continuous', 'Marta’s not in class. She could be [[waiting]] for the bus.', '(wait)', 'Continuous possibility: could be + -ing, waiting.'),
  ('Danger', 'Be careful on the ice. You [[could]] fall.', 'could / can’t', 'Climbing the wall is risky — a fall is possible: could + base verb.'),
  ('Danger', 'Don’t leave your bag there — someone [[might]] take it.', 'might / must', 'A possible risk: might + base verb.'),
  ('Maybe', '[[Maybe]] she’s ill. She looks very pale.', 'maybe / might', '‘Maybe’ is an adverb + normal verb: Maybe she’s ill.'),
  ('Perhaps', '[[Perhaps]] we’ll win the match — who knows?', 'perhaps / may', '‘Perhaps’ + will: Perhaps we’ll win.'),
  ('Question', '[[Do]] you think it’ll be sunny tomorrow?', 'do / may', 'Possibility questions use ‘Do you think…?’, not ‘May it…?’.'),
  ('Question', '[[Could]] this be the right address?', 'could / may', '‘Could’ can ask about a possibility: Could this be…?'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples of possibility with may, might and could.',
  [
  ('Future', 'It might rain later.', []),
  ('Future', 'We may go to Italy.', []),
  ('Future', 'I might see you tomorrow.', []),
  ('Future', 'The shop may be closed.', []),
  ('Present', 'She might be at home.', []),
  ('Present', 'He may know the answer.', []),
  ('Present', 'That could be her car.', []),
  ('Negative', 'I might not come tonight.', []),
  ('Negative', 'They may not have time.', []),
  ('Negative', 'It might not be true.', []),
  ('Continuous', 'She might be sleeping.', []),
  ('Continuous', 'They could be waiting outside.', []),
  ('Continuous', 'He may be working late.', []),
  ('Danger', 'You could hurt yourself.', []),
  ('Danger', 'The ice might break.', []),
  ('Maybe', 'Maybe she’s busy.', []),
  ('Perhaps', 'Perhaps it’s a mistake.', []),
  ('Question', 'Do you think it’ll snow?', []),
  ('Question', 'Could it be a joke?', []),
  ('Future', 'We might win the cup.', []),
  ])

MATCH = {'title': 'Match the same meaning', 'subtitle': 'Tap a sentence with maybe or perhaps, then tap the one that means the same with may, might or could.',
  'leftLabel': 'With maybe / perhaps', 'rightLabel': 'Same meaning', 'rightLabelSub': '(modal)', 'reviewArrowPrefix': '',
  'pairs': [
  ('Maybe it’ll rain.', 'It might rain.'), ('Perhaps she’s at home.', 'She may be at home.'), ('Maybe he knows.', 'He might know.'),
  ('Perhaps we’ll be late.', 'We may be late.'), ('Maybe it isn’t true.', 'It might not be true.'), ('Perhaps they won’t come.', 'They may not come.'),
  ('Maybe she’s sleeping.', 'She might be sleeping.'), ('Perhaps it’s the postman.', 'It could be the postman.'), ('Maybe I’ll go out.', 'I might go out.'),
  ('Perhaps he’s lost.', 'He may be lost.'), ('Maybe we’ll win.', 'We could win.'), ('Perhaps she won’t like it.', 'She might not like it.'),
  ('Maybe they’re waiting.', 'They could be waiting.'), ('Perhaps it’ll snow.', 'It may snow.'), ('Maybe you’re right.', 'You might be right.'),
  ('Perhaps I won’t have time.', 'I may not have time.'), ('Maybe it’s broken.', 'It could be broken.'), ('Perhaps he’s working.', 'He might be working.'),
  ('Maybe the shop is closed.', 'The shop may be closed.'), ('Perhaps we’ll move house.', 'We might move house.'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. May, might and could = perhaps. Watch the negatives: might not, never couldn’t.',
  [
  ('Future', 'Take a jacket. It ___ get cold tonight.', ['might', 'mights', 'might to', 'is might'],
   ['Modals never take -s, even with ‘it’.', '‘Might’ is followed by the base verb with no ‘to’.', '‘Might’ doesn’t need ‘be’ before it.'],
   'The weather may change later, but it isn’t certain: might + base verb.'),
  ('Future', 'I ___ go to the party. I’m not sure yet.', ['may', 'will', 'must', 'can’t'],
   ['‘Will’ sounds certain, but you’re not sure.', '‘Must’ is obligation or certainty.', '‘Can’t’ means impossible.'],
   '‘I’m not sure yet’ shows about 50% certainty, so ‘may’ fits perfectly.'),
  ('Present', 'Someone’s knocking. It ___ be the delivery man.', ['could', 'can', 'must to', 'coulds'],
   ['‘Can’ isn’t used for a specific present possibility like this.', 'No ‘to’ after a modal.', 'Modals never take -s.'],
   'A present possibility: could be.'),
  ('Negative', 'She ___ come tomorrow — she has a cold.', ['might not', 'couldn’t', 'mightn’t to', 'doesn’t might'],
   ['‘Couldn’t come’ means it’s impossible, not ‘perhaps not’.', 'No ‘to’ after a modal.', 'Modals don’t use ‘doesn’t’.'],
   'Her cold means perhaps she won’t come: might not + base verb, never ‘couldn’t’.'),
  ('Negative', 'We ___ have enough money for the trip. Let’s check.', ['may not', 'can’t to', 'couldn’t', 'don’t may'],
   ['No ‘to’ after a modal.', '‘Couldn’t’ means impossible.', 'Modals don’t use ‘don’t’.'],
   'Perhaps we don’t have enough money — we need to check: may not + base verb.'),
  ('Continuous', 'Don’t ring the bell. The baby ___ sleeping.', ['might be', 'might', 'might to be', 'mights be'],
   ['‘Might sleeping’ needs ‘be’ before the -ing form.', 'No ‘to’ after ‘might’.', 'Modals never take -s.'],
   'The baby is perhaps sleeping right now, so use ‘might be’ + -ing.'),
  ('Continuous', 'Pau isn’t here. He ___ waiting at the other entrance.', ['could be', 'could', 'can be', 'could to be'],
   ['‘Could waiting’ needs ‘be’.', '‘Can be’ isn’t used for a specific possibility now.', 'No ‘to’ after ‘could’.'],
   'Pau is perhaps waiting at this moment, so use ‘could be’ + -ing.'),
  ('Couldn’t', 'Which sentence means ‘perhaps it isn’t true’?', ['It might not be true.', 'It couldn’t be true.', 'It mustn’t be true.', 'It can’t be true.'],
   ['‘Couldn’t be’ means it’s impossible.', '‘Mustn’t’ is about prohibition.', '‘Can’t be’ means I’m sure it isn’t true.'],
   '‘Might not’ means perhaps not; ‘couldn’t’ and ‘can’t’ mean you’re sure it isn’t.'),
  ('Maybe', '___ she’s on holiday. Her phone is off.', ['Maybe', 'May be', 'Might', 'Could'],
   ['‘May be’ (two words) is a verb: ‘She may be on holiday’.', '‘Might she’s’ is wrong.', '‘Could she’s’ is wrong.'],
   '‘Maybe’ written as one word is an adverb, followed by a normal verb: she’s.'),
  ('Maybe', 'Which sentence is correct?', ['Maybe it will rain.', 'Maybe it might rain.', 'Maybe it mights rain.', 'May be it rain.'],
   ['Don’t use ‘maybe’ and ‘might’ together.', 'Modal verbs never take -s: ‘It might be cold’.', '‘May be it rain’ is wrong.'],
   'Use ‘maybe’ with ‘will’, or ‘might’ on its own — never both together.'),
  ('Question', '___ you think the bus will be late?', ['Do', 'May', 'Might', 'Are'],
   ['We don’t ask possibility questions with ‘May you think’.', '‘Might you think’ is wrong.', '‘Are you think’ is wrong.'],
   'We usually ask about possibility with ‘Do you think…?’, not with ‘may’.'),
  ('Question', '___ it be a mistake?', ['Could', 'May', 'Does', 'Might to'],
   ['‘May it be’ is very formal and old-fashioned.', '‘Does it be’ is wrong.', 'No ‘to’ after a modal.'],
   '‘Could it be…?’ is the natural way to ask whether something is possible.'),
  ('Danger', 'Don’t climb that wall — you ___ fall.', ['could', 'can’t', 'must', 'couldn’t'],
   ['‘Can’t fall’ means it’s impossible.', '‘Must fall’ means it’s certain or obligatory.', '‘Couldn’t’ means impossible.'],
   'A possible danger: could + base verb.'),
  ('Base verb', 'She may ___ a new job soon.', ['get', 'gets', 'to get', 'getting'],
   ['No -s after a modal.', 'No ‘to’ after a modal.', 'No -ing after a modal (without ‘be’).'],
   'After ‘may’ the verb stays in the base form, with no -s and no ‘to’.'),
  ('Certainty', 'Which word shows the most certainty?', ['will', 'might', 'may', 'could'],
   ['‘Might’ is less than 50%.', '‘May’ is about 50%.', '‘Could’ is just possible.'],
   '‘Will’ shows certainty; may, might and could all mean ‘perhaps’.'),
  ('Present', 'Ask your sister. She ___ have my charger.', ['might', 'must to', 'mights', 'is might'],
   ['No ‘to’ after ‘must’, and it means certainty.', 'No -s on modals.', '‘Is might’ is wrong.'],
   'Your sister perhaps has the charger, so use ‘might’ + the base verb ‘have’.'),
  ('Future', 'They ___ build a new stadium next year — nothing’s decided.', ['might', 'will', 'are going to', 'must'],
   ['‘Will’ sounds decided.', '‘Are going to’ sounds planned.', '‘Must’ is obligation.'],
   '‘Nothing’s decided’ tells you it’s only a possibility, so use ‘might’.'),
  ('Negative', 'Hurry up! The shop ___ be open after six.', ['might not', 'couldn’t', 'mustn’t', 'doesn’t might'],
   ['‘Couldn’t be’ means impossible.', '‘Mustn’t be’ is about prohibition.', 'Modals don’t use ‘doesn’t’.'],
   'Perhaps the shop won’t be open after six: might not, not ‘couldn’t’.'),
  ('Continuous', 'Your dad is late. He ___ be stuck in traffic.', ['may', 'may to', 'mays', 'is may'],
   ['No ‘to’ after a modal.', 'No -s on modals.', '‘Is may’ is wrong.'],
   'Perhaps he is stuck in traffic now: ‘may be stuck’, with no -s and no ‘to’.'),
  ('Future', 'If we hurry, we ___ catch the last train.', ['might', 'must', 'mustn’t', 'shall'],
   ['‘Must’ is obligation.', '‘Mustn’t’ is prohibition.', '‘Shall’ is for offers and suggestions.'],
   'Hurrying gives us a chance, but it isn’t certain: we might catch it.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('-s on a modal', 'It *mights* rain this afternoon.', 'might', 'Modals never take -s: ‘It might rain’.'),
  ('-s on a modal', 'She *mays* be at the gym.', 'may', 'Modals never take -s: ‘She may be…’.'),
  ('-s after a modal', 'He might *knows* the answer.', 'know', 'After ‘might’ use the base verb: ‘know’.'),
  ('-s after a modal', 'The train may *arrives* late.', 'arrive', 'After ‘may’ use the base verb: ‘arrive’.'),
  ('Past after a modal', 'We could *won* the match.', 'win', 'After ‘could’ use the base verb: ‘win’.'),
  ('Wrong negative', 'She might *doesn’t* come.', 'not', 'The negative is ‘might not’: ‘She might not come’.'),
  ('Wrong negative', 'I may *don’t* have time.', 'not', 'The negative is ‘may not’: ‘I may not have time’.'),
  ('Couldn’t for perhaps not', 'Take your coat — it *couldn’t* be warm later.', 'might not', 'Perhaps not: ‘it might not be warm’.'),
  ('Couldn’t for perhaps not', 'I *couldn’t* come tomorrow — I’ll let you know.', 'might not', 'Perhaps not: ‘I might not come’.'),
  ('Maybe + modal', 'Maybe it *might* snow tonight.', 'will', 'Don’t combine: ‘Maybe it will snow’ or ‘It might snow’.'),
  ('May be or maybe', 'She *maybe* at the gym now.', 'may be', 'As a verb it’s two words: ‘She may be at the gym’.'),
  ('Continuous', 'She might *sleeping* now.', 'be sleeping', 'Continuous: ‘might be sleeping’.'),
  ('Continuous', 'They could be *wait* for us.', 'waiting', 'After ‘could be’ use -ing: ‘waiting’.'),
  ('Question', '*May* it rain tomorrow?', 'Will', 'We don’t ask ‘May it rain?’. Ask ‘Will it rain?’ or ‘Do you think it’ll rain?’.'),
  ('Certainty', 'I’m not sure, but she *will* be at home.', 'might', '‘I’m not sure’ needs a possibility modal: ‘she might be at home’.'),
  ('Certainty', 'Perhaps we *must* win the cup this year.', 'will', '‘Perhaps’ + will: ‘Perhaps we will win’.'),
  ('Can for possibility', 'That *can* be the postman at the door.', 'could', 'A specific possibility: ‘That could be the postman’.'),
  ('Danger', 'Be careful — you *can’t* fall.', 'could', 'A possible danger: ‘you could fall’.'),
  ('Spelling', 'We *migth* go to the cinema.', 'might', 'Spelling: ‘might’.'),
  ('Continuous', 'He might be *work* late tonight.', 'working', 'After ‘might be’ use -ing: ‘working’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, how sure, multiple choice and spot-the-mistake. In the typing questions write may, might, could or their negatives. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('certainty', 'How sure?'),
 'fill': [
  ('Future', 'We [[might|may|could]] go camping next weekend.', 'might / will', 'A plan that isn’t decided yet: might + base verb.', 'Not sure → ‘might’.'),
  ('Negative', 'She [[might not|may not]] like spicy food.', 'might not / couldn’t', 'Perhaps she doesn’t like it: might not + base verb.', 'For ‘perhaps not’ use ‘might not’; ‘couldn’t’ means impossible.'),
  ('Continuous', 'He [[might be|may be|could be]] playing football right now.', 'might be', 'An action that is perhaps in progress now: might be + -ing.', 'Use ‘might be’ + -ing.'),
  ('Maybe', '[[Maybe]] the film starts at eight.', 'maybe / may be', 'The adverb ‘maybe’ is one word and goes with a normal verb.', 'Adverb → ‘Maybe’.'),
  ],
 'order': [
  ('Future', 'It might be sunny.', []),
  ('Negative', 'We may not win.', []),
  ('Present', 'She could be right.', []),
  ('Continuous', 'They might be lost.', []),
  ],
 'customItems': [
  ('Certainty', 'I’m completely sure. The shop ___ be open — I just walked past.', ['will', 'might', 'may', 'could'],
   ['‘Might’ shows doubt, but you’re sure.', '‘May’ shows doubt.', '‘Could’ shows doubt.'],
   'You walked past and saw it, so you are certain: will.'),
  ('Certainty', 'I’m not sure. The shop ___ be open — it’s a holiday.', ['might', 'will', 'must', 'is'],
   ['‘Will’ sounds sure.', '‘Must’ sounds sure.', '‘Is’ is a fact.'],
   'A holiday makes it uncertain, so use the possibility modal ‘might’.'),
  ('Certainty', 'Which sentence is the least sure?', ['She might come.', 'She will come.', 'She’s coming.', 'She’s definitely coming.'],
   ['‘Will’ is sure.', 'The present continuous shows a plan.', '‘Definitely’ is very sure.'],
   '‘Might’ shows less than 50% certainty — the least sure option.'),
  ('Certainty', '‘We may go to the beach’ means…', ['perhaps we’ll go', 'we’ll definitely go', 'we must go', 'we can’t go'],
   ['That’s ‘will’.', 'That’s obligation.', 'That’s impossibility.'],
   '‘We may go’ means perhaps we’ll go — it isn’t decided.'),
  ],
 'mc': [
  ('Present', 'His car isn’t here. He ___ have left already.', ['might', 'mights', 'might to', 'is might'],
   ['No -s on modals.', 'No ‘to’ after ‘might’.', '‘Is might’ is wrong.'],
   'His car is missing, so perhaps he has left: might + have left.'),
  ('Couldn’t', 'Which sentence means ‘perhaps they won’t come’?', ['They might not come.', 'They couldn’t come.', 'They can’t come.', 'They mustn’t come.'],
   ['‘Couldn’t’ = impossible / not able.', '‘Can’t’ = not able.', '‘Mustn’t’ = forbidden.'],
   '‘Might not’ means perhaps not; ‘couldn’t’ would mean impossible.'),
  ('Question', '___ you think she’ll call?', ['Do', 'May', 'Might', 'Could'],
   ['‘May you think’ is wrong.', '‘Might you think’ is wrong.', '‘Could you think’ is a request.'],
   'We ask about possibility with ‘Do you think…?’, not with ‘may’.'),
  ('Danger', 'Don’t touch the dog — it ___ bite.', ['might', 'must', 'can’t', 'couldn’t'],
   ['‘Must bite’ is too certain.', '‘Can’t bite’ means it’s impossible.', '‘Couldn’t’ means impossible.'],
   'A warning about a possible danger: it might bite you.'),
  ],
 'error': [
  ('-s on a modal', 'It *mights* be cold.', 'might', 'No -s on modals.'),
  ('Couldn’t for perhaps not', 'I *couldn’t* go — I’ll see.', 'might not', 'Perhaps not → ‘might not’.'),
  ('Maybe + modal', 'Maybe she *might* call.', 'will', 'Don’t combine them: ‘Maybe she will call’ or ‘She might call’.'),
  ('-s after a modal', 'He may *comes* later.', 'come', 'After ‘may’ use the base verb with no -s: ‘He may come later’.'),
  ],
}
