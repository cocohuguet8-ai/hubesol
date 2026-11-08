TITLE = 'Inversion in Conditionals'
AUX = (['Should', 'Were', 'Had'], None, 'Had')
NEXT = ('All conditionals', '/grammar/conditionals/')
BODY = r'''
## How to form inverted conditionals

In formal English we can **drop *if*** and put the auxiliary **before the subject**. The meaning doesn't change; the style becomes more formal.

| Conditional | With *if* | Inverted |
|---|---|---|
| First | **If** you **should** need help, call me. | **Should** you need help, call me. |
| Second | **If** I **were** in your position, I'd accept. | **Were** I in your position, I'd accept. |
| Third | **If** we **had** known, we'd have come. | **Had** we known, we'd have come. |

Only three auxiliaries invert: **should, were, had**. The comma rule stays: comma after the inverted clause when it comes first.

## *Should* (first conditional)

*Should* + subject + base verb = *if* + present simple. It makes the condition sound **less likely** and very polite. It is common in instructions, business letters and notices.

- **Should** you **have** any questions, please contact reception.
- **Should** the alarm **sound**, leave the building immediately.

> ⚠️ Typical error: ~~Should you will need help, call me.~~ → After *should* use the base verb: *Should you need help…*

## *Were* (second conditional)

*Were* + subject + adjective / noun / *to* + verb = *if* + past simple.

- **Were** I rich, I'd buy a castle. (= If I were rich…)
- **Were** she **to** resign, the company would struggle. (= If she resigned…)

For verbs other than *be*, use **were + subject + to + base verb**.

> ⚠️ Typical error: ~~Did I know the answer, I'd tell you.~~ → *Did* cannot invert. Use *Were I to know…* or *If I knew…*

## *Had* (third conditional)

*Had* + subject + past participle = *if* + had + past participle. This is the most common type.

- **Had** I **known** about the strike, I would have taken a taxi.
- **Had** they **left** earlier, they wouldn't have missed the flight.

> ⚠️ Typical error: ~~If had I known, I'd have come.~~ → Drop *if* completely: *Had I known…*

## Negatives

The negative is **not contracted** and goes **after** the subject.

| ✗ | ✓ |
|---|---|
| ~~Hadn't I seen it…~~ | **Had I not** seen it… |
| ~~Weren't it for you…~~ | **Were it not** for you… |
| ~~Shouldn't you agree…~~ | **Should you not** agree… |

- **Had we not** checked the tickets, we'd have gone to the wrong airport.
- **Were it not for** your help, I would fail. (= Without your help…)

## When to use inversion

### Formal contexts

| Context | Example |
|---|---|
| formal letters and emails | **Should** you require further information, do not hesitate to contact us. |
| notices and instructions | **Should** the screen freeze, restart the device. |
| essays and speeches (C1/C2) | **Had** the government acted sooner, the crisis might have been avoided. |
| everyday speech | rarely — *if* sounds more natural |

### Everyday speech

In conversation, *if* is almost always better. Inversion can sound old-fashioned or ironic with friends: *Had I known you were coming, I'd have baked a cake!*

## Mixed inversion

Inversion also works in mixed conditionals:

- **Had** I **taken** the job, I**'d be** living in Paris now.

See [Mixed Conditionals](/grammar/conditionals/mixed-conditionals/).

## Common mistakes

**1. Keeping *if*.** *~~If had we known~~* → **Had we known.**

**2. Contracting the negative.** *~~Hadn't we known~~* → **Had we not known.**

**3. Inverting with *did* or *would*.** Only *should, were, had* work. *~~Would you need help, call me~~* → **Should you need help, call me.**

**4. Forgetting *to* after *were* + subject with a verb.** *~~Were he resign~~* → **Were he to resign.**

**Pro tip:** to check an inverted clause, put *if* back and move the auxiliary after the subject — *Had I known* → *If I had known*.
'''

