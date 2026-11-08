TITLE = 'Prepositions of Place: at/on/in'
AUX = (['at', 'on', 'in'], None, 'in')
NEXT = ('In, On, At: time vs place', '/grammar/prepositions/in-on-at-time-vs-place/')
BODY = r'''
## How to choose at, on or in for place

| Preposition | Think of… | Examples |
|---|---|---|
| **at** | a **point** or a place where something happens | **at** the bus stop, **at** the door, **at** school, **at** a party |
| **on** | a **surface** or a line | **on** the table, **on** the wall, **on** the floor, **on** the coast |
| **in** | an **enclosed space** or area | **in** the box, **in** the kitchen, **in** Girona, **in** Spain |

## When to use *at*

### 1. A point or specific location

- Wait for me **at** the entrance.
- There's someone **at** the door.

### 2. Places where an activity happens

- She's **at** school / **at** work / **at** university.
- We met **at** a concert / **at** a party.

> ⚠️ Typical error: ~~I'm in work.~~ → For the activity, use *at*: *I'm at work.*

### 3. Addresses with a number

- She lives **at** 24 Carrer Major.

## When to use *on*

### 1. Surfaces

- Your keys are **on** the table.
- There's a poster **on** the wall.

> ⚠️ Typical error: ~~The picture is in the wall.~~ → A surface takes *on*: *on the wall.*

### 2. Lines: streets, rivers, coasts

- Our flat is **on** Gran Via.
- Girona is **on** the River Onyar.

### 3. Floors, transport you can stand in

| on the first floor | on the bus | on the train | on a plane | on the left / right |
|---|---|---|---|---|

- I left my umbrella **on** the bus.

> ⚠️ Typical error: ~~She's in the bus.~~ → Public transport takes *on*: *on the bus.*

## When to use *in*

### 1. Enclosed spaces

- The milk is **in** the fridge.
- The children are playing **in** the garden.

### 2. Towns, cities, countries

- I live **in** Girona. My cousins live **in** France.

> ⚠️ Typical error: ~~at Barcelona~~ → Cities take *in*: *in Barcelona.*

### 3. Cars and taxis

- Get **in** the car! (but **on** the bus)

## Same place, different meaning

| Sentence | Meaning |
|---|---|
| She's **at** school. | She's a student there / attending classes. |
| She's **in** the school. | She's inside the building. |
| We're **at** the cinema. | We're watching a film. |
| It's cold **in** the cinema. | Inside the building. |

## Fixed expressions

| at home | at the top / bottom | in bed | in hospital | on the sofa |
|---|---|---|---|---|
| at the station | in the middle | in the corner (of a room) | on the corner (of a street) | on page 5 |

## Common mistakes

**1. *In* with surfaces.** *~~in the table~~* → **on the table.**

**2. *At* with cities.** *~~at Madrid~~* → **in Madrid.**

**3. *In* with buses and trains.** *~~in the train~~* → **on the train.**

**4. *In home*.** *~~I'm in home~~* → **I'm at home.**

**Pro tip:** picture it — a dot (**at**), a flat surface (**on**), or a box around it (**in**).
'''

