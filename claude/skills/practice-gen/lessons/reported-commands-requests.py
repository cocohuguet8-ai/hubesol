TITLE = 'Reported Commands & Requests'
AUX = (['told', 'asked', 'to', 'not'], None, 'told')
NEXT = ('Reporting Verbs', '/grammar/reported-speech/reporting-verbs/')
BODY = r'''
## How to report commands and requests

| Type | Direct speech | Reported speech |
|---|---|---|
| Command | "**Sit** down." | She **told me to sit** down. |
| Negative command | "**Don't** shout." | He **told us not to shout**. |
| Request | "**Can you** help me?" | She **asked me to help** her. |
| Negative request | "Please **don't** be late." | He **asked me not to be** late. |

The pattern is always: **verb + person + (not) to + base verb**. No tense change is needed — the infinitive stays the same.

| ✗ | ✓ |
|---|---|
| ~~She told me sit down.~~ | She told me **to sit** down. |
| ~~He told us don't shout.~~ | He told us **not to** shout. |
| ~~She asked to me to help.~~ | She **asked me** to help. |

## Commands: *tell* + person + *to*

Use **tell** (or *order* for very strong commands).

- "Close the door." → The teacher **told me to close** the door.
- "Stand up!" → The officer **ordered** them **to stand** up.

> ⚠️ Typical error: ~~The teacher said me to close the door.~~ → Use *tell*: *told me to close…*

## Requests: *ask* + person + *to*

Use **ask** for polite requests (*Can you…? Could you…? Will you…? Please…*).

- "Could you pass the salt?" → She **asked me to pass** the salt.
- "Please wait here." → He **asked us to wait** there.

> ⚠️ Typical error: ~~She asked me if I could pass the salt~~ is a reported question, not wrong — but for a request, *asked me to pass* is more natural.

## Negative: *not to*

Put **not** before **to**.

- "Don't touch it." → She told me **not to** touch it.
- "Please don't tell anyone." → He asked me **not to** tell anyone.

> ⚠️ Typical error: ~~She told me to not touch it.~~ → Formal English prefers *not to touch*. ~~She told me don't touch it~~ is wrong.

## The person is necessary

*Tell* and *ask* need a person (the listener) before *to*.

| ✗ | ✓ |
|---|---|
| ~~He told to wait.~~ | He told **us** to wait. |
| ~~She asked to help.~~ (if you mean someone else helps) | She asked **me** to help. |

*Ask to* without a person means the speaker wants to do it: *She asked **to leave** early.* (= She asked if she could leave.)

## Other changes

### Pronouns, time and place

Pronouns, time and place words change as usual.

- "Call **me tomorrow**." → She told me to call **her the next day**.
- "Bring **your** book **here**." → He told me to bring **my** book **there**.

## Other verbs with the same pattern

| Verb | Example |
|---|---|
| order | The police **ordered** him **to stop**. |
| warn | She **warned** us **not to go** near the edge. |
| remind | Mum **reminded** me **to take** my keys. |
| advise | The doctor **advised** me **to rest**. |
| invite | They **invited** us **to stay**. |

More in [Reporting Verbs](/grammar/reported-speech/reporting-verbs/).

## Common mistakes

**1. Missing *to*.** *~~She told me wait~~* → **She told me to wait.**

**2. *Don't* in the report.** *~~He told me don't go~~* → **He told me not to go.**

**3. *Say* + person + *to*.** *~~She said me to sit~~* → **She told me to sit.**

**4. Missing the person.** *~~He told to hurry~~* → **He told us to hurry.**

**Pro tip:** commands and requests never need backshift — just *told / asked + person + (not) to + verb*.
'''

