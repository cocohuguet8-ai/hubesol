TITLE = 'Cleft Sentences'
AUX = ([], None, '')
NEXT = ('All advanced structures', '/grammar/advanced-structures/')
FM = {}
BODY = r'''
## What is a cleft sentence?

A cleft sentence **splits one idea into two parts** so that one part gets all the attention. The new word order puts the important information in a **focus position**. The meaning stays the same; the emphasis changes.

| Plain sentence | Cleft sentence |
|---|---|
| Maria found the keys. | **It was Maria who** found the keys. |
| I need a holiday. | **What I need is** a holiday. |
| The website is too slow. | **The problem is that** the website is too slow. |

There are three main patterns, and each one has the verb **be** in the middle:

| Pattern | Structure | Example |
|---|---|---|
| *It*-cleft | It + be + focus + *that / who* clause | It was the noise that woke her. |
| *Wh*-cleft | What / Where / Why / How + clause + be + focus | What woke her was the noise. |
| *Thing*-cleft | The thing / fact / point / problem + be + (that) clause | The point is that nobody called. |

## *It*-clefts

Use **It + be + focus + that / who + the rest of the sentence**. The focus can be a person, a thing, a time, a place or a reason.

| Focus on… | Example |
|---|---|
| the subject (a person) | It was **Maria** who / that found the keys. |
| the object | It was **the blue jacket** that she bought. |
| time | It was **last Friday** that we met. |
| place | It is **in Girona** that I grew up. |
| reason | It was **because of the storm** that the match stopped. |

- Use **who** or **that** for people, and **that** for everything else.
- *Be* shows the time of the sentence (*is* or *was*). The verb in the second part keeps its own tense: *It was Tom who had called earlier.*
- *It* never changes, even when the focus is plural: **It was the students who complained.**

### Negatives and questions

- **It wasn’t the money that mattered.** (= The money didn’t matter.)
- **Was it Maria who called?** / **Who was it that called?**
- **It wasn’t until midnight that the storm stopped.** (= The storm didn’t stop until midnight.)

> ⚠️ Typical error: ~~Was Maria who called.~~ → An *it*-cleft always needs *it*: *It was Maria who called.*

## *Wh*-clefts

Use **What + clause + be + focus**. The *what*-clause sets the scene, and the focus comes last, in the position of greatest emphasis.

- **What I need is** a holiday. (= I need a holiday.)
- **What surprised me was** his reaction.
- **What the team wants is** a new coach.

When the *what*-clause has the verb **do**, the focus is an action. After *be*, use the **base verb** or *to* + base verb. Never repeat the past form.

- **What she did was call** the police.
- **What I want to do is (to) travel** for a year.

> ⚠️ Typical error: ~~What she did was called the police.~~ → After *what she did was*, use the base verb: *What she did was call the police.*

### *Where, why, how* as the subject

*Where, why* and *how* can also start a cleft clause. They sound formal and are common in writing. The focus can come after *be*, or the whole clause can be the subject.

- **Where we stayed was** a tiny hotel near the river.
- **Why he left was that** the pay was far too low.
- **How she won was** by staying calm under pressure.
- **Where she went** is still a mystery. (the clause is the subject)

### Reverse *wh*-clefts

You can turn a *wh*-cleft around and put the focus first: **A holiday is what I need.** / **The noise is why she left.** / **That is where we met.**

## *Thing*-clefts

Nouns such as **thing, point, problem, fact, trouble** and **reason** can open a cleft sentence. Use **be** and then a noun phrase or a *that*-clause. Adjectives like *only, main, sad* often sit before the noun.

- **The problem is that** the website is too slow.
- **The only thing I want is** some peace.
- **The sad fact is that** many people never vote.
- **The ones that worry me are** the exams.

## When to use cleft sentences

| Purpose | Example |
|---|---|
| correct or contrast | It wasn’t Tom who broke it. It was Anna. |
| stress new information | What I really enjoyed was the final scene. |
| formal writing and speeches | What this report shows is that costs are rising. |
| introduce a problem or opinion | The trouble is that we have no time. |
| everyday speech | Often with stress and intonation: *It was ME who called!* |

Cleft sentences are longer than plain ones. Use them when you really want to emphasise something, not in every sentence.

## Common mistakes

**1. Leaving out *it*.** ✗ ~~Was Maria who called.~~ → ✓ **It was Maria who called.**

**2. Using *it* + a plural verb.** ✗ ~~It were the students who complained.~~ → ✓ **It was the students who complained.**

**3. Repeating the subject.** ✗ ~~It was Maria who she found the keys.~~ → ✓ **It was Maria who found the keys.**

**4. Using the past form after *what… did was*.** ✗ ~~What he did was walked out.~~ → ✓ **What he did was walk out.**

**5. Forgetting *be*.** ✗ ~~What I need a holiday.~~ → ✓ **What I need is a holiday.**

**Pro tip:** to check a cleft sentence, take the focus out and put it back into a plain sentence. If you get a normal sentence, the cleft is correct: *It was Maria who found the keys* → *Maria found the keys.*
'''

