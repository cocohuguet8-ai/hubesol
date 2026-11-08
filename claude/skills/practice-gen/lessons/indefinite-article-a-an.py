TITLE = 'A/An: the indefinite article'
AUX = (['a', 'an'], None, 'a')
NEXT = ('The: the definite article', '/grammar/articles/definite-article-the/')
BODY = r'''
## What is the indefinite article?

**A** and **an** go before a **singular countable noun** when we don't mean one specific thing. (Choose *a* or *an* by the first **sound** of the next word.)

| Use | Example |
|---|---|
| First mention | I saw **a** dog in the park. |
| Jobs | She's **a** nurse. |
| One of many | He's **a** friend of mine. |
| "One" | I need **a** pen. |
| Per / every | twice **a** week, 50 km **an** hour |
| Exclamations | What **a** day! |

## When to use a / an

### 1. First mention

When we talk about something for the first time, the listener doesn't know which one yet.

- I bought **a** new jacket yesterday.
- There's **a** cat on the roof.

### 2. Jobs and roles

In English, jobs always need an article.

- My mum is **a** teacher. — He wants to be **an** engineer.

> ⚠️ Typical error: ~~She is doctor.~~ → *She is a doctor.*

### 3. One of a group

- Lisbon is **a** beautiful city. (one of many beautiful cities)
- It's **an** old song.

### 4. Meaning "one"

- I'd like **a** coffee, please. — Wait **a** minute.

### 5. Per (time, speed, price)

- I go swimming three times **a** week.
- Apples are two euros **a** kilo.

### 6. Exclamations with *what*

- What **a** great idea! — What **an** amazing view!

## When NOT to use a / an

### 1. Plural nouns

- ~~a books~~ → **books** / **some books**

### 2. Uncountable nouns

- ~~a water~~, ~~an information~~, ~~an advice~~ → **some water**, **some information**, **a piece of advice**

> ⚠️ Typical error: ~~Can you give me an advice?~~ → *Can you give me some advice?*

### 3. Before a possessive

- ~~a my friend~~ → **a friend of mine** / **my friend**

## Have / There is + a / an

| Pattern | Example |
|---|---|
| have got + a | I've got **a** brother. |
| there is + a | There's **a** bank near here. |
| Is there + a | Is there **a** café? |

## Common mistakes

**1. No article with jobs.** *~~He's mechanic.~~* → **He's a mechanic.**

**2. A with plurals.** *~~I have a cats.~~* → **I have cats.**

**3. A with uncountables.** *~~a homework~~* → **some homework**.

**4. Missing article with singular nouns.** *~~I have car.~~* → **I have a car.**

**Pro tip:** a singular countable noun almost never stands alone — it needs **a/an**, **the**, or a word like **my**.
'''

