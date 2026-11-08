TITLE = 'Reporting Verbs'
AUX = (['to', 'that', 'for', 'of', 'on'], None, 'to')
NEXT = ('All reported speech', '/grammar/reported-speech/')
BODY = r'''
## Why use reporting verbs?

*Say* and *tell* only report the words. Reporting verbs also show the **function** — was it an offer, a promise, a warning, an apology?

> "I'll help you, I promise." → She **promised to help** me.
> "It was me. I broke it." → He **admitted breaking** it.

Each verb has its own **pattern**. Learn the verb with its pattern.

## The main patterns

| Pattern | Verbs | Example |
|---|---|---|
| verb + **to** + infinitive | agree, offer, promise, refuse, threaten, decide | She **offered to carry** my bag. |
| verb + **person** + **to** + infinitive | advise, ask, encourage, invite, order, persuade, remind, tell, warn | He **advised me to rest**. |
| verb + **-ing** | admit, deny, recommend, suggest | They **denied taking** the money. |
| verb + **preposition** + **-ing** | apologise **for**, insist **on**, complain **about** | She **apologised for being** late. |
| verb + **person** + **preposition** + **-ing** | accuse … **of**, blame … **for**, congratulate … **on**, thank … **for** | They **accused him of cheating**. |
| verb + **that** + clause | explain, admit, deny, insist, promise, suggest, complain | He **explained that** the train was late. |

## Verb + *to* + infinitive

- "I'll lend you some money." → He **offered to lend** me some money.
- "No, I won't do it!" → She **refused to do** it.
- "OK, I'll come." → They **agreed to come**.

> ⚠️ Typical error: ~~She refused doing it.~~ → *Refuse* takes *to*: *She refused to do it.*

## Verb + person + *to* + infinitive

- "You should study more." → The teacher **advised me to study** more.
- "Go on, try it!" → My friends **encouraged me to try** it.
- "Don't forget your keys." → Mum **reminded me to take** my keys.

> ⚠️ Typical error: ~~He advised to me to rest.~~ → No *to* before the person: *advised me to rest.*

## Verb + *-ing*

- "Yes, I took it." → He **admitted taking** it.
- "I didn't break it!" → She **denied breaking** it.
- "Let's go to the beach." → He **suggested going** to the beach.

> ⚠️ Typical error: ~~He suggested to go to the beach.~~ → *Suggest* + *-ing* (or *that*): *suggested going.*

## Verb + preposition + *-ing*

- "Sorry I'm late." → She **apologised for being** late.
- "You stole my phone!" → He **accused** me **of stealing** his phone.
- "Well done on passing!" → They **congratulated** me **on passing**.
- "Thanks for helping." → She **thanked** me **for helping**.

## The *that* clause

### Backshift after the reporting verb

Many verbs can also take *that* + a backshifted clause:

- She **admitted that** she **had** lied.
- He **promised that** he **would** call.
- They **complained that** the room **was** dirty.

## Common mistakes

**1. Wrong pattern.** *~~She suggested me to go~~* → **She suggested (that) I (should) go / She suggested going.**

**2. Missing preposition.** *~~He apologised being late~~* → **He apologised for being late.**

**3. Infinitive after a preposition.** *~~She insisted on to pay~~* → **She insisted on paying.**

**4. Person after verbs that don't take one.** *~~He offered me to help~~* → **He offered to help me.**

**Pro tip:** keep a list of verbs grouped by pattern — when you learn a new reporting verb, learn its pattern at the same time.
'''

