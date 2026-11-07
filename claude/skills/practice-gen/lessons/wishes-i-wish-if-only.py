TITLE = 'Wishes: I wish / if only'
AUX = (['wish', 'had', 'would', 'could'], None, 'wish')
NEXT = ('Inversion in Conditionals', '/grammar/conditionals/inversion-in-conditionals/')
BODY = r'''
## How to form wishes

The verb after *wish* or *if only* moves **one step back** in time, like in the second and third conditionals.

| Wish about… | Form | Example |
|---|---|---|
| the **present** | wish + past simple | I wish I **had** a dog. |
| the **past** | wish + had + past participle | I wish I **had studied** more. |
| someone's annoying **habit** / a future change | wish + would + base verb | I wish you **would stop** shouting. |
| an **ability** now | wish + could + base verb | I wish I **could** swim. |

*If only* means the same as *I wish* but is **stronger** and more emotional: **If only** I **had** more time!

## Wishes about the present

We want something to be different **now**, but it isn't.

- I wish I **lived** by the sea. (I don't live by the sea.)
- She wishes she **were** taller. (She isn't tall.)
- I wish it **wasn't** so cold today.

With *be*, **were** is correct for all subjects; *was* is common in informal speech.

> ⚠️ Typical error: ~~I wish I have a car.~~ → A present wish takes the past simple: *I wish I had a car.*

## Wishes about the past (regrets)

We are sorry about something that happened — or didn't happen.

- I wish I **had gone** to the party. (I didn't go.)
- He wishes he **hadn't eaten** so much. (He ate a lot.)
- **If only** we **had left** earlier!

> ⚠️ Typical error: ~~I wish I went to the party yesterday.~~ → A past regret needs the past perfect: *I wish I had gone…*

## Wishes with *would*

### 1. Complaints about someone's behaviour

We want another person (or thing) to change.

- I wish my brother **would tidy** his room.
- I wish you **wouldn't interrupt** me.
- I wish it **would stop** raining!

> ⚠️ Typical error: ~~I wish I would have more time.~~ → Don't use *would* about yourself: *I wish I had more time.*

### 2. Not for states

*Would* goes with actions, not with states like *be, have, know*.

- ✗ ~~I wish he would be taller.~~ → ✓ **I wish he were taller.**

## Wishes with *could*

For abilities we don't have now.

- I wish I **could** speak Japanese.
- I wish we **could** stay longer.

## *If only*

*If only* expresses a stronger feeling, often with an exclamation mark.

| Time | Example |
|---|---|
| present | **If only** I **knew** the answer! |
| past | **If only** I **hadn't said** that! |
| complaint | **If only** the bus **would come**! |

## *Wish* or *hope*?

*Hope* is for things that are **possible**; it uses a normal tense.

- I **hope** you **pass** the exam. (it's possible)
- I **wish** you **had passed** the exam. (you didn't)

## Common mistakes

**1. Using the present after *wish*.** *~~I wish I am rich~~* → **I wish I were rich.**

**2. Using the past simple for a past regret.** *~~I wish I didn't say that yesterday~~* → **I wish I hadn't said that.**

**3. Using *would* with *I*.** *~~I wish I would know the answer~~* → **I wish I knew the answer.**

**4. Using *would have* after *wish*.** *~~I wish I would have studied~~* → **I wish I had studied.**

**Pro tip:** say the opposite of reality, then go one step back in time: *I don't have → I wish I had; I didn't go → I wish I had gone.*
'''

