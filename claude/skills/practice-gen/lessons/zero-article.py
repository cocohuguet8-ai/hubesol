TITLE = 'Zero Article'
AUX = (['the', 'a'], None, 'the')
NEXT = ('All articles', '/grammar/articles/')
BODY = r'''
## What is the zero article?

The **zero article** means **no article at all**. We use it when we talk about things **in general**, and in many fixed phrases.

| Use | Example |
|---|---|
| Plurals in general | **Dogs** are loyal. |
| Uncountables in general | **Water** is important. |
| Meals | have **breakfast** |
| Sports & games | play **tennis**, play **chess** |
| Languages & subjects | speak **French**, study **maths** |
| Transport with *by* | go **by** bus |
| Fixed places | go to **school**, be in **bed** |

## Things in general

### 1. Plural nouns

- **Cats** sleep a lot. — I love **books**.

### 2. Uncountable nouns

- **Love** is blind. — **Coffee** keeps me awake.

> ⚠️ Typical error: ~~The life is hard.~~ → *Life is hard.*

### 3. General vs specific

| General (zero) | Specific (*the*) |
|---|---|
| I like **cheese**. | **The** cheese in this shop is great. |
| **People** are friendly here. | **The** people next door are friendly. |

## Fixed phrases

### 1. Meals

- have **breakfast / lunch / dinner** — What's for **dinner**?

### 2. Sports, games, languages, subjects

- play **football**, play **cards**, speak **Catalan**, study **biology**

### 3. Transport with *by*

- go **by car / by train / by plane** — but: *on foot*

> ⚠️ Typical error: ~~by the bus~~ → *by bus.*

### 4. Days, months, seasons, holidays

- on **Monday**, in **July**, in **winter**, at **Christmas**

## Places for their main purpose

### School, university, church, hospital, prison, bed, work, home

When we go there **for the usual reason**, no article:

- She's at **school**. (as a student) — He's in **hospital**. (as a patient)
- I go to **work** at eight. — I'm going **home**.

### With *the*: just visiting the building

- My mum went to **the** school to talk to the teacher.

> ⚠️ Typical error: ~~I go to the bed at ten.~~ → *I go to bed at ten.*

## Common mistakes

**1. *The* for things in general.** *~~The children need love.~~* → **Children** need love.

**2. *The* with meals.** *~~have the lunch~~* → **have lunch**.

**3. *The* with transport.** *~~by the train~~* → **by train**.

**4. *The* with home.** *~~go to the home~~* → **go home**.

**Pro tip:** if you mean *all of them, in general*, or it's a fixed phrase like *go to bed*, use **no article**.
'''

