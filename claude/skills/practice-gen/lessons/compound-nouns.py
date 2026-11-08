TITLE = 'Compound Nouns'
AUX = (['noun', 'noun'], None, 'noun')
NEXT = ('Order of Adjectives', '/grammar/nouns-determiners/order-of-adjectives/')
BODY = r'''
## What is a compound noun?

A **compound noun** is two (or more) words that work together as **one noun**.

| Type | Example |
|---|---|
| noun + noun | **bus stop**, **football**, **toothbrush** |
| adjective + noun | **blackboard**, **swimming pool**, **high school** |
| verb-ing + noun | **washing machine**, **dining room** |
| noun + verb-ing | **bird-watching**, **sightseeing** |

## The main word comes last

The **second** word is the main noun. The **first** word describes it.

- a **kitchen** table = a kind of table
- a **table** lamp = a kind of lamp
- a **horse** race (a race) ≠ a **race** horse (a horse)

> ⚠️ Typical error: ~~a cup coffee~~ → *a coffee cup* (a cup for coffee) or *a cup of coffee* (a cup full of coffee).

## How to write them

### 1. One word

- **bedroom**, **toothpaste**, **sunglasses**, **football**

### 2. Two words (most common)

- **bus stop**, **credit card**, **post office**, **tennis ball**

### 3. With a hyphen

- **mother-in-law**, **check-in**, **well-being**

There's no simple rule — check a dictionary.

## The first noun is usually singular

- a **shoe** shop (~~a shoes shop~~) — a **toothbrush** (~~teethbrush~~)
- a **ten-minute** walk — a **five-year-old** boy (~~five-years-old~~)

> ⚠️ Typical error: ~~a books shop~~ → *a bookshop.*

### Exceptions

- **clothes** shop, **sports** centre, **sales** manager

## Plurals

Make the **main** (last) word plural:

- two **bus stops**, three **toothbrushes**, my **football boots**
- But: **mothers-in-law**, **passers-by** (the main word is first)

## Compound noun vs *'s* vs *of*

| Compound noun | *'s* | *of* |
|---|---|---|
| a **car door** (type of door) | **Anna's** door (owner) | a **cup of** tea (contents) |
| a **dog** bed (for dogs) | the **dog's** bed (this dog's) | a **piece of** cake |

## Stress

In most compound nouns we stress the **first** word:

- **BUS** stop, **POST** office, **SWIM**ming pool

## Common mistakes

**1. Wrong order.** *~~a stop bus~~* → **a bus stop**.

**2. Plural first noun.** *~~a shoes shop~~* → **a shoe shop**.

**3. Plural on the wrong word.** *~~buses stop~~* → **bus stops**.

**4. Adding *of* or *'s* wrongly.** *~~the stop of bus~~* → **the bus stop**.

**Pro tip:** ask *"What is it?"* — the answer is the **last** word: a *tennis ball* is a **ball**.
'''

