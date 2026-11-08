TITLE = 'Prepositions of Time: at/on/in'
AUX = (['at', 'on', 'in'], None, 'on')
NEXT = ('Prepositions of Place: at/on/in', '/grammar/prepositions/prepositions-of-place/')
BODY = r'''
## How to choose at, on or in

Think of a pyramid: **at** for small, exact points; **on** for days; **in** for longer periods.

| Preposition | Used for | Examples |
|---|---|---|
| **at** | exact times, points in the day, holidays/weekends (UK) | **at** 7 o'clock, **at** noon, **at** night, **at** Christmas, **at** the weekend |
| **on** | days and dates | **on** Monday, **on** 5 May, **on** my birthday, **on** Christmas Day |
| **in** | months, years, seasons, centuries, parts of the day | **in** July, **in** 2026, **in** winter, **in** the morning |

## When to use *at*

### 1. Clock times

- The film starts **at** 8.30.
- I get up **at** seven o'clock.

> ⚠️ Typical error: ~~The class starts in 9 o'clock.~~ → Exact times take *at*: *at 9 o'clock.*

### 2. Fixed expressions

| at night | at noon / midday | at midnight | at lunchtime |
|---|---|---|---|
| **at** the weekend (UK) | **at** Christmas / Easter | **at** the moment | **at** the same time |

- I never go out **at** night during exams.

> ⚠️ Typical error: ~~in the night~~ → For general night-time use *at night*.

## When to use *on*

### 1. Days and dates

- See you **on** Friday!
- My birthday is **on** 12 March.

> ⚠️ Typical error: ~~in Monday~~ → Days take *on*: *on Monday.*

### 2. Specific days

- **on** my birthday, **on** New Year's Eve, **on** Christmas Day
- **on** Monday morning, **on** Saturday night

## When to use *in*

### 1. Longer periods

- We moved here **in** 2019.
- It often snows **in** January.
- The castle was built **in** the 12th century.

> ⚠️ Typical error: ~~on July~~ → Months take *in*: *in July.*

### 2. Parts of the day

- **in** the morning, **in** the afternoon, **in** the evening
- But: **at** night, **at** noon.

### 3. *In* + time = after

- The train leaves **in** ten minutes. (ten minutes from now)

## No preposition

Don't use *at / on / in* before **this, next, last, every, today, tomorrow, yesterday**.

| ✗ | ✓ |
|---|---|
| ~~on next Monday~~ | **next** Monday |
| ~~in last summer~~ | **last** summer |
| ~~at every day~~ | **every** day |

## Morning, Monday morning

| General | Specific day |
|---|---|
| **in** the morning | **on** Monday morning |
| **in** the evening | **on** Friday evening |

## Common mistakes

**1. *In* with clock times.** *~~in 5 o'clock~~* → **at 5 o'clock.**

**2. *In* with days.** *~~in Saturday~~* → **on Saturday.**

**3. *On* with months.** *~~on August~~* → **in August.**

**4. Preposition with *next / last*.** *~~on next week~~* → **next week.**

**Pro tip:** the shorter the time, the smaller the word — **at** (minutes), **on** (days), **in** (months, years).
'''

