TITLE = 'Passive Reporting Structures'
AUX = (['It', 'is', 'said', 'to', 'have'], None, 'It')
NEXT = ('All about the passive', '/grammar/passive-voice/')
BODY = r'''
## How to form passive reporting structures

When we report what **people in general** say, think or believe, we can use two passive patterns.

> **Active:** People say that the castle is haunted.

| Pattern | Structure | Example |
|---|---|---|
| 1. *It* + passive + *that* | It + is said + that + clause | **It is said that** the castle is haunted. |
| 2. Subject + passive + infinitive | Subject + is said + to + infinitive | **The castle is said to be** haunted. |

Common reporting verbs: **say, think, believe, know, report, expect, consider, claim, rumour, understand**.

## Pattern 1: *It is said that…*

The easiest pattern: the second clause stays the same.

- **It is believed that** the thief escaped by car.
- **It was reported that** two people were injured.
- **It is expected that** prices will rise.

> ⚠️ Typical error: ~~Is said that the castle is haunted.~~ → English needs a subject: *It is said that…*

## Pattern 2: *He is said to…*

The subject of the second clause moves to the front, and the verb becomes an **infinitive**. Choose the infinitive by **time**.

| Time of the second action | Infinitive | Example |
|---|---|---|
| same time (now) | **to + base verb** | She **is thought to live** in Paris. |
| happening now | **to be + -ing** | He **is believed to be hiding** in the mountains. |
| earlier (past) | **to have + past participle** | The painting **is said to have been stolen** in 1990. |
| earlier, in progress | **to have been + -ing** | They **are thought to have been working** together. |

> ⚠️ Typical error: ~~He is said to steal the money last year.~~ → An earlier action needs the perfect infinitive: *He is said to have stolen the money.*

## Choosing the infinitive

### 1. Same time → simple infinitive

- People think he **is** rich. → He **is thought to be** rich.

### 2. Earlier → perfect infinitive

- People believe she **left** the country. → She **is believed to have left** the country.

> ⚠️ Typical error: ~~She is believed to left the country.~~ → *to have left.*

### 3. Past reporting verb

If the reporting verb is past, the time logic stays the same:

- People **thought** he **was** dead. → He **was thought to be** dead.
- People **believed** she **had** escaped. → She **was believed to have escaped**.

## When to use these structures

They are typical of **news, academic and formal writing**, when the source is general or unknown.

| Informal | Formal |
|---|---|
| People say he's a millionaire. | He **is said to be** a millionaire. |
| Everyone knows smoking is bad for you. | **It is known that** smoking is harmful. |

## *There is said to be…*

With *there*, use **there + passive + to be**:

- **There are said to be** wolves in these mountains.
- **There is thought to have been** a mistake.

## Common mistakes

**1. Missing *it*.** *~~Is believed that…~~* → **It is believed that…**

**2. Wrong infinitive for the past.** *~~He is thought to break the record yesterday~~* → **to have broken.**

**3. Mixing the patterns.** *~~It is said to be that…~~* / *~~He is said that he is…~~* → choose one: **It is said that he is…** or **He is said to be…**

**4. *Say* with a person object.** *~~He is said me…~~* — reporting passives don't take a person object.

**Pro tip:** if the second action happened **before** the reporting, you always need **to have + participle**.
'''