GAP = ('Fill in the gaps',
  'Complete the compound noun with one word. Twenty original sentences.',
  [
  ('Noun + noun', 'Let’s wait at the bus [[stop]].', 'bus ___', 'A place where the bus stops: ‘bus stop’. The main word goes last, and the first noun is usually singular.'),
  ('Noun + noun', 'I need to buy a new tooth[[brush]].', 'tooth___', 'A brush for your teeth: ‘toothbrush’. The main word goes last, and the first noun is usually singular.'),
  ('Noun + noun', 'Can I pay by credit [[card]]?', 'credit ___', 'A card for credit: ‘credit card’. The main word goes last, and the first noun is usually singular.'),
  ('Noun + noun', 'I’m going to the post [[office]] to send a parcel.', 'post ___', '‘Post office’: where you send letters. The main word goes last, and the first noun is usually singular.'),
  ('Noun + noun', 'We put the dirty clothes in the washing [[machine]].', 'washing ___', 'A machine for washing: ‘washing machine’. The main word goes last, and the first noun is usually singular.'),
  ('Noun + noun', 'She’s wearing [[sunglasses]] because it’s very bright.', '___glasses', 'Glasses for the sun: ‘sunglasses’. The main word goes last, and the first noun is usually singular.'),
  ('Noun + noun', 'My [[bedroom]] is on the first floor.', '___room', 'A room with a bed: ‘bedroom’. The main word goes last, and the first noun is usually singular.'),
  ('Noun + noun', 'Do you have a [[swimming]] pool in your town?', '___ pool', '‘Swimming pool’: verb-ing + noun. The main word goes last, and the first noun is usually singular.'),
  ('Noun + noun', 'We had dinner in the [[dining]] room.', '___ room', '‘Dining room’: a room for eating. The main word goes last, and the first noun is usually singular.'),
  ('Main word last', 'A cup for coffee is a coffee [[cup]].', 'coffee ___', 'The main word is last: it’s a cup. The main word goes last, and the first noun is usually singular.'),
  ('Main word last', 'A shop that sells shoes is a [[shoe]] shop.', '___ shop', 'First noun singular: ‘shoe shop’. The main word goes last, and the first noun is usually singular.'),
  ('Main word last', 'A race for horses is a horse [[race]].', 'horse ___', 'It’s a race: ‘race’ goes last. The main word goes last, and the first noun is usually singular.'),
  ('Singular first', 'It’s a ten-[[minute]] walk to the station.', 'ten-___', 'Number + noun before another noun: singular ‘minute’.'),
  ('Singular first', 'They have a five-year-[[old]] son.', 'five-year-___', '‘Five-year-old’: ‘year’ is singular. The main word goes last, and the first noun is usually singular.'),
  ('Singular first', 'I bought it in a [[book]]shop.', '___shop', '‘Bookshop’: first noun singular. The main word goes last, and the first noun is usually singular.'),
  ('Exception', 'There’s a new [[sports]] centre near my house.', '___ centre', 'Exception: ‘sports centre’ keeps the -s. The main word goes last, and the first noun is usually singular.'),
  ('Exception', 'I work in a [[clothes]] shop.', '___ shop', '‘Clothes’ has no singular form: ‘clothes shop’. The main word goes last, and the first noun is usually singular.'),
  ('Plural', 'There are two bus [[stops]] on this street.', 'bus ___', 'Make the last word plural: ‘bus stops’. The main word goes last, and the first noun is usually singular.'),
  ('Plural', 'My [[football]] boots are muddy.', '___ boots', '‘Football boots’: first word singular, last word plural.'),
  ('Hyphen', 'My mother-in-[[law]] lives with us.', 'mother-in-___', '‘Mother-in-law’ is written with hyphens. The main word goes last, and the first noun is usually singular.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with compound nouns.',
  [
  ('Noun + noun', 'Wait at the bus stop.', []),
  ('Noun + noun', 'I lost my credit card.', []),
  ('Noun + noun', 'Where is the post office?', []),
  ('Noun + noun', 'The car park is full.', []),
  ('Noun + noun', 'I need a new phone case.', []),
  ('Verb-ing + noun', 'The washing machine is broken.', []),
  ('Verb-ing + noun', 'We have a swimming pool.', []),
  ('Verb-ing + noun', 'Eat in the dining room.', []),
  ('One word', 'My bedroom is small.', []),
  ('One word', 'Where are my sunglasses?', []),
  ('One word', 'I bought some toothpaste.', []),
  ('Singular first', 'It’s a ten-minute walk.', []),
  ('Singular first', 'She works in a shoe shop.', []),
  ('Exception', 'Let’s go to the sports centre.', []),
  ('Plural', 'There are two bus stops.', []),
  ('Plural', 'I need new football boots.', []),
  ('Main word last', 'This is a coffee cup.', []),
  ('Main word last', 'Put it on the kitchen table.', []),
  ('Hyphen', 'My sister-in-law is French.', []),
  ('Noun + noun', 'Turn off the alarm clock.', []),
  ])

MATCH = {'title': 'Build the compound', 'subtitle': 'Tap the first word, then tap the word that completes the compound noun.',
  'leftLabel': 'First word', 'rightLabel': 'Second word', 'rightLabelSub': '', 'reviewArrowPrefix': '',
  'pairs': [
  ('tooth', 'brush'), ('credit', 'card'), ('post', 'office'), ('washing', 'machine'),
  ('sun', 'glasses'), ('bed', 'room'), ('swimming', 'pool'), ('car', 'park'),
  ('rail', 'way'), ('alarm', 'clock'), ('foot', 'ball'), ('hair', 'cut'),
  ('traffic', 'lights'), ('rain', 'coat'), ('door', 'bell'), ('head', 'ache'),
  ('passport', 'control'), ('book', 'shop'), ('birth', 'day'), ('police', 'station'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. The main word goes LAST; the first noun is usually singular.',
  [
  ('Main word last', 'A brush for your hair is a ___.', ['hairbrush', 'brush hair', 'hair’s brush', 'brush of hair'],
   ['Wrong order: the main word (brush) goes last.', 'We don’t use ’s for this kind of thing.', '‘Brush of hair’ isn’t natural.'],
   'Main word last: hairbrush. The main word goes last, and the first noun is usually singular.'),
  ('Main word last', 'Where can I catch the train? — At the ___.', ['train station', 'station train', 'train’s station', 'trains station'],
   ['Wrong order.', 'No ’s for compound nouns.', 'First noun singular.'],
   'Train station. The main word goes last, and the first noun is usually singular.'),
  ('Singular first', 'My dad works in a ___.', ['car factory', 'cars factory', 'factory cars', 'car’s factory'],
   ['First noun normally singular.', 'Wrong order.', 'No ’s.'],
   'Car factory. The main word goes last, and the first noun is usually singular.'),
  ('Singular first', 'It was a three-___ journey.', ['hour', 'hours', 'hour’s', 'hourly'],
   ['Number + noun before another noun: singular.', 'With hyphens we don’t use ’s.', 'Different word.'],
   'A three-hour journey. The main word goes last, and the first noun is usually singular.'),
  ('Singular first', 'She has a ___ daughter.', ['six-year-old', 'six-years-old', 'six-year-olds', 'old-six-year'],
   ['‘Year’ stays singular in the compound.', 'Plural only if we mean several daughters.', 'Wrong order.'],
   'A six-year-old daughter. The main word goes last, and the first noun is usually singular.'),
  ('Plural', 'This street has three ___.', ['bus stops', 'buses stop', 'buses stops', 'bus stop'],
   ['The plural goes on the last word.', 'Only the last word is plural.', 'After ‘three’ we need the plural.'],
   'Bus stops. The main word goes last, and the first noun is usually singular.'),
  ('Plural', 'How many ___ do you have at home?', ['toothbrushes', 'teethbrushes', 'teethbrush', 'toothsbrush'],
   ['The first word stays singular.', 'Not English.', 'Not English.'],
   'Toothbrushes. The main word goes last, and the first noun is usually singular.'),
  ('Exception', 'I bought these jeans in a ___.', ['clothes shop', 'clothe shop', 'shop clothes', 'clothing’s shop'],
   ['‘Clothe’ isn’t a noun.', 'Wrong order.', 'Not English.'],
   'Clothes shop (exception). The main word goes last, and the first noun is usually singular.'),
  ('Compound vs of', 'Can I have a ___? I’m thirsty.', ['cup of tea', 'tea cup', 'cup tea', 'tea’s cup'],
   ['A ‘tea cup’ is an empty cup for tea.', 'Not English.', 'Not English.'],
   'Contents: a cup of tea. The main word goes last, and the first noun is usually singular.'),
  ('Compound vs of', 'I broke my favourite ___ — I’ll buy a new one.', ['coffee cup', 'cup of coffee', 'cup coffee', 'coffee of cup'],
   ['You can’t break the coffee in it — you break the cup.', 'Not English.', 'Not English.'],
   'The object: a coffee cup. The main word goes last, and the first noun is usually singular.'),
  ('Compound vs ’s', 'The ___ is red. (the kind of door)', ['front door', 'door’s front', 'front’s door', 'door front'],
   ['Not English.', 'Not English.', 'Wrong order.'],
   'Front door. The main word goes last, and the first noun is usually singular.'),
  ('Verb-ing + noun', 'We have a new ___ in the kitchen.', ['washing machine', 'machine washing', 'washed machine', 'wash’s machine'],
   ['Wrong order.', 'Wrong form.', 'Not English.'],
   'Washing machine. The main word goes last, and the first noun is usually singular.'),
  ('Verb-ing + noun', 'Is there a ___ in the hotel?', ['swimming pool', 'pool swimming', 'swim pools', 'swimmer pool'],
   ['Wrong order.', 'Wrong form.', 'Not English.'],
   'Swimming pool. The main word goes last, and the first noun is usually singular.'),
  ('Hyphen', 'My brother’s wife is my ___.', ['sister-in-law', 'sister in law’s', 'law sister', 'sister of law'],
   ['Not English.', 'Wrong order.', 'Not English.'],
   'Sister-in-law. The main word goes last, and the first noun is usually singular.'),
  ('Hyphen plural', 'Both my ___ are lovely.', ['sisters-in-law', 'sister-in-laws', 'sisters-in-laws', 'sister-ins-law'],
   ['The main word (sister) is first here.', 'Only ‘sister’ is plural.', 'Not English.'],
   'Sisters-in-law. The main word goes last, and the first noun is usually singular.'),
  ('Meaning', 'A ‘race horse’ is a…', ['horse', 'race', 'person', 'stadium'],
   ['The main word is last: horse.', 'Not a person.', 'Not a place.'],
   'Race horse = a horse for racing. The main word goes last, and the first noun is usually singular.'),
  ('Meaning', 'A ‘horse race’ is a…', ['race', 'horse', 'farm', 'person'],
   ['The main word is last: race.', 'Not a farm.', 'Not a person.'],
   'Horse race = a race with horses. The main word goes last, and the first noun is usually singular.'),
  ('Which', 'Which is correct?', ['a bookshop', 'a booksshop', 'a shop book', 'a books’ shop'],
   ['First noun singular.', 'Wrong order.', 'No apostrophe.'],
   'Bookshop. The main word goes last, and the first noun is usually singular.'),
  ('Which', 'Which is correct?', ['a ten-minute break', 'a ten-minutes break', 'a ten minutes’ break of', 'a break ten-minute'],
   ['Singular in compounds. The main word goes last, and the first noun is usually singular.', 'Not English.', 'Wrong order.'],
   'Ten-minute break. The main word goes last, and the first noun is usually singular.'),
  ('Exception', 'He’s the new ___ manager.', ['sales', 'sale', 'sale’s', 'selling'],
   ['Exception: ‘sales manager’.', 'No apostrophe.', 'Not the usual job title.'],
   'Sales manager. The main word goes last, and the first noun is usually singular.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('Plural first', 'I bought them in a *shoes* shop.', 'shoe', 'First noun singular: ‘shoe shop’. The main word goes last, and the first noun is usually singular.'),
  ('Plural first', 'Is there a *books* shop near here?', 'book', 'First noun singular: ‘book shop / bookshop’.'),
  ('Plural first', 'I need a new *teeth*brush.', 'tooth', '‘Toothbrush’: singular first part. The main word goes last, and the first noun is usually singular.'),
  ('Plural first', 'It’s a *five-minutes* walk.', 'five-minute', 'Singular in compounds: ‘five-minute walk’.'),
  ('Plural first', 'She has a *two-years-old* cat.', 'two-year-old', '‘Two-year-old’: singular. The main word goes last, and the first noun is usually singular.'),
  ('Plural first', 'We stayed in a *three-stars* hotel.', 'three-star', '‘Three-star hotel’: singular. The main word goes last, and the first noun is usually singular.'),
  ('Plural wrong word', 'There are four bus *stop* in my street.', 'stops', 'Plural on the last word: ‘bus stops’. The main word goes last, and the first noun is usually singular.'),
  ('Plural wrong word', 'We need new tennis *ball*.', 'balls', 'Plural on the last word: ‘tennis balls’.'),
  ('’s with things', 'I can’t find the *door’s* key.', 'door', 'Compound noun: ‘the door key’. The main word goes last, and the first noun is usually singular.'),
  ('Wrong compound', 'Turn off the *alarming* clock.', 'alarm', '‘Alarm clock’. The main word goes last, and the first noun is usually singular.'),
  ('’s with things', 'Turn off the *kitchen’s* light.', 'kitchen', 'Compound noun: ‘the kitchen light’. The main word goes last, and the first noun is usually singular.'),
  ('’s with things', 'I left it on the *car’s* seat.', 'car', 'Compound noun: ‘the car seat’. The main word goes last, and the first noun is usually singular.'),
  ('Plural first', 'Leave your car in the *cars* park.', 'car', 'First noun singular: ‘car park’. The main word goes last, and the first noun is usually singular.'),
  ('Cup of', 'Can I have a *tea cup*? I’m thirsty.', 'cup of tea', 'You want tea to drink: ‘a cup of tea’ (a ‘tea cup’ is the empty cup).'),
  ('Exception', 'I work in a *clothe* shop.', 'clothes', '‘Clothes shop’ — ‘clothe’ isn’t a noun. The main word goes last, and the first noun is usually singular.'),
  ('Exception', 'Let’s play at the *sport* centre.', 'sports', '‘Sports centre’ keeps the -s. The main word goes last, and the first noun is usually singular.'),
  ('Hyphen plural', 'My two *sister-in-laws* are teachers.', 'sisters-in-law', 'Plural on the main word: ‘sisters-in-law’.'),
  ('Wrong compound', 'I wash my clothes in the *wash* machine.', 'washing', '‘Washing machine’. The main word goes last, and the first noun is usually singular.'),
  ('Wrong compound', 'We swim in the *swim* pool.', 'swimming', '‘Swimming pool’. The main word goes last, and the first noun is usually singular.'),
  ('Wrong compound', 'Eat your dinner in the *dinner* room.', 'dining', '‘Dining room’. The main word goes last, and the first noun is usually singular.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, which word is the main one, multiple choice and spot-the-mistake. In the typing questions write one word. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('main', 'Main word?'),
 'fill': [
  ('Noun + noun', 'I left my umbrella at the train [[station]].', 'train ___', '‘Train station’. The main word goes last, and the first noun is usually singular.', 'Main word last.'),
  ('Singular first', 'It’s a two-[[hour]] film.', 'two-___', 'Singular in compounds.', 'First part singular.'),
  ('Plural', 'We need more coffee [[cups]].', 'coffee ___', 'Plural on the last word. The main word goes last, and the first noun is usually singular.', 'Plural on main word.'),
  ('Verb-ing + noun', 'The [[washing]] machine is noisy.', '___ machine', '‘Washing machine’. The main word goes last, and the first noun is usually singular.', 'Verb-ing + noun.'),
  ],
 'order': [
  ('Noun + noun', 'Where is the car park?', []),
  ('Singular first', 'It’s a five-minute walk.', []),
  ('Plural', 'I need two tennis balls.', []),
  ('One word', 'My toothbrush is blue.', []),
  ],
 'customItems': [
  ('Main', 'In ‘tennis ball’, the main word is…', ['ball', 'tennis', 'both', 'neither'],
   ['‘Tennis’ describes the ball.', 'Only one word is the main one.', 'The last word is the main one.'],
   'It’s a ball. The main word goes last, and the first noun is usually singular.'),
  ('Main', 'In ‘kitchen table’, the thing is a…', ['table', 'kitchen', 'room', 'chair'],
   ['‘Kitchen’ describes it.', 'Not a room.', 'Not a chair.'],
   'It’s a table. The main word goes last, and the first noun is usually singular.'),
  ('Main', 'In ‘mother-in-law’, which word becomes plural?', ['mother', 'law', 'in', 'all three'],
   ['‘Laws’ is wrong here.', '‘In’ never changes.', 'Only one changes.'],
   'Mothers-in-law. The main word goes last, and the first noun is usually singular.'),
  ('Main', 'A ‘shoe shop’ is a…', ['shop', 'shoe', 'brand', 'factory'],
   ['It isn’t a shoe.', 'Not a brand.', 'Not a factory.'],
   'It’s a shop. The main word goes last, and the first noun is usually singular.'),
  ],
 'mc': [
  ('Main word last', 'Where do you keep the plates? — In the ___.', ['kitchen cupboard', 'cupboard kitchen', 'kitchen’s cupboard of', 'kitchens cupboard'],
   ['Wrong order.', 'Not English.', 'First noun singular.'],
   'Kitchen cupboard. The main word goes last, and the first noun is usually singular.'),
  ('Singular first', 'She lives in a ___ flat.', ['two-bedroom', 'two-bedrooms', 'two-bedroom’s', 'bedroom-two'],
   ['Singular in compounds.', 'No apostrophe.', 'Wrong order.'],
   'Two-bedroom flat. The main word goes last, and the first noun is usually singular.'),
  ('Compound vs of', 'Would you like a ___?', ['glass of water', 'water glass', 'glass water', 'water’s glass'],
   ['A ‘water glass’ is the empty glass.', 'Not English.', 'Not English.'],
   'Contents: a glass of water. The main word goes last, and the first noun is usually singular.'),
  ('Plural', 'Put the ___ in the bin.', ['paper bags', 'papers bag', 'papers bags', 'paper bag’s'],
   ['Plural on the last word.', 'Only the last word is plural.', 'No apostrophe.'],
   'Paper bags. The main word goes last, and the first noun is usually singular.'),
  ],
 'error': [
  ('Plural first', 'I went to a *toys* shop.', 'toy', 'First noun singular: ‘toy shop’. The main word goes last, and the first noun is usually singular.'),
  ('Plural first', 'I found a *ten-euros* note.', 'ten-euro', '‘Ten-euro note’. The main word goes last, and the first noun is usually singular.'),
  ('Wrong compound', 'The *swim* pool is closed.', 'swimming', '‘Swimming pool’. The main word goes last, and the first noun is usually singular.'),
  ('’s with things', 'Close the *car’s* window.', 'car', '‘The car window’. The main word goes last, and the first noun is usually singular.'),
  ],
}