GAP = ('Fill in the gaps',
  'Type the auxiliary that starts the inverted condition — Should, Were or Had — or the verb that follows it. Twenty original sentences.',
  [
  ('Should', '[[Should]] you need any help, please ask at reception.', 'Should / Were / Had', 'A polite, unlikely future condition: Should + subject + base verb.'),
  ('Should', '[[Should]] the alarm sound, leave the building at once.', 'Should / Were / Had', 'An instruction for a possible future event: Should + subject + base verb.'),
  ('Should', '[[Should]] you have any questions, do not hesitate to contact us.', 'Should / Were / Had', 'A formal letter phrase: Should you have… = If you have…'),
  ('Should', 'Should you [[require]] further details, please call our office.', '(require)', 'After inverted ‘should’ use the base verb: ‘require’, not ‘requires’.'),
  ('Should', 'Should the train [[be]] delayed, we will send you an email.', '(be)', 'Base verb after ‘should’: be, not ‘is’.'),
  ('Were', '[[Were]] I in your position, I would accept the offer.', 'Should / Were / Had', 'An imaginary present: Were I… = If I were…'),
  ('Were', '[[Were]] she to resign, the team would be lost.', 'Should / Were / Had', 'Were + subject + to + verb = If she resigned.'),
  ('Were', 'Were they [[to]] win the final, the city would celebrate for a week.', 'to', 'With an action verb, inverted ‘were’ needs ‘to’ + base verb.'),
  ('Were', '[[Were]] it not for your help, I would never finish.', 'Should / Were / Had', 'The fixed phrase ‘Were it not for…’ means ‘Without…’.'),
  ('Were', 'Were I [[richer]], I would buy a house in the mountains.', '(rich)', 'Were + subject + adjective. Comparative: rich → richer.'),
  ('Had', '[[Had]] I known about the strike, I would have taken a taxi.', 'Should / Were / Had', 'An imaginary past: Had I known… = If I had known…'),
  ('Had', '[[Had]] we left earlier, we wouldn’t have missed the flight.', 'Should / Were / Had', 'Third conditional inversion: Had + subject + past participle.'),
  ('Had', 'Had they [[checked]] the forecast, they wouldn’t have gone sailing.', '(check)', 'After inverted ‘had’ use the past participle: checked.'),
  ('Had', 'Had she [[taken]] the job, she would be living in Paris now.', '(take)', 'Mixed inversion: Had + subject + past participle, ‘taken’.'),
  ('Had', 'Had the referee [[seen]] the foul, he would have sent the player off.', '(see)', 'Irregular participle after inverted ‘had’: seen.'),
  ('Negative', 'Had we [[not]] checked the tickets, we’d have gone to the wrong airport.', 'not', 'The negative isn’t contracted and goes after the subject: Had we not…'),
  ('Negative', 'Were it [[not]] for the rain, we would play outside.', 'not', 'Were it not for… — ‘not’ goes after ‘it’, never ‘Weren’t it’.'),
  ('Negative', 'Should you [[not]] receive the parcel by Friday, please call us.', 'not', 'Should + subject + not + base verb: ‘Should you not receive’.'),
  ('Result', 'Had I seen you, I [[would have said]] hello.', '(say)', 'The result clause stays the same as a third conditional: would have said.'),
  ('Result', 'Were I you, I [[would apologise|’d apologise]] immediately.', '(apologise)', 'The result of an inverted second conditional: would + base verb.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each formal sentence — 20 examples with should, were and had. The inverted clause starts with the auxiliary.',
  [
  ('Should', 'Should you need help, call me.', ['call me should you need help.']),
  ('Should', 'Should the price rise, we will tell you.', ['we will tell you should the price rise.']),
  ('Should', 'Should it rain, the event will move indoors.', ['the event will move indoors should it rain.']),
  ('Should', 'Should you have questions, contact us.', ['contact us should you have questions.']),
  ('Should', 'Should the alarm ring, leave immediately.', ['leave immediately should the alarm ring.']),
  ('Should', 'Should you not agree, let us know.', ['let us know should you not agree.']),
  ('Were', 'Were I you, I would accept.', ['I would accept were I you.']),
  ('Were', 'Were she here, she would help.', ['she would help were she here.']),
  ('Were', 'Were they to win, we would celebrate.', ['we would celebrate were they to win.']),
  ('Were', 'Were it not for you, I would fail.', ['I would fail were it not for you.']),
  ('Were', 'Were he to resign, the team would suffer.', ['the team would suffer were he to resign.']),
  ('Were', 'Were I richer, I would travel more.', ['I would travel more were I richer.']),
  ('Had', 'Had I known, I would have come.', ['I would have come had I known.']),
  ('Had', 'Had we left earlier, we would have arrived.', ['we would have arrived had we left earlier.']),
  ('Had', 'Had she asked, I would have helped.', ['I would have helped had she asked.']),
  ('Had', 'Had they trained, they would have won.', ['they would have won had they trained.']),
  ('Had', 'Had I not seen it, I wouldn’t believe it.', ['I wouldn’t believe it had I not seen it.']),
  ('Had', 'Had it not rained, the match would have finished.', ['the match would have finished had it not rained.']),
  ('Had', 'Had you told me, I could have helped.', ['I could have helped had you told me.']),
  ('Mixed', 'Had I taken the job, I would be rich now.', ['I would be rich now had I taken the job.']),
  ])

MATCH = {'title': 'Match the if-clause and its inversion', 'subtitle': 'Tap a clause with if, then tap the inverted clause that means the same.',
  'leftLabel': 'With if', 'rightLabel': 'Inverted', 'rightLabelSub': '(should / were / had)', 'reviewArrowPrefix': '',
  'pairs': [
  ('If you need help,', 'Should you need help,'), ('If the alarm sounds,', 'Should the alarm sound,'), ('If you have any questions,', 'Should you have any questions,'),
  ('If it rains,', 'Should it rain,'), ('If you don’t agree,', 'Should you not agree,'), ('If I were you,', 'Were I you,'),
  ('If she were here,', 'Were she here,'), ('If they won,', 'Were they to win,'), ('If he resigned,', 'Were he to resign,'),
  ('If it weren’t for you,', 'Were it not for you,'), ('If I were richer,', 'Were I richer,'), ('If I had known,', 'Had I known,'),
  ('If we had left earlier,', 'Had we left earlier,'), ('If she had asked,', 'Had she asked,'), ('If they hadn’t trained,', 'Had they not trained,'),
  ('If it hadn’t rained,', 'Had it not rained,'), ('If you had told me,', 'Had you told me,'), ('If he had seen it,', 'Had he seen it,'),
  ('If the train is late,', 'Should the train be late,'), ('If we had checked,', 'Had we checked,'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Only should, were and had invert. No if, no contracted negatives.',
  [
  ('Had', '___ I known about the traffic, I would have left earlier.', ['Had', 'If', 'Did', 'Were'],
   ['‘If I known’ is wrong: with ‘if’ you need ‘had’ after the subject.', '‘Did’ can never start an inverted conditional.', '‘Were I known’ is passive and changes the meaning.'],
   'Third conditional inversion: Had + subject + past participle.'),
  ('Should', '___ you need any assistance, please call us.', ['Should', 'Would', 'Will', 'Did'],
   ['‘Would’ cannot invert in a conditional clause.', '‘Will’ cannot start an inverted condition.', '‘Did’ cannot start an inverted condition.'],
   'Formal first conditional: Should you need…'),
  ('Were', '___ I in your shoes, I would take the job.', ['Were', 'Was', 'Had', 'Should'],
   ['Inverted second conditionals always use ‘were’, never ‘was’.', '‘Had I in your shoes’ has no participle and makes no sense.', '‘Should I in your shoes’ needs a verb.'],
   'Imaginary present: Were I…'),
  ('Were', 'Were she ___ the company, we would lose our best manager.', ['to leave', 'leave', 'leaves', 'left'],
   ['After ‘Were + subject’ an action verb needs ‘to’.', '‘Leaves’ is present simple.', '‘Left’ doesn’t follow ‘were she’ here.'],
   'Were + subject + to + base verb.'),
  ('Should', 'Should the flight ___ cancelled, you will get a refund.', ['be', 'is', 'will be', 'being'],
   ['After ‘should’ use the base verb: ‘be’, not ‘is’.', '‘Will’ cannot follow ‘should’.', '‘Being’ needs a different structure.'],
   'Should + subject + base verb: be.'),
  ('Had', 'Had they ___ the instructions, they wouldn’t have broken it.', ['read', 'reading', 'to read', 'reads'],
   ['After ‘had’ use the past participle: ‘read’.', '‘To read’ follows ‘were’, not ‘had’.', '‘Reads’ is present.'],
   'Had + subject + past participle.'),
  ('Negative', '___ we not booked, we wouldn’t have got a table.', ['Had', 'Hadn’t', 'If had', 'Did'],
   ['Negative inversion isn’t contracted: ‘Had we not…’.', 'Never keep ‘if’ with inversion.', '‘Did’ cannot invert.'],
   'Had + subject + not + participle.'),
  ('Negative', '___ it not been for your advice, I would have made a big mistake.', ['Had', 'Hadn’t', 'Were', 'Weren’t'],
   ['Negative inversion isn’t contracted.', '‘Were it not been’ is impossible: ‘been’ needs ‘had’.', 'Contracted forms can’t invert.'],
   'Past version of ‘Were it not for’: Had it not been for… = without your advice (then).'),
  ('Negative', 'Which is correct?', ['Should you not agree, please tell us.', 'Shouldn’t you agree, please tell us.', 'If should you not agree, please tell us.', 'Should not you agree, please tell us.'],
   ['Inverted negatives are never contracted.', 'Never keep ‘if’ with inversion.', '‘Not’ goes after the subject: Should you not…'],
   'Should + subject + not + base verb.'),
  ('Keep if?', 'Which is correct?', ['Had I seen her, I’d have waved.', 'If had I seen her, I’d have waved.', 'If I seen her, I’d have waved.', 'Had I saw her, I’d have waved.'],
   ['Drop ‘if’ completely when you invert.', 'With ‘if’ you need ‘had’: If I had seen her.', 'After ‘had’ use the participle ‘seen’, not ‘saw’.'],
   'Inverted third conditional: Had I seen…'),
  ('Result', 'Had you called me, I ___ you up.', ['would have picked', 'would pick', 'will pick', 'had picked'],
   ['‘Would pick’ is about now; the call was in the past.', '‘Will’ is for a real future.', '‘Had picked’ is not a result form.'],
   'Third conditional result: would have + participle.'),
  ('Result', 'Were I a millionaire, I ___ a yacht.', ['would buy', 'would have bought', 'will buy', 'bought'],
   ['‘Would have bought’ is about the past; ‘Were I’ is present.', '‘Will’ is for a real future.', '‘Bought’ is a fact.'],
   'Second conditional result: would + base verb.'),
  ('Result', 'Should you see Tom, ___ him I said hello.', ['tell', 'you would tell', 'told', 'telling'],
   ['An instruction uses the imperative, not ‘would’.', '‘Told’ is past.', '‘Telling’ needs an auxiliary.'],
   'First conditional result: an imperative is common.'),
  ('Which auxiliary', 'Which word can start an inverted conditional?', ['Had', 'Did', 'Would', 'Will'],
   ['‘Did’ never inverts in conditionals.', '‘Would’ goes in the result, not the condition.', '‘Will’ never starts a condition.'],
   'Only should, were and had invert in conditionals.'),
  ('Register', 'Inverted conditionals are typical of…', ['formal writing', 'text messages', 'chatting with friends', 'children’s stories'],
   ['Text messages are informal; inversion sounds too formal there.', 'With friends, ‘if’ is more natural.', 'Simple stories normally use ‘if’.'],
   'Inversion is formal: letters, notices, essays and speeches.'),
  ('Had', '___ the government acted sooner, the crisis might have been avoided.', ['Had', 'Should', 'Were', 'Did'],
   ['‘Should’ is for future conditions; this is the past.', '‘Were the government acted’ is wrong: ‘were’ doesn’t go with a participle here.', '‘Did’ cannot invert.'],
   'A past condition: Had + subject + participle.'),
  ('Should', '___ the printer stop working, press the reset button.', ['Should', 'Had', 'Were', 'Would'],
   ['‘Had’ is for past conditions.', '‘Were the printer stop’ needs ‘to’ and sounds unlikely-imaginary.', '‘Would’ cannot invert.'],
   'An instruction for a future possibility: Should…'),
  ('Were', 'Were he ___ the truth, nobody would believe him.', ['to tell', 'tell', 'told', 'tells'],
   ['After ‘Were + subject’ an action verb needs ‘to’.', '‘Told’ doesn’t follow ‘were he’ here.', '‘Tells’ is present.'],
   'Were + subject + to + base verb.'),
  ('Mixed', 'Had I studied medicine, I ___ a doctor now.', ['would be', 'would have been', 'will be', 'had been'],
   ['‘Now’ shows a present result.', '‘Will’ is for a real future.', '‘Had been’ is not a result.'],
   'Mixed inversion: past condition, present result.'),
  ('Should', 'Should you ___ to cancel, please give us 24 hours’ notice.', ['wish', 'wishes', 'will wish', 'wished'],
   ['After ‘should’ use the base verb, no -s.', '‘Will’ cannot follow ‘should’.', '‘Wished’ is past.'],
   'Should + subject + base verb: wish.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('Keeping if', '*If* I known the truth, I would have acted.', 'Had', 'Use inversion without ‘if’: ‘Had I known the truth…’.'),
  ('Contracted negative', '*Hadn’t we* checked, we would have been lost.', 'Had we not', 'Don’t contract: ‘Had we not checked…’.'),
  ('Contracted negative', '*Weren’t it* for you, I would give up.', 'Were it not', 'Don’t contract: ‘Were it not for you…’.'),
  ('Wrong auxiliary', '*Did I know* the answer, I would tell you.', 'Were I to know', '‘Did’ can’t invert. Use ‘Were I to know…’ or ‘If I knew…’.'),
  ('Wrong auxiliary', '*Would* you need help, please call me.', 'Should', 'Only ‘should’ inverts for a future condition: ‘Should you need help…’.'),
  ('Wrong auxiliary', '*Was* I in your position, I would accept.', 'Were', 'Inverted second conditionals always use ‘were’.'),
  ('Verb after should', 'Should you *needs* help, call me.', 'need', 'After ‘should’ use the base verb: ‘need’.'),
  ('Verb after should', 'Should the bus *is* late, take a taxi.', 'be', 'After ‘should’ use the base verb: ‘be’.'),
  ('Will after should', 'Should you *will have* questions, contact us.', 'have', 'No ‘will’ after ‘should’: ‘Should you have questions…’.'),
  ('Missing to', 'Were she *resign*, the company would suffer.', 'to resign', 'Were + subject + to + verb: ‘Were she to resign’.'),
  ('Participle after had', 'Had I *knew*, I would have helped.', 'known', 'After ‘had’ use the participle: ‘known’.'),
  ('Participle after had', 'Had they *went* by train, they’d have arrived.', 'gone', 'After ‘had’ use the participle: ‘gone’.'),
  ('Participle after had', 'Had we *took* a map, we wouldn’t have got lost.', 'taken', 'After ‘had’ use the participle: ‘taken’.'),
  ('Contracted negative', '*Shouldn’t you* agree, please let us know.', 'Should you not', 'Don’t contract: ‘Should you not agree…’.'),
  ('Result', 'Had you told me, I would *help* you yesterday.', 'have helped', 'A past result: ‘I would have helped you’.'),
  ('Result', 'Were I rich, I *will* buy a castle.', 'would', 'Second conditional result: ‘I would buy’.'),
  ('Result', 'Had I known, I would have *came* earlier.', 'come', 'After ‘would have’ use the participle: ‘come’.'),
  ('Should with past', '*Should* I known, I would have called.', 'Had', 'A past condition needs ‘Had I known’.'),
  ('Were with past', '*Were* we left earlier, we’d have caught it.', 'Had', 'A past condition: ‘Had we left earlier…’.'),
  ('Spelling', 'Should you *recieve* this message, please reply.', 'receive', 'Spelling: ‘receive’ — e before i after c.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, which auxiliary, multiple choice and spot-the-mistake. In the typing questions write Should, Were or Had, or the verb after it. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('auxiliary', 'Should, were or had'),
 'fill': [
  ('Had', '[[Had]] I seen the sign, I would have stopped.', 'Should / Were / Had', 'A past condition: Had + subject + participle.', 'Past condition → ‘Had’.'),
  ('Should', '[[Should]] you lose your card, call the bank immediately.', 'Should / Were / Had', 'A possible future event: Should + subject + base verb.', 'Future possibility → ‘Should’.'),
  ('Were', '[[Were]] I taller, I would join the volleyball team.', 'Should / Were / Had', 'An imaginary present: Were + subject + adjective.', 'Imaginary present → ‘Were’.'),
  ('Negative', 'Had she [[not]] called, I would have forgotten.', 'not', 'Negative inversion: Had + subject + not.', 'Don’t contract: ‘Had she not…’.'),
  ],
 'order': [
  ('Had', 'Had I known, I would have called.', ['I would have called had I known.']),
  ('Should', 'Should you need me, call.', ['call should you need me.']),
  ('Were', 'Were I you, I would wait.', ['I would wait were I you.']),
  ('Negative', 'Had we not run, we would have missed it.', ['we would have missed it had we not run.']),
  ],
 'customItems': [
  ('Auxiliary', '___ the weather be bad, the race will be postponed.', ['Should', 'Had', 'Were', 'Did'],
   ['‘Had the weather be’ is wrong: ‘had’ needs a participle.', '‘Were the weather be’ is wrong: ‘were’ is already the verb.', '‘Did’ cannot invert.'],
   'A future possibility + base verb ‘be’: Should.'),
  ('Auxiliary', '___ I a bird, I would fly over the ocean.', ['Were', 'Should', 'Had', 'Was'],
   ['‘Should I a bird’ needs a verb.', '‘Had I a bird’ means ‘if I had a bird’ — different meaning.', 'Inversion uses ‘were’, not ‘was’.'],
   'Imaginary present with a noun: Were I…'),
  ('Auxiliary', '___ we taken the earlier train, we would have arrived on time.', ['Had', 'Were', 'Should', 'Did'],
   ['‘Were we taken’ is passive and wrong here.', '‘Should we taken’ needs a base verb.', '‘Did’ cannot invert.'],
   'Past condition + participle: Had.'),
  ('Auxiliary', '___ you require a receipt, please ask the cashier.', ['Should', 'Had', 'Were', 'Would'],
   ['‘Had you require’ needs a participle.', '‘Were you require’ needs ‘to’.', '‘Would’ cannot invert.'],
   'Polite future condition + base verb: Should.'),
  ],
 'mc': [
  ('Were', 'Were they ___ the match, they would be champions.', ['to win', 'win', 'won', 'winning'],
   ['After ‘Were + subject’ an action verb needs ‘to’.', '‘Won’ doesn’t follow ‘were they’ here.', '‘Winning’ changes the structure.'],
   'Were + subject + to + verb.'),
  ('Keep if?', 'Which is correct?', ['Should you need help, ask.', 'If should you need help, ask.', 'Should you will need help, ask.', 'Should you needs help, ask.'],
   ['Never keep ‘if’ with inversion.', 'No ‘will’ after ‘should’.', 'No -s after ‘should’.'],
   'Should + subject + base verb.'),
  ('Result', 'Had I listened, I ___ the answer.', ['would have known', 'would know', 'will know', 'had known'],
   ['‘Would know’ is about now; listening was in the past.', '‘Will’ is for the future.', '‘Had known’ is not a result.'],
   'Past result: would have known.'),
  ('Negative', 'Which is correct?', ['Were it not for the map, we’d be lost.', 'Weren’t it for the map, we’d be lost.', 'Were not it for the map, we’d be lost.', 'If were it not for the map, we’d be lost.'],
   ['No contracted negatives in inversion.', '‘Not’ goes after the subject.', 'Never keep ‘if’.'],
   'Were it not for… = Without…'),
  ],
 'error': [
  ('Missing to', 'Were he *sell* the house, he’d be rich.', 'to sell', 'Were + subject + to + verb: ‘Were he to sell…’.'),
  ('Contracted negative', '*Hadn’t I* seen it, I wouldn’t believe it.', 'Had I not', 'Don’t contract: ‘Had I not seen it…’.'),
  ('Participle after had', 'Had she *saw* the email, she’d have replied.', 'seen', 'After ‘had’ use the participle: ‘seen’.'),
  ('Wrong auxiliary', '*Did* you need help, call me.', 'Should', 'Only ‘should’ inverts for a future condition.'),
  ],
}
