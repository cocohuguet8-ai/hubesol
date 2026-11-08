TITLE = 'Passive Voice: the basics'
AUX = (['is', 'are', 'was', 'were', 'by'], None, 'is')
NEXT = ('Active vs Passive', '/grammar/passive-voice/active-vs-passive/')
BODY = r'''
## How to form the passive

| Tense | Structure | Example |
|---|---|---|
| Present simple | am / is / are + past participle | English **is spoken** here. |
| Past simple | was / were + past participle | The bridge **was built** in 1890. |
| With *by* | … + by + agent | The film **was directed by** Spielberg. |

The passive always has two parts: the verb **be** (which shows the tense and agrees with the subject) and the **past participle** (which never changes).

| ✗ | ✓ |
|---|---|
| ~~The window broken.~~ | The window **was broken**. |
| ~~Cars is made here.~~ | Cars **are made** here. |
| ~~The cake was ate.~~ | The cake **was eaten**. |

## Negatives and questions

Make negatives and questions with **be**, as usual.

- Rice **isn't grown** in Norway.
- The letters **weren't sent** yesterday.
- **Is** breakfast **included**?
- When **was** the Eiffel Tower **built**?

## When to use the passive

### 1. The action is more important than the person

- The museum **was opened** in 2005.
- These shoes **are made** in Italy.

> ⚠️ Typical error: ~~Someone opened the museum in 2005.~~ → Not wrong, but if *who* doesn't matter, the passive sounds more natural: *The museum was opened in 2005.*

### 2. We don't know who did it

- My bike **was stolen** last night.
- The window **has been** broken. (see [Passive in All Tenses](/grammar/passive-voice/passive-all-tenses/))

> ⚠️ Typical error: ~~My bike stole last night.~~ → A bike can't steal: *My bike was stolen.*

### 3. Facts, processes and the news

The passive is common in science, instructions and news reports.

- Water **is heated** to 100 °C.
- Two people **were injured** in the accident.

## The agent: *by*

Use **by** + person/thing only when it is **important or new information**.

| With *by* (useful) | Without *by* (not needed) |
|---|---|
| *Guernica* **was painted by Picasso**. | My car **was stolen**. (by someone) |
| The song **was written by** my aunt. | English **is spoken** here. (by people) |

> ⚠️ Typical error: ~~The thief was arrested by the police by the police.~~ → Don't add obvious agents: *The thief was arrested.*

## *Is* or *are*? *Was* or *were*?

*Be* agrees with the **new subject** of the passive sentence.

| Singular | Plural |
|---|---|
| The cake **is** made with eggs. | Cakes **are** made with eggs. |
| The letter **was** sent. | The letters **were** sent. |

## Common past participles

| Base | Participle | Base | Participle |
|---|---|---|---|
| make | made | write | written |
| build | built | speak | spoken |
| steal | stolen | take | taken |
| sell | sold | find | found |

## Common mistakes

**1. Forgetting *be*.** *~~The house built in 1900~~* → **The house was built in 1900.**

**2. Past simple instead of the participle.** *~~The book was wrote~~* → **The book was written.**

**3. Wrong form of *be*.** *~~The tickets was sold~~* → **The tickets were sold.**

**4. Using *from* for the agent.** *~~painted from Picasso~~* → **painted by Picasso.**

**Pro tip:** check two things in every passive — the right **be** for the subject and tense, and the **past participle**.
'''