GAP = ('Fill in the gaps',
  'Type the verb form that follows the reporting verb: to + infinitive, -ing, or the missing preposition. Twenty original sentences.',
  [
  ('to-infinitive', '“I’ll carry your bag.” → He offered [[to carry]] my bag.', '(carry)', '‘Offer’ is followed by to + infinitive.'),
  ('to-infinitive', '“I promise I’ll call you.” → She promised [[to call]] me.', '(call)', '‘Promise’ is followed by to + infinitive.'),
  ('to-infinitive', '“No, I won’t apologise.” → He refused [[to apologise]].', '(apologise)', '‘Refuse’ is followed by to + infinitive.'),
  ('to-infinitive', '“OK, I’ll help.” → My brother agreed [[to help]].', '(help)', '‘Agree’ is followed by to + infinitive.'),
  ('to-infinitive', '“Be quiet or I’ll call the police!” → He threatened [[to call]] the police.', '(call)', '‘Threaten’ is followed by to + infinitive.'),
  ('Person + to', '“You should see a doctor.” → She advised me [[to see]] a doctor.', '(see)', '‘Advise’ + person + to + infinitive. Learn each reporting verb together with its pattern.'),
  ('Person + to', '“Go on, enter the competition!” → My teacher encouraged me [[to enter]] the competition.', '(enter)', '‘Encourage’ + person + to + infinitive.'),
  ('Person + to', '“Don’t forget to lock the door.” → Dad reminded me [[to lock]] the door.', '(lock)', '‘Remind’ + person + to + infinitive.'),
  ('Person + to', '“Don’t swim there.” → The lifeguard warned us [[not to swim]] there.', '(not swim)', '‘Warn’ + person + not to + infinitive.'),
  ('-ing', '“Yes, I ate the last biscuit.” → He admitted [[eating]] the last biscuit.', '(eat)', '‘Admit’ is followed by -ing.'),
  ('-ing', '“I didn’t break the window!” → She denied [[breaking]] the window.', '(break)', '‘Deny’ is followed by -ing.'),
  ('-ing', '“Let’s go to the cinema.” → Pau suggested [[going]] to the cinema.', '(go)', '‘Suggest’ is followed by -ing (or that…).'),
  ('-ing', '“You should try the paella.” → The waiter recommended [[trying]] the paella.', '(try)', '‘Recommend’ is followed by -ing.'),
  ('Preposition', '“Sorry I’m late.” → She apologised [[for]] being late.', 'for / of', '‘Apologise’ takes ‘for’ + -ing.'),
  ('Preposition', '“I’ll pay — I insist!” → He insisted [[on]] paying.', 'on / to', '‘Insist’ takes ‘on’ + -ing.'),
  ('Preposition', '“You cheated!” → They accused him [[of]] cheating.', 'of / for', '‘Accuse’ + person + of + -ing. Learn each reporting verb together with its pattern.'),
  ('Preposition', '“Well done on winning!” → Everyone congratulated her [[on]] winning.', 'on / for', '‘Congratulate’ + person + on + -ing.'),
  ('Preposition', '“Thanks for helping me.” → She thanked me [[for]] helping her.', 'for / of', '‘Thank’ + person + for + -ing.'),
  ('After preposition', '“It’s your fault we lost!” → He blamed me for [[losing]] the match.', '(lose)', 'After a preposition use -ing: for losing.'),
  ('That clause', '“The train was delayed.” → She explained [[that]] the train had been delayed.', 'that / to', '‘Explain’ is followed by a that-clause.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 reporting verbs with their patterns.',
  [
  ('to-infinitive', 'She offered to help me.', []),
  ('to-infinitive', 'He promised to call.', []),
  ('to-infinitive', 'They refused to pay.', []),
  ('to-infinitive', 'We agreed to meet at six.', []),
  ('Person + to', 'She advised me to rest.', []),
  ('Person + to', 'He reminded me to call Mum.', []),
  ('Person + to', 'They encouraged me to apply.', []),
  ('Person + to', 'She warned us not to go.', []),
  ('Person + to', 'He persuaded me to stay.', []),
  ('-ing', 'He admitted taking the money.', []),
  ('-ing', 'She denied breaking it.', []),
  ('-ing', 'Pau suggested going to the beach.', []),
  ('-ing', 'The guide recommended visiting the castle.', []),
  ('Preposition', 'She apologised for being late.', []),
  ('Preposition', 'He insisted on paying.', []),
  ('Preposition', 'They accused him of lying.', []),
  ('Preposition', 'We congratulated her on passing.', []),
  ('Preposition', 'She thanked me for helping.', []),
  ('That clause', 'He explained that he was ill.', []),
  ('That clause', 'She complained that the room was cold.', []),
  ])

MATCH = {'title': 'Match the words and the reporting verb', 'subtitle': 'Tap what someone said, then tap the reporting verb that describes it.',
  'leftLabel': 'Direct speech', 'rightLabel': 'Reporting verb', 'rightLabelSub': '(function)', 'reviewArrowPrefix': '',
  'pairs': [
  ('“I’ll help you, I promise.”', 'promised'), ('“Can I carry that for you?”', 'offered'), ('“No, I won’t do it.”', 'refused'),
  ('“OK, I’ll come.”', 'agreed'), ('“You should rest.”', 'advised'), ('“Don’t forget your keys.”', 'reminded'),
  ('“Be careful — it’s dangerous.”', 'warned'), ('“Yes, I took it.”', 'admitted'), ('“I didn’t do it!”', 'denied'),
  ('“Let’s have a party.”', 'suggested'), ('“Sorry I’m late.”', 'apologised'), ('“You stole my bike!”', 'accused'),
  ('“Well done on your exam!”', 'congratulated'), ('“Thank you for the flowers.”', 'thanked'), ('“I’ll pay — I insist.”', 'insisted'),
  ('“Come to my wedding.”', 'invited'), ('“Go on, you can do it!”', 'encouraged'), ('“Do it or I’ll tell the teacher!”', 'threatened'),
  ('“The soup is cold.”', 'complained'), ('“It’s your fault!”', 'blamed'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Every reporting verb has its own pattern: to-infinitive, person + to, -ing, or preposition + -ing.',
  [
  ('to-infinitive', '“I’ll do the washing-up.” → He offered ___ the washing-up.', ['to do', 'doing', 'me to do', 'that doing'],
   ['‘Offer’ takes a to-infinitive, not -ing.', '‘Offer’ doesn’t take a person before ‘to’.', '‘That doing’ is not a correct pattern.'],
   '‘Offer’ + to + infinitive: offered to do. Learn each reporting verb together with its pattern.'),
  ('to-infinitive', '“I won’t tell you!” → She refused ___ me.', ['to tell', 'telling', 'tell', 'for telling'],
   ['‘Refuse’ takes a to-infinitive, not -ing.', 'The base verb alone is missing ‘to’.', '‘Refuse’ doesn’t take ‘for’.'],
   '‘Refuse’ + to + infinitive: refused to tell. Learn each reporting verb together with its pattern.'),
  ('Person + to', '“You should talk to the teacher.” → Mum advised ___ to the teacher.', ['me to talk', 'to talk me', 'me talking', 'to me to talk'],
   ['Wrong word order.', '‘Advise’ + person takes ‘to’, not -ing.', 'No ‘to’ before the person.'],
   '‘Advise’ + person + to + infinitive.'),
  ('-ing', '“Yes, I lied.” → He admitted ___.', ['lying', 'to lie', 'lie', 'for lying'],
   ['‘Admit’ isn’t followed by a to-infinitive.', 'The base verb alone is wrong here.', '‘Admit’ doesn’t take ‘for’.'],
   '‘Admit’ + -ing (or that…). Learn each reporting verb together with its pattern.'),
  ('-ing', '“I didn’t take your phone!” → She denied ___ my phone.', ['taking', 'to take', 'take', 'of taking'],
   ['‘Deny’ isn’t followed by a to-infinitive.', 'The base verb alone is wrong.', '‘Deny’ doesn’t take ‘of’.'],
   '‘Deny’ + -ing. Learn each reporting verb together with its pattern.'),
  ('Suggest', '“Let’s eat out tonight.” → Laia suggested ___ out.', ['eating', 'to eat', 'us to eat', 'eat'],
   ['‘Suggest to eat’ is a very common mistake.', '‘Suggest’ + person + to is wrong.', 'The base verb alone needs ‘that we (should)’.'],
   '‘Suggest’ + -ing, or suggest that + clause. Learn each reporting verb together with its pattern.'),
  ('Preposition', '“Sorry I forgot.” → He apologised ___ forgetting.', ['for', 'of', 'on', 'to'],
   ['‘Apologise of’ is wrong.', '‘Apologise on’ is wrong.', '‘Apologise to’ is for the person: apologise to someone for something.'],
   '‘Apologise for’ + -ing. Learn each reporting verb together with its pattern.'),
  ('Preposition', '“You broke it!” → She accused me ___ breaking it.', ['of', 'for', 'on', 'about'],
   ['‘Accuse for’ is wrong; that’s ‘blame for’.', '‘Accuse on’ is wrong.', '‘Accuse about’ is wrong.'],
   '‘Accuse’ + person + of + -ing.'),
  ('Preposition', '“Congratulations on your new job!” → They congratulated him ___ his new job.', ['on', 'for', 'of', 'about'],
   ['‘Congratulate for’ is a common mistake.', '‘Congratulate of’ is wrong.', '‘Congratulate about’ is wrong.'],
   '‘Congratulate’ + person + on. Learn each reporting verb together with its pattern.'),
  ('After preposition', 'He insisted on ___ for dinner.', ['paying', 'to pay', 'pay', 'paid'],
   ['After a preposition we never use a to-infinitive.', 'After a preposition use -ing.', '‘Paid’ is past.'],
   'Preposition + -ing: insisted on paying. Learn each reporting verb together with its pattern.'),
  ('Person or not', 'Which sentence is correct?', ['She offered to help me.', 'She offered me to help.', 'She offered helping me.', 'She offered me helping.'],
   ['‘Offer’ doesn’t take a person before ‘to’.', '‘Offer’ takes to + infinitive, not -ing.', 'Wrong pattern.'],
   '‘Offer’ + to + infinitive (+ object after). Learn each reporting verb together with its pattern.'),
  ('Person or not', 'Which sentence is correct?', ['He persuaded me to stay.', 'He persuaded to stay me.', 'He persuaded me staying.', 'He persuaded that I stay.'],
   ['Wrong word order.', '‘Persuade’ + person + to, not -ing.', '‘Persuade that’ isn’t the normal pattern.'],
   '‘Persuade’ + person + to + infinitive. Learn each reporting verb together with its pattern.'),
  ('Function', '“If you don’t stop, I’ll call your parents!” → He ___ to call my parents.', ['threatened', 'promised', 'offered', 'suggested'],
   ['‘Promised’ is for something good.', '‘Offered’ is for help.', '‘Suggested’ takes -ing and isn’t a threat.'],
   'A warning with a bad consequence: threaten. Learn each reporting verb together with its pattern.'),
  ('Function', '“Why don’t you try the new café?” → She ___ trying the new café.', ['suggested', 'refused', 'warned', 'denied'],
   ['‘Refused’ is saying no.', '‘Warned’ is about danger.', '‘Denied’ is saying something isn’t true.'],
   'An idea for someone: suggest + -ing. Learn each reporting verb together with its pattern.'),
  ('Function', '“It wasn’t me who ate it!” → He ___ eating it.', ['denied', 'admitted', 'apologised', 'thanked'],
   ['‘Admitted’ is the opposite.', '‘Apologised’ needs ‘for’ and means sorry.', '‘Thanked’ is for gratitude.'],
   'Say something isn’t true: deny. Learn each reporting verb together with its pattern.'),
  ('Remind', '“Remember to take your umbrella.” → She ___ me to take my umbrella.', ['reminded', 'remembered', 'warned', 'refused'],
   ['‘Remember’ doesn’t take a person + to like this.', '‘Warned’ is for danger.', '‘Refused’ is saying no.'],
   '‘Remind’ + person + to. Learn each reporting verb together with its pattern.'),
  ('That clause', '“The shop is closed on Sundays.” → He explained ___ the shop was closed on Sundays.', ['that', 'to', 'for', 'me that'],
   ['‘Explain to’ needs a person: explain to me that…', '‘Explain for’ is wrong.', '‘Explain me’ is a very common mistake.'],
   '‘Explain’ + (to + person) + that + clause. Learn each reporting verb together with its pattern.'),
  ('Blame', '“You made us late!” → She blamed me ___ making us late.', ['for', 'of', 'on', 'about'],
   ['‘Blame of’ is wrong; that’s ‘accuse of’.', '‘Blame on’ needs a different structure.', '‘Blame about’ is wrong.'],
   '‘Blame’ + person + for + -ing. Learn each reporting verb together with its pattern.'),
  ('Thank', '“Thanks for the lift.” → He thanked her ___ the lift.', ['for', 'of', 'on', 'to'],
   ['‘Thank of’ is wrong.', '‘Thank on’ is wrong.', '‘Thank to’ is wrong.'],
   '‘Thank’ + person + for. Learn each reporting verb together with its pattern.'),
  ('Agree', '“Fine, I’ll lend you my car.” → My dad agreed ___ me his car.', ['to lend', 'lending', 'me to lend', 'on lending'],
   ['‘Agree’ takes to + infinitive.', '‘Agree’ doesn’t take a person before ‘to’.', '‘Agree on’ is for a decision, not an action you’ll do.'],
   '‘Agree’ + to + infinitive. Learn each reporting verb together with its pattern.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('Wrong pattern', 'She refused *doing* her homework.', 'to do', '‘Refuse’ + to + infinitive: ‘refused to do’.'),
  ('Wrong pattern', 'He offered *helping* me.', 'to help', '‘Offer’ + to + infinitive: ‘offered to help’.'),
  ('Wrong pattern', 'They promised *coming* early.', 'to come', '‘Promise’ + to + infinitive: ‘promised to come’.'),
  ('Wrong pattern', 'He admitted *steal* the money.', 'stealing', '‘Admit’ + -ing: ‘admitted stealing’. Learn each reporting verb together with its pattern.'),
  ('Wrong pattern', 'She denied *break* the vase.', 'breaking', '‘Deny’ + -ing: ‘denied breaking’. Learn each reporting verb together with its pattern.'),
  ('Wrong pattern', 'Pau suggested *go* to the beach.', 'going', '‘Suggest’ + -ing: ‘suggested going’. Learn each reporting verb together with its pattern.'),
  ('Missing preposition', 'She apologised *being* late.', 'for being', '‘Apologise’ needs ‘for’: ‘apologised for being late’.'),
  ('Wrong preposition', 'They accused him *for* cheating.', 'of', '‘Accuse’ + of: ‘accused him of cheating’.'),
  ('Wrong preposition', 'We congratulated her *for* winning.', 'on', '‘Congratulate’ + on: ‘congratulated her on winning’.'),
  ('Wrong preposition', 'She thanked me *of* helping.', 'for', '‘Thank’ + for: ‘thanked me for helping’.'),
  ('Wrong preposition', 'He blamed me *of* the accident.', 'for', '‘Blame’ + for: ‘blamed me for the accident’.'),
  ('Infinitive after preposition', 'He insisted on *pay* for everything.', 'paying', 'After a preposition use -ing: ‘insisted on paying’.'),
  ('Wrong pattern', 'She offered *carrying* the bags for me.', 'to carry', '‘Offer’ + to + infinitive: ‘offered to carry’.'),
  ('Person + to', 'The doctor advised me *resting* for a week.', 'to rest', '‘Advise’ + person + to: ‘advised me to rest’.'),
  ('Explain me', 'He explained *me* that the bus was late.', 'to me', '‘Explain’ needs ‘to’ before the person: ‘explained to me that…’.'),
  ('Remind or remember', 'Mum *remembered* me to buy bread.', 'reminded', '‘Remind’ + person + to: ‘reminded me to buy bread’.'),
  ('Warn', 'She warned us not *swim* there.', 'to swim', 'Negative: ‘warned us not to swim’. Learn each reporting verb together with its pattern.'),
  ('Past participle', 'He admitted having *broke* it.', 'broken', 'Participle: ‘having broken’. Learn each reporting verb together with its pattern.'),
  ('Wrong verb', '“Sorry!” → She *thanked* for being late.', 'apologised', 'Saying sorry: ‘apologised for being late’.'),
  ('Spelling', 'They *threatend* to leave.', 'threatened', 'Spelling: ‘threatened’. Learn each reporting verb together with its pattern.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, which pattern, multiple choice and spot-the-mistake. In the typing questions write the pattern after the reporting verb. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('pattern', 'Which pattern?'),
 'fill': [
  ('to-infinitive', '“I’ll drive you home.” → She offered [[to drive]] me home.', 'drive', '‘Offer’ is always followed by to + infinitive.', 'Offer → to + verb.'),
  ('-ing', '“OK, it was me.” → He admitted [[breaking]] the glass.', 'break', '‘Admit’ is followed by the -ing form.', 'Admit → -ing.'),
  ('Preposition', '“Sorry for shouting.” → She apologised [[for]] shouting.', 'for / of', '‘Apologise’ always takes ‘for’ before the -ing form.', 'Apologise → for.'),
  ('Person + to', '“You should apply.” → My teacher encouraged me [[to apply]].', 'apply', '‘Encourage’ + person + to + infinitive.', 'Encourage + person + to.'),
  ],
 'order': [
  ('to-infinitive', 'He refused to answer.', []),
  ('-ing', 'She suggested taking a taxi.', []),
  ('Preposition', 'They thanked us for coming.', []),
  ('Person + to', 'He warned me not to touch it.', []),
  ],
 'customItems': [
  ('Pattern', 'Which verb is followed by -ing?', ['deny', 'refuse', 'promise', 'offer'],
   ['‘Refuse’ takes to + infinitive.', '‘Promise’ takes to + infinitive.', '‘Offer’ takes to + infinitive.'],
   'deny / admit / suggest / recommend + -ing.'),
  ('Pattern', 'Which verb needs a person before ‘to’?', ['advise', 'agree', 'refuse', 'offer'],
   ['‘Agree’ takes to + infinitive without a person.', '‘Refuse’ takes to + infinitive without a person.', '‘Offer’ takes to + infinitive without a person.'],
   'advise / remind / warn / encourage + person + to.'),
  ('Pattern', 'Which preposition goes with ‘accuse’?', ['of', 'for', 'on', 'about'],
   ['‘For’ goes with blame, thank, apologise.', '‘On’ goes with insist and congratulate.', '‘About’ goes with complain.'],
   'accuse someone of doing something.'),
  ('Pattern', 'Which verb takes ‘on’ + -ing?', ['insist', 'apologise', 'thank', 'blame'],
   ['‘Apologise’ takes ‘for’.', '‘Thank’ takes ‘for’.', '‘Blame’ takes ‘for’.'],
   'insist on doing / congratulate someone on doing.'),
  ],
 'mc': [
  ('to-infinitive', '“I promise I won’t be late.” → She promised ___ late.', ['not to be', 'not being', 'to not been', 'don’t be'],
   ['‘Promise’ takes to + infinitive.', '‘To not been’ is wrong.', '‘Don’t’ disappears.'],
   'Negative: promised not to be.'),
  ('Suggest', '“Let’s take the bus.” → He suggested ___ the bus.', ['taking', 'to take', 'us to take', 'take'],
   ['A very common mistake: suggest + -ing.', '‘Suggest’ + person + to is wrong.', 'Needs ‘that we (should)’.'],
   'Suggest + -ing.'),
  ('Preposition', 'They complained ___ the noise.', ['about', 'for', 'of', 'on'],
   ['‘Complain for’ is wrong.', '‘Complain of’ is for illness.', '‘Complain on’ is wrong.'],
   'complain about something.'),
  ('Explain', 'She explained ___ the meeting had been cancelled.', ['to me that', 'me that', 'me to', 'for me that'],
   ['‘Explain me’ is wrong.', 'Wrong pattern.', '‘For me’ is wrong.'],
   'explain (to someone) that…'),
  ],
 'error': [
  ('Wrong pattern', 'He refused *helping* us.', 'to help', '‘Refuse’ + to + infinitive.'),
  ('Missing preposition', 'She apologised *breaking* the cup.', 'for breaking', '‘Apologise for’ + -ing.'),
  ('Wrong preposition', 'They accused her *for* lying.', 'of', '‘Accuse of’ + -ing.'),
  ('Explain me', 'He explained *me the rules*.', 'the rules to me', '‘Explain’ + thing + to + person: ‘explained the rules to me’.'),
  ],
}
