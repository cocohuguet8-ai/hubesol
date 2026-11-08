TITLE = 'In, On, At: time vs place'
AUX = (['in', 'on', 'at'], None, 'at')
NEXT = ('Prepositions of Movement', '/grammar/prepositions/prepositions-of-movement/')
BODY = r'''
## The same three words, two jobs

*In, on* and *at* work for both **time** and **place**. The logic is similar: **at** = a point, **on** = a surface or a day, **in** = something bigger that surrounds you.

| | Time | Place |
|---|---|---|
| **at** | at 6 o'clock, at night, at Christmas | at the door, at school, at a party |
| **on** | on Monday, on 3 May, on my birthday | on the table, on the wall, on the bus |
| **in** | in July, in 2026, in the morning | in the box, in the kitchen, in Girona |

## *At*: points

### 1. Time: an exact moment

- The train leaves **at** 10.15.
- I'm free **at** lunchtime.

### 2. Place: a specific point or activity

- I'll meet you **at** the station.
- She's **at** work.

> ⚠️ Typical error: ~~I'll meet you in 10.15 in the station.~~ → *at 10.15 at the station.*

## *On*: days and surfaces

### 1. Time: days and dates

- My exam is **on** Thursday.
- We married **on** 21 June.

### 2. Place: surfaces, lines and public transport

- Your glasses are **on** the sofa.
- I read **on** the train.

> ⚠️ Typical error: ~~on July on the table~~ → *in July*, but *on the table*.

## *In*: bigger periods and spaces

### 1. Time: months, years, seasons, parts of the day

- It snows **in** winter.
- I study **in** the evening.

### 2. Place: enclosed spaces, towns, countries

- The cat is **in** the box.
- They live **in** Portugal.

> ⚠️ Typical error: ~~at the morning at Barcelona~~ → *in the morning in Barcelona.*

## Mixing time and place in one sentence

The usual order in English is **place before time**.

- We had lunch **at** a café **on** Sunday.
- She was born **in** Girona **in** 2010.
- I'll see you **at** the gym **at** six.

## Exceptions to remember

| Time | Place |
|---|---|
| **at** night (not *in*) | **at** home (not *in*) |
| **in** the morning (but **on** Monday morning) | **in** bed / **in** hospital |
| **at** the weekend (UK) / **on** the weekend (US) | **on** the corner (street) / **in** the corner (room) |

## No preposition

Time: **no** preposition before *next, last, this, every, today, tomorrow*.
Place: **no** preposition before *home* after *go / come*: *I went home* (not ~~to home~~).

## Common mistakes

**1. *In* for clock times.** *~~in 8 o'clock~~* → **at 8 o'clock.**

**2. *At* for cities.** *~~at London~~* → **in London.**

**3. *In* for days.** *~~in Friday~~* → **on Friday.**

**4. *In* for surfaces.** *~~in the floor~~* → **on the floor.**

**Pro tip:** for both time and place, go from small to big — **at** (a point) → **on** (a day / a surface) → **in** (a period / a space).
'''