GAP = ('Fill in the gaps',
  'Type the correct form of the verb in brackets after wish or if only: past simple for now, had + participle for the past, would for complaints. Twenty original sentences.',
  [
  ('Present', 'I wish I [[had]] a bigger bedroom.', '(have)', 'A wish about now takes the past simple: have → had.'),
  ('Present', 'I wish I [[lived]] closer to my school.', '(live)', 'You don’t live close now: the past simple ‘lived’.'),
  ('Present', 'My sister wishes she [[were|was]] taller.', '(be)', 'With ‘be’ use ‘were’ for all subjects after ‘wish’.'),
  ('Present', 'I wish I [[knew]] the answer to this question.', '(know)', 'A present wish: irregular past simple, know → knew.'),
  ('Present', 'If only it [[wasn’t|weren’t]] so cold today!', '(not be)', 'A present wish (today): negative past of ‘be’, wasn’t / weren’t.'),
  ('Present', 'I wish we [[didn’t have]] so much homework.', '(not have)', 'A present wish: negative past simple, didn’t + have.'),
  ('Ability', 'I wish I [[could]] play the guitar.', '(can)', 'For an ability you don’t have, use ‘could’ after ‘wish’.'),
  ('Ability', 'I wish we [[could stay]] at the beach longer.', '(can / stay)', 'A wish about an ability or possibility now: could + base verb.'),
  ('Past', 'I wish I [[had studied|’d studied]] harder for the exam.', '(study)', 'A regret about the past: had + past participle.'),
  ('Past', 'He wishes he [[hadn’t eaten]] so much cake.', '(not eat)', 'A past regret: hadn’t + eaten (irregular participle).'),
  ('Past', 'If only I [[had brought|’d brought]] my umbrella!', '(bring)', 'A strong past regret: had + brought.'),
  ('Past', 'I wish I [[hadn’t said]] that to my friend.', '(not say)', 'You said it and regret it: hadn’t + said.'),
  ('Past', 'We wish we [[had seen|’d seen]] the concert last night.', '(see)', '‘Last night’ is past: had + seen.'),
  ('Past', 'She wishes she [[had taken|’d taken]] the job in London.', '(take)', 'A past regret: had + taken.'),
  ('Complaint', 'I wish my brother [[would stop]] playing loud music.', '(stop)', 'A complaint about someone’s habit: would + base verb.'),
  ('Complaint', 'I wish you [[wouldn’t interrupt]] me all the time.', '(not interrupt)', 'A complaint about your behaviour: wouldn’t + base verb.'),
  ('Complaint', 'I wish it [[would stop]] raining!', '(stop)', 'You want the weather to change: would + stop.'),
  ('Complaint', 'If only the bus [[would come]]!', '(come)', 'Impatient wish for a change: would + come.'),
  ('Present', 'I wish my parents [[let]] me stay out later.', '(let)', 'A present wish: ‘let’ has the same past simple form.'),
  ('Past', 'If only we [[hadn’t missed]] the train!', '(not miss)', 'A past regret: hadn’t + missed.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each wish — 20 examples about the present, the past, abilities and annoying habits.',
  [
  ('Present', 'I wish I had a dog.', []),
  ('Present', 'I wish I lived in London.', []),
  ('Present', 'She wishes she were older.', []),
  ('Present', 'I wish it wasn’t so hot.', []),
  ('Present', 'I wish I knew his name.', []),
  ('Present', 'If only I had more time!', []),
  ('Ability', 'I wish I could fly.', []),
  ('Ability', 'I wish we could stay longer.', []),
  ('Past', 'I wish I had studied more.', []),
  ('Past', 'I wish I hadn’t eaten so much.', []),
  ('Past', 'He wishes he had gone to the party.', []),
  ('Past', 'If only we had left earlier!', []),
  ('Past', 'I wish I hadn’t told her.', []),
  ('Past', 'They wish they had booked a table.', []),
  ('Complaint', 'I wish you would listen.', []),
  ('Complaint', 'I wish it would stop raining.', []),
  ('Complaint', 'I wish he wouldn’t shout.', []),
  ('Complaint', 'If only the phone would ring!', []),
  ('Hope', 'I hope you pass your exam.', []),
  ('Hope', 'I hope it doesn’t rain tomorrow.', []),
  ])

MATCH = {'title': 'Match the situation and the wish', 'subtitle': 'Tap the real situation, then tap the wish that says the opposite.',
  'leftLabel': 'Situation', 'rightLabel': 'Wish', 'rightLabelSub': '(I wish…)', 'reviewArrowPrefix': '',
  'pairs': [
  ('I don’t have a car.', 'I wish I had a car.'), ('I live far from school.', 'I wish I lived nearer.'), ('I’m not tall.', 'I wish I were taller.'),
  ('I can’t swim.', 'I wish I could swim.'), ('I don’t know the answer.', 'I wish I knew the answer.'), ('It’s raining.', 'I wish it would stop raining.'),
  ('You always interrupt me.', 'I wish you wouldn’t interrupt me.'), ('I didn’t study.', 'I wish I had studied.'), ('I ate too much.', 'I wish I hadn’t eaten so much.'),
  ('I missed the bus.', 'I wish I hadn’t missed the bus.'), ('I didn’t go to the party.', 'I wish I had gone to the party.'), ('I said something rude.', 'I wish I hadn’t said that.'),
  ('My brother never tidies up.', 'I wish he would tidy up.'), ('I have too much homework.', 'I wish I didn’t have so much homework.'), ('I’m always tired.', 'I wish I weren’t so tired.'),
  ('I can’t speak Japanese.', 'I wish I could speak Japanese.'), ('I forgot your birthday.', 'I wish I hadn’t forgotten your birthday.'), ('The music is too loud.', 'I wish it wasn’t so loud.'),
  ('I didn’t bring a coat.', 'I wish I had brought a coat.'), ('The bus is late again.', 'I wish the bus would come.'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Present → past simple; past → had + participle; complaints → would; abilities → could.',
  [
  ('Present', 'I wish I ___ a bigger flat.', ['had', 'have', 'would have', 'will have'],
   ['After ‘wish’ the verb goes one step back: present ‘have’ becomes ‘had’.', '‘Would’ is for complaints about others, not your own situation.', '‘Will’ never follows ‘wish’ for a present situation.'],
   'A wish about the present: wish + past simple.'),
  ('Present', 'She wishes she ___ better at maths.', ['were', 'is', 'would be', 'has been'],
   ['‘Is’ is present; after ‘wish’ use the past.', '‘Would’ doesn’t go with states like ‘be’.', '‘Has been’ is present perfect.'],
   'With ‘be’ after ‘wish’, use ‘were’.'),
  ('Present', 'I wish I ___ the answer — I’m stuck.', ['knew', 'know', 'had known', 'would know'],
   ['‘Know’ is present; a wish needs the past.', '‘Had known’ is about the past, but you are stuck now.', '‘Would’ isn’t used with ‘I’ or with state verbs.'],
   'A present wish: knew.'),
  ('Past', 'I wish I ___ to the party last night. It was great!', ['had gone', 'went', 'would go', 'go'],
   ['‘Went’ makes it a present wish; ‘last night’ needs the past perfect.', '‘Would go’ is for complaints, not past regrets.', '‘Go’ is present.'],
   'A past regret: had + past participle.'),
  ('Past', 'He wishes he ___ that text to his ex.', ['hadn’t sent', 'didn’t send', 'wouldn’t send', 'doesn’t send'],
   ['‘Didn’t send’ is a present wish; the text was sent in the past.', '‘Wouldn’t’ is for complaints about others.', '‘Doesn’t send’ is present.'],
   'Past regret: hadn’t + sent.'),
  ('Past', 'If only I ___ my keys at home!', ['hadn’t left', 'didn’t leave', 'don’t leave', 'wouldn’t leave'],
   ['Leaving the keys happened in the past: past perfect.', '‘Don’t leave’ is present.', '‘Wouldn’t’ isn’t used for your own past regrets.'],
   'A strong past regret: If only + hadn’t left.'),
  ('Complaint', 'I wish my neighbours ___ so much noise.', ['wouldn’t make', 'don’t make', 'hadn’t made', 'won’t make'],
   ['After ‘wish’ the present ‘don’t’ can’t be used.', '‘Hadn’t made’ is a past regret; the noise is a habit now.', '‘Won’t’ never follows ‘wish’.'],
   'A complaint about others’ habits: wouldn’t + base verb.'),
  ('Complaint', 'I wish it ___ raining. I want to go out!', ['would stop', 'stops', 'had stopped', 'will stop'],
   ['‘Stops’ is present; after ‘wish’ use ‘would’ for a wanted change.', '‘Had stopped’ is about the past.', '‘Will’ never follows ‘wish’.'],
   'Wanting a change (the weather): would + base verb.'),
  ('Complaint', 'I wish you ___ me when I’m talking.', ['wouldn’t interrupt', 'don’t interrupt', 'didn’t interrupted', 'won’t interrupt'],
   ['After ‘wish’ the present ‘don’t’ can’t be used.', 'After ‘didn’t’ use the base verb.', '‘Won’t’ never follows ‘wish’.'],
   'A complaint about someone’s behaviour: wouldn’t + base verb.'),
  ('Ability', 'I wish I ___ speak Chinese.', ['could', 'can', 'would', 'could to'],
   ['‘Can’ is present; after ‘wish’ use the past ‘could’.', '‘Would speak’ with ‘I’ is a mistake.', '‘Could’ is followed by the base verb, no ‘to’.'],
   'A wish about ability: could.'),
  ('Ability', 'We wish we ___ come to your wedding, but we’re abroad.', ['could', 'can', 'will', 'had could'],
   ['‘Can’ is present; after ‘wish’ use ‘could’.', '‘Will’ never follows ‘wish’.', '‘Had could’ isn’t a possible form.'],
   'An impossible thing now: could + base verb.'),
  ('Would with I', 'Which sentence is correct?', ['I wish I had more free time.', 'I wish I would have more free time.', 'I wish I have more free time.', 'I wish I will have more free time.'],
   ['Don’t use ‘would’ about yourself after ‘wish’.', 'After ‘wish’ the present ‘have’ moves back to ‘had’.', '‘Will’ never follows ‘wish’.'],
   'Present wish about yourself: wish + past simple.'),
  ('Would with states', 'Which sentence is correct?', ['I wish he were more patient.', 'I wish he would be more patient.', 'I wish he is more patient.', 'I wish he will be more patient.'],
   ['‘Would’ goes with actions, not states like ‘be’ — this is a common mistake.', 'After ‘wish’ use the past, not ‘is’.', '‘Will’ never follows ‘wish’.'],
   'States after ‘wish’ use the past: were.'),
  ('Would have', 'Which sentence is correct?', ['I wish I had listened.', 'I wish I would have listened.', 'I wish I listen.', 'I wish I have listened.'],
   ['‘Would have’ after ‘wish’ is a common mistake: use ‘had listened’.', '‘Listen’ is present.', '‘Have listened’ is present perfect.'],
   'Past regret: wish + had + participle.'),
  ('Wish or hope', 'I ___ you have a great time in Paris next week!', ['hope', 'wish', 'would wish', 'wished'],
   ['‘Wish’ is for unreal situations; a good trip is possible.', '‘Would wish’ doesn’t fit here.', '‘Wished’ is past.'],
   'For something possible in the future, use ‘hope’ + present.'),
  ('Wish or hope', 'I ___ I had a twin sister.', ['wish', 'hope', 'want', 'think'],
   ['‘Hope’ is for possible things; you can’t get a twin.', '‘Want’ is followed by a noun or ‘to’, not a past clause.', '‘Think’ doesn’t express a wish.'],
   'An impossible situation: ‘wish’ + past.'),
  ('Present', 'If only I ___ so shy!', ['weren’t', 'am not', 'won’t be', 'hadn’t been'],
   ['‘Am not’ is present; after ‘if only’ use the past.', '‘Will’ never follows ‘if only’.', '‘Hadn’t been’ is about a past moment, but shyness is now.'],
   'A present wish: weren’t.'),
  ('Past', 'They wish they ___ more photos on holiday.', ['had taken', 'took', 'take', 'would take'],
   ['‘Took’ makes it a present wish; the holiday is over.', '‘Take’ is present.', '‘Would’ is for complaints about others.'],
   'Past regret: had taken.'),
  ('Present', 'I wish my phone ___ better photos.', ['took', 'takes', 'had taken', 'will take'],
   ['‘Takes’ is present; after ‘wish’ use the past.', '‘Had taken’ is about the past; this is about your phone now.', '‘Will’ never follows ‘wish’.'],
   'A present wish about a thing’s quality: past simple took.'),
  ('Complaint', 'If only my dad ___ smoking!', ['would give up', 'gives up', 'had given up', 'will give up'],
   ['‘Gives up’ is present; after ‘if only’ use ‘would’ for a wanted change.', '‘Had given up’ is a past regret.', '‘Will’ never follows ‘if only’.'],
   'Wanting someone to change: would + give up.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('Present after wish', 'I wish I *have* a car.', 'had', 'A present wish takes the past simple: ‘I wish I had a car’.'),
  ('Present after wish', 'She wishes she *is* taller.', 'were', 'After ‘wish’ use ‘were’: ‘she wishes she were taller’.'),
  ('Present after wish', 'I wish I *know* how to fix this.', 'knew', 'A present wish: ‘I wish I knew…’.'),
  ('Past regret', 'I wish I *went* to the party last night.', 'had gone', 'A past regret needs the past perfect: ‘had gone’.'),
  ('Past regret', 'He wishes he *didn’t* say that yesterday.', 'hadn’t said', 'A past regret: ‘he wishes he hadn’t said that’.'),
  ('Past regret', 'If only I *studied* for yesterday’s test!', 'had studied', 'Yesterday’s test is past: ‘If only I had studied!’.'),
  ('Would with I', 'I wish I *would* have more money.', 'had', 'Don’t use ‘would’ about yourself: ‘I wish I had more money’.'),
  ('Would with I', 'I wish I *would* know the answer.', 'knew', 'Don’t use ‘would’ about yourself: ‘I wish I knew…’.'),
  ('Would have', 'I wish I *would* have listened to you.', 'had', 'After ‘wish’ use ‘had’ + participle: ‘I wish I had listened’.'),
  ('Would with states', 'I wish he *would* be nicer to me.', 'were', '‘Would’ doesn’t go with ‘be’: ‘I wish he were nicer’.'),
  ('Will after wish', 'I wish you *will* stop shouting.', 'would', 'Complaints use ‘would’: ‘I wish you would stop’.'),
  ('Can or could', 'I wish I *can* swim.', 'could', 'After ‘wish’ use ‘could’: ‘I wish I could swim’.'),
  ('Past participle', 'I wish I hadn’t *ate* so much.', 'eaten', 'The participle of ‘eat’ is ‘eaten’.'),
  ('Past participle', 'If only we had *went* earlier!', 'gone', 'The participle of ‘go’ is ‘gone’.'),
  ('Past participle', 'She wishes she had *took* the job.', 'taken', 'The participle of ‘take’ is ‘taken’.'),
  ('Base verb after would', 'I wish it would *stopped* raining.', 'stop', 'After ‘would’ use the base verb: ‘would stop’.'),
  ('Base verb after could', 'I wish I could *spoke* French.', 'speak', 'After ‘could’ use the base verb: ‘could speak’.'),
  ('Wish or hope', 'I *wish* you pass your exam tomorrow.', 'hope', 'For something possible, use ‘hope’ + present: ‘I hope you pass’.'),
  ('Wish or hope', 'I *hope* I had a brother.', 'wish', 'An unreal situation needs ‘wish’: ‘I wish I had a brother’.'),
  ('Negative', 'I wish we *don’t* have exams.', 'didn’t', 'A present wish: ‘I wish we didn’t have exams’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, wish or hope, multiple choice and spot-the-mistake. In the typing questions move the verb one step back: past simple for now, had + participle for the past, would for complaints. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('wishhope', 'Wish or hope'),
 'fill': [
  ('Present', 'I wish I [[had]] my own room.', 'have', 'A present wish: past simple ‘had’.', 'Present wish → past simple: ‘had’.'),
  ('Past', 'I wish I [[hadn’t lost]] my phone yesterday.', 'not lose', 'A past regret: hadn’t + lost.', 'Past regret → hadn’t + participle.'),
  ('Complaint', 'I wish you [[would help]] me with the dishes.', 'help', 'A complaint about someone: would + base verb.', 'Complaint → would + base verb.'),
  ('Ability', 'I wish I [[could]] dance like you.', 'can', 'A wish about ability: could.', 'After ‘wish’, can → could.'),
  ],
 'order': [
  ('Present', 'I wish I were rich.', []),
  ('Past', 'I wish I had said yes.', []),
  ('Complaint', 'I wish you would call me.', []),
  ('Ability', 'If only I could sing!', []),
  ],
 'customItems': [
  ('Hope', 'I ___ the weather is nice for your trip.', ['hope', 'wish', 'had wished', 'would wish'],
   ['‘Wish’ is for unreal situations; nice weather is possible.', '‘Had wished’ is past perfect.', '‘Would wish’ doesn’t fit.'],
   'Something possible → ‘hope’ + present.'),
  ('Wish', 'I ___ I could live on the moon.', ['wish', 'hope', 'want', 'expect'],
   ['‘Hope’ is for possible things; living on the moon isn’t.', '‘Want’ can’t be followed by ‘I could’ in this way.', '‘Expect’ is for things you think will happen.'],
   'An impossible situation → ‘wish’.'),
  ('Hope', 'We ___ you feel better soon.', ['hope', 'wish', 'wished', 'would wish'],
   ['‘Wish you feel’ is wrong: ‘wish’ needs a past form.', '‘Wished’ is past.', '‘Would wish’ doesn’t fit.'],
   'A possible future → ‘hope’.'),
  ('Wish', 'She ___ she hadn’t sold her old bike.', ['wishes', 'hopes', 'expects', 'thinks'],
   ['‘Hopes’ is for possible things, not past regrets.', '‘Expects’ is about the future.', '‘Thinks’ doesn’t express a wish.'],
   'A past regret → ‘wish’ + past perfect.'),
  ],
 'mc': [
  ('Present', 'I wish I ___ so tired every morning.', ['weren’t', 'am not', 'won’t be', 'wouldn’t be'],
   ['After ‘wish’ use the past, not ‘am not’.', '‘Will’ never follows ‘wish’.', '‘Would’ doesn’t go with ‘be’ about yourself.'],
   'Present wish: weren’t.'),
  ('Past', 'If only I ___ the bus this morning!', ['hadn’t missed', 'didn’t miss', 'don’t miss', 'wouldn’t miss'],
   ['‘Didn’t miss’ is a present wish; this morning is past.', '‘Don’t miss’ is present.', '‘Wouldn’t’ is for others’ habits.'],
   'Past regret: hadn’t missed.'),
  ('Complaint', 'I wish my cat ___ on my bed.', ['wouldn’t sleep', 'doesn’t sleep', 'hadn’t slept', 'won’t sleep'],
   ['After ‘wish’ the present ‘doesn’t’ can’t be used.', '‘Hadn’t slept’ is a past regret.', '‘Won’t’ never follows ‘wish’.'],
   'Complaint about a habit: wouldn’t + verb.'),
  ('Would with I', 'Which is correct?', ['I wish I knew.', 'I wish I would know.', 'I wish I know.', 'I wish I will know.'],
   ['No ‘would’ about yourself.', 'After ‘wish’ use the past.', '‘Will’ never follows ‘wish’.'],
   'Present wish: wish + past simple.'),
  ],
 'error': [
  ('Present after wish', 'I wish I *am* on holiday.', 'were', 'A present wish: ‘I wish I were on holiday’.'),
  ('Past regret', 'I wish I *bought* that jacket last week.', 'had bought', 'A past regret: ‘had bought’.'),
  ('Would with I', 'I wish I *would* be better at football.', 'were', 'No ‘would’ about yourself: ‘I wish I were better…’.'),
  ('Wish or hope', 'I *wish* you have a great birthday!', 'hope', 'For a possible good wish, use ‘hope’.'),
  ],
}
