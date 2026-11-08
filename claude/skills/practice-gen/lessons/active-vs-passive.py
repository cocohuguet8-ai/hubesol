TITLE = 'Active vs Passive'
AUX = (['is', 'are', 'was', 'were', 'by'], None, 'was')
NEXT = ('The Passive in All Tenses', '/grammar/passive-voice/passive-all-tenses/')
BODY = r'''
## How to change active into passive

| Step | Active | Passive |
|---|---|---|
| 1. The **object** becomes the subject | Gaudí designed **the park**. | **The park** … |
| 2. Add **be** in the same tense | (past simple) | … **was** … |
| 3. Add the **past participle** | designed | … **designed** … |
| 4. Add **by** + agent (only if useful) | Gaudí | … **by Gaudí**. |

**Active:** Gaudí designed the park. → **Passive:** The park **was designed by** Gaudí.

The tense stays the same: only *be* changes to show it.

| Tense | Active | Passive |
|---|---|---|
| present simple | They **sell** books here. | Books **are sold** here. |
| past simple | Someone **stole** my bag. | My bag **was stolen**. |

## Only verbs with an object

Only **transitive** verbs (verbs with an object) can be passive.

| ✓ Has an object | ✗ No object |
|---|---|
| They **built** a bridge. → A bridge was built. | She **arrived** late. → ~~She was arrived.~~ |
| He **broke** the vase. → The vase was broken. | It **happened** yesterday. → ~~It was happened.~~ |

> ⚠️ Typical error: ~~The accident was happened at night.~~ → *Happen* has no object: *The accident happened at night.*

## When to choose the active

### 1. The person doing the action is important

- **My sister** painted this picture.
- **Barça** won the match.

> ⚠️ Typical error: ~~The match was won by Barça~~ (in normal conversation about your team) → Usually fine, but the active sounds more direct: *Barça won the match.*

### 2. Normal conversation

Most everyday English is active: it's shorter and clearer.

## When to choose the passive

### 1. The doer is unknown, obvious or unimportant

- My phone **was stolen**. (we don't know who)
- The thief **was arrested**. (obviously by the police)

> ⚠️ Typical error: ~~Someone stole my phone by a thief.~~ → Use the passive and drop the obvious agent: *My phone was stolen.*

### 2. Formal writing, news and science

- The results **were published** yesterday.
- The mixture **is heated** for ten minutes.

### 3. To keep the topic at the start

- *The Mona Lisa* is very famous. It **was painted by** Leonardo da Vinci.

## Subject and object pronouns

When the object is a pronoun, it changes to a **subject** pronoun in the passive.

| Active | Passive |
|---|---|
| They invited **me**. | **I** was invited. |
| Someone helped **us**. | **We** were helped. |
| The teacher told **them**. | **They** were told. |

> ⚠️ Typical error: ~~Me was invited.~~ → *I was invited.*

## Common mistakes

**1. Passive with verbs that have no object.** *~~She was died~~* → **She died.**

**2. Changing the tense.** *~~They built it → It is built~~* → **It was built.**

**3. Object pronoun as subject.** *~~Him was chosen~~* → **He was chosen.**

**4. Keeping an unnecessary agent.** *~~It was stolen by someone~~* → **It was stolen.**

**Pro tip:** before making a passive, find the object of the active sentence — if there isn't one, the passive is impossible.
'''

