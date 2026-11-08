TITLE = 'All, Both, Every & Each'
AUX = (['all', 'both', 'every', 'each'], None, 'each')
NEXT = ("Possessives: 's vs of", '/grammar/nouns-determiners/possessives-s-vs-of/')
BODY = r'''
## Quick overview

| Word | Number | Noun | Example |
|---|---|---|---|
| **both** | exactly 2 | plural | **Both** my parents work. |
| **all** | 3 or more / the whole | plural or uncountable | **All** the students passed. |
| **every** | 3 or more, as a group | singular | **Every** student passed. |
| **each** | 2 or more, one by one | singular | **Each** student got a prize. |

## *Both* — two things

### 1. *Both* + plural noun

- **Both** (the) girls are tall. — I like **both** films.

### 2. *Both of* + *the / my* / pronoun

- **Both of** my sisters live in Girona. — **Both of us** were tired.

### 3. *Both … and …*

- **Both** Anna **and** Joan came. — She's **both** clever **and** kind.

> ⚠️ Typical error: ~~Both of girls~~ → *Both girls / Both of the girls.*

## *All* — the whole group

### 1. *All* + plural or uncountable

- **All** children need love. — **All** the food was delicious.

### 2. *All of* + *the / my* / pronoun

- **All of** my friends came. — I ate **all of it**.

### 3. *All* + time words

- **all** day, **all** night, **all** week (= the whole day…)

> ⚠️ Typical error: ~~All the day~~ → *all day / the whole day.*

## *Every* — all, seen as a group

### 1. *Every* + singular noun + singular verb

- **Every** room **has** a TV. — ~~Every rooms have…~~

### 2. Frequency

- **every** day, **every** week, **every** two hours

### 3. Compounds

- **everyone / everybody**, **everything**, **everywhere** (+ singular verb)

> ⚠️ Typical error: ~~Everyone are here.~~ → *Everyone is here.*

## *Each* — one by one

### 1. *Each* + singular noun

- **Each** player has a number. (we think about them individually)

### 2. *Each of* + plural

- **Each of** the rooms **has** a balcony.

### 3. *Each* alone

- The tickets cost €10 **each**.

## *Every* vs *each*

| **every** | **each** |
|---|---|
| 3 or more | 2 or more (also 2) |
| the group as a whole | the members one by one |
| no *of* (~~every of~~) | *each of* is fine |
| **every** two days | the cost **each** |

- She wore a ring on **each** hand. (2 hands → not *every*)

## Common mistakes

**1. *Every* + plural.** *~~every days~~* → **every day**.

**2. *Every of*.** *~~every of the students~~* → **each of / all of the students**.

**3. Plural verb after *every / each*.** *~~Each child have~~* → **Each child has**.

**4. *All* for two.** *~~All my parents~~* → **Both my parents**.

**Pro tip:** two → **both**; the whole group → **all**; one by one → **each**; every single one, as a group → **every**.
'''