GAP = ('Fill in the gaps',
  'Type at, on or in. Some sentences are about time, some about place, some about both. Twenty original sentences.',
  [
  ('Time', 'The meeting starts [[at]] four o’clock.', 'at / on / in', 'Time: an exact clock time takes ‘at’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place', 'I’ll wait for you [[at]] the main entrance.', 'at / on / in', 'Place: a meeting point takes ‘at’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time', 'We’ve got an English exam [[on]] Monday.', 'at / on / in', 'Time: days of the week take ‘on’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place', 'I left my keys [[on]] the kitchen table.', 'at / on / in', 'Place: a surface takes ‘on’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time', 'My brother was born [[in]] 2008.', 'at / on / in', 'Time: years take ‘in’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place', 'My brother lives [[in]] Manchester now.', 'at / on / in', 'Place: cities take ‘in’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time', 'I love walking on the beach [[in]] the evening.', 'at / in', 'Time: parts of the day take ‘in’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time', 'I can’t sleep [[at]] night because of the noise.', 'at / in', 'Time: the fixed phrase is ‘at night’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place', 'She’s [[at]] home today — she’s ill.', 'at / in', 'Place: the fixed phrase is ‘at home’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place', 'He’s been [[in]] bed all day with a fever.', 'at / in', 'Place: the fixed phrase is ‘in bed’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time', 'The shops are very busy [[at]] Christmas.', 'at / on', 'Time: holiday periods take ‘at’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time', 'We open presents [[on]] Christmas morning.', 'at / on / in', 'Time: a specific day + morning takes ‘on’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place', 'I always listen to music [[on]] the bus.', 'on / in', 'Place: public transport takes ‘on’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place', 'Put the milk back [[in]] the fridge.', 'on / in', 'Place: an enclosed space takes ‘in’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time', 'It’s usually hot [[in]] July.', 'on / in', 'Time: months take ‘in’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place', 'We live [[on]] the first floor.', 'on / in', 'Place: floors take ‘on’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Both', 'We had dinner [[at]] a nice restaurant on Saturday.', 'at / in', 'Place: a specific venue for an activity takes ‘at’.'),
  ('Both', 'She was born in Lleida [[on]] 2 February.', 'on / in', 'Time: a date takes ‘on’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Both', 'See you at the gym [[at]] seven.', 'at / in', 'Time: a clock time takes ‘at’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Both', 'I lived in Rome [[in]] the summer of 2022.', 'at / on / in', 'Time: a season or period takes ‘in’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples mixing time and place. Remember: place usually comes before time.',
  [
  ('Time', 'The film starts at nine.', []),
  ('Time', 'I have Spanish on Tuesday.', []),
  ('Time', 'She was born in May.', []),
  ('Time', 'I read in the evening.', []),
  ('Place', 'The keys are on the table.', []),
  ('Place', 'He lives in Madrid.', []),
  ('Place', 'We met at the station.', []),
  ('Place', 'She’s at work.', []),
  ('Both', 'We met at a party on Friday.', []),
  ('Both', 'I was born in Girona in 2010.', []),
  ('Both', 'See you at school at eight.', []),
  ('Both', 'They got married in Rome in June.', []),
  ('Both', 'I’ll be at home on Sunday.', []),
  ('Both', 'We had lunch in a café at one.', []),
  ('Both', 'She works in a bank on Saturdays.', []),
  ('Both', 'I read on the bus in the morning.', []),
  ('Exceptions', 'I can’t sleep at night.', []),
  ('Exceptions', 'He’s in bed now.', []),
  ('Exceptions', 'We stayed at home at the weekend.', []),
  ('Exceptions', 'I’ll call you on Monday morning.', []),
  ])

MATCH = {'title': 'Time or place?', 'subtitle': 'Tap an expression, then tap the preposition it needs. Some are time, some are place.',
  'leftLabel': 'Expression', 'rightLabel': 'Preposition', 'rightLabelSub': '(at / on / in)', 'reviewArrowPrefix': '',
  'pairs': [
  ('___ 5 o’clock', 'at'), ('___ the table', 'on'), ('___ 2024', 'in'), ('___ the station', 'at'), ('___ Monday', 'on'),
  ('___ the kitchen', 'in'), ('___ night', 'at'), ('___ the bus', 'on'), ('___ the morning', 'in'), ('___ home', 'at'),
  ('___ my birthday', 'on'), ('___ Spain', 'in'), ('___ Christmas', 'at'), ('___ the wall', 'on'), ('___ winter', 'in'),
  ('___ a party', 'at'), ('___ 6 June', 'on'), ('___ bed', 'in'), ('___ noon', 'at'), ('___ the floor', 'on'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. At = a point, on = a day or surface, in = a bigger period or space — for both time and place.',
  [
  ('Time', 'The bus leaves ___ 7.45.', ['at', 'on', 'in', 'by'],
   ['‘On’ is for days and dates, not clock times.', '‘In 7.45’ would mean after 7.45 minutes — wrong here.', '‘By 7.45’ means not later than 7.45.'],
   'Time point: an exact clock time takes ‘at’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place', 'Let’s meet ___ the café near the station.', ['at', 'on', 'into', 'onto'],
   ['‘On the café’ means on its roof.', '‘Into’ shows movement inside.', '‘Onto’ shows movement onto a surface.'],
   'Place point: a meeting place takes ‘at’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time', 'My dentist appointment is ___ Wednesday.', ['on', 'in', 'at', '—'],
   ['‘In Wednesday’ is wrong: days take ‘on’.', '‘At Wednesday’ is wrong.', 'A day needs a preposition here.'],
   'Days take ‘on’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place', 'There’s a fly ___ your nose!', ['on', 'in', 'at', 'into'],
   ['‘In your nose’ means inside it.', '‘At your nose’ is wrong.', '‘Into’ shows movement.'],
   'A surface takes ‘on’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time', 'We go to the beach ___ summer.', ['in', 'on', 'at', '—'],
   ['‘On summer’ is wrong.', '‘At summer’ is wrong.', 'A season needs a preposition here.'],
   'Seasons take ‘in’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place', 'My grandparents live ___ a village in the Pyrenees.', ['in', 'at', 'on', 'to'],
   ['‘At a village’ is wrong for where you live.', '‘On a village’ is wrong.', '‘To’ shows movement.'],
   'Villages, towns and cities take ‘in’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Exception', 'I hate walking alone ___ night.', ['at', 'in', 'on', 'by'],
   ['‘In the night’ needs ‘the’, and the fixed phrase is ‘at night’.', '‘On night’ is wrong.', '‘By night’ is literary.'],
   'Fixed phrase: at night. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Exception', 'Is your sister ___ home?', ['at', 'in', 'on', 'to'],
   ['‘In home’ is a common mistake.', '‘On home’ is wrong.', '‘To home’ is wrong.'],
   'Fixed phrase: at home. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Exception', 'I’ll see you ___ Friday morning.', ['on', 'in', 'at', '—'],
   ['‘In Friday morning’ is wrong: a specific day uses ‘on’.', '‘At Friday morning’ is wrong.', 'A preposition is needed.'],
   'Day + part of day: on Friday morning. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Both', 'Which sentence is correct?', ['I was born in Girona in 2011.', 'I was born at Girona in 2011.', 'I was born in Girona on 2011.', 'I was born on Girona in 2011.'],
   ['Cities take ‘in’, not ‘at’.', 'Years take ‘in’, not ‘on’.', 'Cities take ‘in’, not ‘on’.'],
   'City → in; year → in. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Both', 'Which sentence is correct?', ['We met at the cinema on Saturday.', 'We met in the cinema at Saturday.', 'We met on the cinema on Saturday.', 'We met at the cinema in Saturday.'],
   ['Days take ‘on’, not ‘at’.', '‘On the cinema’ is wrong.', 'Days take ‘on’, not ‘in’.'],
   'Event place → at; day → on. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place', 'I read the whole book ___ the plane.', ['on', 'in', 'at', 'by'],
   ['Public transport takes ‘on’.', '‘At the plane’ is wrong.', '‘By plane’ is how you travel.'],
   'Public transport takes ‘on’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time', 'The castle was built ___ the 13th century.', ['in', 'on', 'at', '—'],
   ['‘On’ is for days.', '‘At’ is for points.', 'A preposition is needed.'],
   'Centuries take ‘in’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place', 'Our classroom is ___ the second floor.', ['on', 'in', 'at', 'to'],
   ['‘In the second floor’ is a common mistake.', '‘At the second floor’ is wrong.', '‘To’ shows movement.'],
   'Floors take ‘on’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time', 'She always calls me ___ my birthday.', ['on', 'in', 'at', '—'],
   ['‘In my birthday’ is wrong.', '‘At my birthday’ is used for the party, not the day.', 'A preposition is needed.'],
   'Specific days take ‘on’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place', 'The towels are ___ the bathroom.', ['in', 'on', 'at', 'onto'],
   ['‘On the bathroom’ is wrong.', '‘At the bathroom’ is wrong.', '‘Onto’ shows movement.'],
   'Rooms take ‘in’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Order', 'Which word order is most natural?', ['We played football in the park on Sunday.', 'We played football on Sunday in the park.', 'On Sunday in the park we football played.', 'We in the park played football on Sunday.'],
   ['Possible, but place before time is more usual.', 'The verb and object are in the wrong order.', 'Adverbials don’t go between subject and verb.'],
   'Usual order: place before time. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Exception', 'She’s ___ hospital after an accident.', ['in', 'at', 'on', 'into'],
   ['‘At hospital’ is not used for patients.', '‘On hospital’ is wrong.', '‘Into’ shows movement.'],
   'Fixed phrase for patients: in hospital. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time', 'We usually eat ___ two o’clock.', ['at', 'in', 'on', '—'],
   ['‘In two o’clock’ is wrong.', '‘On two o’clock’ is wrong.', 'A preposition is needed.'],
   'Clock time: at. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place', 'There’s a great bakery ___ the corner of our street.', ['on', 'in', 'into', 'inside'],
   ['‘In the corner’ is for rooms.', '‘Into’ shows movement.', '‘Inside the corner’ is wrong.'],
   'Street corner: on the corner. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('Time: clock', 'The class starts *in* 9 o’clock.', 'at', 'Clock times take ‘at’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time: day', 'I’ll call you *in* Friday.', 'on', 'Days take ‘on’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time: month', 'We travel *on* August.', 'in', 'Months take ‘in’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time: year', 'He was born *at* 2009.', 'in', 'Years take ‘in’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time: night', 'Owls hunt *in* night.', 'at', 'Fixed phrase: ‘at night’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time: morning', 'I run *at* the morning.', 'in', 'Parts of the day take ‘in’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time: date', 'The exam is *in* 3 June.', 'on', 'Dates take ‘on’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place: city', 'She works *at* London.', 'in', 'Cities take ‘in’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place: surface', 'The book is *in* the shelf.', 'on', 'Surfaces take ‘on’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place: transport', 'I saw her *in* the bus.', 'on', 'Public transport takes ‘on’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place: home', 'Are you *in* home?', 'at', 'Fixed phrase: ‘at home’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place: room', 'The dog is *on* the kitchen.', 'in', 'Rooms take ‘in’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place: point', 'Wait *in* the bus stop.', 'at', 'A point takes ‘at’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place: floor', 'Our flat is *in* the third floor.', 'on', 'Floors take ‘on’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Both', 'We met at a café *in* Monday.', 'on', 'Days take ‘on’: ‘on Monday’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Both', 'I moved to Girona *on* 2015.', 'in', 'Years take ‘in’: ‘in 2015’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Exception', 'I’ll see you *in* Monday morning.', 'on', 'Day + part of day: ‘on Monday morning’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Exception', 'She’s *at* bed with a cold.', 'in', 'Fixed phrase: ‘in bed’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Holiday', 'We go skiing *on* Easter.', 'at', 'British English: ‘at Easter’ (the holiday period).'),
  ('Wall', 'There’s a clock *in* the wall.', 'on', 'A wall is a surface: ‘on the wall’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, time or place, multiple choice and spot-the-mistake. In the typing questions write at, on or in. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('which', 'Time or place'),
 'fill': [
  ('Time', 'The shop opens [[at]] nine.', 'at / on / in', 'Time: an exact clock time always takes the preposition ‘at’.', 'Clock time → at.'),
  ('Place', 'The shop is [[in]] the city centre.', 'at / on / in', 'Place: an area like the city centre takes ‘in’.', 'Area → in.'),
  ('Time', 'It closes [[on]] Sundays.', 'at / on / in', 'Time: days of the week always take the preposition ‘on’.', 'Day → on.'),
  ('Place', 'The prices are [[on]] the door.', 'at / on / in', 'Place: a surface such as a door takes the preposition ‘on’.', 'Surface → on.'),
  ],
 'order': [
  ('Both', 'We met at school in 2019.', []),
  ('Both', 'She lives in Rome now.', []),
  ('Exceptions', 'I sleep badly at night.', []),
  ('Both', 'The keys are on the table.', []),
  ],
 'customItems': [
  ('Which', '___ 2030 (time)', ['in', 'on', 'at', '—'],
   ['‘On’ is for days.', '‘At’ is for clock times.', 'A year needs a preposition.'],
   'Years take ‘in’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Which', '___ the corner of the room (place)', ['in', 'on', 'at', 'into'],
   ['‘On the corner’ is for streets.', '‘At the corner’ is possible but ‘in’ is best for rooms.', '‘Into’ shows movement.'],
   'Room corner → in. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Which', '___ Christmas Day (time)', ['on', 'at', 'in', '—'],
   ['‘At Christmas’ is the period; Christmas Day is a day.', '‘In’ is for longer periods.', 'A preposition is needed.'],
   'A specific day takes ‘on’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Which', '___ the airport (place)', ['at', 'on', 'in', 'into'],
   ['‘On the airport’ is wrong.', '‘In the airport’ means inside the building.', '‘Into’ shows movement.'],
   'A point / place of activity → at. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ],
 'mc': [
  ('Time', 'I usually do my homework ___ the afternoon.', ['in', 'at', 'on', '—'],
   ['‘At the afternoon’ is wrong.', '‘On the afternoon’ needs a specific day.', 'A preposition is needed.'],
   'Parts of the day → in. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place', 'He sat ___ the floor to play.', ['on', 'in', 'at', 'into'],
   ['‘In the floor’ means inside it.', '‘At the floor’ is wrong.', '‘Into’ shows movement.'],
   'A surface → on. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Both', 'We’ll meet ___ the station ___ six.', ['at / at', 'in / at', 'at / in', 'on / at'],
   ['‘In the station’ means inside it, but the meeting point is ‘at’.', '‘In six’ means after six units.', '‘On the station’ is wrong.'],
   'Point in place → at; clock time → at. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Exception', 'She’s not at work — she’s ___ home.', ['at', 'in', 'on', 'to'],
   ['‘In home’ is wrong.', '‘On home’ is wrong.', '‘To home’ is wrong.'],
   'Fixed phrase: at home. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ],
 'error': [
  ('Time: clock', 'Lunch is *in* one o’clock.', 'at', 'Clock times take ‘at’: ‘at one o’clock’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place: city', 'I study *at* Barcelona.', 'in', 'Cities take ‘in’: ‘in Barcelona’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Time: day', 'We play football *in* Saturdays.', 'on', 'Days take ‘on’: ‘on Saturdays’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ('Place: surface', 'Your phone is *in* the sofa.', 'on', 'A surface takes ‘on’: ‘on the sofa’. Small to big: at (a point) → on (a day or surface) → in (a period or space).'),
  ],
}
