TITLE = 'This, That, These & Those'
AUX = (['this', 'that', 'these', 'those'], None, 'these')
NEXT = ('All, Both, Every & Each', '/grammar/nouns-determiners/all-both-every-each/')
BODY = r'''
## The four words

| | Near (here) | Far (there) |
|---|---|---|
| **Singular** | **this** book | **that** book |
| **Plural** | **these** books | **those** books |

- **This** pen is mine. (in my hand) — **That** car is red. (over there)
- **These** shoes are new. (I'm wearing them) — **Those** birds are loud. (in the tree)

## *This* and *these* — near

### 1. Things near you

- **This** bag is heavy. — Are **these** your keys?

### 2. Now / the present

- I'm busy **this** week. — **These** days I walk to work.

> ⚠️ Typical error: ~~This books are mine.~~ → Plural: *These books are mine.*

## *That* and *those* — far

### 1. Things far from you

- Look at **that** dog! — **Those** mountains are beautiful.

### 2. The past

- I remember **that** day. — In **those** days we didn't have phones.

> ⚠️ Typical error: ~~Those house is old.~~ → Singular: *That house is old.*

## With or without a noun

### 1. Before a noun (determiner)

- **This** song is great. — I love **those** jeans.

### 2. Alone (pronoun)

- **This** is my brother. — What's **that**? — **These** are delicious!

## Useful phrases

| Phrase | Use |
|---|---|
| **This is** Anna. | introducing someone |
| Hello, **this is** Tom. | on the phone |
| **That's** right! / **That's** great! | reacting to what someone said |
| Is **that** you? | asking who it is |

## Verb agreement

| Singular | Plural |
|---|---|
| **This is** … / **That is** (That's) … | **These are** … / **Those are** … |
| **Is this** your coat? | **Are these** your coats? |

> ⚠️ Typical error: ~~These is my friends.~~ → *These are my friends.*

## *This one / that one*

Use *one* to avoid repeating a singular noun:

- Which cake do you want? — **This one**, please.
- I don't like this shirt. I prefer **that one**.

For plurals, use *these / those* alone (*these ones* is informal).

## Common mistakes

**1. Singular with plural noun.** *~~this shoes~~* → **these shoes**.

**2. Plural with singular noun.** *~~these book~~* → **this book**.

**3. Wrong verb.** *~~Those is nice.~~* → **Those are nice.**

**4. Near/far confusion.** Holding it? → **this**. Pointing far away? → **that**.

**Pro tip:** *th-is / th-ese* = **here**; *th-at / th-ose* = **there**.
'''

