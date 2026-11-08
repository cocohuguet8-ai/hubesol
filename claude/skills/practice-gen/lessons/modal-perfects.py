TITLE = 'Modal Perfects'
AUX = (['must', 'might', 'can’t', 'should', 'have'], None, 'have')
NEXT = ('Would rather & Would prefer', '/grammar/modal-verbs/would-rather-would-prefer/')
BODY = r'''
## How to form modal perfects

| Structure | Example |
|---|---|
| modal + **have** + past participle | She **must have left**. |
| negative: modal + **not** + have + participle | He **can't have seen** us. |
| continuous: modal + have + **been** + -ing | They **must have been sleeping**. |

The modal never changes and *have* never becomes *has* or *had*. In speech, *have* is often contracted: *must've, should've, could've* — but never write ~~must of~~.

## Deductions about the past

| Certainty | Form | Example |
|---|---|---|
| sure it happened | **must have** + participle | The ground is wet. It **must have rained**. |
| possible | **might / may / could have** + participle | She **might have missed** the bus. |
| sure it didn't happen | **can't / couldn't have** + participle | He **can't have finished** already! |

### 1. *Must have* — strong evidence

- You **must have been** tired after the trip.
- Someone **must have taken** my pen.

> ⚠️ Typical error: ~~It must rained.~~ → The past needs *have* + participle: *It must have rained.*

### 2. *Can't have* — impossible

- She **can't have seen** me — I was hiding.

> ⚠️ Typical error: ~~She mustn't have seen me.~~ → The negative deduction is *can't have*: *She can't have seen me.*

### 3. *Might have* — not sure

- I don't know why he's late. He **might have overslept**.

## Criticism and regret: *should have*

*Should have* + participle = it was the right thing to do, but it **didn't** happen.

- You **should have told** me! (you didn't tell me)
- I **shouldn't have eaten** so much. (I ate a lot)

> ⚠️ Typical error: ~~You should told me.~~ → *Should have told.*

## Missed possibilities: *could have*

*Could have* + participle = it was possible, but it **didn't** happen.

- We **could have won** if we'd played better.
- You **could have hurt** yourself! (but you didn't)

### *Couldn't have* + comparative

- The party was great — it **couldn't have been** better!

## *Needn't have* and *would have*

| Form | Meaning | Example |
|---|---|---|
| **needn't have** + participle | you did it, but it wasn't necessary | You **needn't have brought** a present. |
| **would have** + participle | imaginary past result | I **would have come**, but I was ill. |

See [Need & Needn't](/grammar/modal-verbs/need-neednt/) and [Third Conditional](/grammar/conditionals/third-conditional/).

## Continuous modal perfects

For an action **in progress** in the past:

- He didn't answer. He **must have been sleeping**.
- They **might have been joking**.

## Common mistakes

**1. Missing *have*.** *~~She must left~~* → **She must have left.**

**2. Past simple instead of participle.** *~~He should have went~~* → **He should have gone.**

**3. *Mustn't have* for negative deduction.** *~~He mustn't have known~~* → **He can't have known.**

**4. Writing *of*.** *~~could of~~* → **could have / could've.**

**Pro tip:** every modal perfect has the same skeleton — modal + have + past participle. Learn the participles and the rest is easy.
'''