GAP = ('Fill in the gaps',
  'Type the missing part of the passive reporting structure: it, that, to, to have, or the right infinitive. Twenty original sentences.',
  [
  ('It pattern', '[[It]] is said that the old house is haunted.', 'it / there', 'English needs a subject: It is said that…'),
  ('It pattern', 'It is believed [[that]] the thieves escaped by boat.', 'that / to', 'Pattern 1: It + passive reporting verb + that + clause.'),
  ('It pattern', 'It [[is expected]] that prices will rise next year.', '(expect)', 'Present passive of the reporting verb: is expected.'),
  ('It pattern', 'It [[was reported]] that three people were injured.', '(report)', 'Past reporting verb in the passive: was reported.'),
  ('Subject pattern', 'The castle is said [[to be]] over 800 years old.', 'to be / being', 'Same time as the reporting: to + base verb, to be.'),
  ('Subject pattern', 'She is thought [[to live]] somewhere in Paris.', '(live)', 'A present situation: simple infinitive, to live.'),
  ('Subject pattern', 'The singer is believed [[to be]] very rich.', 'to be / to have', 'A present state: to be.'),
  ('Subject pattern', 'He is known [[to speak]] six languages.', '(speak)', 'A general present fact: to speak.'),
  ('Continuous', 'The escaped prisoner is believed [[to be hiding]] in the woods.', '(hide)', 'Happening now: to be + -ing, to be hiding.'),
  ('Continuous', 'The two companies are said [[to be planning]] a merger.', '(plan)', 'In progress now: to be planning.'),
  ('Perfect', 'The painting is said [[to have been]] stolen in 1990.', 'to have been / to be', 'An earlier passive action: to have been + participle.'),
  ('Perfect', 'She is believed [[to have left]] the country last week.', '(leave)', 'An earlier action: to have + left.'),
  ('Perfect', 'The fire is thought [[to have started]] in the kitchen.', '(start)', 'An earlier action: perfect infinitive, to have started.'),
  ('Perfect', 'The thief is reported [[to have escaped]] through a window.', '(escape)', 'Before the report: to have escaped.'),
  ('Past reporting', 'He was thought [[to be]] dead, but he was alive.', 'to be / to have been', 'Same time as ‘was thought’: to be.'),
  ('Past reporting', 'The ship was believed [[to have sunk]] in a storm.', '(sink)', 'Earlier than the belief: to have sunk.'),
  ('There', '[[There]] are said to be wolves in these mountains.', 'there / it', 'With ‘there’: There are said to be…'),
  ('There', 'There is thought [[to have been]] a mistake in the results.', 'to have been / to be', 'An earlier situation with ‘there’: to have been.'),
  ('Perfect continuous', 'They are thought [[to have been working]] together for years.', '(work)', 'Earlier and in progress: to have been + -ing.'),
  ('Reporting verb', 'Smoking [[is known]] to cause serious illness.', '(know)', 'Present passive of the reporting verb: is known.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 formal passive reports with both patterns.',
  [
  ('It pattern', 'It is said that he is rich.', []),
  ('It pattern', 'It is believed that she lied.', []),
  ('It pattern', 'It was reported that two died.', []),
  ('It pattern', 'It is expected that prices will rise.', []),
  ('It pattern', 'It is thought that the fire was deliberate.', []),
  ('Subject pattern', 'He is said to be rich.', []),
  ('Subject pattern', 'She is thought to live abroad.', []),
  ('Subject pattern', 'The house is said to be haunted.', []),
  ('Subject pattern', 'He is known to like jazz.', []),
  ('Continuous', 'He is believed to be hiding.', []),
  ('Continuous', 'They are said to be negotiating.', []),
  ('Perfect', 'She is believed to have lied.', []),
  ('Perfect', 'The thief is thought to have escaped.', []),
  ('Perfect', 'The ring is said to have been stolen.', []),
  ('Past reporting', 'He was thought to be dead.', []),
  ('Past reporting', 'She was believed to have drowned.', []),
  ('There', 'There are said to be bears here.', []),
  ('There', 'There is thought to have been an error.', []),
  ('Reporting verb', 'Exercise is known to reduce stress.', []),
  ('Perfect continuous', 'They are thought to have been spying.', []),
  ])

MATCH = {'title': 'Match the two patterns', 'subtitle': 'Tap a sentence with ‘It is said that…’, then tap the same idea with the subject + to-infinitive.',
  'leftLabel': 'It … that', 'rightLabel': 'Subject … to', 'rightLabelSub': '(infinitive)', 'reviewArrowPrefix': '',
  'pairs': [
  ('It is said that he is rich.', 'He is said to be rich.'), ('It is thought that she lives in Rome.', 'She is thought to live in Rome.'),
  ('It is believed that he is hiding.', 'He is believed to be hiding.'), ('It is said that they left.', 'They are said to have left.'),
  ('It is known that he speaks Russian.', 'He is known to speak Russian.'), ('It is reported that she resigned.', 'She is reported to have resigned.'),
  ('It is thought that the fire started here.', 'The fire is thought to have started here.'), ('It is said that the house is haunted.', 'The house is said to be haunted.'),
  ('It is believed that the ship sank.', 'The ship is believed to have sunk.'), ('It is expected that he will win.', 'He is expected to win.'),
  ('It was thought that he was dead.', 'He was thought to be dead.'), ('It was believed that she had escaped.', 'She was believed to have escaped.'),
  ('It is said that they are planning a strike.', 'They are said to be planning a strike.'), ('It is thought that the painting was stolen.', 'The painting is thought to have been stolen.'),
  ('It is known that smoking kills.', 'Smoking is known to kill.'), ('It is said that she earns millions.', 'She is said to earn millions.'),
  ('It is believed that they have been working together.', 'They are believed to have been working together.'), ('It is reported that the minister is ill.', 'The minister is reported to be ill.'),
  ('It is claimed that he cheated.', 'He is claimed to have cheated.'), ('It is understood that she is leaving.', 'She is understood to be leaving.'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. It is said that… or Subject is said to… — and to have + participle for earlier actions.',
  [
  ('It pattern', '___ is said that the president will resign.', ['It', 'There', 'He', 'That'],
   ['‘There is said that’ is wrong: ‘there’ goes with ‘to be’, not ‘that’.', '‘He is said that’ mixes the two patterns.', '‘That is said that’ is wrong.'],
   'Pattern 1 needs ‘It’ as the subject: It is said that…'),
  ('Subject pattern', 'The singer is said ___ very generous.', ['to be', 'that he is', 'being', 'be'],
   ['‘Is said that he is’ mixes the two patterns.', '‘Is said being’ is wrong; the pattern needs an infinitive.', 'The infinitive needs ‘to’.'],
   'Same-time situation: subject + is said + to be.'),
  ('Perfect', 'The thief is believed ___ the country yesterday.', ['to have left', 'to leave', 'to be leaving', 'leaving'],
   ['‘To leave’ is for the same time, but ‘yesterday’ is earlier.', '‘To be leaving’ means right now.', 'The pattern needs a to-infinitive.'],
   'An earlier action: to have + past participle.'),
  ('Continuous', 'The two leaders are thought ___ a deal at this moment.', ['to be discussing', 'to discuss', 'to have discussed', 'discussing'],
   ['‘To discuss’ is the simple infinitive; ‘at this moment’ needs the continuous.', '‘To have discussed’ is an earlier action.', 'The pattern needs a to-infinitive.'],
   'Happening now: to be + -ing.'),
  ('Perfect passive', 'The painting is said ___ by a servant in 1920.', ['to have been stolen', 'to have stolen', 'to be stolen', 'to steal'],
   ['‘To have stolen’ is active: the painting stole something.', '‘To be stolen’ is not about 1920.', '‘To steal’ is active and wrong in time.'],
   'Earlier and passive: to have been + past participle.'),
  ('Past reporting', 'For years, he was thought ___ dead.', ['to be', 'to have', 'that he was', 'being'],
   ['‘To have dead’ is wrong.', '‘Was thought that he was’ mixes the patterns.', 'The pattern needs a to-infinitive.'],
   'Same time as the past belief: to be.'),
  ('There', '___ are said to be ghosts in the castle.', ['There', 'It', 'They', 'That'],
   ['‘It are said’ is wrong.', '‘They are said to be ghosts’ means the people are ghosts.', '‘That are said’ is wrong.'],
   'Existence: There + passive + to be.'),
  ('Mixing', 'Which sentence is correct?', ['It is believed that he is guilty.', 'It is believed him to be guilty.', 'He is believed that he is guilty.', 'Is believed that he is guilty.'],
   ['This mixes the two patterns.', 'This mixes the two patterns.', 'A subject is missing.'],
   'Pattern 1: It is believed that + clause.'),
  ('Mixing', 'Which sentence is correct?', ['She is said to earn a fortune.', 'She is said that she earns a fortune.', 'It is said her to earn a fortune.', 'She is said earn a fortune.'],
   ['This mixes the two patterns.', 'This mixes the two patterns.', 'The infinitive needs ‘to’.'],
   'Pattern 2: subject + is said + to-infinitive.'),
  ('Reporting verb', 'Exercise ___ to improve your mood.', ['is known', 'knows', 'is knowing', 'known'],
   ['Exercise can’t know: use the passive.', '‘Know’ isn’t used in the continuous.', '‘Is’ is missing.'],
   'Passive reporting verb: is known to…'),
  ('Perfect', 'The fire is thought ___ in the kitchen.', ['to have started', 'to start', 'to be starting', 'that started'],
   ['The fire has already happened: perfect infinitive.', 'It isn’t happening now.', '‘Is thought that started’ is wrong.'],
   'Earlier action: to have started.'),
  ('Simple', 'He is known ___ eight languages.', ['to speak', 'to have spoken', 'speaking', 'that speaks'],
   ['He still speaks them: simple infinitive.', 'The pattern needs a to-infinitive.', '‘Is known that speaks’ is wrong.'],
   'A present fact: to + base verb.'),
  ('Register', 'Where are these structures most common?', ['news reports and formal writing', 'text messages', 'chatting with friends', 'children’s songs'],
   ['They sound too formal for texts.', 'In conversation we say ‘People say…’.', 'They’re too formal for children’s songs.'],
   'Passive reporting is typical of news and academic English.'),
  ('Perfect continuous', 'They are believed ___ together for years before they were caught.', ['to have been working', 'to work', 'to be working', 'to have work'],
   ['‘To work’ is the same time, not earlier.', '‘To be working’ is now.', 'After ‘have’ use the participle.'],
   'Earlier and in progress: to have been + -ing.'),
  ('Future', 'The new law is expected ___ next year.', ['to come into force', 'that comes into force', 'coming into force', 'to have come into force'],
   ['Mixing patterns.', 'The pattern needs a to-infinitive.', 'The perfect is for earlier actions, not the future.'],
   'With ‘expect’, a simple infinitive often refers to the future.'),
  ('It pattern', 'It ___ that the company lost €2 million last year.', ['is reported', 'reports', 'is reporting', 'reported'],
   ['‘It reports’ means something reports.', '‘Is reporting’ is active continuous.', '‘It reported’ is active.'],
   'Pattern 1: It is reported that…'),
  ('Past reporting', 'The ship was believed ___ in the storm, but it was found.', ['to have sunk', 'to sink', 'to be sinking', 'to have sank'],
   ['The sinking was earlier than the belief.', 'Not happening at that moment.', 'The participle is ‘sunk’, not ‘sank’.'],
   'Earlier than a past belief: to have + participle.'),
  ('There', 'There is thought ___ a mistake in the calculations.', ['to have been', 'to have', 'that is', 'being'],
   ['‘To have a mistake’ changes the meaning.', 'Mixing patterns.', 'The pattern needs a to-infinitive.'],
   'Earlier existence: There is thought to have been…'),
  ('Subject pattern', 'The minister is reported ___ ill.', ['to be', 'that is', 'being', 'to being'],
   ['Mixing patterns.', 'The pattern needs a to-infinitive.', '‘To being’ is wrong.'],
   'Same time: is reported to be.'),
  ('Perfect', 'The athlete is claimed ___ drugs before the race.', ['to have taken', 'to take', 'to be taking', 'that took'],
   ['The race is over: perfect infinitive.', 'Not happening now.', 'Mixing patterns.'],
   'Earlier action: to have taken.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('Missing it', '*Is* said that the castle is haunted.', 'It is', 'English needs a subject: ‘It is said that…’.'),
  ('Wrong infinitive', 'He is said to *steal* the money last year.', 'have stolen', 'An earlier action needs the perfect infinitive: ‘to have stolen’.'),
  ('Wrong infinitive', 'She is believed to *left* the country.', 'have left', 'Perfect infinitive: ‘to have left’.'),
  ('Wrong infinitive', 'The fire is thought to *started* in the kitchen.', 'have started', 'Perfect infinitive: ‘to have started’.'),
  ('Wrong participle', 'The ship is believed to have *sank*.', 'sunk', 'Participle of ‘sink’: ‘sunk’.'),
  ('Wrong participle', 'The ring is said to have been *stole*.', 'stolen', 'Participle of ‘steal’: ‘stolen’.'),
  ('Missing to', 'He is known *speak* six languages.', 'to speak', 'Pattern 2 needs ‘to’: ‘is known to speak’.'),
  ('Missing to', 'She is said *be* very kind.', 'to be', 'Pattern 2 needs ‘to’: ‘is said to be’.'),
  ('-ing instead of infinitive', 'He is believed *hiding* in the forest.', 'to be hiding', 'Continuous infinitive: ‘to be hiding’.'),
  ('Active verb', 'The president *says* to be ill.', 'is said', 'Passive: ‘The president is said to be ill’.'),
  ('Active verb', 'Smoking *knows* to cause cancer.', 'is known', 'Passive: ‘Smoking is known to cause cancer’.'),
  ('Wrong be', 'The paintings *is* thought to be fakes.', 'are', 'Plural: ‘are thought’.'),
  ('Wrong be', 'They *was* believed to be lost.', 'were', 'Plural: ‘were believed’.'),
  ('There or it', '*It* are said to be wolves in this forest.', 'There', 'Existence: ‘There are said to be wolves’.'),
  ('There or it', '*There* is believed that he escaped.', 'It', 'Pattern 1 uses ‘It’: ‘It is believed that…’.'),
  ('Wrong tense', 'It *is* reported yesterday that two people died.', 'was', 'Yesterday → ‘It was reported…’.'),
  ('Wrong participle', 'It is *thinked* that prices will fall.', 'thought', 'Participle of ‘think’: ‘thought’.'),
  ('Wrong participle', 'It is *knew* that she lied.', 'known', 'Participle of ‘know’: ‘known’.'),
  ('Wrong form', 'They are thought to have been *work* together.', 'working', 'Perfect continuous: ‘to have been working’.'),
  ('Spelling', 'It is *beleived* that he is innocent.', 'believed', 'Spelling: ‘believed’ (i before e).'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, which infinitive, multiple choice and spot-the-mistake. In the typing questions write it / there / that or the correct to-infinitive. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('infinitive', 'Which infinitive?'),
 'fill': [
  ('It pattern', '[[It]] is thought that the bridge is unsafe.', 'it / there', 'Pattern 1 needs ‘It’ as the subject of the passive verb.', 'Start with ‘It’.'),
  ('Subject pattern', 'The actress is said [[to be]] very shy.', 'to be / being', 'A present state at the same time: to be.', 'Same time → to + base verb.'),
  ('Perfect', 'The thief is believed [[to have escaped]] by car.', 'escape', 'The escape happened earlier: to have + participle.', 'Earlier → to have + participle.'),
  ('Continuous', 'The rebels are thought [[to be hiding]] in the hills.', 'hide', 'In progress now: to be + -ing.', 'Now → to be + -ing.'),
  ],
 'order': [
  ('It pattern', 'It is said that he lied.', []),
  ('Subject pattern', 'He is said to be rich.', []),
  ('Perfect', 'She is thought to have left.', []),
  ('There', 'There are said to be bears.', []),
  ],
 'customItems': [
  ('Infinitive', 'People think he lives in Berlin. → He is thought ___ in Berlin.', ['to live', 'to have lived', 'to be living', 'living'],
   ['‘To have lived’ is for an earlier action.', 'Possible, but a permanent fact uses the simple form.', 'The pattern needs a to-infinitive.'],
   'Same time, permanent → to live.'),
  ('Infinitive', 'People think he lived in Berlin in the 1990s. → He is thought ___ in Berlin.', ['to have lived', 'to live', 'to be living', 'lived'],
   ['‘To live’ is for the same time.', '‘To be living’ is now.', 'The pattern needs a to-infinitive.'],
   'Earlier → to have lived.'),
  ('Infinitive', 'People think he is living in a hotel right now. → He is thought ___ in a hotel.', ['to be living', 'to have lived', 'to live', 'living'],
   ['That’s an earlier action.', 'Possible, but ‘right now’ suggests the continuous.', 'The pattern needs a to-infinitive.'],
   'Now, in progress → to be living.'),
  ('Infinitive', 'People think the house was built in 1600. → The house is thought ___ in 1600.', ['to have been built', 'to have built', 'to be built', 'to build'],
   ['Active: the house built something.', 'Not about 1600.', 'Active and wrong in time.'],
   'Earlier + passive → to have been built.'),
  ],
 'mc': [
  ('It pattern', '___ is expected that the strike will end soon.', ['It', 'There', 'That', 'He'],
   ['‘There is expected that’ is wrong.', '‘That is expected that’ is wrong.', '‘He is expected that’ mixes patterns.'],
   'Pattern 1: It is expected that…'),
  ('Perfect', 'The pilot is reported ___ the plane safely.', ['to have landed', 'to land', 'landing', 'that landed'],
   ['The landing has already happened.', 'The pattern needs a to-infinitive.', 'Mixing patterns.'],
   'Earlier → to have landed.'),
  ('There', '___ is said to be treasure under the church.', ['There', 'It', 'They', 'That'],
   ['‘It is said to be treasure’ means ‘it’ is treasure.', '‘They is’ is wrong.', '‘That is said’ is wrong.'],
   'Existence → There is said to be…'),
  ('Reporting verb', 'Coffee ___ to keep you awake.', ['is known', 'knows', 'is knowing', 'knew'],
   ['Coffee can’t know.', '‘Know’ isn’t used in the continuous.', 'Active past is wrong.'],
   'Passive reporting: is known to…'),
  ],
 'error': [
  ('Missing it', '*Is* reported that he resigned.', 'It is', 'Add the subject: ‘It is reported that…’.'),
  ('Wrong infinitive', 'She is thought to *escape* last night.', 'have escaped', 'Earlier action: ‘to have escaped’.'),
  ('Missing to', 'He is believed *be* in Spain.', 'to be', 'Pattern 2 needs ‘to’: ‘to be’.'),
  ('There or it', '*It* is thought to be a problem with the engine.', 'There', 'Existence: ‘There is thought to be a problem’.'),
  ],
}

QUIZ_COMMON = {10: [('believes', 'It doesn’t believe anything: use the passive ‘is believed’.'), ('is believe', 'After ‘is’ use the participle: ‘believed’.')],
               12: [('is said be', 'Don’t forget ‘to’: ‘is said to be’.'), ('says to be', 'Use the passive: ‘is said to be’.')]}