GAP = ('Fill in the gaps',
  'Complete the passive version of each idea: is / are / was / were + past participle. Keep the same tense as the active. Twenty original sentences.',
  [
  ('Present', 'They sell newspapers here. → Newspapers [[are sold]] here.', '(sell)', 'Active present simple → passive: are + sold.'),
  ('Present', 'People speak Catalan in Andorra. → Catalan [[is spoken]] in Andorra.', '(speak)', 'Same tense (present): is + spoken.'),
  ('Present', 'The school cleans the classrooms every day. → The classrooms [[are cleaned]] every day.', '(clean)', 'Plural new subject, present: are cleaned.'),
  ('Present', 'They don’t allow dogs. → Dogs [[aren’t allowed]].', '(not allow)', 'Negative present passive: aren’t + allowed.'),
  ('Past', 'Someone stole my bike. → My bike [[was stolen]].', '(steal)', 'Active past simple → was + stolen; drop ‘someone’.'),
  ('Past', 'Gaudí designed Park Güell. → Park Güell [[was designed]] by Gaudí.', '(design)', 'Past simple → was designed, and the agent is important.'),
  ('Past', 'The storm destroyed three houses. → Three houses [[were destroyed]].', '(destroy)', 'Plural new subject, past: were destroyed.'),
  ('Past', 'They invited me to the wedding. → [[I]] was invited to the wedding.', 'I / me', 'The object ‘me’ becomes the subject ‘I’.'),
  ('Past', 'Someone helped us. → [[We]] were helped.', 'we / us', 'Object pronoun ‘us’ → subject pronoun ‘we’.'),
  ('Past', 'The police caught the thieves. → The thieves [[were caught]].', '(catch)', 'The agent is obvious, so leave it out: were caught.'),
  ('Past', 'Picasso painted Guernica. → Guernica [[was painted]] by Picasso.', '(paint)', 'Past simple → was painted by Picasso.'),
  ('Past', 'They didn’t cancel the match. → The match [[wasn’t cancelled]].', '(not cancel)', 'Negative past passive: wasn’t + cancelled.'),
  ('No object', 'The accident [[happened]] at midnight.', '(happen)', '‘Happen’ has no object, so it can’t be passive: happened.'),
  ('No object', 'My grandmother [[died]] in 2019.', '(die)', '‘Die’ has no object: always active, ‘died’.'),
  ('No object', 'The train [[arrived]] late.', '(arrive)', '‘Arrive’ has no object: active only.'),
  ('Choice', 'My sister [[painted]] this picture. I’m so proud of her!', '(paint)', 'The person is important, so the active is natural: painted.'),
  ('Choice', 'Breakfast [[is served]] from 7 to 10.', '(serve)', 'Who serves it doesn’t matter: present passive, is served.'),
  ('Choice', 'Our team [[won]] the cup last night!', '(win)', 'In conversation about your team, the active is direct: won.'),
  ('Choice', 'The results [[were published]] yesterday.', '(publish)', 'Formal news style, doer unimportant: were published.'),
  ('Agent', 'The book was translated [[by]] my uncle.', 'by / from', 'The agent is introduced with ‘by’.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 10 active and 10 passive, so you see both forms side by side.',
  [
  ('Active', 'Someone stole my wallet.', []),
  ('Passive', 'My wallet was stolen.', []),
  ('Active', 'Gaudí designed this house.', []),
  ('Passive', 'This house was designed by Gaudí.', []),
  ('Active', 'They speak English here.', []),
  ('Passive', 'English is spoken here.', []),
  ('Active', 'The storm damaged the roof.', []),
  ('Passive', 'The roof was damaged.', []),
  ('Active', 'They invited us to dinner.', []),
  ('Passive', 'We were invited to dinner.', []),
  ('Active', 'The police arrested two men.', []),
  ('Passive', 'Two men were arrested.', []),
  ('Active', 'My dad cooks dinner every night.', []),
  ('Passive', 'Dinner is cooked every night.', []),
  ('Active', 'They didn’t tell me.', []),
  ('Passive', 'I wasn’t told.', []),
  ('No object', 'The accident happened yesterday.', []),
  ('No object', 'She arrived very late.', []),
  ('Active', 'My brother broke the window.', []),
  ('Passive', 'The window was broken.', []),
  ])

MATCH = {'title': 'Match the active and passive', 'subtitle': 'Tap an active sentence, then tap the passive sentence that means the same.',
  'leftLabel': 'Active', 'rightLabel': 'Passive', 'rightLabelSub': '(be + participle)', 'reviewArrowPrefix': '',
  'pairs': [
  ('Someone stole my bike.', 'My bike was stolen.'), ('They speak French here.', 'French is spoken here.'), ('Picasso painted it.', 'It was painted by Picasso.'),
  ('They built the bridge in 1890.', 'The bridge was built in 1890.'), ('They invited me.', 'I was invited.'), ('The police caught him.', 'He was caught.'),
  ('They make cars here.', 'Cars are made here.'), ('Someone broke the window.', 'The window was broken.'), ('They told us the news.', 'We were told the news.'),
  ('They clean the room daily.', 'The room is cleaned daily.'), ('They cancelled the flight.', 'The flight was cancelled.'), ('They grow rice in Valencia.', 'Rice is grown in Valencia.'),
  ('Someone found my keys.', 'My keys were found.'), ('They chose her as captain.', 'She was chosen as captain.'), ('They sell tickets online.', 'Tickets are sold online.'),
  ('A dog bit him.', 'He was bitten by a dog.'), ('They didn’t pay us.', 'We weren’t paid.'), ('They serve lunch at one.', 'Lunch is served at one.'),
  ('The storm destroyed the crops.', 'The crops were destroyed.'), ('They don’t allow phones.', 'Phones aren’t allowed.'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Keep the tense, make the object the subject, add be + past participle.',
  [
  ('Present', 'They grow oranges in Valencia. → Oranges ___ in Valencia.', ['are grown', 'is grown', 'were grown', 'grow'],
   ['‘Oranges’ is plural, so ‘be’ must be ‘are’.', 'The active is present simple, so the passive stays present, not past.', '‘Oranges grow’ is active and changes the focus of the sentence.'],
   'Same tense, plural subject: are + grown.'),
  ('Past', 'Someone broke the window. → The window ___.', ['was broken', 'is broken', 'broke', 'was broke'],
   ['The active is past simple, so the passive must be past: was.', '‘The window broke’ is active and loses the idea that someone did it.', '‘Broke’ is past simple; the passive needs the participle ‘broken’.'],
   'Past simple active → was + broken.'),
  ('Pronoun', 'They chose me for the team. → ___ was chosen for the team.', ['I', 'Me', 'My', 'Mine'],
   ['‘Me’ is an object pronoun; the subject must be ‘I’.', '‘My’ is a possessive adjective.', '‘Mine’ is a possessive pronoun.'],
   'The object ‘me’ becomes the subject ‘I’ in the passive.'),
  ('Pronoun', 'Someone told us the truth. → ___ were told the truth.', ['We', 'Us', 'Our', 'Ours'],
   ['‘Us’ is an object pronoun.', '‘Our’ is a possessive adjective.', '‘Ours’ is a possessive pronoun.'],
   'Object ‘us’ → subject ‘we’.'),
  ('No object', 'Which verb can’t be made passive?', ['happen', 'build', 'steal', 'write'],
   ['‘Build’ has an object: a house was built.', '‘Steal’ has an object: a car was stolen.', '‘Write’ has an object: a letter was written.'],
   '‘Happen’ has no object, so a passive like ‘was happened’ is impossible.'),
  ('No object', 'The accident ___ at 8 p.m.', ['happened', 'was happened', 'is happened', 'were happened'],
   ['‘Happen’ can’t be passive.', '‘Happen’ can’t be passive.', '‘Happen’ can’t be passive.'],
   'Verbs without an object stay active: the accident happened.'),
  ('Agent', 'Leonardo painted the Mona Lisa. → The Mona Lisa was painted ___ Leonardo.', ['by', 'from', 'of', 'with'],
   ['‘From’ is a common error for the agent.', '‘Of’ isn’t used for the agent.', '‘With’ is for the instrument.'],
   'Agent: by + person.'),
  ('Agent needed?', 'The police arrested the thief. → Which passive is best?', ['The thief was arrested.', 'The thief was arrested by the police.', 'The thief arrested.', 'The thief is arrested by them.'],
   ['Correct, but ‘by the police’ is obvious and unnecessary.', 'This is active and wrong in meaning.', 'Wrong tense and an unclear agent.'],
   'Drop the obvious agent: The thief was arrested.'),
  ('Tense', 'They built this castle in 1300. → This castle ___ in 1300.', ['was built', 'is built', 'has built', 'built'],
   ['The tense must stay past.', '‘Has built’ is active present perfect.', '‘Built’ alone is active.'],
   'Past active → past passive: was built.'),
  ('Tense', 'They clean the beach every morning. → The beach ___ every morning.', ['is cleaned', 'was cleaned', 'cleans', 'is clean'],
   ['The active is present, so the passive is present.', 'A beach can’t clean.', '‘Is clean’ is an adjective, not the passive.'],
   'Present active → present passive: is cleaned.'),
  ('Negative', 'They didn’t invite Pau. → Pau ___.', ['wasn’t invited', 'didn’t invite', 'didn’t invited', 'isn’t invited'],
   ['‘Didn’t invite’ is active.', 'Passive negatives use ‘be’, not ‘did’.', 'The tense must stay past.'],
   'Negative past passive: wasn’t invited.'),
  ('Choice', 'Which sentence sounds more natural in conversation?', ['My mum made this cake.', 'This cake was made by my mum.', 'This cake made my mum.', 'My mum was made this cake.'],
   ['Correct, but in conversation the active is more direct.', 'This changes the meaning completely.', 'This is grammatically wrong.'],
   'When the person matters, the active is usually more natural.'),
  ('Choice', 'Which sentence is best for a news report?', ['Two climbers were rescued yesterday.', 'Someone rescued two climbers yesterday.', 'Two climbers rescued yesterday.', 'Two climbers was rescued yesterday.'],
   ['‘Someone’ is vague; the passive is more natural in news.', '‘Be’ is missing.', '‘Climbers’ is plural: were.'],
   'News focuses on what happened: the passive.'),
  ('Present', 'They don’t allow pets. → Pets ___.', ['aren’t allowed', 'don’t allow', 'isn’t allowed', 'weren’t allowed'],
   ['‘Pets don’t allow’ changes the meaning.', '‘Pets’ is plural: aren’t.', 'The tense must stay present.'],
   'Negative present passive: aren’t allowed.'),
  ('Past', 'A dog bit my brother. → My brother ___ by a dog.', ['was bitten', 'was bit', 'bit', 'is bitten'],
   ['‘Bit’ is past simple; use the participle ‘bitten’.', '‘My brother bit’ is active.', 'The tense must stay past.'],
   'Irregular participle: bite → bitten.'),
  ('Pronoun', 'They saw him at the station. → ___ was seen at the station.', ['He', 'Him', 'His', 'He’s'],
   ['‘Him’ is an object pronoun.', '‘His’ is possessive.', '‘He’s’ = he is.'],
   'Object ‘him’ → subject ‘he’.'),
  ('No object', 'Which sentence is correct?', ['My grandfather died last year.', 'My grandfather was died last year.', 'My grandfather is died last year.', 'My grandfather were died last year.'],
   ['‘Die’ can’t be passive.', '‘Die’ can’t be passive.', '‘Die’ can’t be passive.'],
   '‘Die’ has no object: always active.'),
  ('Topic', 'Rome is very old. It ___ thousands of years ago.', ['was founded', 'founded', 'is founded', 'was found'],
   ['‘It founded’ means Rome founded something.', 'The tense must be past.', '‘Found’ is the participle of ‘find’; we need ‘founded’.'],
   'Keep the topic (Rome) as subject: was founded.'),
  ('Present', 'People use this app all over the world. → This app ___ all over the world.', ['is used', 'uses', 'are used', 'is using'],
   ['An app can’t use: the passive.', '‘This app’ is singular: is.', '‘Is using’ is active continuous.'],
   'Present passive: is used.'),
  ('Past', 'They found the missing boy. → The missing boy ___.', ['was found', 'was founded', 'found', 'is found'],
   ['‘Founded’ is from ‘found’ (to start); here it’s ‘find’ → found.', '‘The boy found’ is active.', 'The tense must stay past.'],
   'Past passive: was found.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('No passive with happen', 'The accident *happen* at night last week.', 'happened', '‘Happen’ has no object and stays active: ‘happened’.'),
  ('No passive with die', 'My grandmother *die* in 2010.', 'died', 'Active past simple: ‘died’ — ‘die’ is never passive.'),
  ('No passive with arrive', 'The plane *arrive* on time yesterday.', 'arrived', 'Active past simple: ‘arrived’ — ‘arrive’ is never passive.'),
  ('Object pronoun', '*Me* was invited to the party.', 'I', 'Subject pronoun: ‘I was invited’.'),
  ('Object pronoun', '*Us* were told to wait.', 'We', 'Subject pronoun: ‘We were told’.'),
  ('Object pronoun', '*Him* was chosen as captain.', 'He', 'Subject pronoun: ‘He was chosen’.'),
  ('Wrong tense', 'They built it in 1900. It *is* built in 1900.', 'was', 'Keep the past: ‘It was built’.'),
  ('Wrong tense', 'Someone stole my phone. My phone *is* stolen yesterday.', 'was', 'Past: ‘was stolen’.'),
  ('Missing be', 'The thieves *caught* last night.', 'were caught', 'Passive needs ‘be’: ‘were caught’.'),
  ('Wrong be', 'The windows *was* cleaned.', 'were', 'Plural: ‘were’.'),
  ('Wrong participle', 'He was *bit* by a dog.', 'bitten', 'Participle of ‘bite’: ‘bitten’.'),
  ('Wrong participle', 'The castle was *builded* in 1300.', 'built', 'Participle of ‘build’: ‘built’.'),
  ('Wrong agent preposition', 'It was written *from* Cervantes.', 'by', 'Agent: ‘by’.'),
  ('Wrong agent preposition', 'This park was designed *for* Gaudí.', 'by', 'Agent: ‘designed by Gaudí’.'),
  ('Wrong negative', 'Pau *didn’t* invited.', 'wasn’t', 'Negative passive: ‘Pau wasn’t invited’.'),
  ('Wrong negative', 'Dogs *don’t* allowed here.', 'aren’t', 'Negative passive: ‘Dogs aren’t allowed’.'),
  ('Active form', 'My bag *stole* on the train.', 'was stolen', 'A bag can’t steal: ‘was stolen’.'),
  ('Active form', 'This cake *made* by my mum.', 'was made', 'Passive: ‘was made’.'),
  ('Found or founded', 'Barcelona was *found* by the Romans.', 'founded', '‘Found’ (start a city) → ‘founded’.'),
  ('Spelling', 'The results were *publised* today.', 'published', 'Spelling: ‘published’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, active or passive, multiple choice and spot-the-mistake. In the typing questions write the passive (be + past participle) or the active when the verb has no object. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('choice', 'Active or passive'),
 'fill': [
  ('Past', 'Someone took my umbrella. → My umbrella [[was taken]].', 'take', 'Past active → was + taken; drop ‘someone’.', 'Past passive: was + participle.'),
  ('Present', 'They make violins here. → Violins [[are made]] here.', 'make', 'Present active → are + made.', 'Plural present → are + participle.'),
  ('Pronoun', 'They told me. → [[I]] was told.', 'I / me', 'Object ‘me’ → subject ‘I’ in the passive.', 'Use the subject pronoun.'),
  ('No object', 'The concert [[started]] at nine.', 'start', '‘Start’ has no object here: active, started.', 'No object → active.'),
  ],
 'order': [
  ('Passive', 'The car was repaired.', []),
  ('Active', 'My dad repaired the car.', []),
  ('Passive', 'We were invited.', []),
  ('No object', 'The match ended late.', []),
  ],
 'customItems': [
  ('Choice', 'You want to say who made it: ‘___ this necklace.’', ['My grandma made', 'This necklace was made', 'This necklace made', 'My grandma was made'],
   ['The passive hides the person you want to mention.', 'This is active with the wrong meaning.', 'This changes the meaning completely.'],
   'The person is important → active.'),
  ('Choice', 'You don’t know who did it: ‘My car ___ last night.’', ['was stolen', 'stole', 'is stealing', 'was stole'],
   ['A car can’t steal.', 'Wrong tense and meaning.', '‘Stole’ is past simple; use ‘stolen’.'],
   'Unknown doer → passive.'),
  ('Choice', 'Which verb must stay active?', ['arrive', 'send', 'build', 'sell'],
   ['‘Send’ can be passive.', '‘Build’ can be passive.', '‘Sell’ can be passive.'],
   '‘Arrive’ has no object, so no passive.'),
  ('Choice', 'A science report: ‘The water ___ to 80 °C.’', ['was heated', 'heated', 'we heated it', 'was heat'],
   ['‘The water heated’ is unclear in a report.', 'Reports usually avoid ‘we’.', 'After ‘was’ use the participle.'],
   'Science style → passive.'),
  ],
 'mc': [
  ('Tense', 'They sell stamps here. → Stamps ___ here.', ['are sold', 'were sold', 'sold', 'is sold'],
   ['The tense must stay present.', '‘Stamps sold’ is active.', '‘Stamps’ is plural.'],
   'Present passive: are sold.'),
  ('Pronoun', 'They helped her. → ___ was helped.', ['She', 'Her', 'Hers', 'She’s'],
   ['‘Her’ is an object pronoun.', '‘Hers’ is possessive.', '‘She’s’ = she is.'],
   'Object ‘her’ → subject ‘she’.'),
  ('No object', 'The fire ___ in the kitchen.', ['started', 'was started', 'is started', 'were started'],
   ['Possible if someone started it on purpose, but here it simply began.', 'Wrong tense and meaning.', '‘The fire’ is singular.'],
   'Here ‘start’ has no object: active.'),
  ('Agent', 'This bridge was designed ___ a team of engineers.', ['by', 'from', 'with', 'of'],
   ['‘From’ is wrong.', '‘With’ is for instruments.', '‘Of’ is wrong.'],
   'Agent: by.'),
  ],
 'error': [
  ('No object', 'The meeting *finish* at six yesterday.', 'finished', 'No object, so active past simple: ‘finished’.'),
  ('Object pronoun', '*Them* were invited too.', 'They', 'Subject pronoun: ‘They were invited’.'),
  ('Wrong tense', 'They painted it in 1920. It *is* painted in 1920.', 'was', 'Keep the past: ‘was painted’.'),
  ('Missing be', 'The letters *posted* yesterday.', 'were posted', 'Passive needs ‘be’: ‘were posted’.'),
  ],
}