GAP = ('Fill in the gaps',
  'Type a, an, or — (dash) when no article is needed. Twenty original sentences.',
  [
  ('First mention', 'I saw [[a]] fox in the garden this morning.', 'a / an / —', 'First mention of a singular countable noun: ‘a fox’.'),
  ('First mention', 'There’s [[an]] old castle near my town.', 'a / an / —', 'First mention; ‘old’ starts with a vowel sound: ‘an old castle’.'),
  ('Job', 'My sister is [[a]] nurse.', 'a / an / —', 'Jobs need an article in English: ‘a nurse’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Job', 'He wants to be [[an]] architect.', 'a / an / —', 'Job + vowel sound: ‘an architect’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Job', 'My uncle works as [[a]] chef.', 'a / an / —', '‘Work as’ + job also needs an article: ‘as a chef’.'),
  ('One of many', 'Barcelona is [[a]] big city.', 'a / an / —', 'One of many big cities: ‘a big city’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('One of many', 'She’s [[a]] friend of mine.', 'a / an / —', 'One friend among several: ‘a friend of mine’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('One', 'Can I have [[a]] glass of water?', 'a / an / —', '‘A’ here means ‘one’: a glass of water. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('One', 'Wait [[a]] minute, please.', 'a / an / —', '‘A minute’ = one minute. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Per', 'I play tennis twice [[a]] week.', 'a / an / —', '‘A’ means ‘per’: twice a week. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Per', 'The car was going 100 kilometres [[an]] hour.', 'a / an / —', '‘Per’ + silent h: ‘an hour’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Exclamation', 'What [[a]] beautiful day!', 'a / an / —', '‘What’ + singular countable noun needs ‘a’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Exclamation', 'What [[an]] amazing goal!', 'a / an / —', '‘What’ + ‘amazing’ (vowel sound): ‘what an’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('There is', 'Is there [[a]] bank near here?', 'a / an / —', 'First mention after ‘Is there’: ‘a bank’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Have got', 'I’ve got [[a]] younger brother.', 'a / an / —', '‘Have got’ + singular countable noun: ‘a younger brother’.'),
  ('Plural', 'We saw [[—|-]] dolphins on our holiday.', 'a / an / —', 'Plural noun: no ‘a’. Write the dash. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Plural', 'She has [[—|-]] green eyes.', 'a / an / —', '‘Eyes’ is plural, so no indefinite article. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Uncountable', 'I need [[—|-]] information about the trip.', 'a / an / —', '‘Information’ is uncountable: never ‘an information’.'),
  ('Uncountable', 'They gave us [[—|-]] good advice.', 'a / an / —', '‘Advice’ is uncountable: no ‘a’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Uncountable', 'Do you want [[—|-]] milk in your tea?', 'a / an / —', '‘Milk’ is uncountable here: no ‘a’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with a and an.',
  [
  ('First mention', 'I saw a fox.', []),
  ('First mention', 'There is a castle here.', []),
  ('Job', 'She is a nurse.', []),
  ('Job', 'He is an artist.', []),
  ('Job', 'My dad is a pilot.', []),
  ('One of many', 'Rome is a big city.', []),
  ('One of many', 'She is a friend of mine.', []),
  ('One', 'I need a pen.', []),
  ('One', 'Wait a minute.', []),
  ('Per', 'I swim twice a week.', []),
  ('Per', 'It costs two euros a kilo.', []),
  ('Exclamation', 'What a great idea!', []),
  ('Exclamation', 'What an amazing view!', []),
  ('There is', 'Is there a café near here?', []),
  ('Have got', 'I have got a sister.', []),
  ('First mention', 'We bought a new car.', []),
  ('Job', 'He wants to be an engineer.', []),
  ('One', 'Can I have a coffee?', []),
  ('Per', 'We eat out once a month.', []),
  ('One of many', 'It is an old song.', []),
  ])

MATCH = {'title': 'Why a / an?', 'subtitle': 'Tap a sentence, then tap the reason for the article.',
  'leftLabel': 'Sentence', 'rightLabel': 'Reason', 'rightLabelSub': '(use)', 'reviewArrowPrefix': '',
  'pairs': [
  ('I saw a fox in the garden.', 'first mention'),
  ('My mum is a dentist.', 'job'),
  ('Rome is a beautiful city.', 'one of many'),
  ('I go to the gym three times a week.', 'per'),
  ('What a lovely surprise!', 'exclamation'),
  ('I’d like a coffee, please.', 'meaning “one”'),
  ('There’s a new shop on my street.', 'first mention'),
  ('He’s an electrician.', 'job'),
  ('She’s a cousin of mine.', 'one of many'),
  ('Bananas are one euro a kilo.', 'per'),
  ('What an ugly dog!', 'exclamation'),
  ('Wait a second!', 'meaning “one”'),
  ('We met a strange man at the station.', 'first mention'),
  ('I want to be a vet.', 'job'),
  ('It’s an interesting book.', 'one of many'),
  ('He drives at 50 miles an hour.', 'per'),
  ('What a mess!', 'exclamation'),
  ('Can I borrow a pencil?', 'meaning “one”'),
  ('Is there a pharmacy near here?', 'first mention'),
  ('My brother is a firefighter.', 'job'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Singular countable noun → a / an. Plural or uncountable → no article.',
  [
  ('First mention', 'Yesterday I met ___ interesting woman on the train.', ['an', 'a', 'the', '—'],
   ['‘Interesting’ starts with a vowel sound, so not ‘a’.', '‘The’ would mean the listener already knows her.', 'A singular countable noun needs an article.'],
   'First mention + vowel sound: an interesting woman. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Job', 'My brother is ___ police officer.', ['a', 'an', 'the', '—'],
   ['‘Police’ starts with a consonant sound.', '‘The police officer’ suggests a specific one we know.', 'Jobs need an article in English.'],
   'Jobs take a/an: a police officer. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Job', 'She works as ___ engineer at a big company.', ['an', 'a', 'the', '—'],
   ['‘Engineer’ starts with a vowel sound.', '‘The engineer’ would be a specific one.', '‘Work as’ + job needs an article.'],
   '‘Work as’ + job: as an engineer. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Plural', 'I bought ___ apples at the market.', ['—', 'an', 'a', 'one'],
   ['‘Apples’ is plural, so no ‘an’.', '‘Apples’ is plural, so no ‘a’.', '‘One’ doesn’t go with a plural noun.'],
   'Plural noun: no indefinite article. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Uncountable', 'Can you give me ___ advice?', ['some', 'an', 'a', 'one'],
   ['‘Advice’ is uncountable: never ‘an advice’.', '‘Advice’ is uncountable: never ‘a advice’.', '‘One advice’ is wrong; say ‘a piece of advice’.'],
   'Uncountable noun: some advice. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Per', 'I visit my grandparents once ___ month.', ['a', 'the', 'an', 'per a'],
   ['‘Once the month’ is wrong.', '‘Month’ starts with a consonant sound.', '‘Per a’ is not English.'],
   '‘A’ means ‘per’: once a month. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Exclamation', 'What ___ terrible film!', ['a', 'an', 'the', '—'],
   ['‘Terrible’ starts with a consonant sound.', '‘What the’ isn’t used in exclamations.', 'Singular countable after ‘what’ needs ‘a’.'],
   'What + a + adjective + singular noun. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Exclamation', 'What ___ lovely weather!', ['—', 'a', 'an', 'the'],
   ['‘Weather’ is uncountable: no ‘a’.', '‘Weather’ is uncountable: no ‘an’.', '‘What the’ isn’t used in exclamations.'],
   'Uncountable after ‘what’: no article. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('One', 'I’d like ___ orange juice and two coffees, please.', ['an', 'a', 'the', 'some a'],
   ['‘Orange’ starts with a vowel sound.', '‘The’ is for a specific one.', '‘Some a’ is not English.'],
   'In a café, ‘an orange juice’ = one glass. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('There is', 'There’s ___ supermarket at the end of the street.', ['a', 'an', 'the', '—'],
   ['‘Supermarket’ starts with a consonant sound.', '‘There’s the’ is unusual for first mention.', 'A singular countable noun needs an article.'],
   '‘There is’ + first mention: a supermarket. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Have got', 'Have you got ___ umbrella?', ['an', 'a', 'the', '—'],
   ['‘Umbrella’ starts with a vowel sound.', '‘The umbrella’ is a specific one.', 'A singular countable noun needs an article.'],
   'Have got + an umbrella. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('One of many', 'Shakespeare was ___ English writer.', ['an', 'a', 'the', '—'],
   ['‘English’ starts with a vowel sound.', '‘The English writer’ suggests only one.', 'A singular noun needs an article.'],
   'One of many English writers: an English writer. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Uncountable', 'We need ___ furniture for the new flat.', ['some', 'a', 'an', 'one'],
   ['‘Furniture’ is uncountable.', '‘Furniture’ is uncountable.', '‘One furniture’ is wrong; say ‘a piece of furniture’.'],
   'Uncountable: some furniture. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Possessive', 'He’s ___ old friend of my father’s.', ['an', 'a', 'the', 'my'],
   ['‘Old’ starts with a vowel sound.', '‘The’ would suggest the only one.', '‘My old friend of my father’s’ repeats the possessive.'],
   'a/an + noun + of + possessive: an old friend of my father’s.'),
  ('Per', 'The speed limit is 30 miles ___ hour.', ['an', 'a', 'the', 'per a'],
   ['Silent h in ‘hour’ → an.', '‘The hour’ isn’t used for speed.', '‘Per a’ is not English.'],
   '‘Per’ + silent h: an hour. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Job', 'Is your sister ___ student?', ['a', 'an', 'the', '—'],
   ['‘Student’ starts with a consonant sound.', '‘The student’ is a specific one.', 'Roles need an article.'],
   'Role: a student. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Which', 'Which sentence is correct?', ['She’s an actress.', 'She’s actress.', 'She’s a actress.', 'She’s the actress.'],
   ['Jobs need an article.', '‘Actress’ starts with a vowel sound.', '‘The actress’ means a specific one we know.'],
   'Job + vowel sound: an actress. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Which', 'Which sentence is correct?', ['I have some homework.', 'I have a homework.', 'I have an homework.', 'I have one homework.'],
   ['‘Homework’ is uncountable.', '‘Homework’ is uncountable.', '‘One homework’ is wrong.'],
   'Uncountable: some homework. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('First mention', 'I had ___ strange dream last night.', ['a', 'an', 'the', '—'],
   ['‘Strange’ starts with a consonant sound.', '‘The strange dream’ suggests we know it.', 'A singular noun needs an article.'],
   'First mention: a strange dream. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Plural', 'They are ___ doctors.', ['—', 'a', 'an', 'one'],
   ['Plural noun: no ‘a’.', 'Plural noun: no ‘an’.', '‘One’ doesn’t go with a plural.'],
   'Plural job: no article. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('Wrong form', 'My mother is *an* teacher.', 'a', '‘Teacher’ starts with a consonant sound: ‘a teacher’.'),
  ('Wrong article', 'He works as *the* mechanic in a small garage.', 'a', 'Jobs take a/an, not ‘the’: ‘as a mechanic’.'),
  ('Wrong form', 'I have *an* car.', 'a', '‘Car’ starts with a consonant sound: ‘a car’.'),
  ('Wrong article', 'Excuse me, is there *the* bank near here?', 'a', 'First mention after ‘is there’: ‘a bank’.'),
  ('Wrong form', 'She’s *a* engineer.', 'an', '‘Engineer’ starts with a vowel sound: ‘an engineer’.'),
  ('Wrong form', 'It takes *a* hour to get there.', 'an', 'Silent h: ‘an hour’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Wrong form', 'What *an* nice surprise!', 'a', '‘Nice’ starts with a consonant sound: ‘a’.'),
  ('A + plural', 'I bought *a* shoes yesterday.', 'some', '‘Shoes’ is plural: ‘some shoes’ or just ‘shoes’.'),
  ('A + plural', 'We saw *a* dolphins in the sea.', 'some', '‘Dolphins’ is plural: ‘some dolphins’ or just ‘dolphins’.'),
  ('A + uncountable', 'Can you give me *an* advice?', 'some', '‘Advice’ is uncountable: ‘some advice’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('A + uncountable', 'I need *an* information.', 'some', '‘Information’ is uncountable: ‘some information’.'),
  ('A + uncountable', 'I drink *a* water every morning.', 'some', '‘Water’ is uncountable: ‘some water’ (or ‘a glass of water’).'),
  ('A + uncountable', 'She gave me *a* money.', 'some', '‘Money’ is uncountable: ‘some money’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Per', 'I go swimming twice *the* week.', 'a', '‘A’ means ‘per’: ‘twice a week’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Per', 'Tomatoes are three euros *the* kilo.', 'a', 'For prices per unit we normally say ‘a kilo’.'),
  ('Exclamation', 'What *the* lovely house!', 'a', 'Exclamations: ‘What a lovely house!’ Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Possessive', 'He’s *my* friend of mine.', 'a', 'Say ‘a friend of mine’ or ‘my friend’, not both.'),
  ('Wrong article', 'I saw *the* fox in the garden — it was beautiful!', 'a', 'First mention, the listener doesn’t know it yet: ‘a fox’.'),
  ('Wrong article', 'My dad is *the* pilot.', 'a', 'For jobs we use ‘a/an’: ‘a pilot’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Wrong form', 'Have you got *a* umbrella?', 'an', '‘Umbrella’ starts with a vowel sound: ‘an umbrella’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, which use, multiple choice and spot-the-mistake. In the typing questions write a, an, or — (dash) for no article. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('use', 'Which use?'),
 'fill': [
  ('Job', 'My aunt is [[a]] lawyer.', 'a / an / —', 'Jobs need an article in English: ‘a lawyer’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.', 'Job → a/an.'),
  ('Per', 'I drink coffee three times [[a]] day.', 'a / an / —', '‘A’ means ‘per’: three times a day. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.', 'Per → a.'),
  ('Uncountable', 'Can I have [[—|-]] bread, please?', 'a / an / —', '‘Bread’ is uncountable: no ‘a’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.', 'Uncountable → no a/an.'),
  ('First mention', 'I found [[an]] old photo in a box.', 'a / an / —', 'First mention + vowel sound: ‘an old photo’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.', 'First mention → a/an.'),
  ],
 'order': [
  ('Job', 'He is a dentist.', []),
  ('Per', 'I run once a week.', []),
  ('Exclamation', 'What a nice day!', []),
  ('First mention', 'I saw an owl.', []),
  ],
 'customItems': [
  ('Use', 'In ‘She’s a dentist’, why ‘a’?', ['job', 'per', 'exclamation', 'plural'],
   ['‘Per’ is for time or price: twice a week.', 'Exclamations start with ‘what’.', '‘Dentist’ is singular.'],
   'Jobs take a/an. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Use', 'In ‘twice a week’, ‘a’ means…', ['per', 'the', 'one of many', 'first mention'],
   ['‘The week’ would be a specific week.', 'It isn’t about a group.', 'It isn’t introducing a new thing.'],
   '‘A’ = per / every. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Use', 'Why no article in ‘I need information’?', ['it’s uncountable', 'it’s a job', 'it’s plural', 'it’s first mention'],
   ['It isn’t a job.', '‘Information’ isn’t plural.', 'First mention of a countable noun would need ‘a’.'],
   'Uncountable nouns never take a/an. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Use', 'In ‘I saw a fox’, why ‘a’?', ['first mention', 'job', 'per', 'exclamation'],
   ['It isn’t a job.', 'It isn’t about frequency or price.', 'There’s no ‘what’.'],
   'First mention of a singular countable noun. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ],
 'mc': [
  ('Plural', 'We saw ___ elephants at the safari park.', ['—', 'an', 'a', 'one'],
   ['Plural noun: no ‘an’.', 'Plural noun: no ‘a’.', '‘One’ doesn’t go with a plural.'],
   'Plural: no indefinite article. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Exclamation', 'What ___ awful noise!', ['an', 'a', 'the', '—'],
   ['‘Awful’ starts with a vowel sound.', '‘What the’ isn’t used.', 'Singular countable needs an article.'],
   'What + an + awful noise. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Uncountable', 'They gave me ___ useful advice.', ['some', 'a', 'an', 'one'],
   ['‘Advice’ is uncountable.', '‘Advice’ is uncountable.', '‘One advice’ is wrong.'],
   'Uncountable: some advice. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Job', 'He wants to be ___ actor.', ['an', 'a', 'the', '—'],
   ['‘Actor’ starts with a vowel sound.', '‘The actor’ is a specific one.', 'Jobs need an article.'],
   'Job + vowel sound: an actor. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ],
 'error': [
  ('Wrong article', 'My cousin is *the* nurse.', 'a', 'Jobs take a/an: ‘a nurse’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('A + uncountable', 'I need *a* help.', 'some', '‘Help’ is uncountable: ‘some help’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('Per', 'I see her once *the* month.', 'a', '‘Once a month’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ('A + plural', 'I bought *a* new clothes.', 'some', '‘Clothes’ is plural: ‘some new clothes’. Remember: a singular countable noun needs a/an; plurals and uncountables don’t take it.'),
  ],
}
