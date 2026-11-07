TITLE = 'If vs When'
AUX = ([], None, '')
NEXT = ('Unless, as long as, provided that', '/grammar/conditionals/unless-as-long-as-provided/')
BODY = r'''
## How to form sentences with *if* and *when*

Both words introduce a clause with the **present simple** when we talk about the future. The main clause uses **will**, a modal or an imperative.

| Word | Clause | Main clause | Example |
|---|---|---|---|
| if | if + present simple | will + base verb | **If** I **see** her, I**'ll tell** her. |
| when | when + present simple | will + base verb | **When** I **see** her, I**'ll tell** her. |

The grammar is the same. The **meaning** is different. Comma rule: comma after the *if*/*when* clause when it comes first.

## The key difference

| Word | The speaker thinks… | Example |
|---|---|---|
| **if** | it is **possible**, but not sure | **If** you **come**, we'll have fun. (Maybe you won't come.) |
| **when** | it is **sure** to happen | **When** you **come**, we'll have fun. (You're definitely coming.) |

- I'll call you **if** I get the job. (I don't know if I'll get it.)
- I'll call you **when** I get home. (I'll definitely get home.)

## When to use *if*

### 1. Something that may or may not happen

- **If** it **rains**, we'll stay inside.
- **If** you **need** help, ask me.

> ⚠️ Typical error: ~~When it rains tomorrow, we'll stay inside.~~ (you're not sure it'll rain) → Use *if* for a possibility: *If it rains tomorrow…*

### 2. Imaginary or unlikely situations

Only *if* works in the second and third conditionals.

- **If** I **won** the lottery, I'd travel.
- **If** we **had left** earlier, we'd have arrived on time.

> ⚠️ Typical error: ~~When I won the lottery, I'd travel.~~ → Imaginary situations take *if*: *If I won the lottery…*

## When to use *when*

### 1. Something we are sure will happen

- **When** I **finish** school, I'll go to university.
- I'll have dinner **when** Mum **gets** home.

> ⚠️ Typical error: ~~If I finish school, I'll go to university.~~ (you will certainly finish) → For a certain event, use *when*.

### 2. Facts and habits (zero conditional)

For things that are always true, *if* and *when* mean almost the same.

- **If/When** you **heat** ice, it **melts**.
- **When/If** I'm tired, I **go** to bed early.

## No *will* after *if* or *when*

The most common mistake. Even when the clause is about the future, use the **present simple** after *if* and *when*. The same rule applies to *as soon as, before, after, until*.

| ✗ | ✓ |
|---|---|
| ~~when I will arrive~~ | **when I arrive** |
| ~~if it will rain~~ | **if it rains** |
| ~~as soon as she will call~~ | **as soon as she calls** |

## *When* in questions

In a direct question about time, *when* is a question word and can take *will*:

- **When will** you **arrive**? (a question → *will* is fine)
- I'll call you **when** you **arrive**. (a time clause → no *will*)

## Common mistakes

**1. Using *will* after *if* or *when*.** *~~I'll tell you when I will know~~* → **I'll tell you when I know.**

**2. Using *when* for something uncertain.** *~~When I pass the exam, I'll celebrate~~* (if you're worried you'll fail) → **If I pass the exam, I'll celebrate.**

**3. Using *if* for something certain.** *~~If it's Christmas, we'll visit Grandma~~* → **When it's Christmas, we'll visit Grandma.**

**4. Using *when* in imaginary sentences.** *~~When I were rich, I'd buy a boat~~* → **If I were rich, I'd buy a boat.**

**Pro tip:** ask "Am I sure it will happen?" Sure → *when*. Not sure → *if*.
'''