GAP = ('Fill in the gaps',
  'Type the missing part of the reported command or request: told / asked, to, not to, or the base verb. Twenty original sentences.',
  [
  ('Command', '“Sit down.” → The teacher told us [[to sit]] down.', '(sit)', 'A command is reported with told + person + to + base verb.'),
  ('Command', '“Open your books.” → She [[told]] us to open our books.', 'told / said', 'Commands use ‘tell’ + person: told us.'),
  ('Command', '“Be quiet!” → The librarian told the students [[to be]] quiet.', '(be)', 'Imperative ‘be’ becomes ‘to be’ in reported speech.'),
  ('Command', '“Turn off your phones.” → The guide told everyone [[to turn]] off their phones.', '(turn)', 'told + person + to + base verb: to turn.'),
  ('Negative command', '“Don’t shout.” → Mum told us [[not to]] shout.', 'not to / don’t', 'A negative command is reported with ‘not to’.'),
  ('Negative command', '“Don’t touch the paintings.” → The guard told me [[not to touch]] the paintings.', '(not touch)', 'told + person + not to + base verb. Remember the pattern: told / asked + person + (not) to + verb.'),
  ('Negative command', '“Don’t be late!” → The coach told us not [[to be]] late.', '(be)', 'Negative: not + to be.'),
  ('Request', '“Can you help me?” → My sister [[asked]] me to help her.', 'asked / told', 'Polite requests are reported with ‘ask’.'),
  ('Request', '“Could you pass the salt?” → He asked me [[to pass]] the salt.', '(pass)', 'asked + person + to + base verb.'),
  ('Request', '“Please wait here.” → She asked us to wait [[there]].', 'here / there', 'Place words change: ‘here’ becomes ‘there’.'),
  ('Request', '“Will you close the window?” → He asked me [[to close]] the window.', '(close)', 'A request with ‘Will you…?’: asked me to close.'),
  ('Negative request', '“Please don’t tell anyone.” → She asked me [[not to tell]] anyone.', '(not tell)', 'Negative request: asked + person + not to + verb.'),
  ('Negative request', '“Could you not make so much noise?” → He asked us [[not to make]] so much noise.', '(not make)', 'Negative request: not to make.'),
  ('Pronoun', '“Call me tomorrow.” → She told me to call [[her]] the next day.', '(me)', 'She was talking about herself: ‘me’ becomes ‘her’.'),
  ('Possessive', '“Bring your passport.” → He told me to bring [[my]] passport.', '(your)', 'He was speaking to me: ‘your’ becomes ‘my’.'),
  ('Order', '“Stop the car!” → The police officer [[ordered]] him to stop the car.', 'ordered / said', 'A very strong command: ordered + person + to.'),
  ('Warn', '“Don’t go near the edge.” → She warned us [[not to go]] near the edge.', '(not go)', 'warn + person + not to + base verb.'),
  ('Remind', '“Remember to take your keys.” → Mum reminded me [[to take]] my keys.', '(take)', 'remind + person + to + base verb.'),
  ('Person needed', '“Hurry up!” → He told [[us]] to hurry up.', 'us / —', '‘Tell’ needs a person before ‘to’.'),
  ('Ask to', '“Can I leave early?” → Pau asked [[to leave]] early.', '(leave)', 'Without a person, ‘asked to’ = the speaker wanted to do it.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each reported command or request.',
  [
  ('Command', 'She told me to sit down.', []),
  ('Command', 'The teacher told us to be quiet.', []),
  ('Command', 'He told them to wait outside.', []),
  ('Command', 'Mum told me to tidy my room.', []),
  ('Negative command', 'He told us not to shout.', []),
  ('Negative command', 'She told me not to worry.', []),
  ('Negative command', 'The guard told us not to touch it.', []),
  ('Request', 'She asked me to help her.', []),
  ('Request', 'He asked us to wait there.', []),
  ('Request', 'They asked me to close the window.', []),
  ('Negative request', 'She asked me not to tell anyone.', []),
  ('Negative request', 'He asked us not to be late.', []),
  ('Pronoun', 'She told me to call her.', []),
  ('Order', 'The police ordered him to stop.', []),
  ('Warn', 'She warned us not to swim there.', []),
  ('Remind', 'Dad reminded me to lock the door.', []),
  ('Advise', 'The doctor advised me to rest.', []),
  ('Invite', 'They invited us to stay for dinner.', []),
  ('Ask to', 'He asked to leave early.', []),
  ('Possessive', 'He told me to bring my passport.', []),
  ])

MATCH = {'title': 'Match the direct and reported command', 'subtitle': 'Tap a direct command or request, then tap its reported version.',
  'leftLabel': 'Direct speech', 'rightLabel': 'Reported', 'rightLabelSub': '(told / asked + to)', 'reviewArrowPrefix': '',
  'pairs': [
  ('“Sit down.”', 'She told me to sit down.'), ('“Don’t run.”', 'She told me not to run.'), ('“Can you help me?”', 'She asked me to help her.'),
  ('“Please don’t go.”', 'She asked me not to go.'), ('“Be careful.”', 'She told me to be careful.'), ('“Could you open the door?”', 'She asked me to open the door.'),
  ('“Don’t be late.”', 'She told me not to be late.'), ('“Wait here.”', 'She told me to wait there.'), ('“Will you call me?”', 'She asked me to call her.'),
  ('“Don’t tell anyone.”', 'She told me not to tell anyone.'), ('“Close your eyes.”', 'She told me to close my eyes.'), ('“Please turn the music down.”', 'She asked me to turn the music down.'),
  ('“Don’t forget your keys.”', 'She reminded me not to forget my keys.'), ('“Stop!”', 'She ordered me to stop.'), ('“Don’t touch the dog.”', 'She warned me not to touch the dog.'),
  ('“Come to my party.”', 'She invited me to come to her party.'), ('“Could you not smoke here?”', 'She asked me not to smoke there.'), ('“Bring your book.”', 'She told me to bring my book.'),
  ('“Remember to call Grandma.”', 'She reminded me to call Grandma.'), ('“You should rest.”', 'She advised me to rest.'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. told / asked + person + (not) to + base verb — no backshift needed.',
  [
  ('Command', '“Close the window.” → The teacher told me ___ the window.', ['to close', 'close', 'closing', 'that I close'],
   ['A reported command needs ‘to’ before the base verb.', 'The -ing form doesn’t follow ‘tell + person’.', '‘That I close’ isn’t the normal pattern for commands.'],
   'Commands: told + person + to + base verb. Remember the pattern: told / asked + person + (not) to + verb.'),
  ('Negative command', '“Don’t eat in class.” → She told us ___ in class.', ['not to eat', 'don’t eat', 'to don’t eat', 'not eat'],
   ['‘Don’t’ disappears in reported commands.', '‘To don’t’ is impossible.', '‘Not eat’ is missing ‘to’.'],
   'Negative commands: told + person + not to + base verb. Remember the pattern: told / asked + person + (not) to + verb.'),
  ('Request', '“Could you lend me your notes?” → Pau ___ me to lend him my notes.', ['asked', 'told', 'said', 'asked to'],
   ['‘Told’ sounds like an order, but this was a polite request.', '‘Said me’ is wrong.', 'No ‘to’ between ‘asked’ and the person.'],
   'Polite requests are reported with ask + person + to. Remember the pattern: told / asked + person + (not) to + verb.'),
  ('Tell or say', 'Which sentence is correct?', ['She told me to wait.', 'She said me to wait.', 'She told to me wait.', 'She said to wait me.'],
   ['‘Say’ can’t take a person + to-infinitive.', 'No ‘to’ before the person, and ‘to’ is needed before ‘wait’.', 'Wrong word order.'],
   'Use tell + person + to + verb. Remember the pattern: told / asked + person + (not) to + verb.'),
  ('Person needed', '“Hurry up!” → The coach told ___ to hurry up.', ['us', 'to us', '—', 'that we'],
   ['No ‘to’ before the person after ‘tell’.', '‘Tell’ needs a person here.', '‘Told that we to hurry’ is wrong.'],
   '‘Tell’ always needs a person before ‘to’. Remember the pattern: told / asked + person + (not) to + verb.'),
  ('Negative request', '“Please don’t call after ten.” → She asked me ___ after ten.', ['not to call', 'to not calling', 'don’t call', 'not calling'],
   ['‘To not calling’ is wrong.', '‘Don’t’ disappears.', '‘Not calling’ is missing ‘to’.'],
   'Negative requests: asked + person + not to + verb. Remember the pattern: told / asked + person + (not) to + verb.'),
  ('No backshift', '“Be careful.” → She told me ___ careful.', ['to be', 'to was', 'to been', 'being'],
   ['‘To was’ is impossible: the infinitive never changes.', '‘To been’ is wrong.', 'The -ing form doesn’t fit.'],
   'The infinitive doesn’t change: to be. Remember the pattern: told / asked + person + (not) to + verb.'),
  ('Pronoun', '“Call me later.” → He told me to call ___ later.', ['him', 'me', 'you', 'his'],
   ['He was talking about himself.', '‘You’ would be the listener.', '‘His’ is a possessive.'],
   'Pronouns change: me → him. Remember the pattern: told / asked + person + (not) to + verb.'),
  ('Place', '“Wait here.” → She told us to wait ___.', ['there', 'here', 'where', 'then'],
   ['‘Here’ is where you are now.', '‘Where’ is a question word.', '‘Then’ is a time word.'],
   'here → there. Pattern: told / asked + person + (not) to + verb.'),
  ('Order', '“Put your hands up!” → The police officer ___ him to put his hands up.', ['ordered', 'asked', 'said', 'invited'],
   ['‘Asked’ is too polite for this strong command.', '‘Said’ can’t take a person + to.', '‘Invited’ changes the meaning.'],
   '‘Order’ is for very strong commands. Remember the pattern: told / asked + person + (not) to + verb.'),
  ('Warn', '“Don’t swim here — it’s dangerous.” → She ___ us not to swim there.', ['warned', 'invited', 'asked', 'said'],
   ['‘Invited’ is the opposite meaning.', '‘Asked’ loses the idea of danger.', '‘Said us’ is wrong.'],
   '‘Warn’ + person + not to = advise against something dangerous.'),
  ('Remind', '“Don’t forget to post the letter.” → Mum ___ me to post the letter.', ['reminded', 'remembered', 'warned', 'ordered'],
   ['‘Remembered me’ is wrong: ‘remind’ is the verb for making someone remember.', '‘Warned’ is for dangers.', '‘Ordered’ is too strong.'],
   '‘Remind’ + person + to + verb. Remember the pattern: told / asked + person + (not) to + verb.'),
  ('Ask to', '“Can I leave early, please?” → She asked ___ early.', ['to leave', 'me to leave', 'leave', 'if leaving'],
   ['‘Asked me to leave’ means she wanted ME to leave.', '‘Asked leave’ is missing ‘to’.', '‘If leaving’ is wrong.'],
   'Without a person, ‘asked to leave’ = she wanted to leave.'),
  ('Possessive', '“Take your coat.” → He told me to take ___ coat.', ['my', 'your', 'his', 'me'],
   ['He was speaking to me.', 'Only if it was his own coat.', '‘Me’ isn’t a possessive.'],
   'your → my. Remember the pattern: told / asked + person + (not) to + verb.'),
  ('Request', '“Will you turn the TV off, please?” → She asked me ___ the TV off.', ['to turn', 'turn', 'turning', 'if turn'],
   ['A request needs ‘to’ + base verb.', 'The -ing form doesn’t fit.', '‘If turn’ is wrong.'],
   'asked + person + to turn. Remember the pattern: told / asked + person + (not) to + verb.'),
  ('Not to', 'Which sentence is the most standard?', ['He told me not to worry.', 'He told me to not worry.', 'He told me don’t worry.', 'He told me not worry.'],
   ['Common in speech, but ‘not to worry’ is the standard form.', '‘Don’t’ disappears in reported speech.', '‘To’ is missing.'],
   'Standard negative: not to + base verb. Remember the pattern: told / asked + person + (not) to + verb.'),
  ('Command', '“Stand in a line.” → The teacher told the children ___ in a line.', ['to stand', 'stand', 'standing', 'stood'],
   ['A command needs ‘to’.', '-ing doesn’t fit.', '‘Stood’ is past.'],
   'told + person + to + base verb. Remember the pattern: told / asked + person + (not) to + verb.'),
  ('Advise', '“You should see a dentist.” → She ___ me to see a dentist.', ['advised', 'ordered', 'said', 'invited'],
   ['‘Ordered’ is too strong for advice.', '‘Said me’ is wrong.', '‘Invited’ changes the meaning.'],
   'Advice is reported with ‘advise’ + person + to. Remember the pattern: told / asked + person + (not) to + verb.'),
  ('Invite', '“Come to dinner on Saturday.” → They ___ us to come to dinner on Saturday.', ['invited', 'ordered', 'warned', 'reminded'],
   ['‘Ordered’ sounds like a command.', '‘Warned’ is for danger.', '‘Reminded’ is for things you might forget.'],
   'An invitation is reported with ‘invite’ + person + to. Remember the pattern: told / asked + person + (not) to + verb.'),
  ('Negative command', '“Don’t open the door to strangers.” → Mum told me ___ the door to strangers.', ['not to open', 'to not opened', 'don’t open', 'not open'],
   ['‘To not opened’ is wrong.', '‘Don’t’ disappears.', '‘To’ is missing.'],
   'told + person + not to + base verb.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('Missing to', 'She told me *wait* outside.', 'to wait', 'A reported command needs ‘to’: ‘told me to wait’.'),
  ('Missing to', 'He asked us *help* him.', 'to help', 'A reported request needs ‘to’: ‘asked us to help’.'),
  ('Don’t in the report', 'Mum told me *don’t* shout.', 'not to', 'Negative: ‘told me not to shout’. Pattern: told / asked + person + (not) to + verb.'),
  ('Don’t in the report', 'The guard told us *don’t* touch it.', 'not to', 'Negative: ‘told us not to touch it’. Pattern: told / asked + person + (not) to + verb.'),
  ('Say + person', 'The teacher *said* me to sit down.', 'told', 'Use ‘tell’: ‘told me to sit down’. Pattern: told / asked + person + (not) to + verb.'),
  ('Say + person', 'She *said* us to be quiet.', 'told', 'Use ‘tell’: ‘told us to be quiet’. Pattern: told / asked + person + (not) to + verb.'),
  ('Tell or ask', '“Could you help me, please?” → She *told* me to help her.', 'asked', 'A polite request is reported with ‘ask’: ‘asked me to help’.'),
  ('Backshift on infinitive', 'She told me to *was* careful.', 'be', 'The infinitive doesn’t change: ‘to be careful’.'),
  ('-ing after to', 'He told us to *waiting* there.', 'wait', 'After ‘to’ use the base verb: ‘to wait’.'),
  ('-s after to', 'She asked me to *calls* her.', 'call', 'After ‘to’ use the base verb: ‘to call’.'),
  ('Past after to', 'The coach told us to *ran* faster.', 'run', 'After ‘to’ use the base verb: ‘to run’. Pattern: told / asked + person + (not) to + verb.'),
  ('Pronoun', '“Call me.” → She told me to call *me*.', 'her', 'She talked about herself: ‘call her’. Pattern: told / asked + person + (not) to + verb.'),
  ('Possessive', '“Bring your ID.” → He told me to bring *your* ID.', 'my', 'He spoke to me: ‘my ID’. Pattern: told / asked + person + (not) to + verb.'),
  ('Place', '“Stay here.” → She told us to stay *here*. (We’re somewhere else now.)', 'there', 'here → there.'),
  ('Wrong verb', '“Please help me.” → She *ordered* me to help her.', 'asked', 'A polite request: ‘asked me to help’. Pattern: told / asked + person + (not) to + verb.'),
  ('Wrong verb', '“Don’t forget the tickets.” → He *remembered* me not to forget the tickets.', 'reminded', '‘Remind’ + person: ‘reminded me’. Pattern: told / asked + person + (not) to + verb.'),
  ('Wrong verb', '“Don’t go near the dog.” → She *invited* me not to go near the dog.', 'warned', 'A warning: ‘warned me not to go’. Pattern: told / asked + person + (not) to + verb.'),
  ('Past after to', 'She asked me to *came* early.', 'come', 'After ‘to’ use the base verb: ‘to come’.'),
  ('Not position', 'She told me *don’t* to worry.', 'not', 'Negative: ‘told me not to worry’. Pattern: told / asked + person + (not) to + verb.'),
  ('Spelling', 'He *adviced* me to study more.', 'advised', 'The verb is ‘advise’: ‘advised’. Pattern: told / asked + person + (not) to + verb.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, which reporting verb, multiple choice and spot-the-mistake. In the typing questions write told / asked, to, not to or the base verb. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('verb', 'Which reporting verb?'),
 'fill': [
  ('Command', '“Sit still.” → The dentist told me [[to sit]] still.', 'sit', 'A command: told + person + to + base verb.', 'Add ‘to’ before the verb.'),
  ('Negative command', '“Don’t run.” → She told us [[not to]] run.', 'not to / don’t', 'A negative command uses ‘not to’, never ‘don’t’.', 'Negative → not to.'),
  ('Request', '“Could you call me?” → He [[asked]] me to call him.', 'asked / told', 'Polite requests are reported with ‘ask’.', 'Request → asked.'),
  ('Pronoun', '“Help me.” → She asked me to help [[her]].', 'me', 'She talked about herself: ‘me’ becomes ‘her’.', 'me → her.'),
  ],
 'order': [
  ('Command', 'He told us to leave.', []),
  ('Negative command', 'She told me not to cry.', []),
  ('Request', 'He asked me to wait.', []),
  ('Warn', 'She warned us not to go.', []),
  ],
 'customItems': [
  ('Verb', '“Please pass the bread.” → She ___ me to pass the bread.', ['asked', 'ordered', 'warned', 'reminded'],
   ['‘Ordered’ is too strong for a polite request.', '‘Warned’ is for danger.', '‘Reminded’ is for things you might forget.'],
   'Polite request → asked.'),
  ('Verb', '“Don’t touch the wire — it’s live!” → He ___ me not to touch the wire.', ['warned', 'invited', 'asked', 'reminded'],
   ['‘Invited’ is the opposite.', '‘Asked’ loses the danger.', '‘Reminded’ is for forgetting.'],
   'Danger → warned.'),
  ('Verb', '“Remember to buy milk.” → Dad ___ me to buy milk.', ['reminded', 'remembered', 'warned', 'ordered'],
   ['‘Remembered me’ is wrong.', '‘Warned’ is for danger.', '‘Ordered’ is too strong.'],
   'Make someone remember → reminded.'),
  ('Verb', '“Get out of the car now!” → The officer ___ him to get out of the car.', ['ordered', 'invited', 'reminded', 'advised'],
   ['‘Invited’ is far too soft.', '‘Reminded’ is wrong.', '‘Advised’ is too soft.'],
   'A strong command → ordered.'),
  ],
 'mc': [
  ('Tell or say', '“Be quiet.” → The teacher ___ us to be quiet.', ['told', 'said', 'said to', 'spoke'],
   ['‘Said us’ is wrong.', '‘Said to us to be quiet’ is very unnatural.', '‘Spoke us’ is wrong.'],
   'Commands → told + person + to.'),
  ('Negative request', '“Please don’t laugh.” → She asked us ___.', ['not to laugh', 'don’t laugh', 'to don’t laugh', 'not laughing'],
   ['‘Don’t’ disappears.', '‘To don’t’ is impossible.', '‘To’ is missing.'],
   'asked + person + not to + verb.'),
  ('No backshift', '“Stop talking.” → She told them ___ talking.', ['to stop', 'to stopped', 'stopping', 'stop'],
   ['The infinitive doesn’t change.', '-ing doesn’t fit.', '‘To’ is missing.'],
   'No backshift: to stop.'),
  ('Ask to', '“Can I go to the toilet?” → Joan asked ___ to the toilet.', ['to go', 'me to go', 'go', 'if go'],
   ['That would mean Joan wanted me to go.', '‘To’ is missing.', 'Wrong structure.'],
   'Without a person: asked to go.'),
  ],
 'error': [
  ('Missing to', 'He told me *stay* at home.', 'to stay', 'Add ‘to’: ‘told me to stay’.'),
  ('Don’t in the report', 'She told us *don’t* be late.', 'not to', 'Negative: ‘told us not to be late’.'),
  ('Say + person', 'He *said* me to hurry.', 'told', 'Use ‘tell’: ‘told me to hurry’.'),
  ('Wrong verb', '“Please wait.” → She *ordered* me to wait.', 'asked', 'A polite request: ‘asked me to wait’.'),
  ],
}