GAP = ('Fill in the gaps',
  'Type at, on or in. Think: a point (at), a surface or line (on), or an enclosed space (in). Twenty original sentences.',
  [
  ('At', 'I’ll wait for you [[at]] the bus stop.', 'at / on / in', 'A point where you meet someone: at the bus stop.'),
  ('At', 'There’s someone [[at]] the door. Can you open it?', 'at / on / in', 'A point (the door): at the door.'),
  ('At', 'My mum is [[at]] work until six.', 'at / in', 'A place where an activity happens: at work.'),
  ('At', 'We met [[at]] Laia’s birthday party.', 'at / in', 'An event: at a party, at a concert.'),
  ('At', 'I stayed [[at]] home all weekend.', 'at / in', 'Fixed expression: at home. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('At', 'They live [[at]] 15 Carrer Nou.', 'at / on / in', 'An address with a number takes ‘at’.'),
  ('On', 'Your phone is [[on]] the kitchen table.', 'at / on / in', 'A surface: on the table.'),
  ('On', 'There’s a beautiful painting [[on]] the wall.', 'on / in', 'A wall is a surface: on the wall.'),
  ('On', 'Our flat is [[on]] the third floor.', 'on / in', 'Floors of a building take ‘on’.'),
  ('On', 'I left my jacket [[on]] the train.', 'on / in', 'Public transport (train, bus, plane) takes ‘on’.'),
  ('On', 'The answer is [[on]] page 42.', 'on / in', 'Fixed expression: on page 42.'),
  ('On', 'Turn left and the bakery is [[on]] the right.', 'on / in', 'Fixed expression: on the left / right.'),
  ('In', 'The milk is [[in]] the fridge.', 'at / on / in', 'An enclosed space: in the fridge.'),
  ('In', 'My grandparents live [[in]] a small village near Olot.', 'at / in', 'Villages, towns and cities take ‘in’.'),
  ('In', 'She has lived [[in]] Germany for two years.', 'at / in', 'Countries take ‘in’.'),
  ('In', 'The kids are playing [[in]] the garden.', 'on / in', 'An area with boundaries: in the garden.'),
  ('In', 'Get [[in]] the car — we’re late!', 'on / in', 'Cars and taxis take ‘in’ (but ‘on’ the bus).'),
  ('In', 'He’s still [[in]] bed. He’s got a fever.', 'at / in', 'Fixed expression: in bed.'),
  ('In', 'There’s a lamp [[in]] the corner of the room.', 'on / in', 'Inside a room: in the corner. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('On', 'There’s a café [[on]] the corner of our street.', 'on / in', 'Where two streets meet: on the corner.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with at, on and in for place.',
  [
  ('At', 'I’m waiting at the station.', []),
  ('At', 'She’s at work now.', []),
  ('At', 'We stayed at home.', []),
  ('At', 'There’s someone at the door.', []),
  ('At', 'They met at a concert.', []),
  ('On', 'The keys are on the table.', []),
  ('On', 'There’s a map on the wall.', []),
  ('On', 'We live on the second floor.', []),
  ('On', 'I fell asleep on the bus.', []),
  ('On', 'The bank is on the left.', []),
  ('In', 'The cat is in the box.', []),
  ('In', 'She lives in Barcelona.', []),
  ('In', 'My shoes are in the cupboard.', []),
  ('In', 'We swam in the sea.', []),
  ('In', 'Get in the taxi.', []),
  ('In', 'He’s in bed.', []),
  ('Mixed', 'She’s at school in Girona.', []),
  ('Mixed', 'Your book is on the desk in my room.', []),
  ('Mixed', 'I left it on the train at Sants.', []),
  ('Mixed', 'We live in a flat on Main Street.', []),
  ])

MATCH = {'title': 'Match the place and the preposition', 'subtitle': 'Tap a place, then tap the preposition it needs.',
  'leftLabel': 'Place', 'rightLabel': 'Preposition', 'rightLabelSub': '(at / on / in)', 'reviewArrowPrefix': '',
  'pairs': [
  ('___ the bus stop', 'at'), ('___ the table', 'on'), ('___ the fridge', 'in'), ('___ home', 'at'), ('___ the wall', 'on'),
  ('___ Spain', 'in'), ('___ work', 'at'), ('___ the bus', 'on'), ('___ the car', 'in'), ('___ a party', 'at'),
  ('___ the floor', 'on'), ('___ the kitchen', 'in'), ('___ the door', 'at'), ('___ page 10', 'on'), ('___ bed', 'in'),
  ('___ school', 'at'), ('___ the left', 'on'), ('___ London', 'in'), ('___ the station', 'at'), ('___ the second floor', 'on'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. At for points and activities, on for surfaces, lines and public transport, in for enclosed spaces and places.',
  [
  ('On', 'Put the plates ___ the table, please.', ['on', 'in', 'at', 'into'],
   ['‘In the table’ would mean inside it.', '‘At the table’ means sitting there, not on its surface.', '‘Into’ shows movement inside something.'],
   'A surface takes ‘on’: on the table. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In', 'The ice cream is ___ the freezer.', ['in', 'on', 'at', 'onto'],
   ['‘On the freezer’ means on top of it.', '‘At the freezer’ means next to it.', '‘Onto’ shows movement onto a surface.'],
   'An enclosed space takes ‘in’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('At', 'Let’s meet ___ the entrance at six.', ['at', 'in', 'on', 'into'],
   ['‘In the entrance’ suggests inside an area.', '‘On the entrance’ is wrong.', '‘Into’ shows movement.'],
   'A meeting point takes ‘at’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In', 'My cousins live ___ Valencia.', ['in', 'at', 'on', 'to'],
   ['‘At Valencia’ is a common mistake for cities.', '‘On Valencia’ is wrong.', '‘To Valencia’ shows movement.'],
   'Cities and countries take ‘in’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('At', 'He isn’t at home. He’s ___ work.', ['at', 'in', 'on', 'to'],
   ['‘In work’ is wrong for being at your job.', '‘On work’ is wrong.', '‘To work’ shows movement.'],
   'Activity places: at work, at school, at university. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('On', 'I always read ___ the train.', ['on', 'in', 'at', 'by'],
   ['‘In the train’ is less natural; public transport takes ‘on’.', '‘At the train’ is wrong.', '‘By train’ is how you travel, not where you read.'],
   'Public transport takes ‘on’: on the train, on the bus. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In', 'Jump ___ the car — I’ll drive you.', ['in', 'on', 'at', 'by'],
   ['Cars take ‘in’, not ‘on’.', '‘At the car’ means next to it.', '‘By the car’ means next to it.'],
   'Cars and taxis take ‘in’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('On', 'There’s a spider ___ the ceiling!', ['on', 'in', 'at', 'under'],
   ['‘In the ceiling’ means inside it.', '‘At the ceiling’ is wrong.', '‘Under the ceiling’ is unnatural.'],
   'The ceiling is a surface: on the ceiling. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('On', 'They live ___ the fifth floor.', ['on', 'in', 'at', 'to'],
   ['‘In the fifth floor’ is a common mistake.', '‘At the fifth floor’ is wrong.', '‘To’ shows movement.'],
   'Floors take ‘on’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('At', 'There were lots of people ___ the concert.', ['at', 'on', 'in', 'to'],
   ['‘On the concert’ is wrong.', '‘In the concert’ is possible inside the hall, but for the event use ‘at’.', '‘To’ shows movement.'],
   'Events take ‘at’: at a concert, at a wedding. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('At', 'I spent the whole weekend ___ home.', ['at', 'in', 'on', 'to'],
   ['‘In home’ is a common mistake.', '‘On home’ is wrong.', '‘To home’ is wrong (it’s just ‘go home’).'],
   'Fixed expression: at home. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In', 'She’s been ___ hospital since Monday.', ['in', 'at', 'on', 'into'],
   ['‘At hospital’ is not used for patients.', '‘On hospital’ is wrong.', '‘Into’ shows movement.'],
   'Fixed expression for a patient: in hospital. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('On', 'Look at the photo ___ page 12.', ['on', 'in', 'at', 'from'],
   ['‘In page 12’ is wrong.', '‘At page 12’ is wrong.', '‘From page 12’ changes the meaning.'],
   'Fixed expression: on page 12. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('At / in', 'Which sentence means she is a student there?', ['She’s at university.', 'She’s in the university building.', 'She’s on university.', 'She’s into university.'],
   ['That only says she is inside the building.', '‘On university’ is wrong.', '‘Into’ shows movement or interest.'],
   '‘At university’ describes the activity of studying there.'),
  ('On', 'Sitges is ___ the coast, south of Barcelona.', ['on', 'in', 'at', 'by the'],
   ['‘In the coast’ is wrong.', '‘At the coast’ is possible but less common for a town’s position.', '‘By the the coast’ repeats ‘the’.'],
   'Lines like coasts and rivers take ‘on’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In', 'There’s a plant ___ the corner of the classroom.', ['in', 'on', 'at', 'into'],
   ['‘On the corner’ is for street corners.', '‘At the corner’ is possible but ‘in’ is best inside a room.', '‘Into’ shows movement.'],
   'Inside a room: in the corner. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('On', 'The chemist’s is ___ the corner of Carrer Nou.', ['on', 'in', 'into', 'inside'],
   ['‘In the corner’ is for rooms.', '‘Into’ shows movement.', '‘Inside the corner’ is wrong.'],
   'Where streets meet: on the corner. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('At', 'She lives ___ 12 Oxford Road.', ['at', 'in', 'on', 'by'],
   ['‘In’ is for the street or town without a number.', '‘On Oxford Road’ is fine without the number, but with a number use ‘at’.', '‘By’ means next to.'],
   'Full address with a number: at. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('Mixed', 'Which sentence is correct?', ['My keys are on the desk in my bedroom.', 'My keys are in the desk on my bedroom.', 'My keys are at the desk in my bedroom.', 'My keys are on the desk at my bedroom.'],
   ['‘In the desk’ means inside a drawer; ‘on my bedroom’ is wrong.', '‘At the desk’ means sitting there.', '‘At my bedroom’ is wrong.'],
   'Surface → on; room → in. Check each place separately. Check each place separately.'),
  ('Mixed', 'Which sentence is correct?', ['I’m at the station in Girona.', 'I’m in the station at Girona.', 'I’m on the station in Girona.', 'I’m at the station at Girona.'],
   ['‘At Girona’ is wrong for a city.', '‘On the station’ is wrong.', 'Cities take ‘in’.'],
   'Point → at; city → in. Check each place separately. Check each place separately.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('In for surface', 'Your book is *in* the table.', 'on', 'A surface takes ‘on’: ‘on the table’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In for surface', 'There’s a poster *in* the wall.', 'on', 'A wall is a surface: ‘on the wall’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('At for city', 'My aunt lives *at* Madrid.', 'in', 'Cities take ‘in’: ‘in Madrid’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('At for country', 'We spent a week *at* Italy.', 'in', 'Countries take ‘in’: ‘in Italy’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In for transport', 'I met him *in* the bus.', 'on', 'Public transport takes ‘on’: ‘on the bus’.'),
  ('In for transport', 'She fell asleep *in* the plane.', 'on', 'Planes take ‘on’: ‘on the plane’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('On for car', 'Get *on* the car, quickly!', 'in', 'Cars take ‘in’: ‘in the car’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In for home', 'I stayed *in* home yesterday.', 'at', 'Fixed expression: ‘at home’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In for work', 'Dad is still *in* work.', 'at', 'Activity place: ‘at work’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In for floor', 'We live *in* the fourth floor.', 'on', 'Floors take ‘on’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('At for fridge', 'The juice is *at* the fridge.', 'in', 'An enclosed space: ‘in the fridge’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('On for garden', 'The dog is playing *on* the garden.', 'in', 'An area with borders: ‘in the garden’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In for page', 'Read the text *in* page 30.', 'on', 'Fixed expression: ‘on page 30’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('On for event', 'We met *on* a wedding.', 'at', 'Events take ‘at’: ‘at a wedding’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('At for bed', 'She’s still *at* bed.', 'in', 'Fixed expression: ‘in bed’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In for right', 'The school is *in* the right.', 'on', 'Fixed expression: ‘on the right’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In for door', 'There’s somebody *in* the door.', 'at', 'A point: ‘at the door’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('At for street', 'The shop is *at* Gran Via.', 'on', 'Streets (without a number) take ‘on’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('On for room', 'The children are *on* the living room.', 'in', 'Rooms take ‘in’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In for bus stop', 'Wait for me *in* the bus stop.', 'at', 'A point: ‘at the bus stop’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, at / on / in, multiple choice and spot-the-mistake. In the typing questions write at, on or in. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('which', 'At, on or in'),
 'fill': [
  ('On', 'There’s a cat [[on]] the roof.', 'at / on / in', 'A roof is a surface, so it takes the preposition ‘on’.', 'Surface → on. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In', 'We live [[in]] a small town.', 'at / on / in', 'Towns and cities take ‘in’: in a small town. Picture it: a point (at), a surface or line (on), a space around it (in).', 'Town → in.'),
  ('At', 'She’s [[at]] the dentist’s.', 'at / on / in', 'A place where something happens: at the dentist’s.', 'Point / activity → at.'),
  ('On', 'I saw her [[on]] the train.', 'on / in', 'Public transport like trains and buses takes ‘on’.', 'Train → on.'),
  ],
 'order': [
  ('On', 'The vase is on the shelf.', []),
  ('In', 'He works in Paris.', []),
  ('At', 'We’re at the airport.', []),
  ('In', 'Get in the taxi.', []),
  ],
 'customItems': [
  ('Which', '___ the sofa', ['on', 'in', 'at', 'into'],
   ['‘In the sofa’ means inside it.', '‘At the sofa’ is wrong.', '‘Into’ shows movement.'],
   'Sitting on a surface → on the sofa. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('Which', '___ the bathroom', ['in', 'on', 'at', 'onto'],
   ['‘On the bathroom’ is wrong.', '‘At the bathroom’ is wrong.', '‘Onto’ shows movement.'],
   'Rooms → in. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('Which', '___ the bus stop', ['at', 'on', 'in', 'into'],
   ['‘On the bus stop’ is wrong.', '‘In the bus stop’ is wrong.', '‘Into’ shows movement.'],
   'A point → at. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('Which', '___ Portugal', ['in', 'at', 'on', 'to'],
   ['‘At Portugal’ is wrong.', '‘On Portugal’ is wrong.', '‘To’ shows movement.'],
   'Countries → in. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ],
 'mc': [
  ('At', 'He’s not here — he’s ___ school.', ['at', 'in', 'on', 'to'],
   ['‘In school’ is American English or means inside the building.', '‘On school’ is wrong.', '‘To school’ shows movement.'],
   'Activity place → at school. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('On', 'The bakery is ___ Carrer Major.', ['on', 'in', 'at', 'to'],
   ['‘In Carrer Major’ is possible in British English, but ‘on’ is more common.', 'Without a number, ‘at’ is wrong.', '‘To’ shows movement.'],
   'Streets → on. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In', 'Your coat is ___ the wardrobe.', ['in', 'on', 'at', 'onto'],
   ['‘On the wardrobe’ means on top of it.', '‘At the wardrobe’ means next to it.', '‘Onto’ shows movement.'],
   'Enclosed space → in. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('On', 'We sat ___ the grass.', ['on', 'in', 'at', 'into'],
   ['‘In the grass’ means hidden in long grass.', '‘At the grass’ is wrong.', '‘Into’ shows movement.'],
   'Surface → on.'),
  ],
 'error': [
  ('In for surface', 'The cup is *in* the shelf.', 'on', 'A surface takes ‘on’: ‘on the shelf’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('At for city', 'They live *at* Paris.', 'in', 'Cities take ‘in’: ‘in Paris’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In for transport', 'I left my bag *in* the bus.', 'on', 'Buses take ‘on’: ‘on the bus’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ('In for home', 'She works *in* home.', 'at', 'Fixed expression: ‘at home’. Picture it: a point (at), a surface or line (on), a space around it (in).'),
  ],
}