GAP = ('Fill in the gaps',
  'Type this, that, these or those. Look at near/far and singular/plural. Twenty original sentences.',
  [
  ('Near singular', '[[This|this]] bag is very heavy. (in my hand)', 'this / these', 'Near + singular: ‘this’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Near singular', 'Is [[this]] your phone? (on the table here)', 'this / these', 'Near + singular: ‘this’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Near plural', '[[These|these]] biscuits are delicious! (I’m eating them)', 'this / these', 'Near + plural: ‘these’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Near plural', 'Are [[these]] your gloves? (here, on my chair)', 'this / these', 'Near + plural: ‘these’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Far singular', 'Look at [[that]] bird in the sky!', 'that / those', 'Far + singular: ‘that’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Far singular', 'Who is [[that]] man over there?', 'that / those', 'Far + singular: ‘that’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Far plural', '[[Those|those]] houses on the hill are very old.', 'that / those', 'Far + plural: ‘those’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Far plural', 'Can you see [[those]] boats on the sea?', 'that / those', 'Far + plural: ‘those’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Introducing', 'Mum, [[this]] is my friend Lucas.', 'this / that', 'Introducing someone next to you: ‘this is’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Phone', 'Hello, [[this]] is Marta. Can I speak to Joan?', 'this / that', 'On the phone, say who you are: ‘this is’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Reaction', 'I passed my exam! — [[That’s|That is|that’s|that is|Thats]] fantastic!', 'this / that', 'Reacting to what someone said: ‘that’s’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Present time', 'I’m very busy [[this]] week.', 'this / that', 'Now / present: ‘this week’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Past time', 'In [[those]] days, people wrote letters.', 'these / those', 'The past + plural: ‘those days’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Present time', '[[These|these]] days I go to bed early.', 'these / those', 'Now + plural: ‘these days’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Verb', 'These [[are]] my new trainers.', 'is / are', '‘These’ is plural: ‘are’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Verb', 'That [[is]] a beautiful painting.', 'is / are', '‘That’ is singular: ‘is’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Verb', '[[Are|are]] those your children?', 'Is / Are', '‘Those’ is plural: ‘Are those…?’ Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('One', 'Which T-shirt do you want? — [[This|this]] one, please.', 'this / these', 'Singular + ‘one’: ‘this one’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Pronoun', 'What’s [[that]]? There, on the wall.', 'this / that', 'Far, no noun: ‘that’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Pronoun', 'Try [[these]] — they’re my favourite sweets.', 'these / those', 'Near plural, no noun: ‘these’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with this, that, these and those.',
  [
  ('Near singular', 'This is my bag.', []),
  ('Near singular', 'This book is great.', []),
  ('Near plural', 'These are my keys.', []),
  ('Near plural', 'These shoes are new.', []),
  ('Far singular', 'That car is red.', []),
  ('Far singular', 'Who is that girl?', []),
  ('Far plural', 'Those birds are loud.', []),
  ('Far plural', 'Look at those clouds.', []),
  ('Introducing', 'This is my sister.', []),
  ('Phone', 'Hello, this is Tom.', []),
  ('Reaction', 'That’s a great idea!', []),
  ('Present time', 'I’m busy this week.', []),
  ('Past time', 'I remember that day.', []),
  ('Question', 'Is this your coat?', []),
  ('Question', 'Are these your pens?', []),
  ('Question', 'What is that over there?', []),
  ('One', 'I want this one.', []),
  ('One', 'I prefer that one.', []),
  ('Past time', 'Those were good times.', []),
  ('Present time', 'These days I cycle.', []),
  ])

MATCH = {'title': 'Which word?', 'subtitle': 'Tap a description, then tap the right word.',
  'leftLabel': 'Situation', 'rightLabel': 'Word', 'rightLabelSub': '', 'reviewArrowPrefix': '',
  'pairs': [
  ('one apple in my hand', 'this'), ('two apples in my hand', 'these'), ('one star in the sky', 'that'), ('many stars in the sky', 'those'),
  ('the pen I’m holding', 'this'), ('the shoes I’m wearing', 'these'), ('a car across the street', 'that'), ('the cars across the street', 'those'),
  ('introducing a friend next to me', 'this'), ('the photos on my phone', 'these'), ('a house far away', 'that'), ('the hills far away', 'those'),
  ('the week we’re in now', 'this'), ('nowadays (plural)', 'these'), ('a day long ago', 'that'), ('days long ago', 'those'),
  ('on the phone: “Hi, ___ is Ana.”', 'this'), ('the keys in my pocket', 'these'), ('“___’s great news!”', 'that'), ('the birds in that tree', 'those'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Near → this / these. Far → that / those. One → this / that. Many → these / those.',
  [
  ('Near singular', '___ sandwich is really good. Do you want some?', ['This', 'These', 'Those', 'That’s'],
   ['‘Sandwich’ is singular: not ‘these’.', '‘Those’ is plural and far.', '‘That’s sandwich’ isn’t English.'],
   'Near + singular: this. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Far plural', 'I love ___ earrings you’re wearing!', ['those', 'this', 'that', 'these'],
   ['‘This’ is singular, but ‘earrings’ is plural.', '‘That’ is singular, but ‘earrings’ is plural.', 'The earrings are on the other person, not with me: ‘those’ fits better.'],
   'Plural, on the other person: those. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Far singular', 'Can you see ___ plane up there?', ['that', 'this', 'these', 'those'],
   ['The plane is far: not ‘this’.', '‘Plane’ is singular.', '‘Plane’ is singular.'],
   'Far + singular: that. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Far plural', '___ trees over there are very tall.', ['Those', 'These', 'That', 'This'],
   ['The trees are far: not ‘these’.', '‘Trees’ is plural.', '‘Trees’ is plural.'],
   'Far + plural: those. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Near plural', 'Are ___ your glasses? They were on my desk.', ['these', 'this', 'that', 'it'],
   ['‘Glasses’ is plural.', '‘Glasses’ is plural.', '‘It’ doesn’t go with ‘are’.'],
   'Near + plural: these. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Introducing', 'Dad, ___ is my teacher, Mr Puig.', ['this', 'these', 'those', 'it'],
   ['One person: not ‘these’.', 'One person, next to you: not ‘those’.', 'We don’t introduce people with ‘it’.'],
   'Introducing: this is… Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Phone', 'Hi, ___ is Laura. Is Pau there?', ['this', 'that', 'these', 'here'],
   ['On the phone, ‘that’ is used for the other person.', 'One person: not ‘these’.', '‘Here is Laura’ isn’t natural.'],
   'Phone: this is… Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Reaction', 'We won the match! — ___ amazing!', ['That’s', 'This', 'Those are', 'These are'],
   ['‘This amazing’ has no verb.', 'Plural doesn’t fit.', 'Plural doesn’t fit.'],
   'Reaction: that’s… Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Verb', 'These ___ my favourite jeans.', ['are', 'is', 'am', 'be'],
   ['‘These’ is plural.', '‘Am’ is only with ‘I’.', 'We need a conjugated verb.'],
   'These are. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Verb', '___ that your sister?', ['Is', 'Are', 'Am', 'Do'],
   ['‘That’ is singular.', '‘Am’ is only with ‘I’.', '‘Do’ doesn’t fit with a noun.'],
   'Is that…? Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Past time', 'In ___ days, there were no cars.', ['those', 'these', 'this', 'that'],
   ['‘These days’ means now.', '‘Days’ is plural.', '‘Days’ is plural.'],
   'Past + plural: those days. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Present time', 'I’m on holiday ___ week!', ['this', 'that', 'these', 'those'],
   ['‘That week’ is a different week.', '‘Week’ is singular.', '‘Week’ is singular.'],
   'Now: this week. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('One', 'Which pen is yours? — ___ one, on the left.', ['That', 'Those', 'These', 'It'],
   ['‘One’ is singular.', '‘One’ is singular.', '‘It one’ isn’t English.'],
   'Singular + one: that one. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Pronoun', 'What’s ___ noise? Can you hear it?', ['that', 'these', 'those', 'this is'],
   ['‘Noise’ is singular.', '‘Noise’ is singular.', '‘What’s this is’ isn’t English.'],
   'A sound from somewhere else: that. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Near singular', 'I don’t like ___ soup. It’s too salty.', ['this', 'these', 'those', 'that’s'],
   ['‘Soup’ is uncountable/singular.', '‘Soup’ is singular.', '‘That’s soup’ changes the meaning.'],
   'Near + singular: this soup. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Far plural', 'Who are ___ people at the door?', ['those', 'that', 'this', 'it'],
   ['‘People’ is plural.', '‘People’ is plural.', '‘It’ doesn’t fit.'],
   'Far + plural: those. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Which', 'Which sentence is correct?', ['These books are mine.', 'This books are mine.', 'These book is mine.', 'Those book are mine.'],
   ['‘Books’ is plural.', '‘These’ needs a plural noun.', '‘Those’ needs a plural noun.'],
   'Plural: these books are. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Which', 'Which sentence is correct?', ['That house is old.', 'Those house is old.', 'That houses are old.', 'These house is old.'],
   ['‘House’ is singular.', '‘That’ needs a singular noun.', '‘These’ needs a plural noun.'],
   'Singular: that house is. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Near plural', '___ are my grandparents in the photo.', ['These', 'This', 'That', 'It'],
   ['‘Grandparents’ is plural.', '‘Grandparents’ is plural.', '‘It are’ isn’t English.'],
   'Plural, in my hands: these are. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Far singular', 'Is ___ your car in the car park?', ['that', 'this', 'those', 'these'],
   ['The car is far.', '‘Car’ is singular.', '‘Car’ is singular.'],
   'Far + singular: that. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('This + plural', '*This* shoes are too small.', 'These', 'Plural noun: ‘these shoes’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('This + plural', 'I bought *this* apples at the market.', 'these', 'Plural noun: ‘these apples’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('That + plural', 'Look at *that* clouds!', 'those', 'Plural noun: ‘those clouds’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('That + plural', '*That* people are very friendly.', 'Those', '‘People’ is plural: ‘those people’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('These + singular', '*These* book is very interesting.', 'This', 'Singular noun: ‘this book’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('These + singular', 'Can I borrow *these* pencil?', 'this', 'Singular noun: ‘this pencil’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Those + singular', '*Those* car is really fast.', 'That', 'Singular noun: ‘that car’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Those + singular', 'Who lives in *those* house?', 'that', 'Singular noun: ‘that house’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Verb', 'These *is* my friends from school.', 'are', '‘These’ is plural: ‘are’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Verb', 'Those *is* my parents.', 'are', '‘Those’ is plural: ‘are’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Verb', 'That *are* a good idea.', 'is', '‘That’ is singular: ‘is’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Verb', 'This *are* my brother, Marc.', 'is', '‘This’ is singular: ‘is’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Verb', '*Is* these your keys?', 'Are', '‘These’ is plural: ‘Are these…?’ Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Plural noun', 'These *flower* are beautiful.', 'flowers', '‘These’ needs a plural noun: ‘flowers’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Plural noun', 'Those *child* are noisy.', 'children', '‘Those’ needs a plural noun: ‘children’.'),
  ('Time', 'I’m very tired *that* week.', 'this', 'The present week: ‘this week’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Time', 'In *these* days, there was no internet.', 'those', 'The past: ‘in those days’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Phone', 'Hello, *that* is Pau speaking.', 'this', 'On the phone: ‘this is Pau’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Introducing', '*These* is my cousin Anna.', 'This', 'One person: ‘This is my cousin’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('One', 'I don’t want this one. I want *those* one.', 'that', 'Singular ‘one’: ‘that one’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, near or far, multiple choice and spot-the-mistake. In the typing questions write this, that, these or those. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('distance', 'Near or far?'),
 'fill': [
  ('Near plural', '[[These|these]] cookies are fresh. (on my plate)', 'this / these', 'Near + plural: ‘these’. Near → this/these; far → that/those; singular → this/that; plural → these/those.', 'Near plural → these.'),
  ('Far singular', 'What’s [[that]] building over there?', 'that / those', 'Far + singular: ‘that’. Near → this/these; far → that/those; singular → this/that; plural → these/those.', 'Far singular → that.'),
  ('Far plural', 'Look at [[those]] horses in the field!', 'that / those', 'Far + plural: ‘those’. Near → this/these; far → that/those; singular → this/that; plural → these/those.', 'Far plural → those.'),
  ('Introducing', 'Everyone, [[this]] is Sara.', 'this / that', 'Introducing: ‘this is’. Near → this/these; far → that/those; singular → this/that; plural → these/those.', 'Introducing → this.'),
  ],
 'order': [
  ('Near singular', 'This is my room.', []),
  ('Far plural', 'Those are my friends.', []),
  ('Near plural', 'These are new.', []),
  ('Far singular', 'That is my house.', []),
  ],
 'customItems': [
  ('Distance', 'A pen in your hand →', ['this pen', 'that pen', 'those pens', 'these pen'],
   ['‘That’ is for far things.', 'One pen, not many.', '‘These’ needs a plural noun.'],
   'Near + singular: this. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Distance', 'Mountains far away →', ['those mountains', 'these mountains', 'that mountains', 'this mountains'],
   ['‘These’ is for near things.', '‘That’ is singular.', '‘This’ is singular and near.'],
   'Far + plural: those. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Distance', 'Shoes you are wearing →', ['these shoes', 'those shoes', 'this shoes', 'that shoes'],
   ['They’re on you: near.', '‘This’ is singular.', '‘That’ is singular and far.'],
   'Near + plural: these. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Distance', 'A day long ago →', ['that day', 'this day', 'these days', 'those day'],
   ['‘This day’ is today.', '‘These days’ means nowadays.', '‘Those’ needs a plural noun.'],
   'Past + singular: that day. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ],
 'mc': [
  ('Near singular', '___ is my new bike!', ['This', 'These', 'Those', 'They'],
   ['One bike, near.', 'Plural and far.', '‘They is’ isn’t English.'],
   'Near + singular: this. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Far plural', 'Are ___ your dogs in the park?', ['those', 'that', 'this', 'it'],
   ['‘Dogs’ is plural.', '‘Dogs’ is plural.', '‘It’ doesn’t fit.'],
   'Far + plural: those. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Verb', 'Those ___ my cousins.', ['are', 'is', 'am', 'be'],
   ['‘Those’ is plural.', '‘Am’ is for ‘I’.', 'We need a conjugated verb.'],
   'Those are. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Reaction', 'I got the job! — ___ great news!', ['That’s', 'These are', 'Those', 'This are'],
   ['‘News’ is singular.', 'Missing a verb.', '‘This are’ is wrong.'],
   'Reaction: that’s great news. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ],
 'error': [
  ('This + plural', '*This* socks are wet.', 'These', 'Plural: ‘these socks’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Verb', 'These *is* my books.', 'are', '‘These’ is plural. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Those + singular', '*Those* boy is my brother.', 'That', 'Singular: ‘that boy’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ('Time', 'We’re going to Paris *that* weekend — in two days!', 'this', 'The coming weekend, now: ‘this weekend’. Near → this/these; far → that/those; singular → this/that; plural → these/those.'),
  ],
}
