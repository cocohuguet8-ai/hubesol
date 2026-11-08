TITLE = 'Passive with Two Objects'
AUX = (['was', 'were', 'to', 'by'], None, 'was')
NEXT = ('The Get Passive', '/grammar/passive-voice/get-passive/')
BODY = r'''
## How to form a passive with two objects

Some verbs have **two objects**: a person (indirect object) and a thing (direct object).

> **Active:** My aunt gave **me** (person) **a watch** (thing).

Either object can become the subject of the passive.

| Subject of the passive | Passive | Notes |
|---|---|---|
| the **person** | **I was given** a watch. | most common and natural |
| the **thing** | **A watch was given to me**. | needs **to** (or *for*) before the person |

## Verbs with two objects

| give | send | show | offer | lend |
|---|---|---|---|---|
| **tell** | **teach** | **pay** | **promise** | **award** |

- They **sent** her a letter. → **She was sent** a letter.
- They **offered** him a job. → **He was offered** a job.
- They **showed** us the room. → **We were shown** the room.

## When to make the person the subject

### 1. When the person is the topic

This is the normal choice in English because people are usually more interesting than things.

- **I was told** the news by my sister.
- **The winners were awarded** gold medals.

> ⚠️ Typical error: ~~Me was given a present.~~ → Use the subject pronoun: *I was given a present.*

### 2. Pronouns change to subject form

| Active (object) | Passive (subject) |
|---|---|
| They gave **him** a prize. | **He** was given a prize. |
| They told **us** a story. | **We** were told a story. |
| They paid **them** €50. | **They** were paid €50. |

## When to make the thing the subject

### 1. When the thing is the topic

- **The prize was given to** the youngest student.
- **This book was lent to** me by my teacher.

> ⚠️ Typical error: ~~A watch was given me.~~ → In modern English, add *to*: *A watch was given to me.*

### 2. *To* or *for*?

| Verb | Preposition | Example |
|---|---|---|
| give, send, show, lend, offer, tell, teach | **to** | The letter was sent **to** her. |
| buy, make, cook, find | **for** | A cake was made **for** him. |

## Agreement

*Be* agrees with the **new subject**.

- **I was** sent two emails. (subject = I)
- **Two emails were** sent to me. (subject = two emails)

> ⚠️ Typical error: ~~Two emails was sent to me.~~ → *Two emails were sent to me.*

## Other tenses

The rule works in every tense:

- **She has been offered** a place at university.
- **You will be shown** the way.
- **We are being taught** by a new teacher this term.

## Common mistakes

**1. Object pronoun as subject.** *~~Him was offered a job~~* → **He was offered a job.**

**2. Missing *to* when the thing is the subject.** *~~The book was given me~~* → **The book was given to me.**

**3. Wrong agreement.** *~~We was told~~* → **We were told.**

**4. Using *to* when the person is the subject.** *~~I was given to a watch~~* → **I was given a watch.**

**Pro tip:** start with the person — *I was given…, She was told…* — it's shorter and sounds the most natural.
'''