GAP = ('Fill in the gaps',
  'Type the passive form of the verb in brackets: am / is / are or was / were + past participle. Twenty original sentences.',
  [
  ('Present', 'English [[is spoken]] in many countries.', '(speak)', 'A general fact in the present: is + past participle spoken.'),
  ('Present', 'These trainers [[are made]] in Vietnam.', '(make)', 'Plural subject in the present: are + made.'),
  ('Present', 'The museum [[is visited]] by thousands of people every year.', '(visit)', 'Singular subject, regular participle: is visited.'),
  ('Present', 'Paella [[is cooked]] in a large, flat pan.', '(cook)', 'A process described in the present passive: is cooked.'),
  ('Present', 'Rice [[isn’t grown]] in Iceland — it’s too cold.', '(not grow)', 'Negative present passive: isn’t + grown.'),
  ('Present', '[[Is]] breakfast included in the price?', 'is / are', 'Question: is + subject + past participle.'),
  ('Past', 'The Sagrada Família [[was designed]] by Gaudí.', '(design)', 'A past fact with a famous agent: was designed by.'),
  ('Past', 'My bike [[was stolen]] last night.', '(steal)', 'We don’t know who did it: was + stolen (irregular).'),
  ('Past', 'The first iPhone [[was sold]] in 2007.', '(sell)', 'Past passive: was + sold (irregular participle).'),
  ('Past', 'Two people [[were injured]] in the accident.', '(injure)', 'Plural subject in the past: were + injured.'),
  ('Past', 'The letters [[were sent]] on Monday.', '(send)', 'Plural, past: were sent.'),
  ('Past', 'The match [[wasn’t played]] because of the rain.', '(not play)', 'Negative past passive: wasn’t + played.'),
  ('Past', 'When [[was]] the bridge built?', 'was / were', 'Past passive question with a singular subject: was.'),
  ('Past', 'This book [[was written]] by my favourite author.', '(write)', 'Irregular participle: write → written.'),
  ('Past', 'The thieves [[were caught]] the next day.', '(catch)', 'Plural, past: were + caught.'),
  ('Agent', 'Guernica was painted [[by]] Picasso.', 'by / from', 'The agent is introduced with ‘by’, not ‘from’.'),
  ('Participle', 'The cake was [[eaten]] in five minutes!', '(eat)', 'After ‘was’ use the participle: eaten, not ate.'),
  ('Participle', 'A wallet was [[found]] in the park.', '(find)', 'Irregular participle: find → found.'),
  ('Present', 'The rubbish [[is collected]] every Tuesday.', '(collect)', 'A regular routine in the present passive: is collected.'),
  ('Present', 'Our classes [[are taught]] in English.', '(teach)', 'Plural, present: are + taught.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each passive sentence — 20 examples in the present and past simple.',
  [
  ('Present', 'English is spoken here.', []),
  ('Present', 'Cars are made in this factory.', []),
  ('Present', 'The shop is closed on Sundays.', ['on Sundays the shop is closed.']),
  ('Present', 'Breakfast is served at eight.', []),
  ('Present', 'Rice isn’t grown here.', []),
  ('Present', 'Is the tip included?', []),
  ('Past', 'My phone was stolen.', []),
  ('Past', 'The bridge was built in 1890.', ['in 1890 the bridge was built.']),
  ('Past', 'The window was broken yesterday.', []),
  ('Past', 'The letters were sent last week.', []),
  ('Past', 'Three people were rescued.', []),
  ('Past', 'The match wasn’t cancelled.', []),
  ('Past', 'When was this house built?', []),
  ('Agent', 'The song was written by Shakira.', []),
  ('Agent', 'The book was translated by my aunt.', []),
  ('Agent', 'This photo was taken by Laia.', []),
  ('Past', 'The thief was caught.', []),
  ('Present', 'Our homework is checked every day.', []),
  ('Past', 'Were the tickets sold?', []),
  ('Present', 'The streets are cleaned at night.', ['at night the streets are cleaned.']),
  ])

MATCH = {'title': 'Match the base verb and past participle', 'subtitle': 'Tap a base verb, then tap its past participle — the form you need in every passive.',
  'leftLabel': 'Base verb', 'rightLabel': 'Past participle', 'rightLabelSub': '(was / were + …)', 'reviewArrowPrefix': 'was ',
  'pairs': [
  ('make', 'made'), ('build', 'built'), ('write', 'written'), ('speak', 'spoken'), ('steal', 'stolen'), ('take', 'taken'), ('sell', 'sold'),
  ('find', 'found'), ('eat', 'eaten'), ('break', 'broken'), ('send', 'sent'), ('catch', 'caught'), ('teach', 'taught'), ('give', 'given'),
  ('choose', 'chosen'), ('drive', 'driven'), ('hide', 'hidden'), ('grow', 'grown'), ('invent', 'invented'), ('paint', 'painted'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Be + past participle — choose the right form of be and the right participle.',
  [
  ('Present', 'Spanish ___ in most of South America.', ['is spoken', 'speaks', 'is speaking', 'is spoke'],
   ['‘Speaks’ is active: a language can’t speak, people speak it.', '‘Is speaking’ is present continuous active, not passive.', '‘Spoke’ is past simple; the passive needs the participle ‘spoken’.'],
   'Present passive: is + past participle. Spanish is spoken there.'),
  ('Present', 'Most of these toys ___ in China.', ['are made', 'is made', 'make', 'are make'],
   ['‘These toys’ is plural, so the verb ‘be’ must be ‘are’.', 'Toys can’t make anything: the sentence needs the passive.', 'After ‘are’ use the participle ‘made’, not the base verb.'],
   'Plural subject + are + past participle: are made.'),
  ('Past', 'The Eiffel Tower ___ in 1889.', ['was built', 'built', 'was build', 'is built'],
   ['‘Built’ alone is active: the tower didn’t build anything.', 'After ‘was’ use the participle ‘built’, not the base verb.', '‘Is built’ is present, but 1889 is past.'],
   'Past passive: was + past participle, built.'),
  ('Past', 'My wallet ___ on the bus yesterday.', ['was stolen', 'stole', 'was stole', 'were stolen'],
   ['A wallet can’t steal: use the passive.', '‘Stole’ is past simple; after ‘was’ use the participle ‘stolen’.', '‘My wallet’ is singular, so ‘was’, not ‘were’.'],
   'We don’t know who did it, so the passive: was stolen.'),
  ('Past', 'Fifty people ___ to the wedding.', ['were invited', 'was invited', 'invited', 'were invite'],
   ['‘Fifty people’ is plural: were.', '‘Invited’ alone would mean the people invited someone.', 'After ‘were’ use the participle ‘invited’.'],
   'Plural, past: were + invited.'),
  ('Agent', 'This novel was written ___ Mercè Rodoreda.', ['by', 'from', 'of', 'with'],
   ['‘From’ is a very common mistake: the agent always takes ‘by’.', '‘Of’ isn’t used for the agent.', '‘With’ is for an instrument, not the person.'],
   'The agent of a passive is introduced with ‘by’.'),
  ('Negative', 'Coffee ___ in Britain. It’s too cold.', ['isn’t grown', 'doesn’t grow', 'isn’t growing', 'not grown'],
   ['‘Doesn’t grow’ is possible for plants, but here the focus is farming: the passive.', '‘Isn’t growing’ is continuous active.', '‘Not grown’ is missing ‘is’.'],
   'Negative present passive: isn’t + grown.'),
  ('Negative', 'The concert ___ because the singer was ill.', ['was cancelled', 'cancelled', 'was cancel', 'were cancelled'],
   ['‘Cancelled’ alone means the concert cancelled something.', 'After ‘was’ use the participle.', '‘The concert’ is singular: was.'],
   'Past passive: was + cancelled.'),
  ('Question', '___ the windows cleaned every week?', ['Are', 'Is', 'Do', 'Does'],
   ['‘The windows’ is plural, so not ‘is’.', 'Passive questions use ‘be’, not ‘do’.', 'Passive questions use ‘be’, not ‘does’.'],
   'Present passive question: Are + plural subject + participle?'),
  ('Question', 'When ___ penicillin discovered?', ['was', 'were', 'did', 'is'],
   ['‘Penicillin’ is singular: was.', 'Passive questions use ‘be’, not ‘did’.', 'The discovery was in the past.'],
   'Past passive question: When was + subject + participle?'),
  ('Participle', 'The cake was ___ before I arrived.', ['eaten', 'ate', 'eat', 'eating'],
   ['‘Ate’ is past simple, but the passive needs the participle.', 'After ‘was’ use the participle, not the base verb.', '‘Was eating’ is past continuous active.'],
   'Irregular participle: eat → eaten.'),
  ('Participle', 'The prize was ___ to the youngest student.', ['given', 'gave', 'give', 'giving'],
   ['‘Gave’ is past simple; use the participle.', 'After ‘was’ use the participle.', '‘Was giving’ is active continuous.'],
   'Irregular participle: give → given.'),
  ('Agent needed?', 'Which sentence has an unnecessary agent?', ['My bag was stolen by someone.', 'The film was directed by Almodóvar.', 'The song was written by my brother.', 'The house was designed by a famous architect.'],
   ['The director is important information.', 'Your brother is new, interesting information.', 'A famous architect is useful information.'],
   '‘By someone’ adds nothing: just say ‘My bag was stolen’.'),
  ('Active or passive', 'Which sentence is correct?', ['The letters were posted this morning.', 'The letters posted this morning.', 'The letters was posted this morning.', 'The letters were post this morning.'],
   ['Letters can’t post anything: the passive needs ‘were’.', '‘Letters’ is plural: were.', 'After ‘were’ use the participle.'],
   'Plural past passive: were + posted.'),
  ('Present', 'Our exams ___ by the teachers from another school.', ['are marked', 'is marked', 'mark', 'are marking'],
   ['‘Our exams’ is plural: are.', 'Exams can’t mark: use the passive.', '‘Are marking’ is active continuous.'],
   'Plural present passive: are marked.'),
  ('Past', 'The thieves ___ by the police an hour later.', ['were arrested', 'was arrested', 'arrested', 'were arrest'],
   ['‘The thieves’ is plural: were.', '‘Arrested’ alone means the thieves arrested someone.', 'After ‘were’ use the participle.'],
   'Plural past passive: were arrested.'),
  ('Present', 'The museum ___ on Mondays.', ['is closed', 'closes', 'is closing', 'closed'],
   ['‘Closes’ is active and possible, but the passive describes the state here.', '‘Is closing’ means right now.', '‘Closed’ alone is past active.'],
   'Present passive: is closed.'),
  ('Past', 'The first photograph ___ in 1826.', ['was taken', 'was took', 'took', 'is taken'],
   ['‘Took’ is past simple; use the participle ‘taken’.', 'A photograph can’t take anything.', '‘Is’ is present, but 1826 is past.'],
   'Past passive: was taken.'),
  ('Participle', 'Hundreds of houses were ___ in the earthquake.', ['destroyed', 'destroy', 'destroying', 'destroys'],
   ['After ‘were’ use the participle.', '‘Were destroying’ is active continuous.', '‘Destroys’ is present active.'],
   'Regular participle: destroyed.'),
  ('Be', 'Which form of ‘be’ fits? ‘The keys ___ found under the sofa.’', ['were', 'was', 'is', 'be'],
   ['‘The keys’ is plural: were.', '‘Is’ is present singular.', '‘Be’ is the base form.'],
   'Plural past passive: were found.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('Missing be', 'The house *built* in 1920.', 'was built', 'The passive needs ‘be’: ‘The house was built’.'),
  ('Missing be', 'My phone *stolen* yesterday.', 'was stolen', 'Passive: ‘My phone was stolen’.'),
  ('Past simple instead of participle', 'The letter was *wrote* by hand.', 'written', 'After ‘was’ use the participle: ‘written’.'),
  ('Past simple instead of participle', 'The cake was *ate* by the dog.', 'eaten', 'Participle: ‘eaten’.'),
  ('Past simple instead of participle', 'The window was *broke* by the ball.', 'broken', 'Participle: ‘broken’.'),
  ('Base verb instead of participle', 'The tickets were *sell* online.', 'sold', 'After ‘were’ use the participle: ‘sold’.'),
  ('Wrong be', 'The tickets *was* sold in an hour.', 'were', '‘The tickets’ is plural: ‘were sold’.'),
  ('Wrong be', 'These cars *is* made in Germany.', 'are', 'Plural subject: ‘are made’.'),
  ('Wrong be', 'English *are* spoken here.', 'is', '‘English’ is singular: ‘is spoken’.'),
  ('Wrong tense', 'The bridge *is* built in 1890.', 'was', '1890 is past: ‘was built’.'),
  ('Wrong agent preposition', 'The song was written *from* Rosalía.', 'by', 'The agent takes ‘by’.'),
  ('Wrong agent preposition', 'This photo was taken *of* my dad.', 'by', 'Agent: ‘taken by my dad’.'),
  ('Do in passive question', '*Did* the letters sent yesterday?', 'Were', 'Passive question: ‘Were the letters sent?’.'),
  ('Do in passive question', '*Does* breakfast included?', 'Is', 'Passive question: ‘Is breakfast included?’.'),
  ('Wrong negative', 'Rice *doesn’t* grown in Iceland.', 'isn’t', 'Negative passive: ‘isn’t grown’.'),
  ('Wrong negative', 'The match *didn’t* played.', 'wasn’t', 'Negative passive: ‘wasn’t played’.'),
  ('Active instead of passive', 'My bike *stole* last week.', 'was stolen', 'A bike can’t steal: ‘My bike was stolen’.'),
  ('Spelling', 'Two people were *injuried*.', 'injured', 'Spelling: ‘injured’.'),
  ('Wrong participle', 'The money was *hided* under the bed.', 'hidden', 'Participle of ‘hide’: ‘hidden’.'),
  ('Wrong participle', 'He was *teached* by a great teacher.', 'taught', 'Participle of ‘teach’: ‘taught’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, past participles, multiple choice and spot-the-mistake. In the typing questions write am / is / are or was / were + past participle. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('participle', 'Past participles'),
 'fill': [
  ('Present', 'Chocolate [[is made]] from cocoa beans.', 'make', 'A present process: is + made (irregular participle).', 'Present passive: is + participle.'),
  ('Past', 'The castle [[was built]] in the 12th century.', 'build', 'A past fact: was + built (irregular participle).', 'Past passive: was + participle.'),
  ('Past', 'The winners [[were chosen]] by the public.', 'choose', 'Plural, past: were + chosen.', 'Plural past → were + participle.'),
  ('Negative', 'The shop [[isn’t opened]] on Sundays.', 'not open', 'Negative present passive: isn’t + opened.', 'Negative → isn’t + participle.'),
  ],
 'order': [
  ('Present', 'French is spoken here.', []),
  ('Past', 'The car was repaired.', []),
  ('Agent', 'It was painted by Dalí.', []),
  ('Question', 'Were the letters sent?', []),
  ],
 'customItems': [
  ('Participle', 'The book was ___ in 1950.', ['written', 'wrote', 'write', 'writed'],
   ['‘Wrote’ is past simple, not the participle.', 'After ‘was’ use the participle.', '‘Write’ is irregular: written.'],
   'Irregular participle: write → written.'),
  ('Participle', 'The money was ___ in a box.', ['hidden', 'hid', 'hided', 'hide'],
   ['‘Hid’ is past simple.', '‘Hided’ doesn’t exist.', 'After ‘was’ use the participle.'],
   'Irregular participle: hide → hidden.'),
  ('Participle', 'All the tickets were ___ in a day.', ['sold', 'sell', 'selled', 'selling'],
   ['After ‘were’ use the participle.', '‘Selled’ doesn’t exist.', '‘Were selling’ is active continuous.'],
   'Irregular participle: sell → sold.'),
  ('Participle', 'He was ___ to the hospital.', ['taken', 'took', 'take', 'taked'],
   ['‘Took’ is past simple.', 'After ‘was’ use the participle.', '‘Taked’ doesn’t exist.'],
   'Irregular participle: take → taken.'),
  ],
 'mc': [
  ('Be', 'These photos ___ in Venice.', ['were taken', 'was taken', 'took', 'were took'],
   ['‘These photos’ is plural: were.', 'Photos can’t take anything.', '‘Took’ is past simple, not the participle.'],
   'Plural past passive: were taken.'),
  ('Agent', 'The telephone was invented ___ Bell.', ['by', 'from', 'of', 'with'],
   ['‘From’ is wrong for the agent.', '‘Of’ is wrong for the agent.', '‘With’ is for instruments.'],
   'Agent: by + person.'),
  ('Question', '___ the parcel delivered yesterday?', ['Was', 'Did', 'Were', 'Is'],
   ['Passive questions use ‘be’, not ‘did’.', '‘The parcel’ is singular: was.', 'Yesterday is past.'],
   'Past passive question: Was…?'),
  ('Present', 'Football ___ all over the world.', ['is played', 'plays', 'are played', 'is play'],
   ['Football can’t play: use the passive.', '‘Football’ is singular: is.', 'After ‘is’ use the participle.'],
   'Present passive: is played.'),
  ],
 'error': [
  ('Missing be', 'The letter *sent* yesterday.', 'was sent', 'Passive needs ‘be’: ‘was sent’.'),
  ('Wrong be', 'The windows *was* cleaned.', 'were', 'Plural: ‘were cleaned’.'),
  ('Past simple instead of participle', 'The song was *sang* by a choir.', 'sung', 'Participle: ‘sung’.'),
  ('Wrong agent preposition', 'It was cooked *from* my grandma.', 'by', 'Agent: ‘by’.'),
  ],
}
