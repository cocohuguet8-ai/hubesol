TITLE = 'A/An vs The'
AUX = (['a', 'an', 'the'], None, 'the')
NEXT = ('A/An vs One', '/grammar/articles/a-an-vs-one/')
BODY = r'''
## The key difference

| **a / an** (indefinite) | **the** (definite) |
|---|---|
| any one, not specific | a specific one |
| the listener doesn't know which | the listener knows which |
| first mention | second mention |
| singular countable only | singular, plural, uncountable |

- I want **a** sandwich. (any sandwich)
- I want **the** sandwich with cheese. (that specific one)

## First mention → second mention

The most common pattern in stories:

- Yesterday I saw **a** man with **a** dog. **The** man was old and **the** dog was tiny.

### Why it changes

The first time, the listener doesn't know them. After that, they do — so *a* becomes *the*.

> ⚠️ Typical error: ~~I bought a book. A book is great.~~ → *The book is great.*

## Any one vs a specific one

### *A / an* = any one

- Can I borrow **a** pen? (any pen is fine)
- Is there **a** chemist near here? (any chemist)

### *The* = we both know which

- Can I borrow **the** pen on your desk? (that one)
- Where's **the** chemist? (the one we always use)

## One of many vs the only one

| a / an | the |
|---|---|
| She's **a** teacher at my school. (one of several) | She's **the** head teacher. (only one) |
| It's **a** planet. | **The** sun is a star. |
| He's **a** student in my class. | He's **the** best student. |

> ⚠️ Typical error: ~~He's a tallest boy.~~ → Superlatives always take *the*.

## Describing vs identifying

### Describing → *a / an*

- My dad has **a** red car. — It's **an** old house.

### Identifying → *the*

- **The** red car outside is my dad's. — **The** house on the corner is old.

## Common mistakes

**1. *A* for something already mentioned.** *~~We stayed in a hotel. A hotel was nice.~~* → **The hotel**.

**2. *The* for first mention.** *~~I have the brother.~~* → **a brother**.

**3. *A* with unique things.** *~~a sun~~* → **the sun**.

**4. *A* with plurals.** *~~a cars~~* → **cars** / **the cars**.

**Pro tip:** ask *"Does the listener know which one?"* No → **a/an**. Yes → **the**.
'''