GAP = ('Fill in the gaps',
  'Type the or a when needed, or — (dash) for the zero article. Twenty original sentences.',
  [
  ('General plural', '[[—|-]] Dogs need a lot of exercise.', 'the / a / —', 'Dogs in general: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('General plural', 'I’m afraid of [[—|-]] spiders.', 'the / a / —', 'Spiders in general: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('General uncountable', '[[—|-]] Water boils at 100 degrees.', 'the / a / —', 'Water in general: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('General uncountable', 'She hates [[—|-]] violence in films.', 'the / a / —', 'Violence in general: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Specific', '[[The|the]] water in this bottle is warm.', 'the / a / —', '‘In this bottle’ makes it specific: ‘the’. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Specific', '[[The|the]] dogs next door bark all night.', 'the / a / —', '‘Next door’ makes them specific: ‘the dogs’. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Meal', 'We usually have [[—|-]] dinner at nine.', 'the / a / —', 'Meals: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Meal', 'What did you have for [[—|-]] breakfast?', 'the / a / —', 'Meals: ‘for breakfast’. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Sport', 'My sister plays [[—|-]] volleyball.', 'the / a / —', 'Sports: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Game', 'Do you want to play [[—|-]] chess?', 'the / a / —', 'Games: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Language', 'Can you speak [[—|-]] Catalan?', 'the / a / —', 'Languages: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Subject', 'I have [[—|-]] maths on Mondays.', 'the / a / —', 'School subjects: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Transport', 'We went to Madrid by [[—|-]] train.', 'the / a / —', '‘By’ + transport: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Time', 'My birthday is in [[—|-]] April.', 'the / a / —', 'Months: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Time', 'We go skiing in [[—|-]] winter.', 'the / a / —', 'Seasons: usually zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Place purpose', 'The kids are at [[—|-]] school until five.', 'the / a / —', 'At school as students: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Place purpose', 'I’m tired. I’m going to [[—|-]] bed.', 'the / a / —', '‘Go to bed’ (to sleep): zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Place purpose', 'What time do you finish [[—|-]] work?', 'the / a / —', '‘Finish work’: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Place purpose', 'Let’s go [[—|-]] home.', 'the / a / —', '‘Go home’: never ‘to the home’. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Building visit', 'Dad went to [[the]] school to talk to my teacher.', 'the / a / —', 'Visiting the building, not studying: ‘the school’.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with the zero article.',
  [
  ('General plural', 'Cats sleep a lot.', []),
  ('General plural', 'I love books.', []),
  ('General uncountable', 'Love is blind.', []),
  ('General uncountable', 'Coffee keeps me awake.', []),
  ('Meal', 'We have lunch at two.', []),
  ('Meal', 'What is for dinner?', []),
  ('Sport', 'They play football.', []),
  ('Game', 'We play cards on Sundays.', []),
  ('Language', 'She speaks English.', []),
  ('Subject', 'I study biology.', []),
  ('Transport', 'I go to work by bus.', []),
  ('Transport', 'They travelled by plane.', []),
  ('Time', 'It is cold in winter.', []),
  ('Time', 'See you on Monday.', []),
  ('Place purpose', 'She is at school.', []),
  ('Place purpose', 'I go to bed early.', []),
  ('Place purpose', 'Let us go home.', []),
  ('Place purpose', 'He is at work.', []),
  ('Specific', 'The coffee here is great.', []),
  ('General plural', 'People are friendly here.', []),
  ])

MATCH = {'title': 'Zero or the?', 'subtitle': 'Tap a phrase, then tap the article it needs.',
  'leftLabel': 'Phrase', 'rightLabel': 'Article', 'rightLabelSub': '(the / —)', 'reviewArrowPrefix': '',
  'pairs': [
  ('have ___ breakfast', '—'), ('play ___ guitar', 'the'), ('go by ___ car', '—'), ('play ___ basketball', '—'),
  ('speak ___ Italian', '—'), ('___ sun', 'the'), ('go to ___ bed', '—'), ('___ best day ever', 'the'),
  ('in ___ summer', '—'), ('___ people next door', 'the'), ('go ___ home', '—'), ('___ moon', 'the'),
  ('study ___ history', '—'), ('___ first time', 'the'), ('on ___ Friday', '—'), ('___ internet', 'the'),
  ('at ___ work', '—'), ('play ___ piano', 'the'), ('___ dogs are loyal', '—'), ('___ door, please', 'the'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. In general or fixed phrase → no article. Specific or known → the.',
  [
  ('General plural', '___ teenagers often sleep late at weekends.', ['—', 'The', 'A', 'An'],
   ['‘The teenagers’ means specific ones.', '‘A’ doesn’t go with plurals.', '‘An’ doesn’t go with plurals.'],
   'Teenagers in general: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('General uncountable', 'I think ___ music helps me study.', ['—', 'the', 'a', 'an'],
   ['‘The music’ means specific music.', '‘Music’ is uncountable here.', '‘Music’ is uncountable here.'],
   'Music in general: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Specific', '___ music at the party was too loud.', ['The', '—', 'A', 'An'],
   ['‘At the party’ makes it specific.', '‘Music’ is uncountable.', '‘Music’ is uncountable.'],
   'Specific music: the. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Meal', 'Let’s meet after ___ lunch.', ['—', 'the', 'a', 'an'],
   ['Meals take no article.', 'Normal meals take no article.', '‘An’ doesn’t fit.'],
   'Meals: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Transport', 'I usually go to school by ___ bike.', ['—', 'the', 'a', 'my the'],
   ['‘By’ + transport: no article.', '‘By a bike’ is wrong.', '‘My the’ is not English.'],
   'By + transport: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Sport', 'Do you like watching ___ rugby?', ['—', 'the', 'a', 'an'],
   ['Sports take no article.', 'Sports take no article.', 'Sports take no article.'],
   'Sports: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Instrument', 'He’s learning ___ trumpet.', ['the', '—', 'a', 'an'],
   ['Instruments usually take ‘the’.', '‘A trumpet’ is an object, not the skill.', '‘Trumpet’ starts with a consonant sound.'],
   'Instruments: the trumpet. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Language', 'In Andorra people speak ___ Catalan.', ['—', 'the', 'a', 'an'],
   ['Languages take no article.', 'Languages take no article.', 'Languages take no article.'],
   'Languages: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Place purpose', 'My grandpa is in ___ hospital with a broken leg.', ['—', 'the', 'a', 'an'],
   ['In British English, a patient is ‘in hospital’.', '‘In a hospital’ is less natural for a patient in British English.', '‘An’ doesn’t fit.'],
   'In hospital (as a patient): zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Building visit', 'I went to ___ hospital to visit my grandpa.', ['the', '—', 'a', 'an'],
   ['Visiting the building: ‘the hospital’.', 'He’s visiting, not a patient.', '‘An’ doesn’t fit.'],
   'Visiting the building: the hospital. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Place purpose', 'It’s late — I’m going ___ home.', ['—', 'to the', 'the', 'to'],
   ['‘Go home’: no article, no ‘to’.', '‘Go the home’ is wrong.', '‘Go to home’ is wrong.'],
   'Go home: no article, no ‘to’. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Time', 'Shops are closed on ___ Sundays.', ['—', 'the', 'a', 'an'],
   ['Days take no article.', '‘A Sundays’ is wrong.', '‘An’ doesn’t fit.'],
   'Days: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Time', 'We met in ___ 2019.', ['—', 'the', 'a', 'an'],
   ['Years take no article.', 'Years take no article.', 'Years take no article.'],
   'Years: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Unique', '___ moon goes round the earth.', ['The', '—', 'A', 'An'],
   ['Unique things take ‘the’.', 'There’s only one moon.', 'There’s only one moon.'],
   'Unique: the moon. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Subject', 'She’s really good at ___ chemistry.', ['—', 'the', 'a', 'an'],
   ['Subjects take no article.', 'Subjects take no article.', 'Subjects take no article.'],
   'Subjects: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('General uncountable', '___ time is money.', ['—', 'The', 'A', 'An'],
   ['Time in general: no article.', '‘A time’ means one occasion.', '‘An’ doesn’t fit.'],
   'Abstract uncountable in general: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Which', 'Which is correct?', ['I go to bed at eleven.', 'I go to the bed at eleven.', 'I go to a bed at eleven.', 'I go bed at eleven.'],
   ['‘Go to bed’ (to sleep): no ‘the’.', '‘A bed’ is wrong here.', 'We need ‘to’.'],
   'Go to bed: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Which', 'Which is correct?', ['Children love games.', 'The children love the games.', 'A children love games.', 'Children love the games in general.'],
   ['This means specific children and games.', '‘A’ doesn’t go with plurals.', '‘In general’ + ‘the’ contradicts itself.'],
   'General plurals: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Specific', 'Have you read ___ books I lent you?', ['the', '—', 'a', 'some'],
   ['‘I lent you’ makes them specific.', '‘A’ doesn’t go with plurals.', '‘Some’ doesn’t identify them.'],
   'Specific: the books. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Meal', '___ dinner we had last night was delicious.', ['The', '—', 'A', 'An'],
   ['‘We had last night’ makes it specific.', 'This isn’t the general meal.', '‘An’ doesn’t fit.'],
   'A specific meal: the dinner. In general or in a fixed phrase → no article; specific or known → the.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('The for general', '*The life* is short.', 'Life', 'Life in general: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('The for general', '*The children* need lots of sleep.', 'Children', 'Children in general: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('The for general', 'I don’t eat *the meat*.', 'meat', 'Meat in general: zero article (‘I don’t eat meat’).'),
  ('The for general', '*The honesty* is very important.', 'Honesty', 'Abstract nouns in general: zero article.'),
  ('The for meal', 'We had *the breakfast* at the hotel.', 'breakfast', 'Meals: ‘had breakfast’.'),
  ('The for meal', 'Shall we have *the lunch* now?', 'lunch', 'Meals: ‘have lunch’.'),
  ('The for sport', 'My brother plays *the tennis*.', 'tennis', 'Sports: zero article (‘plays tennis’).'),
  ('The for language', 'She’s learning *the Arabic*.', 'Arabic', 'Languages: zero article.'),
  ('The for subject', 'I hate *the physics*.', 'physics', 'Subjects: zero article.'),
  ('The for transport', 'We came *by the train*.', 'by train', 'By + transport: zero article (‘by train’).'),
  ('A for transport', 'I go to work *by a car*.', 'by car', 'By + transport: zero article (‘by car’).'),
  ('The for time', 'My birthday is *in the March*.', 'in March', 'Months: zero article (‘in March’).'),
  ('The for time', 'I play football *on the Saturdays*.', 'on Saturdays', 'Days: zero article.'),
  ('The for place', 'I’m very tired. I’m going *to the bed*.', 'to bed', '‘Go to bed’: zero article.'),
  ('The for place', 'The kids are *at the school* until three.', 'at school', '‘At school’ as students: zero article.'),
  ('The for place', 'He goes *to the work* by bike.', 'to work', '‘Go to work’: zero article.'),
  ('Missing the: specific', 'Can you pass *a* salt, please?', 'the', 'The salt on this table: ‘the salt’. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Missing the: unique', 'Look at *a* sky! It’s orange.', 'the', 'Only one sky: ‘the sky’. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Missing the: instrument', 'She plays *a* cello in an orchestra.', 'the', 'Instruments: ‘the cello’. In general or in a fixed phrase → no article; specific or known → the.'),
  ('A with uncountable', 'We need *a* bread for the sandwiches.', 'some', '‘Bread’ is uncountable: ‘some bread’. In general or in a fixed phrase → no article; specific or known → the.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, general or specific, multiple choice and spot-the-mistake. In the typing questions write the or a when needed, or — (dash) for no article. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('general', 'General or specific?'),
 'fill': [
  ('General plural', '[[—|-]] Bees make honey.', 'the / a / —', 'Bees in general: zero article. In general or in a fixed phrase → no article; specific or known → the.', 'General → no article.'),
  ('Transport', 'They travelled to Paris by [[—|-]] plane.', 'the / a / —', 'By + transport: zero article. In general or in a fixed phrase → no article; specific or known → the.', 'By + transport → no article.'),
  ('Specific', '[[The|the]] bread in this bakery is amazing.', 'the / a / —', '‘In this bakery’ makes it specific: ‘the’. In general or in a fixed phrase → no article; specific or known → the.', 'Specific → the. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Place purpose', 'My sister is at [[—|-]] university in Lleida.', 'the / a / —', '‘At university’ as a student: zero article. In general or in a fixed phrase → no article; specific or known → the.', 'Place purpose → no article.'),
  ],
 'order': [
  ('General plural', 'Bees make honey.', []),
  ('Meal', 'We have dinner at nine.', []),
  ('Transport', 'I go by train.', []),
  ('Place purpose', 'She is in bed.', []),
  ],
 'customItems': [
  ('General', '‘I love animals.’ — animals are…', ['in general', 'specific', 'unique', 'second mention'],
   ['Specific animals would take ‘the’.', 'Animals aren’t unique.', 'There’s no first mention.'],
   'In general → zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('General', '‘The animals at this zoo look happy.’ — animals are…', ['specific', 'in general', 'unique', 'a fixed phrase'],
   ['‘At this zoo’ makes them specific.', 'They aren’t unique.', 'It isn’t a fixed phrase.'],
   'Specific → the.'),
  ('General', 'Why ‘at school’ but ‘at the school gate’?', ['purpose vs a specific place', 'school is plural', 'gate is a sport', 'it’s random'],
   ['‘School’ isn’t plural.', 'A gate isn’t a sport.', 'It isn’t random.'],
   'Purpose → zero; a specific part of the building → the.'),
  ('General', 'Why no article in ‘go by bus’?', ['fixed phrase with by', 'bus is uncountable', 'it’s a superlative', 'bus is unique'],
   ['‘Bus’ is countable.', 'There’s no superlative.', 'There are many buses.'],
   'By + transport is a fixed phrase. In general or in a fixed phrase → no article; specific or known → the.'),
  ],
 'mc': [
  ('General uncountable', '___ chocolate is my weakness.', ['—', 'The', 'A', 'An'],
   ['Chocolate in general: no ‘the’.', 'Uncountable: no ‘a’.', 'Uncountable: no ‘an’.'],
   'General uncountable: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Place purpose', 'Is your dad still at ___ work?', ['—', 'the', 'a', 'an'],
   ['‘At work’: zero article.', '‘At a work’ is wrong.', '‘An’ doesn’t fit.'],
   'At work: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Specific', '___ students in my class are very friendly.', ['The', '—', 'A', 'An'],
   ['‘In my class’ makes them specific.', '‘A’ doesn’t go with plurals.', '‘An’ doesn’t go with plurals.'],
   'Specific: the students. In general or in a fixed phrase → no article; specific or known → the.'),
  ('Time', 'It often rains in ___ autumn.', ['—', 'the', 'a', 'an'],
   ['Seasons usually take no article.', '‘An autumn’ is unusual here.', 'Seasons usually take no article.'],
   'Seasons: zero article (‘the’ is also possible but less common).'),
  ],
 'error': [
  ('The for general', '*The cats* are independent animals.', 'Cats', 'Cats in general: zero article. In general or in a fixed phrase → no article; specific or known → the.'),
  ('The for meal', 'Let’s have *the lunch* outside.', 'lunch', 'Meals: ‘have lunch’.'),
  ('The for language', 'Do you speak *the Portuguese*?', 'Portuguese', 'Languages: zero article (‘speak Portuguese’).'),
  ('The for place', 'Time to go *to the bed*!', 'to bed', '‘Go to bed’: zero article.'),
  ],
}