GAP = ('Fill in the gaps',
  'Type all, both, every or each. Twenty original sentences.',
  [
  ('Both', 'I have two brothers. [[Both|both]] of them play football.', 'all / both', 'Exactly two: ‘both of them’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Both', 'She speaks [[both]] English and French.', 'all / both', '‘Both … and …’ joins two things. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Both', 'I like [[both]] colours — blue and green.', 'all / both', 'Two colours: ‘both’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('All', '[[All|all]] the students in my class passed the exam.', 'all / both', 'The whole group (more than two): ‘all’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('All', 'He ate [[all]] the cake! There’s nothing left.', 'all / both', 'The whole cake: ‘all’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('All', 'It rained [[all]] day yesterday.', 'all / every', '‘All day’ = the whole day. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('All', '[[All|all]] of my friends came to the party.', 'all / both', 'More than two friends: ‘all of’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Every', 'I go to the gym [[every]] Monday.', 'every / each', 'Frequency: ‘every Monday’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Every', '[[Every|every]] room in the hotel has a balcony.', 'every / each', 'All the rooms, as a group: ‘every room’ (‘each’ is also possible).'),
  ('Every', 'The bus comes [[every]] ten minutes.', 'every / each', 'Repeated interval: ‘every ten minutes’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Every', '[[Everyone|Everybody|everyone|everybody]] is waiting for you.', 'every- / each', 'Compound with a singular verb: ‘everyone is’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Every', 'I looked [[everywhere]] for my keys.', 'every- / each', 'All places: ‘everywhere’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Each', 'The teacher gave a book to [[each]] student.', 'every / each', 'One by one: ‘each student’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Each', 'She had a bag in [[each]] hand.', 'every / each', 'Two hands: ‘each’, not ‘every’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Each', '[[Each|each]] of the rooms has its own bathroom.', 'every / each', '‘Each of’ + plural, singular verb. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Each', 'The tickets cost twenty euros [[each]].', 'every / each', '‘Each’ alone at the end = per item. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Each', 'The two teams played well. [[Each|each]] team scored a goal.', 'every / each', 'Two teams, one by one: ‘each’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('All', 'I’ve spent [[all]] my money.', 'all / both', 'The whole amount: ‘all my money’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Both', '[[Both|both]] my parents are teachers.', 'all / both', 'Two parents: ‘both’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Every', 'I’ve read [[every]] book in this series.', 'every / each', 'All of them, as a group: ‘every book’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with all, both, every and each.',
  [
  ('Both', 'Both my parents work.', []),
  ('Both', 'Both of us were tired.', []),
  ('Both … and', 'She is both clever and kind.', []),
  ('All', 'All the students passed.', []),
  ('All', 'I ate all of it.', []),
  ('All', 'It rained all day.', []),
  ('All', 'All children need love.', []),
  ('Every', 'Every room has a TV.', []),
  ('Every', 'I swim every day.', []),
  ('Every', 'Everyone is here.', []),
  ('Every', 'The bus comes every hour.', []),
  ('Every', 'Everything is ready.', []),
  ('Each', 'Each player has a number.', []),
  ('Each', 'Each of the rooms has a bed.', []),
  ('Each', 'They cost ten euros each.', []),
  ('Each', 'She had a ring on each hand.', []),
  ('All', 'All of my friends came.', []),
  ('Both', 'I like both films.', []),
  ('Every', 'I go there every week.', []),
  ('Each', 'Each child got a present.', []),
  ])

MATCH = {'title': 'Which word?', 'subtitle': 'Tap a sentence, then tap the word that fills the gap.',
  'leftLabel': 'Sentence', 'rightLabel': 'Word', 'rightLabelSub': '', 'reviewArrowPrefix': '',
  'pairs': [
  ('___ my eyes are blue.', 'both'), ('___ the people in the room laughed.', 'all'), ('I brush my teeth ___ morning.', 'every'), ('She held a cup in ___ hand.', 'each'),
  ('___ Lisbon and Porto are in Portugal.', 'both'), ('We danced ___ night.', 'all'), ('___ student needs a password.', 'every'), ('The pens cost €1 ___.', 'each'),
  ('I’ve got two cats; ___ are black.', 'both'), ('___ of the milk is gone.', 'all'), ('___thing is fine, thanks.', 'every'), ('___ of the twins has a bike.', 'each'),
  ('___ of my hands are cold.', 'both'), ('I spent ___ my money.', 'all'), ('The train leaves ___ two hours.', 'every'), ('The two girls ___ got a prize.', 'each'),
  ('___ of us went — me and Pau.', 'both'), ('___ children love stories.', 'all'), ('I’ve seen ___ film he made.', 'every'), ('___ side of the coin is different.', 'each'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Two → both. The whole group → all. Group of singular nouns → every. One by one → each.',
  [
  ('Both', 'I’ve got two cousins and ___ live in London.', ['both', 'all', 'every', 'each'],
   ['‘All’ is for more than two.', '‘Every’ needs a noun after it.', '‘Each live’ needs a singular verb: ‘each lives’.'],
   'Exactly two: both. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('All', '___ the windows were open.', ['All', 'Every', 'Each', 'Both'],
   ['‘Every’ needs a singular noun, without ‘the’.', '‘Each’ needs a singular noun or ‘each of’.', '‘Both’ is only for two (and we don’t know there are two).'],
   'The whole group + plural: all the windows. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Every', '___ student must bring a dictionary.', ['Every', 'All', 'Both', 'Each of'],
   ['‘All’ needs a plural noun: ‘all students’.', '‘Both’ needs a plural noun.', '‘Each of’ needs ‘the’ + plural.'],
   'Every + singular noun. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Every', 'I check my email ___ morning.', ['every', 'all', 'both', 'each of'],
   ['‘All morning’ means the whole morning, not every day.', 'Not for frequency.', '‘Each of morning’ is wrong.'],
   'Frequency: every morning. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('All', 'The baby cried ___ night.', ['all', 'every', 'each', 'both'],
   ['‘Every night’ means many nights.', '‘Each night’ means many nights, one by one.', '‘Both night’ is wrong.'],
   'The whole night: all night. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Each', 'There’s a lamp on ___ side of the bed.', ['each', 'every', 'all', 'both'],
   ['A bed has two sides: ‘every’ needs three or more.', '‘All side’ is wrong.', '‘Both’ needs a plural: ‘both sides’.'],
   'Two sides, one by one: each side. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Each', '___ of the players has a different shirt.', ['Each', 'Every', 'All', 'Both'],
   ['‘Every of’ is never correct.', '‘All of … has’ — ‘all’ takes a plural verb.', '‘Both … has’ — ‘both’ takes a plural verb.'],
   'Each of + plural + singular verb. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Every', '___ is ready for the party.', ['Everything', 'All things', 'Each', 'Both'],
   ['‘All things’ sounds unnatural here.', '‘Each’ alone needs context.', '‘Both’ is for two.'],
   'Everything + singular verb. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Both', '___ Marc and his sister are doctors.', ['Both', 'All', 'Every', 'Each'],
   ['‘Both … and …’ is the pattern.', '‘Every … and’ is wrong.', '‘Each … and’ is wrong.'],
   'Both … and … Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Every', 'Trains leave ___ fifteen minutes.', ['every', 'each', 'all', 'both'],
   ['‘Each fifteen minutes’ isn’t used.', '‘All fifteen minutes’ is wrong.', '‘Both’ is for two.'],
   'Every + number + time. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Each', 'The oranges cost 50 cents ___.', ['each', 'every', 'all', 'both'],
   ['‘Every’ can’t stand alone at the end.', '‘All’ doesn’t mean ‘per item’.', '‘Both’ is for two.'],
   'Per item: each. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('All', 'Have you finished ___ your homework?', ['all', 'every', 'each', 'both'],
   ['‘Every your homework’ is wrong.', '‘Each your homework’ is wrong.', '‘Both’ is for two.'],
   'The whole amount: all your homework. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Both', '___ of my parents were born in Lleida.', ['Both', 'Every', 'Each', 'All'],
   ['‘Every of’ is wrong.', '‘Each of … were’ — ‘each’ needs a singular verb.', '‘All’ is for three or more; parents are two.'],
   'Two people: both of. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Every', '___ is talking about the new film.', ['Everyone', 'All', 'Both', 'Each'],
   ['‘All is talking’ is wrong.', '‘Both is talking’ is wrong.', '‘Each is talking’ needs context.'],
   'Everyone + singular verb. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Verb', 'Every child ___ a present.', ['gets', 'get', 'are getting', 'have got'],
   ['‘Every’ takes a singular verb.', '‘Are’ is plural.', '‘Have’ is plural.'],
   'Every + singular verb. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Verb', 'All the shops ___ closed on Sunday.', ['are', 'is', 'has', 'was'],
   ['‘All the shops’ is plural.', '‘Has’ is singular and wrong meaning.', '‘Was’ is singular.'],
   'All + plural + plural verb. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Which', 'Which sentence is correct?', ['I go swimming every day.', 'I go swimming every days.', 'I go swimming all days.', 'I go swimming each of day.'],
   ['‘Every’ + singular.', 'Not with plural ‘days’ here.', '‘Each of day’ is wrong.'],
   'Every day. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Which', 'Which sentence is correct?', ['Each of the boys has a bike.', 'Every of the boys has a bike.', 'Each of the boys have a bike.', 'Each the boys has a bike.'],
   ['Never ‘every of’.', '‘Each of’ takes a singular verb.', 'We need ‘of’.'],
   'Each of + plural + singular verb. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Every', 'We visit our grandma ___ summer.', ['every', 'all', 'both', 'each of'],
   ['‘All summer’ means the whole summer.', '‘Both summer’ is wrong.', '‘Each of summer’ is wrong.'],
   'Frequency: every summer. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Each', 'The two boxers looked at ___ other.', ['each', 'every', 'all', 'both'],
   ['Fixed phrase: ‘each other’.', 'Not English.', 'Not English.'],
   'Fixed phrase: each other. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('Every + plural', 'I walk to school every *days*.', 'day', '‘Every’ + singular: ‘every day’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Every + plural', 'Every *students* has a locker.', 'student', '‘Every’ + singular: ‘every student’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Every of', '*Every* of my friends has a phone.', 'Each', 'Never ‘every of’: ‘each of / all of’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Every of', 'I’ve read *every* of his books.', 'all', 'Never ‘every of’: ‘all of his books’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Verb after every', 'Everyone *are* happy today.', 'is', '‘Everyone’ takes a singular verb. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Verb after every', 'Every room *have* a window.', 'has', '‘Every’ + singular verb. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Verb after each', 'Each child *have* a name tag.', 'has', '‘Each’ + singular verb. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Verb after each', 'Each of the girls *are* wearing a hat.', 'is', '‘Each of’ takes a singular verb. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('All for two', '*All* my parents are from Girona.', 'Both', 'Two parents: ‘both’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('All for two', 'I’ve got two sisters and *all* of them are older.', 'both', 'Two people: ‘both of them’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Both for more', 'I have three brothers and *both* are tall.', 'all', 'More than two: ‘all’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Both of', 'Both *of* girls passed.', 'the', 'Say ‘both girls’, ‘both the girls’ or ‘both of the girls’ — not ‘both of girls’.'),
  ('Every for two', 'She wore a bracelet on *every* wrist.', 'each', 'Two wrists: ‘each’, not ‘every’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('All the day', 'I worked *all the day*.', 'all day', '‘All day’, not ‘all the day’.'),
  ('Every + time', 'The bus comes *each* ten minutes.', 'every', 'Interval with a number: ‘every ten minutes’.'),
  ('Each alone', 'The tickets cost five euros *every*.', 'each', 'At the end, ‘each’ = per item. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Both and', 'Both Pere *or* Laia are coming.', 'and', 'The pattern is ‘both … and …’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('All + singular', 'All *student* must wear a uniform.', 'students', '‘All’ + plural: ‘all students’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Everything', 'Everything *are* fine.', 'is', '‘Everything’ takes a singular verb. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Each other', 'They love *every* other.', 'each', 'Fixed phrase: ‘each other’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, how many, multiple choice and spot-the-mistake. In the typing questions write all, both, every or each. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('number', 'How many?'),
 'fill': [
  ('Both', 'I have two dogs. [[Both|both]] of them are brown.', 'all / both', 'Two dogs: ‘both’. Two → both; the whole group → all; every + singular noun; each = one by one.', 'Two → both.'),
  ('All', '[[All|all]] the cakes were sold in an hour.', 'all / both', 'The whole group: ‘all’. Two → both; the whole group → all; every + singular noun; each = one by one.', 'Group → all.'),
  ('Every', 'I read the news [[every]] morning.', 'every / each', 'Frequency: ‘every morning’. Two → both; the whole group → all; every + singular noun; each = one by one.', 'Frequency → every.'),
  ('Each', 'The two winners [[each]] got a medal.', 'every / each', 'One by one, two people: ‘each’. Two → both; the whole group → all; every + singular noun; each = one by one.', 'One by one → each.'),
  ],
 'order': [
  ('Both', 'Both my sisters sing.', []),
  ('All', 'All the shops are closed.', []),
  ('Every', 'I run every day.', []),
  ('Each', 'Each room has a key.', []),
  ],
 'customItems': [
  ('Number', '‘Both’ is for…', ['exactly two', 'three or more', 'one', 'uncountable nouns'],
   ['That’s ‘all’.', 'That’s ‘a / one’.', 'That’s ‘all’ (all the water).'],
   'Both = two. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Number', '‘Every’ is for…', ['three or more, as a group', 'exactly two', 'uncountable nouns', 'plural nouns'],
   ['For two use ‘both’ or ‘each’.', 'Uncountables take ‘all’.', '‘Every’ takes singular nouns.'],
   'Every = all of a group of 3+, singular noun. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Number', 'Which word can be used for TWO things one by one?', ['each', 'every', 'all', 'everyone'],
   ['‘Every’ needs three or more.', '‘All’ is the whole group.', '‘Everyone’ is for people in general.'],
   'Each works for two: each hand. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Number', 'Which word takes a PLURAL verb?', ['all (the students)', 'every', 'each', 'everyone'],
   ['‘Every’ takes a singular verb.', '‘Each’ takes a singular verb.', '‘Everyone’ takes a singular verb.'],
   'All the students are… Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ],
 'mc': [
  ('Every', '___ house in the street is white.', ['Every', 'All', 'Both', 'Each of'],
   ['‘All’ needs a plural noun.', '‘Both’ needs a plural noun.', '‘Each of’ needs ‘the’ + plural.'],
   'Every + singular noun. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Both', 'She invited ___ of us — me and my brother.', ['both', 'all', 'every', 'each'],
   ['Two people: ‘both’.', '‘Every of’ is wrong.', '‘Each of us’ is possible but less natural here.'],
   'Two people: both of us. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('All', 'We stayed in bed ___ morning.', ['all', 'every', 'each', 'both'],
   ['‘Every morning’ means many mornings.', '‘Each morning’ means many mornings.', '‘Both morning’ is wrong.'],
   'The whole morning: all morning. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Verb', 'Each of my friends ___ a bike.', ['has', 'have', 'are having', 'were'],
   ['‘Each of’ takes a singular verb.', 'Plural verb.', 'Plural verb.'],
   'Each of + singular verb. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ],
 'error': [
  ('Every + plural', 'I see her every *weeks*.', 'week', '‘Every week’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('All for two', '*All* my hands are dirty.', 'Both', 'Two hands: ‘both’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Verb after every', 'Everybody *love* pizza.', 'loves', 'Singular verb. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ('Every of', '*Every* of the rooms is clean.', 'Each', 'Never ‘every of’. Two → both; the whole group → all; every + singular noun; each = one by one.'),
  ],
}