GAP = ('Fill in the gaps',
  'Type at, on or in — or leave it out (type —) when no preposition is needed. Twenty original sentences.',
  [
  ('At', 'The film starts [[at]] half past eight.', 'at / on / in', 'Clock times take ‘at’: at half past eight, at 8.30.'),
  ('At', 'I usually go to bed [[at]] eleven o’clock.', 'at / on / in', 'An exact time on the clock always takes ‘at’.'),
  ('At', 'My little brother is scared of the dark, so he sleeps with a light on [[at]] night.', 'at / in', 'The fixed phrase is ‘at night’ (but ‘in the morning’).'),
  ('At', 'We always visit our grandparents [[at]] Christmas.', 'at / on', 'Holiday periods like Christmas and Easter take ‘at’.'),
  ('At', 'Sorry, I can’t talk [[at]] the moment — I’m in class.', 'at / in', 'Fixed expression: at the moment = now.'),
  ('On', 'We have a maths test [[on]] Friday.', 'at / on / in', 'Days of the week take ‘on’: on Friday.'),
  ('On', 'My birthday is [[on]] 14 July.', 'on / in', 'Dates take ‘on’: on 14 July.'),
  ('On', 'They got married [[on]] a sunny Saturday in May.', 'on / in', 'A specific day takes ‘on’, even with an adjective.'),
  ('On', 'We open our presents [[on]] Christmas Day.', 'at / on', 'A specific day (Christmas Day) takes ‘on’; the period takes ‘at’.'),
  ('On', 'I’ve got football practice [[on]] Monday evening.', 'on / in', 'Day + part of the day: on Monday evening.'),
  ('In', 'It’s very hot in Spain [[in]] August.', 'on / in', 'Months take ‘in’: in August.'),
  ('In', 'My parents met [[in]] 2005.', 'on / in', 'Years take ‘in’: in 2005.'),
  ('In', 'We go skiing [[in]] winter.', 'on / in', 'Seasons take ‘in’: in winter.'),
  ('In', 'I study better [[in]] the morning.', 'at / in', 'Parts of the day take ‘in’: in the morning.'),
  ('In', 'The cathedral was built [[in]] the 14th century.', 'on / in', 'Centuries take ‘in’. Remember: at for times, on for days, in for longer periods.'),
  ('In', 'Hurry up! The bus leaves [[in]] five minutes.', 'at / in', '‘In’ + a period = after that time from now. The bigger the time period, the bigger the word: at → on → in.'),
  ('No preposition', 'See you [[next]] Monday!', 'next / on next', 'Write just ‘next’: no preposition goes before next.'),
  ('No preposition', 'We went to Italy [[last]] summer.', 'last / in last', 'Write just ‘last’: no preposition goes before last.'),
  ('No preposition', 'I walk to school [[every]] day.', 'every / at every', 'Write just ‘every’: no preposition goes before every.'),
  ('At', 'I’m usually hungry [[at]] lunchtime.', 'at / in', 'Fixed point in the day: at lunchtime.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with at, on and in for time.',
  [
  ('At', 'The class starts at nine.', []),
  ('At', 'I get up at seven o’clock.', []),
  ('At', 'Owls hunt at night.', []),
  ('At', 'We eat turkey at Christmas.', []),
  ('At', 'She’s busy at the moment.', []),
  ('On', 'I have English on Monday.', []),
  ('On', 'My birthday is on 3 May.', []),
  ('On', 'We relax on Sunday afternoon.', []),
  ('On', 'They arrived on Christmas Eve.', []),
  ('In', 'It rains a lot in November.', []),
  ('In', 'She was born in 2011.', []),
  ('In', 'We swim in the summer.', []),
  ('In', 'I read in the evening.', []),
  ('In', 'The bus comes in ten minutes.', []),
  ('In', 'The house was built in the 1920s.', []),
  ('No preposition', 'I’ll call you next week.', []),
  ('No preposition', 'We met last year.', []),
  ('No preposition', 'He runs every morning.', []),
  ('No preposition', 'See you tomorrow.', []),
  ('Mixed', 'I’ll see you on Friday at six.', ['I’ll see you at six on Friday.']),
  ])

MATCH = {'title': 'Match the time and the preposition', 'subtitle': 'Tap a time expression, then tap the preposition it needs.',
  'leftLabel': 'Time', 'rightLabel': 'Preposition', 'rightLabelSub': '(at / on / in)', 'reviewArrowPrefix': '',
  'pairs': [
  ('___ 7.30', 'at'), ('___ Monday', 'on'), ('___ July', 'in'), ('___ night', 'at'), ('___ 2025', 'in'),
  ('___ my birthday', 'on'), ('___ the morning', 'in'), ('___ Christmas', 'at'), ('___ 10 March', 'on'), ('___ winter', 'in'),
  ('___ noon', 'at'), ('___ Friday evening', 'on'), ('___ the 21st century', 'in'), ('___ the weekend (UK)', 'at'), ('___ New Year’s Day', 'on'),
  ('___ the afternoon', 'in'), ('___ midnight', 'at'), ('___ Sunday', 'on'), ('___ spring', 'in'), ('___ lunchtime', 'at'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. At for clock times and points, on for days and dates, in for longer periods — and nothing before next / last / every.',
  [
  ('At', 'The concert starts ___ nine o’clock.', ['at', 'on', 'in', '—'],
   ['‘On’ is for days and dates, not clock times.', '‘In’ is for longer periods like months or years.', 'A clock time needs a preposition: you can’t leave it out.'],
   'Clock times always take ‘at’: at nine o’clock. The bigger the time period, the bigger the word: at → on → in.'),
  ('On', 'We’ve got a party ___ Saturday.', ['on', 'at', 'in', '—'],
   ['‘At’ is for clock times and points like ‘at night’.', '‘In’ is for months, years and seasons.', 'A day of the week needs ‘on’ here.'],
   'Days of the week take ‘on’: on Saturday. The bigger the time period, the bigger the word: at → on → in.'),
  ('In', 'My cousin was born ___ 2012.', ['in', 'on', 'at', '—'],
   ['‘On’ is for specific days and dates.', '‘At’ is for exact times.', 'A year needs a preposition.'],
   'Years take ‘in’: in 2012. The bigger the time period, the bigger the word: at → on → in.'),
  ('In', 'It’s cold here ___ January.', ['in', 'on', 'at', '—'],
   ['‘On January’ is wrong: months take ‘in’.', '‘At’ is for clock times.', 'A month needs a preposition here.'],
   'Months take ‘in’: in January. The bigger the time period, the bigger the word: at → on → in.'),
  ('On', 'Her birthday is ___ 2 October.', ['on', 'in', 'at', '—'],
   ['‘In’ is for the month alone, but with a date use ‘on’.', '‘At’ is for clock times.', 'A date needs ‘on’.'],
   'Dates take ‘on’: on 2 October. The bigger the time period, the bigger the word: at → on → in.'),
  ('At', 'I can’t sleep ___ night when it’s hot.', ['at', 'in', 'on', 'during the'],
   ['‘In the night’ is used for a specific night, but the general phrase is ‘at night’.', '‘On night’ is wrong.', '‘During the night’ needs ‘the’ and isn’t one option here.'],
   'Fixed phrase: at night (but in the morning / afternoon / evening).'),
  ('In', 'I always have a shower ___ the morning.', ['in', 'at', 'on', '—'],
   ['‘At the morning’ is a common mistake.', '‘On the morning’ needs a specific day.', 'A preposition is needed.'],
   'Parts of the day: in the morning, in the evening. The bigger the time period, the bigger the word: at → on → in.'),
  ('On', 'I’ll see you ___ Tuesday morning.', ['on', 'in', 'at', '—'],
   ['With a specific day, ‘in the morning’ becomes ‘on Tuesday morning’.', '‘At Tuesday’ is wrong.', 'A preposition is needed.'],
   'Day + part of day takes ‘on’: on Tuesday morning. The bigger the time period, the bigger the word: at → on → in.'),
  ('No preposition', 'We’re going to Paris ___ next week.', ['—', 'on', 'in', 'at'],
   ['No preposition before ‘next’.', 'No preposition before ‘next’.', 'No preposition before ‘next’.'],
   'No at / on / in before next, last, this, every. Words like next, last, this and every replace the preposition.'),
  ('No preposition', 'She started her new job ___ last Monday.', ['—', 'on', 'in', 'at'],
   ['No preposition before ‘last’.', 'No preposition before ‘last’.', 'No preposition before ‘last’.'],
   'No preposition before ‘last’: last Monday. Words like next, last, this and every replace the preposition.'),
  ('At', 'Many families get together ___ Easter.', ['at', 'on', 'in', 'by'],
   ['‘On Easter’ is American English for the day; in British English the holiday period is ‘at Easter’.', '‘In Easter’ is wrong.', '‘By Easter’ means before Easter.'],
   'Holiday periods take ‘at’: at Easter, at Christmas. The bigger the time period, the bigger the word: at → on → in.'),
  ('On', 'They exchange presents ___ Christmas Day.', ['on', 'at', 'in', '—'],
   ['‘At Christmas’ is the period; ‘Christmas Day’ is a specific day.', '‘In Christmas Day’ is wrong.', 'A preposition is needed.'],
   'A specific day takes ‘on’: on Christmas Day. The bigger the time period, the bigger the word: at → on → in.'),
  ('In', 'Lots of birds fly south ___ autumn.', ['in', 'on', 'at', 'by'],
   ['‘On autumn’ is wrong.', '‘At autumn’ is wrong.', '‘By autumn’ means before autumn.'],
   'Seasons take ‘in’: in autumn. The bigger the time period, the bigger the word: at → on → in.'),
  ('In', 'The pizza will be ready ___ fifteen minutes.', ['in', 'at', 'on', 'for'],
   ['‘At fifteen minutes’ is wrong.', '‘On fifteen minutes’ is wrong.', '‘For fifteen minutes’ means duration.'],
   '‘In’ + a period = after that time from now.'),
  ('At', 'We have a break ___ eleven.', ['at', 'in', 'on', '—'],
   ['‘In eleven’ would mean after eleven units of time.', '‘On eleven’ is wrong.', 'A preposition is needed.'],
   'Clock time: at eleven. The bigger the time period, the bigger the word: at → on → in.'),
  ('In', 'Gaudí was born ___ the 19th century.', ['in', 'on', 'at', '—'],
   ['‘On the century’ is wrong.', '‘At the century’ is wrong.', 'A preposition is needed.'],
   'Centuries take ‘in’. The bigger the time period, the bigger the word: at → on → in.'),
  ('Mixed', 'Which sentence is correct?', ['See you on Friday at six.', 'See you in Friday at six.', 'See you on Friday in six.', 'See you at Friday on six.'],
   ['‘In Friday’ is wrong.', '‘In six’ means after six units.', 'Both prepositions are wrong.'],
   'on + day, at + clock time. Check each time expression separately.'),
  ('Mixed', 'Which sentence is correct?', ['I was born in May, on a Sunday.', 'I was born on May, in a Sunday.', 'I was born at May, on a Sunday.', 'I was born in May, in a Sunday.'],
   ['Months take ‘in’, days take ‘on’.', '‘At May’ is wrong.', 'Days take ‘on’, not ‘in’.'],
   'in + month, on + day. Check each time expression separately.'),
  ('No preposition', 'I go swimming ___ every Wednesday.', ['—', 'on', 'at', 'in'],
   ['No preposition before ‘every’.', 'No preposition before ‘every’.', 'No preposition before ‘every’.'],
   'No preposition before ‘every’. Words like next, last, this and every replace the preposition.'),
  ('At', 'The shops close ___ midnight on Saturdays.', ['at', 'in', 'on', 'by the'],
   ['‘In midnight’ is wrong.', '‘On midnight’ is wrong.', '‘By the midnight’ is wrong.'],
   'Points of the day: at midnight, at noon. The bigger the time period, the bigger the word: at → on → in.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('In for clock time', 'The lesson starts *in* nine o’clock.', 'at', 'Clock times take ‘at’: ‘at nine o’clock’.'),
  ('On for clock time', 'I’ll meet you *on* 6.30.', 'at', 'Clock times take ‘at’: ‘at 6.30’. Remember: at for times, on for days, in for longer periods.'),
  ('In for day', 'We have PE *in* Thursday.', 'on', 'Days take ‘on’: ‘on Thursday’. Remember: at for times, on for days, in for longer periods.'),
  ('At for day', 'I’m free *at* Sunday.', 'on', 'Days take ‘on’: ‘on Sunday’. Remember: at for times, on for days, in for longer periods.'),
  ('On for month', 'My exams are *on* June.', 'in', 'Months take ‘in’: ‘in June’. Remember: at for times, on for days, in for longer periods.'),
  ('On for year', 'She moved to Girona *on* 2020.', 'in', 'Years take ‘in’: ‘in 2020’. Remember: at for times, on for days, in for longer periods.'),
  ('At for season', 'We go to the beach *at* summer.', 'in', 'Seasons take ‘in’: ‘in summer’. Remember: at for times, on for days, in for longer periods.'),
  ('In for date', 'The party is *in* 5 April.', 'on', 'Dates take ‘on’: ‘on 5 April’. Remember: at for times, on for days, in for longer periods.'),
  ('At for morning', 'I study best *at* the morning.', 'in', 'Parts of the day: ‘in the morning’. Remember: at for times, on for days, in for longer periods.'),
  ('In for night', 'He works *in* night.', 'at', 'Fixed phrase: ‘at night’. Remember: at for times, on for days, in for longer periods.'),
  ('In for birthday', 'I got a bike *in* my birthday.', 'on', 'Specific days: ‘on my birthday’. Remember: at for times, on for days, in for longer periods.'),
  ('On for Christmas', 'We visit Grandma *on* Christmas every year.', 'at', 'The holiday period: ‘at Christmas’. Remember: at for times, on for days, in for longer periods.'),
  ('In for weekend', 'I play tennis *in* the weekend.', 'at', 'British English: ‘at the weekend’ (American: ‘on the weekend’).'),
  ('At for evening', 'I watch TV *at* the evening.', 'in', 'Parts of the day take ‘in’: ‘in the evening’.'),
  ('On for afternoon', 'We go swimming *on* the afternoon.', 'in', 'Parts of the day take ‘in’: ‘in the afternoon’.'),
  ('In for day + morning', 'I have an exam *in* Monday morning.', 'on', 'Day + part of day: ‘on Monday morning’. Remember: at for times, on for days, in for longer periods.'),
  ('On for century', 'It was painted *on* the 15th century.', 'in', 'Centuries take ‘in’.'),
  ('At for after', 'The film starts *at* ten minutes — hurry!', 'in', '‘In ten minutes’ = ten minutes from now.'),
  ('In for noon', 'We eat *in* noon.', 'at', 'Fixed point: ‘at noon’. Remember: at for times, on for days, in for longer periods.'),
  ('On for moment', 'I’m busy *on* the moment.', 'at', 'Fixed phrase: ‘at the moment’. Remember: at for times, on for days, in for longer periods.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, at / on / in, multiple choice and spot-the-mistake. In the typing questions write at, on, in or — for no preposition. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('which', 'At, on or in'),
 'fill': [
  ('At', 'Breakfast is served [[at]] 8 a.m.', 'at / on / in', 'An exact clock time always takes the preposition ‘at’.', 'Clock time → at.'),
  ('On', 'The match is [[on]] Saturday.', 'at / on / in', 'Days of the week always take the preposition ‘on’.', 'Day → on.'),
  ('In', 'We go camping [[in]] August.', 'at / on / in', 'Months, years and seasons take the preposition ‘in’.', 'Month → in.'),
  ('No preposition', 'I’ll finish it [[tomorrow]].', 'tomorrow / on tomorrow', 'No preposition before tomorrow, next, last or every.', 'Just ‘tomorrow’.'),
  ],
 'order': [
  ('At', 'I wake up at six.', []),
  ('On', 'We meet on Fridays.', []),
  ('In', 'She skis in winter.', []),
  ('No preposition', 'I saw him last week.', []),
  ],
 'customItems': [
  ('Which', '___ 3 o’clock', ['at', 'on', 'in', '—'],
   ['‘On’ is for days and dates.', '‘In’ is for longer periods.', 'A clock time needs a preposition.'],
   'Clock times → at.'),
  ('Which', '___ Wednesday', ['on', 'at', 'in', '—'],
   ['‘At’ is for clock times.', '‘In’ is for months and years.', 'A day needs a preposition here.'],
   'Days → on.'),
  ('Which', '___ the 1990s', ['in', 'on', 'at', '—'],
   ['‘On’ is for days.', '‘At’ is for clock times.', 'A decade needs a preposition.'],
   'Decades and centuries → in.'),
  ('Which', '___ my wedding day', ['on', 'in', 'at', '—'],
   ['‘In’ is for longer periods.', '‘At’ is for clock times and holidays.', 'A specific day needs ‘on’.'],
   'Specific days → on.'),
  ],
 'mc': [
  ('At', 'The museum closes ___ five.', ['at', 'in', 'on', '—'],
   ['‘In five’ means after five units.', '‘On five’ is wrong.', 'A preposition is needed.'],
   'Clock time → at.'),
  ('In', 'I usually read ___ the evening.', ['in', 'at', 'on', '—'],
   ['‘At the evening’ is wrong.', '‘On the evening’ needs a specific day.', 'A preposition is needed.'],
   'Parts of the day → in.'),
  ('On', 'We have a holiday ___ 1 May.', ['on', 'in', 'at', '—'],
   ['‘In 1 May’ is wrong: dates take ‘on’.', '‘At 1 May’ is wrong.', 'A preposition is needed.'],
   'Dates → on.'),
  ('No preposition', 'He visits us ___ every summer.', ['—', 'in', 'on', 'at'],
   ['No preposition before ‘every’.', 'No preposition before ‘every’.', 'No preposition before ‘every’.'],
   'No preposition before every.'),
  ],
 'error': [
  ('In for clock time', 'The bus leaves *in* 7.15.', 'at', 'Clock times take ‘at’: ‘at 7.15’.'),
  ('In for day', 'I go to the gym *in* Tuesdays.', 'on', 'Days take ‘on’: ‘on Tuesdays’.'),
  ('On for month', 'School starts *on* September.', 'in', 'Months take ‘in’: ‘in September’.'),
  ('At for year', 'He was born *at* 2010.', 'in', 'Years take ‘in’: ‘in 2010’.'),
  ],
}