GAP = ('Fill in the gaps',
  'Type the missing word or form to complete each cleft sentence. Twenty original sentences with it-clefts, wh-clefts and thing-clefts.',
  [
  ('Focus on a person', 'It was Maria [[who|that]] found the missing keys.', '(linking word)', 'Focus on the subject, a person: It + was + Maria + who / that + verb.'),
  ('Focus on a person', 'It is our head teacher [[who|that]] decides the exam dates.', '(linking word)', 'The focus is the person who does the action, so who or that introduces the verb ‘decides’.'),
  ('Focus on a thing', 'It was the blue jacket [[that|which]] she bought, not the red one.', '(linking word)', 'Focus on the object, a thing: It + was + the blue jacket + that + she bought.'),
  ('Focus on time', 'It [[was]] last Friday that we finally met.', '(be)', 'The meeting is finished, so ‘be’ is past: It was last Friday that we met.'),
  ('Focus on place', 'It is in Girona [[that]] I grew up.', '(linking word)', 'Focus on a place: It is + in Girona + that + clause.'),
  ('Focus on a reason', 'It was because of the storm [[that]] the match stopped.', '(linking word)', 'Focus on the reason: It was + because of the storm + that + clause.'),
  ('Negative', 'Last year, it [[wasn’t|was not]] the money that mattered to her.', '(be)', 'The negative goes on ‘be’. ‘Last year’ is past, so: it wasn’t the money that mattered.'),
  ('Negative', 'It wasn’t [[until]] midnight that the noise stopped.', '(linking word)', 'The pattern is It wasn’t until + time + that + clause.'),
  ('Question', '[[Was]] it Maria who called you last night?', '(be)', 'The question form puts ‘be’ first: Was it Maria who…? ‘Last night’ is past, so ‘was’.'),
  ('Wh-cleft', '[[What]] I need most right now is a long holiday.', '(wh-word)', 'A wh-cleft starts with ‘What’ + clause, then be, then the focus.'),
  ('Wh-cleft', 'What surprised everyone [[was]] his calm reaction.', '(be)', 'The what-clause is followed by ‘be’. The surprise happened in the past, so ‘was’.'),
  ('Focus on an action', 'What she did was [[call|to call]] the police.', '(call)', 'After ‘what she did was’ use the base verb (or to + base verb), not the past form.'),
  ('Focus on an action', 'What I want to do is [[travel|to travel]] for a whole year.', '(travel)', 'The focus is an action, so use the base verb or to + base verb after ‘is’.'),
  ('Place, reason, manner', '[[Where]] we stayed in Paris was a tiny hotel near the river.', '(wh-word)', 'The focus is a place (a tiny hotel near the river), so the cleft clause starts with ‘Where’.'),
  ('Place, reason, manner', '[[Why]] he left the company was that the pay was far too low.', '(wh-word)', 'The focus gives the reason (the pay was too low), so the cleft clause starts with ‘Why’.'),
  ('Place, reason, manner', '[[How]] she won the match was by staying calm under pressure.', '(wh-word)', 'The focus gives the way she did it (by staying calm), so the cleft clause starts with ‘How’.'),
  ('Reversed focus', 'A long holiday is [[what]] I need.', '(wh-word)', 'In a reverse wh-cleft the focus comes first, then ‘is what’ + clause.'),
  ('Introducing a problem', 'The problem [[is]] that the website is far too slow.', '(be)', 'In a thing-cleft, ‘be’ links the noun (problem) to the that-clause. The problem exists now, so ‘is’.'),
  ('Introducing a problem', 'The only [[thing]] I want is some peace and quiet.', '(noun)', 'A thing-cleft opens with a noun such as ‘thing’: The only thing I want is…'),
  ('Introducing a problem', 'The sad fact is [[that]] many people never vote.', '(linking word)', 'After ‘the fact is’, the that-clause gives the information.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each cleft sentence — 20 examples with it-clefts, wh-clefts and thing-clefts. Some sentences can be built in more than one correct order.',
  [
  ('Focus on a person', 'It was Maria who found the keys.', None),
  ('Focus on a person', 'It is our teacher who chooses the film.', None),
  ('Focus on a thing', 'It was the noise that woke the baby.', None),
  ('Focus on a thing', 'It was the red scarf that she lost.', None),
  ('Focus on time', 'It was last summer that we first met.', None),
  ('Focus on place', 'It was in Girona that they got married.', None),
  ('Focus on a reason', 'It was the rain that made us stay home.', None),
  ('Negative', 'It wasn’t the money that mattered.', None),
  ('Focus on a person', 'It was the manager who signed the contract.', None),
  ('Question', 'Was it your brother who called?', None),
  ('Question', 'Who was it that called you?', None),
  ('Wh-cleft', 'What I need is a holiday.', ['a holiday is what I need.']),
  ('Wh-cleft', 'What surprised me was his reaction.', ['his reaction was what surprised me.']),
  ('Wh-cleft', 'What the team wants is a new coach.', ['a new coach is what the team wants.']),
  ('Focus on an action', 'What she did was call the police.', None),
  ('Place, reason, manner', 'Where she went is still a mystery.', None),
  ('Place, reason, manner', 'Why he left remains unclear.', None),
  ('Reversed focus', 'The noise is why she left.', ['why she left is the noise.']),
  ('Introducing a problem', 'The problem is that the website is slow.', None),
  ('Introducing a problem', 'The only thing I want is some peace.', ['some peace is the only thing I want.']),
  ])

MATCH = {'title': 'Match the plain sentence and its cleft', 'subtitle': 'Tap a plain sentence, then tap the cleft sentence that gives the same information with a focus.',
  'leftLabel': 'Plain sentence', 'rightLabel': 'Cleft sentence', 'rightLabelSub': '(with focus)', 'reviewArrowPrefix': '',
  'pairs': [
  ('Maria found the keys.', 'It was Maria who found the keys.'),
  ('We met in Girona.', 'It was in Girona that we met.'),
  ('Tom lost his phone on Monday.', 'It was on Monday that Tom lost his phone.'),
  ('The noise woke the baby.', 'It was the noise that woke the baby.'),
  ('She stayed in because of the storm.', 'It was because of the storm that she stayed in.'),
  ('Our teacher chose the film.', 'It was our teacher who chose the film.'),
  ('The money didn’t matter.', 'It wasn’t the money that mattered.'),
  ('The storm didn’t stop until midnight.', 'It wasn’t until midnight that the storm stopped.'),
  ('I need a holiday.', 'What I need is a holiday.'),
  ('She called the police.', 'What she did was call the police.'),
  ('His reaction surprised me.', 'What surprised me was his reaction.'),
  ('The team wants a new coach.', 'What the team wants is a new coach.'),
  ('Nobody knows where she went.', 'Where she went is a mystery.'),
  ('Nobody explained how they did it.', 'How they did it was never explained.'),
  ('The noise annoys her.', 'The noise is what annoys her.'),
  ('The website is too slow.', 'The problem is that the website is too slow.'),
  ('We have no time.', 'The trouble is that we have no time.'),
  ('I only want some peace.', 'The only thing I want is some peace.'),
  ('The exams worry me most.', 'The thing that worries me most is the exams.'),
  ('Many people never vote.', 'The sad fact is that many people never vote.'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Check what is being emphasised, and watch the linking words and the verb forms.',
  [
  ('Focus on a person', 'It ___ Anna who broke the window, not Ben.', ['was', 'were', 'did', 'has'],
   ['‘It’ never changes, and ‘were’ doesn’t agree with ‘it’.', '‘Did’ can’t be the verb ‘be’ in an it-cleft.', '‘Has’ is not the verb ‘be’, which every it-cleft needs.'],
   'An it-cleft needs ‘be’ after ‘it’. The window was broken in the past: It was Anna who…'),
  ('Focus on a thing', 'It was the keys ___ she lost, not her wallet.', ['that', 'what', 'where', 'whose'],
   ['‘What’ can’t follow a noun focus like ‘the keys’.', '‘Where’ is for places, and ‘the keys’ is a thing.', '‘Whose’ shows possession, which isn’t the meaning here.'],
   'After a thing in focus, ‘that’ introduces the rest of the sentence.'),
  ('Focus on a thing', 'It was the price ___ put people off, not the quality.', ['that', 'who', 'where', 'what'],
   ['‘Who’ is for people, but the price is a thing.', '‘Where’ is for places, but the price is a thing.', '‘What’ can’t follow a noun focus like ‘the price’.'],
   'After a thing in focus, ‘that’ links it to the verb ‘put’.'),
  ('Focus on a place', 'It was in Barcelona ___ they first met.', ['that', 'who', 'what', 'whom'],
   ['‘Who’ is for people, and ‘in Barcelona’ is a place.', '‘What’ doesn’t link a place focus to the clause.', '‘Whom’ is for people, and ‘in Barcelona’ is a place.'],
   'For places, times and reasons, the linking word is ‘that’.'),
  ('Focus on time', 'It wasn’t ___ midnight that the music stopped.', ['until', 'since', 'during', 'while'],
   ['‘Since’ would need a starting point in a present perfect sentence.', '‘During’ doesn’t fit the pattern ‘It wasn’t… that’.', '‘While’ is a conjunction and can’t come before ‘midnight’.'],
   'The fixed pattern is It wasn’t until + time + that + clause.'),
  ('Wh-cleft', '___ I need is a long holiday.', ['What', 'That', 'Which', 'It'],
   ['‘That’ can’t be the subject in this wh-cleft.', '‘Which’ needs a choice of things, but nothing is given.', '‘It’ needs a ‘that’ or ‘who’ clause after the focus.'],
   'A wh-cleft starts with ‘What’ + clause, then be, then the focus.'),
  ('Wh-cleft', 'What surprised everyone ___ his reaction.', ['was', 'were', 'did', 'has'],
   ['‘Were’ doesn’t agree with ‘what surprised everyone’, which is singular.', '‘Did’ can’t link the clause to the focus.', '‘Has’ can’t link the clause to the focus.'],
   'After the what-clause you need ‘be’. The surprise was in the past: was.'),
  ('Focus on an action', 'What he did ___ walk out of the meeting.', ['was', 'were', 'does', 'had'],
   ['‘Were’ doesn’t agree with the singular ‘what he did’.', '‘Does’ is not the linking verb ‘be’.', '‘Had’ is not the linking verb ‘be’.'],
   '‘What he did’ is in the past, so the verb ‘be’ is ‘was’, followed by the base verb ‘walk’.'),
  ('Focus on an action', 'What she did was ___ the police.', ['call', 'called', 'calls', 'has called'],
   ['After ‘what she did was’, we don’t repeat the past form.', 'The verb has no -s here; it is a base verb.', 'A present perfect form can’t follow ‘what she did was’.'],
   'After ‘what… did was’, use the base verb (or to + base verb).'),
  ('Where / why / how', '___ we stayed in Paris was a tiny hotel near the river.', ['Where', 'What', 'Why', 'Who'],
   ['‘What’ doesn’t fit: we stayed in a place, so the clause needs ‘where’.', '‘Why’ would ask for a reason, but the focus is a place.', '‘Who’ would ask for a person, but the focus is a place.'],
   'The focus (a tiny hotel near the river) is a place, so the cleft clause starts with ‘Where’.'),
  ('Where / why / how', '___ she won the match was by staying calm under pressure.', ['How', 'What', 'Where', 'Who'],
   ['‘What she won the match’ is not a possible clause here.', '‘Where’ would ask for a place, but the focus is a way of doing something.', '‘Who’ would ask for a person, but the focus is a way of doing something.'],
   'The focus (by staying calm) is a way of doing something, so the cleft clause starts with ‘How’.'),
  ('Reversed focus', 'The noise is ___ annoys her.', ['what', 'that', 'who', 'where'],
   ['‘That’ can’t introduce a reverse wh-cleft here; the sentence needs ‘what’.', '‘Who’ is for people, but the noise is a thing.', '‘Where’ is for places, but the noise is a thing.'],
   'A reverse wh-cleft has the structure focus + is + what + clause.'),
  ('Introducing a problem', 'The problem ___ that the website is too slow.', ['is', 'are', 'does', 'has'],
   ['‘Are’ doesn’t agree with the singular ‘the problem’.', '‘Does’ can’t link the noun and the that-clause.', '‘Has’ can’t link the noun and the that-clause.'],
   'In a thing-cleft, ‘be’ links the noun (problem) and the that-clause.'),
  ('Introducing a problem', 'The only thing I want right now ___ some peace and quiet.', ['is', 'are', 'does', 'was'],
   ['‘Are’ doesn’t agree with ‘the only thing’, which is singular.', '‘Does’ can’t link the noun phrase and the focus.', '‘Was’ is past, but ‘want’ is present.'],
   '‘The only thing I want’ is singular and present, so the linking verb is ‘is’.'),
  ('Question', '___ it Maria who called you last night?', ['Was', 'Did', 'Has', 'Does'],
   ['‘Did’ can’t be followed by ‘it Maria who’ in a cleft question.', '‘Has’ is not the verb ‘be’.', '‘Does’ is present, but the call was last night.'],
   'A cleft question puts ‘be’ first: Was it Maria who…?'),
  ('Negative', 'It ___ the money that mattered; it was the people.', ['wasn’t', 'didn’t', 'hadn’t', 'weren’t'],
   ['‘Didn’t’ can’t be followed by ‘the money that mattered’ in this pattern.', '‘Hadn’t’ would be past perfect, which does not fit.', '‘Weren’t’ doesn’t agree with ‘it’.'],
   'The negative goes on ‘be’: It wasn’t the money that mattered.'),
  ('Focus on a reason', 'It was ___ the storm that the match stopped.', ['because of', 'because', 'although', 'so'],
   ['‘Because’ needs a full clause, but ‘the storm’ is a noun phrase.', '‘Although’ shows contrast, not a reason.', '‘So’ can’t come before a noun phrase.'],
   'Before a noun phrase, use ‘because of’: It was because of the storm that…'),
  ('Contrast', 'Which sentence is correct?', ['It was Tom who broke the vase.', 'Was Tom who broke the vase.', 'It were Tom who broke the vase.', 'It was Tom who he broke the vase.'],
   ['An it-cleft can’t leave out ‘it’.', '‘It’ is singular, so ‘were’ is wrong.', 'The subject can’t be repeated: ‘who he’ is wrong.'],
   'It + was + focus + who + verb, with no repeated subject.'),
  ('Wh-cleft', 'Which sentence is correct?', ['What I really love is the music.', 'What I really love the music.', 'What I really love it is the music.', 'What I really love are the music.'],
   ['The verb ‘be’ is missing.', 'You can’t add ‘it’ after the what-clause.', '‘Are’ doesn’t agree with ‘the music’, which is singular.'],
   'What + clause + is + focus, with no extra words.'),
  ('Formal writing', 'Which sentence is more suitable for a formal report?', ['What this survey shows is that costs are rising.', 'The survey shows costs are rising, you know.', 'Costs are rising and stuff, the survey says.', 'Survey says costs rising.'],
   ['‘You know’ is a spoken filler and doesn’t belong in a formal report.', '‘And stuff’ is too vague and informal for a report.', 'It is too short and incomplete for a formal report.'],
   'A wh-cleft with a clear subject suits formal reports and speeches.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('Missing it', '*Was* Maria who called me yesterday.', 'It was', 'An it-cleft needs ‘it’: It was Maria who called.'),
  ('Plural verb', 'It *were* the students who complained about the noise.', 'was', '‘It’ is always singular: It was the students who complained.'),
  ('Wrong linking word', 'It was the keys *who* she lost on the train.', 'that', '‘Who’ is for people. For a thing use ‘that’: It was the keys that she lost.'),
  ('Wrong linking word', 'It was Anna *what* broke the window.', 'who', 'Use ‘who’ or ‘that’ after a person, not ‘what’: It was Anna who broke the window.'),
  ('Repeated subject', 'It was Maria who *she found* the keys.', 'found', 'Don’t repeat the subject: It was Maria who found the keys.'),
  ('Extra word', 'It was in Girona that we *there got* married.', 'got', 'Don’t add ‘there’: the place is already the focus.'),
  ('Wrong preposition', 'It wasn’t *since* midnight that the music stopped.', 'until', 'The pattern is It wasn’t until + time + that…'),
  ('Wrong negative', 'It *didn’t* the money that mattered.', 'wasn’t', 'The negative of an it-cleft goes on ‘be’: It wasn’t the money…'),
  ('Cleft question', '*Did* it your brother who called?', 'Was', 'A cleft question uses ‘be’: Was it your brother who called?'),
  ('Missing be', 'What I need *a* holiday.', 'is', 'A wh-cleft needs ‘be’ before the focus: What I need is a holiday.'),
  ('Missing be', 'What surprised me *his* reaction.', 'was', 'The verb ‘be’ is missing: What surprised me was his reaction.'),
  ('Wrong wh-word', '*That* I need is a long holiday.', 'What', 'A wh-cleft starts with ‘What’: What I need is a long holiday.'),
  ('Past form after did', 'What she did was *called* the police.', 'call', 'After ‘what she did was’, use the base verb: call, not called.'),
  ('Past form after did', 'What he did was *walked* out of the meeting.', 'walk', 'After ‘what he did was’, use the base verb: walk, not walked.'),
  ('Agreement', 'What surprised everyone *were* his calm reaction.', 'was', 'The what-clause is singular, so ‘was’ with the singular ‘reaction’.'),
  ('Wrong wh-word', '*What* we stayed in Paris was a tiny hotel by the river.', 'Where', 'For a place, use ‘Where’: Where we stayed in Paris was a tiny hotel by the river.'),
  ('Wrong wh-word', '*Where* she won the match was by staying calm.', 'How', 'For the way something was done, use ‘How’: How she won the match was by staying calm.'),
  ('Reverse cleft', 'A long holiday is *that* I need.', 'what', 'A reverse wh-cleft uses ‘what’: A long holiday is what I need.'),
  ('Thing-cleft', 'The problem *are* that the website is slow.', 'is', '‘The problem’ is singular, so ‘is’.'),
  ('Wrong linking word', 'It was my sister *which* taught me to swim.', 'who', '‘Which’ isn’t used for people. Use ‘who’ or ‘that’: It was my sister who taught me to swim.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, which linking word, multiple choice and spot-the-mistake. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('linking', 'Linking words'),
 'fill': [
  ('Focus on a person', 'It was Tom [[who|that]] fixed the broken printer.', 'relative word', 'Focus on a person who did the action: It was Tom who / that fixed it.', 'Use ‘who’ or ‘that’ after a person in an it-cleft.'),
  ('Focus on an action', 'What he did was [[apologise|to apologise]] to everyone.', 'apologise', 'After ‘what he did was’ use the base verb, or to + base verb.', 'Use the base verb after ‘what… did was’: apologise, not apologised.'),
  ('Negative', 'It wasn’t [[until]] after dinner that she told us.', 'linking word', 'The pattern is It wasn’t until + time + that + clause.', 'The pattern needs ‘until’.'),
  ('Wh-cleft', '[[What]] annoys me most is the constant noise.', 'wh-word', 'A wh-cleft starts with ‘What’ + clause + be + focus.', 'Start the wh-cleft with ‘What’.'),
  ],
 'order': [
  ('Focus on a person', 'It was Anna who won the prize.', None),
  ('Wh-cleft', 'What I like is the quiet.', ['the quiet is what I like.']),
  ('Question', 'Was it Tom who called?', None),
  ('Introducing a problem', 'The trouble is that we have no time.', None),
  ],
 'customItems': [
  ('Linking words', 'It was last summer ___ we first visited Lisbon.', ['that', 'who', 'what', 'which'],
   ['‘Who’ is for people, but ‘last summer’ is a time.', '‘What’ doesn’t link a time focus to the clause.', '‘Which’ is too formal and not used after a time focus.'],
   'After a time in focus, the linking word is ‘that’.'),
  ('Linking words', 'It is our manager ___ makes the final decision.', ['who', 'what', 'where', 'whose'],
   ['‘What’ can’t follow a person focus.', '‘Where’ is for places.', '‘Whose’ shows possession, which isn’t the meaning here.'],
   'After a person who does the action, use ‘who’ (or ‘that’).'),
  ('Linking words', 'The sad fact is ___ many young people never vote.', ['that', 'what', 'who', 'where'],
   ['‘What’ can’t follow ‘the sad fact is’.', '‘Who’ would need a person as the focus.', '‘Where’ would need a place as the focus.'],
   'A thing-cleft with ‘fact’ is followed by a that-clause.'),
  ('Linking words', 'A cold drink is ___ I need right now.', ['what', 'that', 'who', 'where'],
   ['‘That’ can’t introduce a reverse wh-cleft.', '‘Who’ is for people, but a cold drink is a thing.', '‘Where’ is for places, but a cold drink is a thing.'],
   'A reverse wh-cleft has the structure focus + is + what + clause.'),
  ],
 'mc': [
  ('Contrast', 'It ___ the teacher who made the mistake, it was the student.', ['wasn’t', 'weren’t', 'didn’t', 'hadn’t'],
   ['‘Weren’t’ doesn’t agree with ‘it’.', '‘Didn’t’ can’t be followed by ‘the teacher who’.', '‘Hadn’t’ can’t be followed by ‘the teacher who’.'],
   'The negative goes on ‘be’, and the past ‘made’ needs ‘wasn’t’.'),
  ('Wh-cleft', 'What she did ___ close the door quietly.', ['was', 'were', 'did', 'has'],
   ['‘Were’ doesn’t agree with the singular ‘what she did’.', '‘Did’ can’t link the clause and the focus.', '‘Has’ can’t link the clause and the focus.'],
   'The linking verb is ‘be’, and ‘did’ shows the past: was.'),
  ('Cleft sentence', 'Which sentence is correct?', ['It was Maria who called me.', 'Was Maria who called me.', 'It were Maria who called me.', 'It was Maria who she called me.'],
   ['An it-cleft needs ‘it’.', '‘It’ is singular, so ‘were’ is wrong.', 'The subject can’t be repeated.'],
   'It + was + focus + who + verb.'),
  ('Reason', 'Which sentence is correct?', ['Why she left remains a mystery.', 'What she left remains a mystery.', 'Why she left it remains a mystery.', 'Why she left are a mystery.'],
   ['‘What she left’ has a different meaning.', 'You can’t add ‘it’ after the clause.', '‘Are’ doesn’t agree with the singular clause.'],
   '‘Why’ + clause is the subject of ‘remains’.'),
  ],
 'error': [
  ('Missing it', '*Was* Maria who found the keys.', 'It was', 'An it-cleft needs ‘it’: It was Maria who found the keys.'),
  ('Plural verb', 'It *were* the students who complained.', 'was', '‘It’ is singular: It was the students who complained.'),
  ('Past form after did', 'What he did was *walked* away.', 'walk', 'After ‘what he did was’, use the base verb.'),
  ('Wrong linking word', 'It was the book *who* she wanted.', 'that', '‘Who’ is for people. For a thing use ‘that’.'),
  ],
}