GAP = ('Fill in the gaps',
  'Type the modal perfect: modal + have + past participle. Read the clue to choose must, might, can’t, should or could. Twenty original sentences.',
  [
  ('Must have', 'The streets are wet. It [[must have rained]] last night.', '(must / rain)', 'Strong evidence about the past: must have + past participle.'),
  ('Must have', 'You walked thirty kilometres? You [[must have been]] exhausted!', '(must / be)', 'Sure deduction about the past: must have been.'),
  ('Must have', 'My pen isn’t here. Someone [[must have taken]] it.', '(must / take)', 'A sure conclusion: must have + taken (irregular participle).'),
  ('Must have', 'She speaks Italian perfectly. She [[must have lived]] in Italy.', '(must / live)', 'Evidence → sure past deduction: must have lived.'),
  ('Can’t have', 'He [[can’t have seen]] us — we were hiding behind the car.', '(can’t / see)', 'Sure it didn’t happen: can’t have + seen.'),
  ('Can’t have', 'You [[can’t have finished]] already! You only started five minutes ago.', '(can’t / finish)', 'Impossible in the time: can’t have finished.'),
  ('Can’t have', 'She [[couldn’t have known]] about the party. It was a secret.', '(couldn’t / know)', 'A softer negative deduction: couldn’t have + known.'),
  ('Might have', 'Pau is late. He [[might have missed]] the bus.', '(might / miss)', 'Not sure what happened: might have + missed.'),
  ('Might have', 'I can’t find my keys. I [[may have left]] them at school.', '(may / leave)', 'A possible past event: may have + left.'),
  ('Might have', 'Don’t worry. She [[could have forgotten]] to charge her phone.', '(could / forget)', 'A possible explanation: could have + forgotten.'),
  ('Should have', 'You [[should have told]] me about the exam! I didn’t know.', '(should / tell)', 'Criticism: it was right to tell me, but you didn’t.'),
  ('Should have', 'I [[shouldn’t have eaten]] so much cake. I feel sick.', '(shouldn’t / eat)', 'Regret: I ate it, and it was a mistake.'),
  ('Should have', 'We [[should have booked]] a table. The restaurant is full.', '(should / book)', 'A past mistake: should have + booked.'),
  ('Could have', 'Be careful! You [[could have hurt]] yourself.', '(could / hurt)', 'It was possible, but it didn’t happen: could have hurt.'),
  ('Could have', 'We [[could have won]] the match if we’d played better.', '(could / win)', 'A missed possibility: could have + won.'),
  ('Needn’t have', 'You [[needn’t have bought]] flowers — but thank you!', '(needn’t / buy)', 'You did it, but it wasn’t necessary: needn’t have bought.'),
  ('Would have', 'I [[would have come]] to the party, but I was ill.', '(would / come)', 'An imaginary past result: would have + come.'),
  ('Continuous', 'He didn’t answer. He must have been [[sleeping]].', '(sleep)', 'An action in progress in the past: must have been + -ing.'),
  ('Participle', 'They should have [[gone]] home earlier.', '(go)', 'After ‘have’ use the past participle: gone, not went.'),
  ('Participle', 'She can’t have [[written]] this — it’s not her handwriting.', '(write)', 'Irregular participle: write → written.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 modal perfects for deduction, criticism and missed chances.',
  [
  ('Must have', 'It must have rained.', []),
  ('Must have', 'She must have been tired.', []),
  ('Must have', 'They must have left early.', []),
  ('Can’t have', 'He can’t have seen us.', []),
  ('Can’t have', 'You can’t have finished yet.', []),
  ('Can’t have', 'She couldn’t have known.', []),
  ('Might have', 'He might have missed the bus.', []),
  ('Might have', 'I may have left it at home.', []),
  ('Might have', 'They could have got lost.', []),
  ('Should have', 'You should have called me.', []),
  ('Should have', 'I shouldn’t have said that.', []),
  ('Should have', 'We should have left earlier.', []),
  ('Could have', 'You could have hurt yourself.', []),
  ('Could have', 'We could have won the game.', []),
  ('Needn’t have', 'You needn’t have waited.', []),
  ('Would have', 'I would have helped you.', []),
  ('Continuous', 'He must have been sleeping.', []),
  ('Continuous', 'They might have been joking.', []),
  ('Couldn’t have', 'It couldn’t have been better.', []),
  ('Should have', 'She should have studied more.', []),
  ])

MATCH = {'title': 'Match the situation and the comment', 'subtitle': 'Tap a situation, then tap the best modal perfect comment.',
  'leftLabel': 'Situation', 'rightLabel': 'Comment', 'rightLabelSub': '(modal perfect)', 'reviewArrowPrefix': '',
  'pairs': [
  ('The grass is wet.', 'It must have rained.'), ('She didn’t tell me.', 'She should have told me.'), ('He was at home all day.', 'He can’t have been at the match.'),
  ('I’m not sure why she’s late.', 'She might have missed the train.'), ('I ate too much.', 'I shouldn’t have eaten so much.'), ('You nearly fell off the wall.', 'You could have hurt yourself.'),
  ('The cake has gone.', 'Someone must have eaten it.'), ('We lost 3–2.', 'We could have won.'), ('He didn’t answer the phone.', 'He might have been asleep.'),
  ('You brought a present, but there was no need.', 'You needn’t have bought anything.'), ('She looks very brown.', 'She must have been on holiday.'), ('I didn’t study.', 'I should have studied.'),
  ('The door was locked.', 'He can’t have gone in.'), ('My bag isn’t here.', 'I may have left it on the bus.'), ('The test was very easy.', 'It couldn’t have been easier.'),
  ('You didn’t wear a coat.', 'You should have worn a coat.'), ('She’s got a medal.', 'She must have won the race.'), ('He doesn’t know about it.', 'He can’t have heard the news.'),
  ('I was ill, so I didn’t come.', 'I would have come.'), ('The road was icy.', 'There could have been an accident.'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Modal + have + past participle. Choose the modal by its meaning: sure, possible, impossible, criticism or missed chance.',
  [
  ('Must have', 'The floor is wet. Someone ___ water.', ['must have spilt', 'must spilt', 'must has spilt', 'mustn’t have spilt'],
   ['A past deduction needs ‘have’ between the modal and the participle.', 'After a modal, ‘have’ never changes to ‘has’.', '‘Mustn’t have’ is not used for deduction.'],
   'Strong evidence about the past: must have + past participle.'),
  ('Can’t have', 'He ___ the exam — he didn’t study at all!', ['can’t have passed', 'mustn’t have passed', 'can’t passed', 'can’t have pass'],
   ['‘Mustn’t have’ is not used for negative deduction.', '‘Have’ is missing before the participle.', 'After ‘have’ use the participle ‘passed’, not the base verb.'],
   'Sure it didn’t happen: can’t have + past participle.'),
  ('Might have', 'I’m not sure why she’s late. She ___ the bus.', ['might have missed', 'must have missed', 'can’t have missed', 'might missed'],
   ['‘Must have’ means you’re sure, but you aren’t.', '‘Can’t have’ means you’re sure it didn’t happen.', '‘Have’ is missing.'],
   'Not sure about the past: might have + past participle.'),
  ('Should have', 'You ___ me you were coming! I’d have made dinner.', ['should have told', 'should told', 'should have tell', 'must have told'],
   ['‘Have’ is missing.', 'After ‘have’ use the participle ‘told’.', '‘Must have told’ is a deduction, not a criticism.'],
   'Criticism of a past action that didn’t happen: should have + participle.'),
  ('Should have', 'I feel terrible. I ___ so much pizza.', ['shouldn’t have eaten', 'mustn’t have eaten', 'shouldn’t eat', 'shouldn’t have ate'],
   ['‘Mustn’t have’ isn’t used for regret.', '‘Shouldn’t eat’ is about now, not the past.', '‘Ate’ is past simple; use the participle ‘eaten’.'],
   'Regret about the past: shouldn’t have + past participle.'),
  ('Could have', 'Why did you climb that wall? You ___ yourself!', ['could have hurt', 'could hurt', 'must have hurt', 'can’t have hurt'],
   ['‘Could hurt’ is about now or the future.', '‘Must have hurt’ means you’re sure you did.', '‘Can’t have hurt’ means it was impossible.'],
   'It was possible but didn’t happen: could have + participle.'),
  ('Could have', 'We lost 1–0. We ___ if we’d been luckier.', ['could have won', 'could won', 'must have won', 'can have won'],
   ['‘Have’ is missing.', '‘Must have won’ is the opposite: we lost.', '‘Can have’ isn’t used this way.'],
   'A missed possibility: could have + won.'),
  ('Participle', 'They should have ___ home earlier.', ['gone', 'went', 'go', 'going'],
   ['‘Went’ is past simple; after ‘have’ use the participle.', 'After ‘have’ use the participle, not the base verb.', 'After ‘have’ use the participle, not -ing.'],
   'Modal + have + past participle: gone.'),
  ('Participle', 'She must have ___ the news by now.', ['heard', 'hear', 'heared', 'hearing'],
   ['After ‘have’ use the participle.', '‘Hear’ is irregular: heard.', 'After ‘have’ use the participle, not -ing.'],
   'Irregular participle: hear → heard.'),
  ('Would of', 'Which is correct in writing?', ['could have', 'could of', 'could has', 'could had'],
   ['‘Could of’ is just how ‘could’ve’ sounds — never write it.', '‘Has’ never follows a modal.', '‘Had’ never follows a modal here.'],
   'Write ‘could have’ or ‘could’ve’.'),
  ('Needn’t have', 'You ___ a taxi. The station is only five minutes away!', ['needn’t have taken', 'mustn’t have taken', 'didn’t need take', 'needn’t taken'],
   ['‘Mustn’t have’ is the wrong structure.', '‘Didn’t need take’ is missing ‘to’.', '‘Have’ is missing.'],
   'You did it but it wasn’t necessary: needn’t have + participle.'),
  ('Would have', 'I ___ you, but my phone was dead.', ['would have called', 'would called', 'should have called', 'must have called'],
   ['‘Have’ is missing.', '‘Should have called’ is a criticism, not an imaginary result.', '‘Must have called’ is a deduction.'],
   'An imaginary past result: would have + participle.'),
  ('Continuous', 'He didn’t hear the doorbell. He ___ music.', ['must have been listening to', 'must have listened to', 'must be listening to', 'must listened to'],
   ['‘Must have listened’ is possible, but the action was in progress: continuous fits better.', '‘Must be listening’ is about now.', '‘Have’ is missing.'],
   'An action in progress in the past: must have been + -ing.'),
  ('Couldn’t have', 'The concert was perfect. It ___ better!', ['couldn’t have been', 'can’t be', 'shouldn’t have been', 'mustn’t have been'],
   ['‘Can’t be’ is about now.', '‘Shouldn’t have been’ is criticism.', '‘Mustn’t have been’ isn’t used here.'],
   '‘Couldn’t have been better’ = it was the best possible.'),
  ('Must have', 'She’s got a suntan. She ___ on holiday.', ['must have been', 'must be', 'can’t have been', 'should have been'],
   ['‘Must be on holiday’ is about now; the tan shows a past holiday.', '‘Can’t have been’ contradicts the evidence.', '‘Should have been’ is criticism.'],
   'Past deduction: must have been.'),
  ('Can’t have', 'You ___ Marta at the party. She was in Paris.', ['can’t have seen', 'must have seen', 'should have seen', 'can’t seen'],
   ['‘Must have seen’ contradicts the evidence.', '‘Should have seen’ is criticism.', '‘Have’ is missing.'],
   'Impossible in the past: can’t have seen.'),
  ('Might have', 'Where’s my phone? I ___ it in the car.', ['may have left', 'must left', 'may left', 'can’t have leave'],
   ['‘Have’ is missing.', '‘Have’ is missing.', 'After ‘have’ use the participle ‘left’.'],
   'A possible past event: may have + left.'),
  ('Should have', 'We missed the start. We ___ earlier.', ['should have left', 'must have left', 'can’t have left', 'should leave'],
   ['‘Must have left’ is a deduction.', '‘Can’t have left’ is a negative deduction.', '‘Should leave’ is about now.'],
   'A past mistake: should have left.'),
  ('Have, not has', 'Which sentence is correct?', ['He must have forgotten.', 'He must has forgotten.', 'He must have forgot.', 'He must forgotten.'],
   ['After a modal ‘have’ never changes to ‘has’.', '‘Forget’ → participle ‘forgotten’.', '‘Have’ is missing.'],
   'Modal + have + past participle.'),
  ('Mustn’t have', 'Which sentence is a correct negative deduction?', ['She can’t have known.', 'She mustn’t have known.', 'She can’t knew.', 'She don’t must have known.'],
   ['‘Mustn’t have’ isn’t used for deduction.', 'The structure needs ‘have’ + participle.', 'Modals don’t use ‘don’t’.'],
   'Negative past deduction: can’t have + participle.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('Missing have', 'It must *rained* last night.', 'have rained', 'Past deduction: ‘It must have rained’.'),
  ('Missing have', 'You should *told* me earlier.', 'have told', 'Criticism: ‘You should have told me’.'),
  ('Missing have', 'They might *gone* home already.', 'have gone', 'Possibility: ‘They might have gone home’.'),
  ('Has after a modal', 'She must *has* left early.', 'have', 'After a modal use ‘have’, never ‘has’.'),
  ('Had after a modal', 'He should *had* called.', 'have', 'After a modal use ‘have’: ‘should have called’.'),
  ('Past simple instead of participle', 'You should have *went* to bed.', 'gone', 'After ‘have’ use the participle: ‘gone’.'),
  ('Past simple instead of participle', 'She must have *forgot* her keys.', 'forgotten', 'Participle: ‘forgotten’.'),
  ('Past simple instead of participle', 'We could have *took* the train.', 'taken', 'Participle: ‘taken’.'),
  ('Base verb instead of participle', 'He can’t have *finish* already.', 'finished', 'After ‘have’ use the participle: ‘finished’.'),
  ('Base verb instead of participle', 'You might have *break* it.', 'broken', 'Participle: ‘broken’.'),
  ('Mustn’t have', 'He *mustn’t* have seen us — we were hiding.', 'can’t', 'Negative deduction: ‘He can’t have seen us’.'),
  ('Mustn’t have', 'She *mustn’t* have known about it.', 'can’t', 'Negative deduction: ‘She can’t have known’.'),
  ('Of instead of have', 'You could *of* told me!', 'have', 'Write ‘could have’, not ‘could of’.'),
  ('Of instead of have', 'I should *of* listened to you.', 'have', 'Write ‘should have’, not ‘should of’.'),
  ('Wrong modal', 'You *must* have told me — now it’s too late!', 'should', 'Criticism: ‘You should have told me’.'),
  ('Wrong modal', 'I’m not sure. He *must* have gone home.', 'might', 'Not sure → ‘He might have gone home’.'),
  ('Wrong modal', 'The road is wet. It *can’t* have rained.', 'must', 'The evidence shows ‘It must have rained’.'),
  ('Continuous', 'He must have been *sleep* when I called.', 'sleeping', 'Continuous: ‘must have been sleeping’.'),
  ('Needn’t have', 'You needn’t have *bring* anything.', 'brought', 'Participle: ‘brought’.'),
  ('Would have', 'I would have *came*, but I was ill.', 'come', 'Participle: ‘come’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, which meaning, multiple choice and spot-the-mistake. In the typing questions write modal + have + past participle. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('meaning', 'Which meaning?'),
 'fill': [
  ('Must have', 'There’s cake on his face. He [[must have eaten]] it!', 'must / eat', 'Strong evidence about the past: must have eaten.', 'Sure → must have + participle.'),
  ('Should have', 'You [[should have asked]] for help.', 'should / ask', 'Criticism: it was right, but you didn’t do it.', 'Criticism → should have + participle.'),
  ('Can’t have', 'She [[can’t have gone]] far — her coat is still here.', 'can’t / go', 'Sure it didn’t happen: can’t have gone.', 'Impossible → can’t have + participle.'),
  ('Could have', 'You [[could have fallen]]! Be more careful.', 'could / fall', 'Possible, but it didn’t happen: could have fallen.', 'Missed danger → could have + participle.'),
  ],
 'order': [
  ('Must have', 'She must have forgotten.', []),
  ('Should have', 'I should have studied.', []),
  ('Might have', 'They might have left.', []),
  ('Can’t have', 'He can’t have known.', []),
  ],
 'customItems': [
  ('Meaning', '‘You should have called me’ means…', ['you didn’t call, and that was wrong', 'I’m sure you called', 'perhaps you called', 'calling wasn’t necessary'],
   ['That’s ‘must have called’.', 'That’s ‘might have called’.', 'That’s ‘needn’t have called’.'],
   '‘Should have’ = criticism of something that didn’t happen.'),
  ('Meaning', '‘She must have left’ means…', ['I’m sure she left', 'she didn’t leave, but it was right', 'perhaps she left', 'it was impossible for her to leave'],
   ['That’s ‘should have left’.', 'That’s ‘might have left’.', 'That’s ‘can’t have left’.'],
   '‘Must have’ = a sure deduction about the past.'),
  ('Meaning', '‘We could have won’ means…', ['winning was possible, but we didn’t win', 'I’m sure we won', 'we had to win', 'we won easily'],
   ['That’s ‘must have won’.', 'That’s obligation.', 'That contradicts ‘could have’.'],
   '‘Could have’ = a missed possibility.'),
  ('Meaning', '‘You needn’t have waited’ means…', ['you waited, but it wasn’t necessary', 'you didn’t wait', 'you had to wait', 'perhaps you waited'],
   ['That’s ‘didn’t need to wait’.', 'That’s obligation.', 'That’s ‘might have waited’.'],
   '‘Needn’t have’ = done, but unnecessary.'),
  ],
 'mc': [
  ('Participle', 'He might have ___ the email.', ['deleted', 'delete', 'deleting', 'deletes'],
   ['After ‘have’ use the participle.', 'After ‘have’ use the participle, not -ing.', 'After ‘have’ use the participle, not -s.'],
   'Modal + have + past participle.'),
  ('Must have', 'The lights are off. They ___ to bed.', ['must have gone', 'must gone', 'must have went', 'must go'],
   ['‘Have’ is missing.', '‘Went’ is past simple; use ‘gone’.', '‘Must go’ is obligation now.'],
   'Past deduction: must have gone.'),
  ('Can’t have', 'You ___ the whole book in an hour!', ['can’t have read', 'mustn’t have read', 'can’t read', 'shouldn’t have read'],
   ['‘Mustn’t have’ isn’t used for deduction.', '‘Can’t read’ is about now.', '‘Shouldn’t have’ is criticism.'],
   'Impossible: can’t have read.'),
  ('Should have', 'I ___ that. I’m sorry.', ['shouldn’t have said', 'mustn’t have said', 'can’t have said', 'shouldn’t said'],
   ['‘Mustn’t have’ isn’t used for regret.', '‘Can’t have said’ is a deduction.', '‘Have’ is missing.'],
   'Regret: shouldn’t have said.'),
  ],
 'error': [
  ('Missing have', 'She must *left* early.', 'have left', 'Past deduction: ‘must have left’.'),
  ('Past simple instead of participle', 'You should have *saw* it!', 'seen', 'Participle: ‘seen’.'),
  ('Mustn’t have', 'He *mustn’t* have heard me.', 'can’t', 'Negative deduction: ‘can’t have heard’.'),
  ('Of instead of have', 'We might *of* won.', 'have', 'Write ‘might have’, never ‘might of’.'),
  ],
}