GAP = ('Fill in the gaps',
  'Type if or when. Ask yourself: is the speaker sure it will happen (when) or is it only possible (if)? Twenty original sentences.',
  [
  ('Certain', 'I’ll call you [[when]] I get home tonight.', 'if / when', 'You will certainly get home tonight, so use ‘when’.'),
  ('Possible', 'I’ll buy you a present [[if]] I have enough money.', 'if / when', 'You may not have enough money: a possibility needs ‘if’.'),
  ('Certain', '[[When]] the film finishes, let’s get a pizza.', 'if / when', 'The film will definitely finish, so use ‘when’.'),
  ('Possible', '[[If]] it rains on Saturday, the match will be cancelled.', 'if / when', 'Rain is only possible: use ‘if’.'),
  ('Certain', 'We’ll open the presents [[when]] Grandpa arrives.', 'if / when', 'Grandpa is definitely coming, so it’s a time: ‘when’.'),
  ('Possible', '[[If]] you see Marc, tell him to call me.', 'if / when', 'You may or may not see Marc: ‘if’.'),
  ('Certain', '[[When]] I’m eighteen, I’ll learn to drive.', 'if / when', 'You will certainly be eighteen one day: ‘when’.'),
  ('Possible', 'You can borrow my bike [[if]] you’re careful.', 'if / when', 'It’s a condition: only if you’re careful. Use ‘if’.'),
  ('Imaginary', '[[If]] I won the lottery, I’d buy a house.', 'if / when', 'Imaginary situations (second conditional) only take ‘if’.'),
  ('Imaginary', 'What would you do [[if]] you met a famous footballer?', 'if / when', 'An imaginary situation with ‘would’: only ‘if’ works.'),
  ('Certain', 'I’ll do my homework [[when]] I finish dinner.', 'if / when', 'Dinner will definitely end: ‘when’ for a sure future time.'),
  ('Possible', '[[If]] the shop is closed, we’ll go to the market.', 'if / when', 'You don’t know if it’s closed: ‘if’.'),
  ('Certain', 'Mum will be happy [[when]] she sees the clean kitchen.', 'if / when', 'She will certainly see it: ‘when’.'),
  ('Possible', '[[If]] you don’t understand, put your hand up.', 'if / when', 'Maybe you will understand: a condition, ‘if’.'),
  ('Certain', 'Text me [[when]] your train leaves.', 'if / when', 'The train will certainly leave: ‘when’ for a time.'),
  ('Possible', 'We’ll go to the beach [[if]] it’s sunny.', 'if / when', 'Sun is only a possibility: ‘if’.'),
  ('Certain', '[[When]] summer comes, the days get longer.', 'if / when', 'Summer always comes: ‘when’ for a sure, repeated event.'),
  ('Imaginary', '[[If]] I were you, I’d say sorry.', 'if / when', 'The fixed phrase is ‘If I were you’ — never ‘when’.'),
  ('Possible', 'I’ll be really surprised [[if]] she says yes.', 'if / when', 'You don’t expect her to say yes: ‘if’.'),
  ('Certain', 'I’ll show you my photos [[when]] I see you on Monday.', 'if / when', 'You have a plan to see them on Monday: ‘when’.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with if (possible) and when (certain). Remember: no will after if or when.',
  [
  ('Certain', 'I’ll call you when I arrive.', ['when I arrive, I’ll call you.']),
  ('Certain', 'When the bell rings, we’ll go out.', ['we’ll go out when the bell rings.']),
  ('Certain', 'When I finish school, I’ll travel.', ['I’ll travel when I finish school.']),
  ('Certain', 'We’ll eat when Dad gets home.', ['when Dad gets home, we’ll eat.']),
  ('Certain', 'When it’s my birthday, I’ll have a party.', ['I’ll have a party when it’s my birthday.']),
  ('Certain', 'Text me when you get there.', ['when you get there, text me.']),
  ('Possible', 'If it rains, we’ll stay inside.', ['we’ll stay inside if it rains.']),
  ('Possible', 'If you need help, ask me.', ['ask me if you need help.']),
  ('Possible', 'I’ll come if I have time.', ['if I have time, I’ll come.']),
  ('Possible', 'If she calls, tell her I’m out.', ['tell her I’m out if she calls.']),
  ('Possible', 'If we win, we’ll celebrate.', ['we’ll celebrate if we win.']),
  ('Possible', 'You can go if you finish.', ['if you finish, you can go.']),
  ('Imaginary', 'If I were rich, I’d buy a boat.', ['I’d buy a boat if I were rich.']),
  ('Imaginary', 'If I could fly, I’d visit Japan.', ['I’d visit Japan if I could fly.']),
  ('Imaginary', 'What would you do if you were me?', ['if you were me, what would you do?']),
  ('Fact', 'When you heat ice, it melts.', ['ice melts when you heat it.']),
  ('Fact', 'If I’m tired, I go to bed early.', ['I go to bed early if I’m tired.']),
  ('Time linker', 'I’ll wait until you come.', ['until you come, I’ll wait.']),
  ('Time linker', 'Call me as soon as you know.', ['as soon as you know, call me.']),
  ('Question', 'When will you be home?', []),
  ])

MATCH = {'title': 'If or when?', 'subtitle': 'Tap a situation, then tap the word it needs. Sure to happen → when; only possible or imaginary → if.',
  'leftLabel': 'Situation', 'rightLabel': 'Word', 'rightLabelSub': '(if / when)', 'reviewArrowPrefix': '',
  'pairs': [
  ('___ I get home tonight', 'when'), ('___ I win the lottery', 'if'), ('___ the sun goes down', 'when'), ('___ it snows in May', 'if'),
  ('___ I’m eighteen', 'when'), ('___ you need help', 'if'), ('___ the lesson ends', 'when'), ('___ I were you', 'if'),
  ('___ Grandma arrives on Sunday', 'when'), ('___ you see a ghost', 'if'), ('___ I finish my homework', 'when'), ('___ the shop is closed', 'if'),
  ('___ summer comes', 'when'), ('___ you don’t understand', 'if'), ('___ the bus stops', 'when'), ('___ I could fly', 'if'),
  ('___ the film starts', 'when'), ('___ she says yes', 'if'), ('___ we land in London', 'when'), ('___ you lose your ticket', 'if'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Is it certain (when) or only possible (if)? And never will after if or when.',
  [
  ('Certain', 'I’ll have a shower ___ I get home.', ['when', 'if', 'unless', 'so'],
   ['You will certainly get home, so ‘if’ sounds strange.', '‘Unless’ means ‘if not’, which makes no sense here.', '‘So’ shows a result, not a time.'],
   'Getting home is certain to happen, so it’s a time, not a condition: ‘when’.'),
  ('Possible', '___ it’s sunny tomorrow, we’ll have a picnic.', ['If', 'When', 'Unless', 'Because'],
   ['Tomorrow’s weather isn’t certain, so ‘when’ is wrong.', '‘Unless’ reverses the meaning.', '‘Because’ gives a reason, not a condition.'],
   'Nobody knows tomorrow’s weather for sure, so it’s a possibility: ‘if’.'),
  ('Certain', '___ the holidays start, I’ll sleep until noon.', ['When', 'If', 'Unless', 'Until'],
   ['The holidays will certainly start, so not ‘if’.', '‘Unless’ means ‘if not’.', '‘Until the holidays start’ means before they start, not at that time.'],
   'The holidays are certain to start, so we use ‘when’ for that future time.'),
  ('Possible', 'I’ll lend you my phone ___ you promise to be careful.', ['if', 'when', 'unless', 'because'],
   ['It’s a condition, not a sure time, so not ‘when’.', '‘Unless’ reverses the meaning.', '‘Because’ gives a reason.'],
   'Being careful is a condition for borrowing the phone, so we use ‘if’.'),
  ('Imaginary', '___ I had a time machine, I’d visit the dinosaurs.', ['If', 'When', 'As soon as', 'After'],
   ['Imaginary situations never take ‘when’.', 'A time linker can’t introduce an imaginary situation.', '‘After’ can’t introduce an imaginary condition.'],
   'A time machine is imaginary (second conditional), and only ‘if’ works there.'),
  ('No will', 'I’ll call you when I ___ the results.', ['get', 'will get', 'got', 'would get'],
   ['No ‘will’ after ‘when’ in a time clause.', '‘Got’ is past; you’ll get them in the future.', 'No ‘would’ after ‘when’.'],
   'In a future time clause, ‘when’ takes the present simple, not ‘will’: ‘get’.'),
  ('No will', 'If it ___, we’ll take the car.', ['rains', 'will rain', 'rained', 'is going to rain'],
   ['No ‘will’ after ‘if’.', '‘Rained’ is second conditional, but the result is ‘we’ll’.', 'After ‘if’ the simple present is used, not ‘going to’.'],
   'After ‘if’ use the present simple with -s for ‘it’: ‘rains’, not ‘will rain’.'),
  ('No will', 'Tell me as soon as she ___.', ['arrives', 'will arrive', 'arrived', 'arrive'],
   ['No ‘will’ after ‘as soon as’.', '‘Arrived’ is past.', '‘She’ needs -s: ‘arrives’.'],
   'Like ‘when’, ‘as soon as’ takes the present simple for the future: ‘arrives’.'),
  ('Question', '___ will the concert start?', ['When', 'If', 'Unless', 'As soon as'],
   ['‘If will’ is not a question.', '‘Unless’ can’t start a question.', '‘As soon as’ can’t start a question.'],
   'A direct question about time starts with ‘When will…?’ — here ‘will’ is fine.'),
  ('Certain', 'We’ll start the meeting ___ everyone is here.', ['when', 'if', 'unless', 'because'],
   ['Everyone is coming, so it’s a time, not a condition.', '‘Unless’ reverses the meaning.', '‘Because’ gives a reason.'],
   'Everyone is coming, so it’s a sure event at a future time: ‘when’.'),
  ('Possible', 'You’ll get wet ___ you don’t take an umbrella.', ['if', 'when', 'until', 'as soon as'],
   ['You may take one, so it’s a condition: ‘if’.', '‘Until’ doesn’t fit a condition.', '‘As soon as’ is about time, not a condition.'],
   'You might take an umbrella or not, so this warning is a condition: ‘if’.'),
  ('Fact', '___ you mix red and white, you get pink.', ['If', 'Unless', 'Although', 'So'],
   ['‘Unless’ means ‘if not’.', '‘Although’ shows contrast.', '‘So’ shows a result.'],
   'A general fact: ‘if’ (or ‘when’) — both are fine in the zero conditional.'),
  ('Imaginary', 'What would you do ___ you were the president?', ['if', 'when', 'after', 'until'],
   ['‘When you were the president’ talks about a real past time; this is imaginary.', '‘After’ is about time.', '‘Until’ is about time.'],
   'Being president is imaginary here (would), so only ‘if’ is possible.'),
  ('Certain', 'Don’t forget to call Granny ___ you’re in Paris next week.', ['when', 'if', 'unless', 'so'],
   ['The trip is planned, so it’s a sure time: not ‘if’.', '‘Unless’ reverses the meaning.', '‘So’ shows a result.'],
   'The trip next week is planned, so it’s a sure future time: ‘when’.'),
  ('Possible', 'I’ll be amazed ___ he remembers my birthday.', ['if', 'when', 'as soon as', 'until'],
   ['‘When’ means you’re sure he’ll remember; ‘amazed’ shows you’re not.', '‘As soon as’ is about time.', '‘Until’ is about time.'],
   '‘Amazed’ shows you don’t expect it to happen, so use ‘if’, not ‘when’.'),
  ('No will', 'Wait here until I ___ back.', ['come', 'will come', 'came', 'coming'],
   ['No ‘will’ after ‘until’.', '‘Came’ is past.', '‘Coming’ needs an auxiliary.'],
   'After ‘until’ the future is shown with the present simple: ‘until I come’.'),
  ('Certain', 'I’ll be twenty ___ we go to Japan next year.', ['when', 'if', 'unless', 'because'],
   ['Next year’s trip is planned and age is certain: ‘when’.', '‘Unless’ reverses the meaning.', '‘Because’ gives a reason.'],
   'Both your age and the planned trip are certain, so use ‘when’.'),
  ('Imaginary', '___ I were taller, I’d play volleyball.', ['If', 'When', 'Because', 'So'],
   ['‘When I were’ is impossible.', '‘Because’ gives a reason.', '‘So’ shows a result.'],
   'The past ‘were’ shows an imaginary situation, which only works with ‘if’.'),
  ('No will', 'If you ___ hungry later, there’s pizza in the fridge.', ['are', 'will be', 'were', 'be'],
   ['No ‘will’ after ‘if’.', '‘Were’ is second conditional.', '‘Be’ is the base form.'],
   'After ‘if’ use the present simple for the future, even with ‘later’: ‘are’.'),
  ('Possible', 'Ask the teacher ___ you have any questions.', ['if', 'when', 'until', 'because'],
   ['You may not have questions, so it’s a condition.', '‘Until’ doesn’t fit.', '‘Because’ gives a reason.'],
   'You may or may not have questions, so it’s a condition: ‘if’.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('Will after when', 'I’ll call you when I *will* arrive.', 'arrive', 'No ‘will’ after ‘when’: ‘when I arrive’.'),
  ('Will after if', 'If it *will* rain, we’ll stay in.', 'rains', 'No ‘will’ after ‘if’: ‘If it rains…’.'),
  ('Will after linker', 'Tell me as soon as you *will* know.', 'know', 'No ‘will’ after ‘as soon as’: ‘as soon as you know’.'),
  ('Will after linker', 'We’ll wait until the rain *will* stop.', 'stops', 'No ‘will’ after ‘until’: ‘until the rain stops’.'),
  ('When for imaginary', '*When* I were rich, I’d buy a yacht.', 'If', 'Imaginary situations take ‘if’: ‘If I were rich…’.'),
  ('When for imaginary', 'What would you do *when* you won the lottery?', 'if', 'Winning is imaginary here (would): ‘if you won’.'),
  ('When for uncertain', 'We’ll go to the beach *when* it’s sunny — but the forecast is bad.', 'if', 'The sun isn’t certain: ‘if it’s sunny’.'),
  ('If for certain', 'I’ll go to bed *if* the film finishes.', 'when', 'The film will certainly finish: ‘when the film finishes’.'),
  ('If for certain', 'Happy holidays! See you *if* we come back in September.', 'when', 'Coming back is certain: ‘when we come back’.'),
  ('If I were you', '*When* I were you, I’d take the bus.', 'If', 'The fixed phrase is ‘If I were you’.'),
  ('Missing -s', 'I’ll start dinner when Dad *get* home.', 'gets', '‘Dad’ is he, so add -s: ‘when Dad gets home’.'),
  ('Missing will', 'When I see her, I *tell* her tomorrow.', '’ll tell', 'The main clause needs ‘will’: ‘I’ll tell her’.'),
  ('Wrong tense', 'If you *finished* early, you can leave.', 'finish', 'A real condition with ‘can’: present simple ‘finish’.'),
  ('Wrong tense', 'When I *will* be older, I’ll be a vet.', 'am', 'No ‘will’ after ‘when’: ‘When I am older…’.'),
  ('Unless + not', 'You’ll miss the bus unless you *don’t* run.', 'run', '‘Unless’ already means ‘if not’: ‘unless you run’.'),
  ('Question', '*If* will you be back?', 'When', 'A direct question about time starts with ‘When’.'),
  ('Will + base verb', 'When you arrive, I’ll *gave* you the keys.', 'give', 'After ‘will’ use the base verb: ‘I’ll give’.'),
  ('Wrong word', 'If you need anything, *asks* me.', 'ask', 'An imperative has no -s: ‘ask me’.'),
  ('Will after when', 'Call me when the plane *will* land.', 'lands', 'No ‘will’ after ‘when’: ‘when the plane lands’.'),
  ('Spelling', 'If the baby *crys*, pick her up.', 'cries', 'Consonant + -y → -ies: cry → cries.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, if or when, multiple choice and spot-the-mistake. In the typing questions write if or when, or the present simple after them. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('certain', 'Certain or possible'),
 'fill': [
  ('Certain', 'I’ll phone you [[when]] I land in Rome.', 'if / when', 'Landing is certain: ‘when’ for a sure future time.', 'Sure to happen → ‘when’.'),
  ('Possible', '[[If]] you find my keys, please call me.', 'if / when', 'You may not find them: ‘if’.', 'Only possible → ‘if’.'),
  ('No will', 'I’ll tell you when I [[know]].', 'know', 'After ‘when’ use the present simple, not ‘will know’.', 'No ‘will’ after ‘when’: ‘know’.'),
  ('No will', 'If she [[calls]], I’ll answer.', 'call', 'After ‘if’ use the present simple with -s for ‘she’.', 'Present simple with -s: ‘calls’.'),
  ],
 'order': [
  ('Certain', 'I’ll eat when I get home.', ['when I get home, I’ll eat.']),
  ('Possible', 'If you’re cold, close the window.', ['close the window if you’re cold.']),
  ('Imaginary', 'If I were you, I’d go.', ['I’d go if I were you.']),
  ('Time linker', 'Call me as soon as you arrive.', ['as soon as you arrive, call me.']),
  ],
 'customItems': [
  ('Certain', 'The party starts at eight. ___ it starts, we’ll dance.', ['When', 'If', 'Unless', 'Because'],
   ['The party will definitely start, so not ‘if’.', '‘Unless’ means ‘if not’.', '‘Because’ gives a reason.'],
   'Certain event: ‘when’.'),
  ('Possible', 'I don’t know if I’ll pass. ___ I pass, I’ll be thrilled.', ['If', 'When', 'Until', 'As soon as'],
   ['‘I don’t know’ shows it isn’t certain.', '‘Until’ doesn’t fit.', '‘As soon as’ sounds certain.'],
   'Not certain: ‘if’.'),
  ('Certain', 'I’ll be sixteen in May. ___ I’m sixteen, I’ll get a scooter.', ['When', 'If', 'Unless', 'Although'],
   ['Your age is certain, so not ‘if’.', '‘Unless’ reverses the meaning.', '‘Although’ shows contrast.'],
   'Certain: ‘when’.'),
  ('Possible', 'Maybe it’ll snow. ___ it snows, we’ll build a snowman.', ['If', 'When', 'Because', 'So'],
   ['‘Maybe’ shows it isn’t certain.', '‘Because’ gives a reason.', '‘So’ shows a result.'],
   'Only possible: ‘if’.'),
  ],
 'mc': [
  ('No will', 'We’ll leave as soon as the taxi ___.', ['comes', 'will come', 'came', 'come'],
   ['No ‘will’ after ‘as soon as’.', '‘Came’ is past.', '‘The taxi’ needs -s.'],
   'Present simple after a time linker: ‘comes’.'),
  ('Imaginary', '___ dogs could talk, what would they say?', ['If', 'When', 'As soon as', 'Until'],
   ['Imaginary situations never take ‘when’.', '‘As soon as’ is for real times.', '‘Until’ is for real times.'],
   'Imaginary: ‘if’.'),
  ('Question', '___ will you finish your project?', ['When', 'If', 'Unless', 'Until'],
   ['‘If will’ is not a question.', '‘Unless’ can’t start a question.', '‘Until will’ is not a question.'],
   'A question about time: ‘When will…?’.'),
  ('Fact', 'Water boils ___ you heat it to 100 °C.', ['when', 'unless', 'although', 'so'],
   ['‘Unless’ would mean the opposite.', '‘Although’ shows contrast.', '‘So’ shows a result.'],
   'A fact: ‘when’ (or ‘if’).'),
  ],
 'error': [
  ('Will after when', 'I’ll help you when I *will* finish.', 'finish', 'No ‘will’ after ‘when’: ‘when I finish’.'),
  ('When for imaginary', '*When* I had wings, I’d fly to Italy.', 'If', 'Imaginary situations take ‘if’.'),
  ('If for certain', 'I’ll brush my teeth *if* I wake up tomorrow.', 'when', 'Waking up is certain: ‘when I wake up’.'),
  ('Will after if', 'If you *will* need me, call me.', 'need', 'No ‘will’ after ‘if’: ‘If you need me…’.'),
  ],
}