GAP = ('Fill in the gaps',
  'Type a, an or the. Ask yourself: does the listener know which one? Twenty original sentences.',
  [
  ('First → second', 'I saw [[a]] cat in the street. The cat was black.', 'a / an / the', 'First mention: the listener doesn’t know it yet, so ‘a cat’.'),
  ('First → second', 'I saw a cat in the street. [[The|the]] cat was black.', 'a / an / the', 'Second mention: now we know which cat, so ‘the cat’.'),
  ('First → second', 'We bought [[a]] sofa and two chairs.', 'a / an / the', 'First mention of a singular noun: ‘a sofa’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('First → second', 'We bought a sofa and two chairs. [[The|the]] sofa is grey.', 'a / an / the', 'Second mention: ‘the sofa’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('First → second', 'There was [[an]] old man on the bus.', 'a / an / the', 'First mention + vowel sound: ‘an old man’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Any one', 'Can I borrow [[a]] pencil? Any pencil is fine.', 'a / an / the', 'Any pencil, not a specific one: ‘a’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Specific', 'Can I borrow [[the]] pencil on your desk?', 'a / an / the', '‘On your desk’ tells us which: ‘the’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Any one', 'Is there [[a]] bus stop near here?', 'a / an / the', 'Any bus stop: ‘a’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Specific', 'Where’s [[the]] remote control? I can’t find it.', 'a / an / the', 'The one we have at home: ‘the’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('One of many', 'Lisbon is [[a]] beautiful city.', 'a / an / the', 'One of many beautiful cities: ‘a’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Only one', 'Madrid is [[the]] capital of Spain.', 'a / an / the', 'There’s only one capital of Spain: ‘the’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Job', 'My mum is [[an]] engineer.', 'a / an / the', 'Jobs take a/an; vowel sound: ‘an engineer’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Unique', '[[The|the]] moon is very bright tonight.', 'a / an / the', 'Only one moon: ‘the moon’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Superlative', 'It was [[the]] best day of my life.', 'a / an / the', 'Superlatives take ‘the’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Describing', 'She has [[a]] lovely garden.', 'a / an / the', 'Describing what she has: ‘a lovely garden’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Identifying', '[[The|the]] garden behind our house is huge.', 'a / an / the', '‘Behind our house’ identifies it: ‘the garden’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Specific', 'Did you lock [[the]] front door?', 'a / an / the', 'Our front door, we both know it: ‘the’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('First mention', 'I had [[an]] amazing dream last night.', 'a / an / the', 'First mention + vowel sound: ‘an amazing dream’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Per', 'I go to the gym three times [[a]] week.', 'a / an / the', '‘A’ means ‘per’: three times a week. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Instrument', 'Can you play [[the]] piano?', 'a / an / the', 'Instruments take ‘the’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with a, an and the.',
  [
  ('First mention', 'I saw a dog.', []),
  ('Second mention', 'The dog was huge.', []),
  ('First mention', 'We met an actor.', []),
  ('Second mention', 'The actor was funny.', []),
  ('Any one', 'Can I have a pen?', []),
  ('Specific', 'Pass me the red pen.', []),
  ('Any one', 'Is there a bank here?', []),
  ('Specific', 'Where is the bank?', []),
  ('One of many', 'She is a doctor.', []),
  ('Only one', 'He is the boss.', []),
  ('Unique', 'The sun is hot.', []),
  ('Superlative', 'It is the best film.', []),
  ('Describing', 'He has a big house.', []),
  ('Identifying', 'The house is on the hill.', []),
  ('Specific', 'Close the window, please.', []),
  ('Job', 'My dad is an artist.', []),
  ('Per', 'I run twice a week.', []),
  ('Instrument', 'She plays the guitar.', []),
  ('Only one', 'Rome is the capital of Italy.', []),
  ('One of many', 'Rome is a big city.', []),
  ])

MATCH = {'title': 'A/an or the?', 'subtitle': 'Tap a sentence, then tap the article that fits the gap.',
  'leftLabel': 'Sentence', 'rightLabel': 'Article', 'rightLabelSub': '(a / an / the)', 'reviewArrowPrefix': '',
  'pairs': [
  ('I bought ___ new phone yesterday.', 'a'),
  ('___ sun is shining.', 'the'),
  ('She is ___ architect.', 'an'),
  ('He’s ___ tallest boy in class.', 'the'),
  ('Can I have ___ apple?', 'an'),
  ('There’s ___ cat on the wall.', 'a'),
  ('Paris is ___ capital of France.', 'the'),
  ('I waited for ___ hour.', 'an'),
  ('Close ___ door, please.', 'the'),
  ('My aunt is ___ nurse.', 'a'),
  ('It was ___ easy test.', 'an'),
  ('Who is ___ man in the photo?', 'the'),
  ('Is there ___ café near here?', 'a'),
  ('Look at ___ stars!', 'the'),
  ('I have ___ idea!', 'an'),
  ('I saw a film. ___ film was long.', 'the'),
  ('We need ___ taxi.', 'a'),
  ('She plays ___ violin.', 'the'),
  ('He’s ___ honest man.', 'an'),
  ('I eat out once ___ week.', 'a'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Does the listener know which one? No → a/an. Yes → the.',
  [
  ('First mention', 'Last week I read ___ book about sharks.', ['a', 'the', 'an', '—'],
   ['‘The book’ means the listener already knows which book.', '‘Book’ starts with a consonant sound.', 'A singular countable noun needs an article.'],
   'First mention: a book. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Second mention', 'I read a book about sharks. ___ book was fascinating.', ['The', 'A', 'An', '—'],
   ['We already mentioned it, so not ‘a’.', '‘Book’ starts with a consonant sound, and it’s second mention.', 'A singular noun needs an article.'],
   'Second mention: the book. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Any one', 'Excuse me, is there ___ toilet in this building?', ['a', 'the', 'an', '—'],
   ['We don’t know which toilet yet.', '‘Toilet’ starts with a consonant sound.', 'A singular noun needs an article.'],
   'Any toilet: a. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Specific', 'Excuse me, where’s ___ toilet?', ['the', 'a', 'an', '—'],
   ['We mean the toilet in this building.', '‘Toilet’ starts with a consonant sound.', 'A singular noun needs an article.'],
   'The one in this place: the toilet. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Only one', 'Who is ___ president of your club?', ['the', 'a', 'an', '—'],
   ['There’s only one president.', '‘President’ starts with a consonant sound.', 'A singular noun needs an article.'],
   'Only one: the president. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('One of many', 'My friend Tom is ___ member of the club.', ['a', 'the', 'an', '—'],
   ['There are many members.', '‘Member’ starts with a consonant sound.', 'A singular noun needs an article.'],
   'One of many: a member. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Superlative', 'It’s ___ most expensive restaurant in town.', ['the', 'a', 'an', '—'],
   ['Superlatives never take ‘a’.', 'Superlatives never take ‘an’.', 'Superlatives need ‘the’.'],
   'Superlative: the most expensive. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Unique', '___ earth is the third planet from the sun.', ['The', 'An', 'A', '—'],
   ['There’s only one earth.', 'There’s only one earth.', 'We say ‘the earth’ (or ‘Earth’ as a name).'],
   'Unique: the earth. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Job', 'Her husband is ___ electrician.', ['an', 'the', 'a', '—'],
   ['Jobs take a/an, not ‘the’.', '‘Electrician’ starts with a vowel sound.', 'Jobs need an article.'],
   'Job + vowel sound: an electrician. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Identifying', '___ girl with long hair is my cousin.', ['The', 'A', 'An', '—'],
   ['‘With long hair’ identifies her: not ‘a’.', '‘Girl’ starts with a consonant sound.', 'A singular noun needs an article.'],
   'Identified by a phrase: the girl. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Describing', 'My cousin is ___ girl with long hair.', ['a', 'the', 'an', '—'],
   ['We’re describing her, not identifying her.', '‘Girl’ starts with a consonant sound.', 'A singular noun needs an article.'],
   'Describing: a girl with long hair. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Specific', 'Can you turn on ___ light? It’s dark.', ['the', 'a', 'an', '—'],
   ['We mean the light in this room.', '‘Light’ starts with a consonant sound.', 'A singular noun needs an article.'],
   'Specific: the light. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('First mention', 'We saw ___ owl in the forest.', ['an', 'the', 'a', '—'],
   ['First mention: not ‘the’.', '‘Owl’ starts with a vowel sound.', 'A singular noun needs an article.'],
   'First mention + vowel sound: an owl. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Instrument', 'He’s learning to play ___ saxophone.', ['the', 'a', 'an', '—'],
   ['Instruments take ‘the’.', '‘Saxophone’ starts with a consonant sound.', 'Instruments usually need ‘the’.'],
   'Instrument: the saxophone. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Per', 'The tickets cost ten euros ___ person.', ['a', 'the', 'an', '—'],
   ['Per unit: ‘a person’.', '‘Person’ starts with a consonant sound.', 'We need ‘a’ (or ‘per’).'],
   '‘A’ = per: ten euros a person. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Only one', 'What’s ___ name of your teacher?', ['the', 'a', 'an', '—'],
   ['Your teacher has one name.', '‘Name’ starts with a consonant sound.', 'A singular noun needs an article.'],
   'Only one name: the name. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Which', 'Which is correct?', ['I have a sister. The sister lives in Rome.', 'I have the sister. A sister lives in Rome.', 'I have a sister. A sister lives in Rome.', 'I have sister. The sister lives in Rome.'],
   ['First mention needs ‘a’.', 'Second mention needs ‘the’.', 'A singular noun needs an article.'],
   'First mention a, second mention the. (More natural: ‘She lives in Rome.’)'),
  ('Which', 'Which is correct?', ['She’s the best singer in the band.', 'She’s a best singer in the band.', 'She’s best singer in the band.', 'She’s an best singer in the band.'],
   ['Superlatives never take ‘a’.', 'Superlatives need ‘the’.', 'Superlatives never take ‘an’.'],
   'Superlative: the best. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Any one', 'I’m hungry. I want ___ sandwich.', ['a', 'the', 'an', '—'],
   ['Any sandwich: not ‘the’.', '‘Sandwich’ starts with a consonant sound.', 'A singular noun needs an article.'],
   'Any one: a sandwich. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Specific', 'Who ate ___ sandwich I left in the fridge?', ['the', 'a', 'an', '—'],
   ['‘I left in the fridge’ identifies it.', '‘Sandwich’ starts with a consonant sound.', 'A singular noun needs an article.'],
   'Identified: the sandwich. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('A for second mention', 'I bought a dress. *A* dress is red.', 'The', 'Second mention: ‘the dress’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('A for second mention', 'We met a man and a woman. *A* woman was French.', 'The', 'Second mention: ‘the woman’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('The for first mention', 'I have *the* brother and two sisters.', 'a', 'First mention: ‘a brother’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('The for first mention', 'Last night I saw *the* strange light in the sky.', 'a', 'First mention, the listener doesn’t know it: ‘a strange light’.'),
  ('The for first mention', 'Is there *the* supermarket near here?', 'a', 'Any supermarket: ‘a supermarket’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('A for unique', '*A* sun is very hot today.', 'The', 'Only one sun: ‘the sun’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('A for unique', 'Rome is *a* capital of Italy.', 'the', 'Only one capital: ‘the capital’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('A for superlative', 'She’s *a* best cook in my family.', 'the', 'Superlatives take ‘the’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('A for superlative', 'It’s *an* oldest church in town.', 'the', 'Superlatives take ‘the’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('A for specific', 'Can you open *a* window? It’s hot in here.', 'the', 'The window in this room: ‘the’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('A for specific', '*A* man in the blue shirt is my boss.', 'The', '‘In the blue shirt’ identifies him: ‘the man’.'),
  ('The for job', 'My uncle is *the* plumber.', 'a', 'Jobs take a/an: ‘a plumber’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('The for job', 'She wants to be *the* actress.', 'an', 'Jobs take a/an: ‘an actress’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('The for describing', 'He has *the* very big nose.', 'a', 'Describing: ‘a very big nose’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Wrong form', 'I had *a* awful day.', 'an', '‘Awful’ starts with a vowel sound: ‘an awful day’.'),
  ('Wrong form', 'She’s *an* doctor.', 'a', '‘Doctor’ starts with a consonant sound: ‘a doctor’.'),
  ('A for instrument', 'He plays *a* piano beautifully.', 'the', 'Instruments take ‘the’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('The for per', 'I see him once *the* week.', 'a', '‘A’ = per: ‘once a week’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('A with plural', 'I bought *a* tomatoes for the salad.', 'some', 'Plural: ‘some tomatoes’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('A for only one', 'What’s *a* name of this street?', 'the', 'A street has only one name: ‘the name’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, known or not, multiple choice and spot-the-mistake. In the typing questions write a, an or the. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('known', 'Known or not?'),
 'fill': [
  ('First mention', 'I found [[a]] wallet in the park.', 'a / an / the', 'First mention: the listener doesn’t know it, so ‘a wallet’.', 'First mention → a/an.'),
  ('Second mention', 'I found a wallet in the park. [[The|the]] wallet was empty.', 'a / an / the', 'Second mention: ‘the wallet’. Ask: does the listener know which one? No → a/an. Yes → the.', 'Second mention → the.'),
  ('Only one', 'Who is [[the]] captain of the team?', 'a / an / the', 'A team has only one captain: ‘the’. Ask: does the listener know which one? No → a/an. Yes → the.', 'Only one → the. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Job', 'My neighbour is [[an]] artist.', 'a / an / the', 'Jobs take a/an; vowel sound: ‘an artist’. Ask: does the listener know which one? No → a/an. Yes → the.', 'Job → a/an.'),
  ],
 'order': [
  ('First mention', 'I saw a bird.', []),
  ('Second mention', 'The bird was blue.', []),
  ('Superlative', 'It is the best café.', []),
  ('Job', 'She is an engineer.', []),
  ],
 'customItems': [
  ('Known', 'In ‘Can I have a biscuit?’, the listener…', ['doesn’t know which one', 'knows which one', 'has only one', 'must choose the best'],
   ['If they knew, we’d say ‘the biscuit’.', 'Having only one would need ‘the’.', 'There’s no superlative.'],
   'Any one → a. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Known', 'In ‘Where’s the car?’, the listener…', ['knows which car', 'doesn’t know which car', 'has never seen it', 'wants any car'],
   ['If they didn’t know, we’d say ‘a car’.', 'They know it: it’s our car.', '‘Any car’ would need ‘a’.'],
   'Known → the. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Known', 'Why ‘the’ in ‘the capital of Peru’?', ['there’s only one', 'it’s first mention', 'it’s a job', 'it’s any city'],
   ['First mention alone isn’t the reason.', 'A capital isn’t a job.', 'It’s one specific city.'],
   'Only one → the.'),
  ('Known', 'Why ‘a’ in ‘Peru is a big country’?', ['one of many', 'only one exists', 'second mention', 'superlative'],
   ['There are many big countries.', 'It isn’t second mention.', 'There’s no superlative.'],
   'One of many → a. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ],
 'mc': [
  ('Second mention', 'I ordered a pizza. ___ pizza was cold.', ['The', 'A', 'An', '—'],
   ['Already mentioned: not ‘a’.', '‘Pizza’ starts with a consonant sound.', 'A singular noun needs an article.'],
   'Second mention: the pizza. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Any one', 'I need ___ new laptop.', ['a', 'the', 'an', '—'],
   ['Any new laptop: not ‘the’.', '‘New’ starts with a consonant sound.', 'A singular noun needs an article.'],
   'Any one: a new laptop. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Superlative', 'This is ___ worst day ever!', ['the', 'a', 'an', '—'],
   ['Superlatives never take ‘a’.', 'Superlatives never take ‘an’.', 'Superlatives need ‘the’.'],
   'Superlative: the worst. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('Identifying', '___ boy next to Anna is her brother.', ['The', 'A', 'An', '—'],
   ['‘Next to Anna’ identifies him.', '‘Boy’ starts with a consonant sound.', 'A singular noun needs an article.'],
   'Identified: the boy. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ],
 'error': [
  ('A for second mention', 'I saw a film. *A* film was boring.', 'The', 'Second mention: ‘the film’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('The for first mention', 'I have *the* dog called Max.', 'a', 'First mention: ‘a dog’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('A for unique', 'Look at *a* moon!', 'the', 'Only one moon: ‘the moon’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ('The for job', 'He’s *the* waiter in a café.', 'a', 'Jobs take a/an: ‘a waiter’. Ask: does the listener know which one? No → a/an. Yes → the.'),
  ],
}