GAP = ('Fill in the gaps',
  'Complete each passive sentence: the right form of be, the past participle, a subject pronoun, or to / for. Twenty original sentences.',
  [
  ('Person subject', 'My aunt gave me a watch. → I [[was given]] a watch.', '(give)', 'The person (I) becomes the subject: was + given.'),
  ('Person subject', 'They sent her a letter. → She [[was sent]] a letter.', '(send)', 'Person as subject: was sent + the thing.'),
  ('Person subject', 'They offered him a job. → He [[was offered]] a job.', '(offer)', 'Person as subject: was offered a job.'),
  ('Person subject', 'The guide showed us the castle. → We [[were shown]] the castle.', '(show)', 'Plural person subject: were shown.'),
  ('Person subject', 'They paid the workers €100. → The workers [[were paid]] €100.', '(pay)', 'Plural subject: were + paid.'),
  ('Person subject', 'Someone told me a secret. → I [[was told]] a secret.', '(tell)', 'Person as subject: was told.'),
  ('Pronoun', 'They gave him a medal. → [[He]] was given a medal.', 'he / him', 'Object ‘him’ becomes the subject ‘he’.'),
  ('Pronoun', 'They told us the news. → [[We]] were told the news.', 'we / us', 'Object ‘us’ becomes the subject ‘we’.'),
  ('Pronoun', 'They lent them a car. → [[They]] were lent a car.', 'they / them', 'Object ‘them’ becomes the subject ‘they’.'),
  ('Thing subject', 'My aunt gave me a watch. → A watch was given [[to]] me.', 'to / for', 'Thing as subject: add ‘to’ before the person.'),
  ('Thing subject', 'They sent her a letter. → A letter was sent [[to]] her.', 'to / for', 'With ‘send’, use ‘to’ before the person.'),
  ('Thing subject', 'Mum made me a cake. → A cake was made [[for]] me.', 'to / for', 'With ‘make’, use ‘for’ before the person.'),
  ('Thing subject', 'Dad bought her a bike. → A bike was bought [[for]] her.', 'to / for', 'With ‘buy’, use ‘for’ before the person.'),
  ('Thing subject', 'They showed the visitors the photos. → The photos [[were shown]] to the visitors.', '(show)', 'Plural thing as subject: were shown to.'),
  ('Agreement', 'Two emails [[were]] sent to me this morning.', 'was / were', '‘Two emails’ is plural: were.'),
  ('Agreement', 'I [[was]] sent two emails this morning.', 'was / were', '‘I’ takes ‘was’, whatever the object.'),
  ('Other tenses', 'She [[has been offered]] a place at university.', '(offer)', 'Present perfect passive with the person as subject: has been offered.'),
  ('Other tenses', 'You [[will be shown]] your room by the receptionist.', '(show)', 'A future passive with the person as subject: will be + shown (the participle).'),
  ('Other tenses', 'We [[are being taught]] by a new teacher this term.', '(teach)', 'Present continuous passive: are being taught.'),
  ('Award', 'The winners [[were awarded]] gold medals.', '(award)', 'Person subject, plural: were awarded.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each passive sentence — 10 with the person as subject and 10 with the thing as subject.',
  [
  ('Person subject', 'I was given a present.', []),
  ('Person subject', 'She was offered a job.', []),
  ('Person subject', 'We were shown the way.', []),
  ('Person subject', 'He was sent a message.', []),
  ('Person subject', 'They were told a story.', []),
  ('Person subject', 'I was lent a book.', []),
  ('Person subject', 'The players were paid well.', []),
  ('Person subject', 'She has been promised a pay rise.', []),
  ('Person subject', 'You will be told later.', []),
  ('Person subject', 'We were taught French.', []),
  ('Thing subject', 'A present was given to me.', []),
  ('Thing subject', 'A job was offered to her.', []),
  ('Thing subject', 'The way was shown to us.', []),
  ('Thing subject', 'A message was sent to him.', []),
  ('Thing subject', 'The book was lent to me.', []),
  ('Thing subject', 'A cake was made for her.', []),
  ('Thing subject', 'The tickets were sent to us.', []),
  ('Thing subject', 'A prize was awarded to Laia.', []),
  ('Thing subject', 'A bike was bought for him.', []),
  ('Thing subject', 'The photos were shown to everyone.', []),
  ])

MATCH = {'title': 'Match the two passives', 'subtitle': 'Tap a passive with the person as subject, then tap the same idea with the thing as subject.',
  'leftLabel': 'Person subject', 'rightLabel': 'Thing subject', 'rightLabelSub': '(+ to / for)', 'reviewArrowPrefix': '',
  'pairs': [
  ('I was given a watch.', 'A watch was given to me.'), ('She was sent a letter.', 'A letter was sent to her.'), ('He was offered a job.', 'A job was offered to him.'),
  ('We were shown the room.', 'The room was shown to us.'), ('They were told the truth.', 'The truth was told to them.'), ('I was lent a pen.', 'A pen was lent to me.'),
  ('She was awarded a prize.', 'A prize was awarded to her.'), ('We were taught Latin.', 'Latin was taught to us.'), ('He was promised a bonus.', 'A bonus was promised to him.'),
  ('I was sent the photos.', 'The photos were sent to me.'), ('They were given free tickets.', 'Free tickets were given to them.'), ('You were offered a seat.', 'A seat was offered to you.'),
  ('She was shown the results.', 'The results were shown to her.'), ('We were sent an invitation.', 'An invitation was sent to us.'), ('He was given a second chance.', 'A second chance was given to him.'),
  ('I was told a joke.', 'A joke was told to me.'), ('They were lent some money.', 'Some money was lent to them.'), ('She was given flowers.', 'Flowers were given to her.'),
  ('We were offered coffee.', 'Coffee was offered to us.'), ('He was sent a parcel.', 'A parcel was sent to him.'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Person as subject is most natural; thing as subject needs to / for. Be agrees with the new subject.',
  [
  ('Person subject', 'My grandparents gave me a guitar. → I ___ a guitar.', ['was given', 'gave', 'was gave', 'were given'],
   ['‘I gave a guitar’ is active and changes the meaning completely.', '‘Gave’ is past simple; after ‘was’ use the participle ‘given’.', '‘I’ takes ‘was’, not ‘were’.'],
   'The person becomes the subject: I was given a guitar.'),
  ('Pronoun', 'They offered him a scholarship. → ___ was offered a scholarship.', ['He', 'Him', 'His', 'He’s'],
   ['‘Him’ is an object pronoun; the subject of the passive must be ‘he’.', '‘His’ is a possessive adjective.', '‘He’s’ means ‘he is’ or ‘he has’.'],
   'Object pronoun → subject pronoun: He was offered…'),
  ('Thing subject', 'They sent us the tickets. → The tickets were sent ___ us.', ['to', 'for', 'by', 'with'],
   ['‘For’ is used with buy, make and cook, not with ‘send’.', '‘By’ introduces the agent, not the receiver.', '‘With’ is for instruments.'],
   'When the tickets are the subject, ‘send’ needs ‘to’ before the receiver: sent to us.'),
  ('Thing subject', 'Dad cooked her a special dinner. → A special dinner was cooked ___ her.', ['for', 'to', 'by', 'at'],
   ['With ‘cook’, the receiver takes ‘for’, not ‘to’.', '‘By her’ would mean she cooked it.', '‘At’ is a place preposition.'],
   'Verbs like buy, make and cook take ‘for’ before the receiver: cooked for her.'),
  ('Agreement', 'Three new books ___ to the library yesterday.', ['were given', 'was given', 'were gave', 'gave'],
   ['‘Three new books’ is plural: were.', '‘Gave’ is past simple; use the participle.', 'Books can’t give: use the passive.'],
   '‘Three new books’ is the plural subject of the passive, so use ‘were given’.'),
  ('Agreement', 'We ___ three new books yesterday.', ['were given', 'was given', 'gave', 'were give'],
   ['‘We’ takes ‘were’, not ‘was’.', '‘We gave’ is active.', 'After ‘were’ use the participle.'],
   '‘We’ is the subject, so ‘be’ agrees with it: ‘we were given’, whatever the object.'),
  ('Natural', 'Which sentence is the most natural?', ['She was told the news.', 'The news was told her.', 'Her was told the news.', 'She was told to the news.'],
   ['Without ‘to’ this sounds old-fashioned or wrong.', '‘Her’ can’t be a subject.', 'No ‘to’ when the person is the subject.'],
   'The most natural passive starts with the person.'),
  ('Missing to', 'Which sentence is correct?', ['A prize was awarded to Joan.', 'A prize was awarded Joan.', 'A prize was awarded for Joan.', 'A prize awarded to Joan.'],
   ['When the thing is the subject, add ‘to’.', '‘Award’ takes ‘to’, not ‘for’.', '‘Was’ is missing.'],
   'When the thing is the subject, put ‘to’ before the person: awarded to Joan.'),
  ('Extra to', 'Which sentence is correct?', ['I was shown the photos.', 'I was shown to the photos.', 'Me was shown the photos.', 'I was showed the photos.'],
   ['No ‘to’ when the person is the subject.', '‘Me’ can’t be the subject.', 'The participle of ‘show’ is ‘shown’.'],
   'Person subject + participle + thing, no ‘to’.'),
  ('Other tenses', 'She ___ a job in London. She starts next week!', ['has been offered', 'has offered', 'has being offered', 'is offered been'],
   ['‘Has offered’ is active: she offered someone a job.', 'After ‘has’ use ‘been’.', 'Wrong order.'],
   'Present perfect passive: has been offered.'),
  ('Other tenses', 'Don’t worry, you ___ the way by the guide.', ['will be shown', 'will show', 'will shown', 'are being show'],
   ['‘Will show’ is active.', 'After ‘will’ add ‘be’.', 'After ‘being’ use the participle.'],
   'Future passive: will be shown.'),
  ('Other tenses', 'The students ___ Mandarin this year.', ['are being taught', 'are teaching', 'are being teach', 'is being taught'],
   ['‘Are teaching’ is active.', 'After ‘being’ use the participle ‘taught’.', '‘The students’ is plural.'],
   'Present continuous passive: are being taught.'),
  ('Participle', 'I was ___ a ring for my birthday.', ['given', 'gave', 'give', 'giving'],
   ['‘Gave’ is past simple.', 'After ‘was’ use the participle.', '‘Was giving’ is active.'],
   'The passive needs the participle, and ‘give’ is irregular: give → given.'),
  ('Participle', 'We were ___ the answers before the test.', ['told', 'telled', 'tell', 'telling'],
   ['‘Telled’ doesn’t exist.', 'After ‘were’ use the participle.', '‘Were telling’ is active.'],
   'The passive needs the participle, and ‘tell’ is irregular: tell → told.'),
  ('Pronoun', 'They paid us €200. → ___ were paid €200.', ['We', 'Us', 'Our', 'Ours'],
   ['‘Us’ is an object pronoun.', '‘Our’ is a possessive adjective.', '‘Ours’ is a possessive pronoun.'],
   'The object ‘us’ in the active becomes the subject ‘we’ in the passive.'),
  ('Thing subject', 'They lent me their car. → Their car was lent ___ me.', ['to', 'for', 'by', 'from'],
   ['‘Lend’ takes ‘to’.', '‘By me’ would mean I lent it.', '‘From’ is the opposite direction.'],
   'With ‘lend’, the receiver is introduced with ‘to’ when the thing is the subject.'),
  ('Thing subject', 'My uncle bought us pizza. → Pizza was bought ___ us.', ['for', 'to', 'by', 'with'],
   ['‘Buy’ takes ‘for’, not ‘to’.', '‘By us’ would mean we bought it.', '‘With’ is wrong.'],
   'With ‘buy’, the receiver is introduced with ‘for’, not ‘to’: bought for us.'),
  ('Agreement', 'The children ___ a story every night.', ['are told', 'is told', 'tell', 'are tell'],
   ['‘The children’ is plural.', 'The children don’t tell; they are told.', 'After ‘are’ use the participle.'],
   '‘The children’ is plural and it happens every night: present passive ‘are told’.'),
  ('Person subject', 'Someone sent Marc a strange email. → Marc ___ a strange email.', ['was sent', 'sent', 'was send', 'were sent'],
   ['‘Marc sent’ is active.', 'After ‘was’ use the participle.', '‘Marc’ is singular.'],
   'Marc (the person) becomes the subject: ‘Marc was sent a strange email’.'),
  ('Natural', 'Your manager is talking about you. Which is more natural?', ['You will be given a laptop.', 'A laptop will be given you.', 'A laptop will given to you.', 'You will give a laptop.'],
   ['Missing ‘to’ and sounds old-fashioned.', '‘Be’ is missing.', 'That’s active and changes the meaning.'],
   'When the person is the topic, start with the person.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('Object pronoun', '*Me* was given a present.', 'I', 'Subject pronoun: ‘I was given a present’.'),
  ('Object pronoun', '*Him* was offered a job.', 'He', 'Subject pronoun: ‘He was offered a job’.'),
  ('Object pronoun', '*Us* were shown the way.', 'We', 'Subject pronoun: ‘We were shown the way’.'),
  ('Object pronoun', '*Her* was told the news.', 'She', 'Subject pronoun: ‘She was told the news’.'),
  ('Missing preposition', 'A watch was given *me* for my birthday.', 'to me', 'Thing as subject needs ‘to’: ‘given to me’.'),
  ('Wrong preposition', 'A cake was made *to* her.', 'for', '‘Make’ takes ‘for’: ‘made for her’.'),
  ('Wrong preposition', 'A bike was bought *to* my brother.', 'for', '‘Buy’ takes ‘for’: ‘bought for my brother’.'),
  ('Wrong preposition', 'The letter was sent *for* the manager.', 'to', '‘Send’ takes ‘to’: ‘sent to the manager’.'),
  ('Wrong preposition', 'A seat was offered *for* me on the bus.', 'to', '‘Offer’ takes ‘to’: ‘offered to me’.'),
  ('Agreement', 'We *was* told a story.', 'were', '‘We’ takes ‘were’.'),
  ('Agreement', 'Two emails *was* sent to me.', 'were', 'Plural: ‘were sent’.'),
  ('Agreement', 'I *were* offered a seat.', 'was', '‘I’ takes ‘was’.'),
  ('Wrong participle', 'She was *gave* a medal.', 'given', 'Participle: ‘given’.'),
  ('Wrong participle', 'We were *showed* the room.', 'shown', 'Participle: ‘shown’.'),
  ('Wrong participle', 'He was *teached* Spanish at school.', 'taught', 'Participle: ‘taught’.'),
  ('Missing be', 'I *given* a second chance.', 'was given', 'Passive needs ‘be’: ‘I was given’.'),
  ('Missing been', 'She has *offered* a place at university.', 'been offered', 'Perfect passive: ‘has been offered’.'),
  ('Active form', 'Marc *sent* a strange email by someone.', 'was sent', 'Passive with the person as subject: ‘Marc was sent…’.'),
  ('Wrong tense', 'Yesterday I *am* given a prize.', 'was', 'Past: ‘I was given’.'),
  ('Spelling', 'They were *payed* €50.', 'paid', 'Participle of ‘pay’: ‘paid’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, to or for, multiple choice and spot-the-mistake. In the typing questions write be + past participle, a subject pronoun, or to / for. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('prep', 'To or for'),
 'fill': [
  ('Person subject', 'They gave her a prize. → She [[was given]] a prize.', 'give', 'The person becomes the subject of the passive: was + given.', 'Was + participle.'),
  ('Pronoun', 'They told me the truth. → [[I]] was told the truth.', 'I / me', 'The object pronoun ‘me’ becomes the subject pronoun ‘I’.', 'Subject pronoun.'),
  ('Thing subject', 'The photos were sent [[to]] all the parents.', 'to / for', 'When the thing is the subject, ‘send’ takes ‘to’ before the person.', 'Send → ‘to’.'),
  ('Agreement', 'The players [[were]] given new shirts.', 'was / were', '‘The players’ is plural, so the passive uses ‘were’ + participle.', 'Plural → ‘were’.'),
  ],
 'order': [
  ('Person subject', 'He was given a medal.', []),
  ('Thing subject', 'A medal was given to him.', []),
  ('Person subject', 'We were offered tea.', []),
  ('Thing subject', 'A cake was made for me.', []),
  ],
 'customItems': [
  ('Prep', 'A present was sent ___ my cousin.', ['to', 'for', 'by', 'of'],
   ['‘Send’ takes ‘to’, not ‘for’.', '‘By’ would mean your cousin sent it.', '‘Of’ is wrong.'],
   'With ‘send’, the receiver is introduced with ‘to’: sent to my cousin.'),
  ('Prep', 'A birthday cake was made ___ my cousin.', ['for', 'to', 'by', 'of'],
   ['‘Make’ takes ‘for’, not ‘to’.', '‘By’ would mean your cousin made it.', '‘Of’ is wrong.'],
   'With ‘make’, the receiver is introduced with ‘for’: made for my cousin.'),
  ('Prep', 'The keys were lent ___ the neighbours.', ['to', 'for', 'by', 'from'],
   ['‘Lend’ takes ‘to’.', '‘By’ would mean the neighbours lent them.', '‘From’ is the opposite direction.'],
   'With ‘lend’, the receiver is introduced with ‘to’: lent to the neighbours.'),
  ('Prep', 'Some flowers were bought ___ the teacher.', ['for', 'to', 'by', 'with'],
   ['‘Buy’ takes ‘for’.', '‘By’ would mean the teacher bought them.', '‘With’ is wrong.'],
   'With ‘buy’, the receiver is introduced with ‘for’: bought for the teacher.'),
  ],
 'mc': [
  ('Pronoun', 'They showed us the stadium. → ___ were shown the stadium.', ['We', 'Us', 'Our', 'Ours'],
   ['‘Us’ is an object pronoun.', '‘Our’ is possessive.', '‘Ours’ is possessive.'],
   'The object ‘us’ becomes the subject ‘we’ in the passive sentence.'),
  ('Agreement', 'Free tickets ___ to everyone.', ['were offered', 'was offered', 'offered', 'were offer'],
   ['Plural subject: were.', 'Tickets can’t offer.', 'After ‘were’ use the participle.'],
   '‘Free tickets’ is a plural subject, so use ‘were’ + offered.'),
  ('Natural', 'Which is the most natural?', ['I was sent an invitation.', 'An invitation was sent me.', 'Me was sent an invitation.', 'I was sent to an invitation.'],
   ['Missing ‘to’.', '‘Me’ can’t be a subject.', 'No ‘to’ with a person subject.'],
   'Starting with the person (‘I was sent…’) is the most natural passive.'),
  ('Other tenses', 'He ___ a promotion.', ['has been promised', 'has promised', 'has being promised', 'have been promised'],
   ['‘Has promised’ is active.', 'After ‘has’ use ‘been’.', '‘He’ takes ‘has’.'],
   'Present perfect passive with the person as subject: has been promised.'),
  ],
 'error': [
  ('Object pronoun', '*Them* were paid €100.', 'They', 'The subject must be a subject pronoun: ‘They were paid €100’.'),
  ('Missing preposition', 'The letter was given *her* this morning.', 'to her', 'When the thing is the subject, add ‘to’ before the person: ‘given to her’.'),
  ('Wrong preposition', 'A dress was made *to* the bride.', 'for', 'With ‘make’ the receiver takes ‘for’: ‘made for the bride’.'),
  ('Agreement', 'We *was* given homework.', 'were', '‘We’ always takes ‘were’ in the past passive: ‘We were given homework’.'),
  ],
}
