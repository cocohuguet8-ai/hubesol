TITLE = 'The Passive in All Tenses'
AUX = (['is', 'was', 'being', 'been', 'will', 'be'], None, 'been')
NEXT = ('Passive with Two Objects', '/grammar/passive-voice/passive-two-objects/')
BODY = r'''
## How to form the passive in every tense

The rule never changes: **be** (in the tense you need) + **past participle**.

| Tense | Active | Passive |
|---|---|---|
| Present simple | They **clean** the room. | The room **is cleaned**. |
| Present continuous | They **are cleaning** the room. | The room **is being cleaned**. |
| Past simple | They **cleaned** the room. | The room **was cleaned**. |
| Past continuous | They **were cleaning** the room. | The room **was being cleaned**. |
| Present perfect | They **have cleaned** the room. | The room **has been cleaned**. |
| Past perfect | They **had cleaned** the room. | The room **had been cleaned**. |
| Future (*will*) | They **will clean** the room. | The room **will be cleaned**. |
| *Going to* | They**'re going to clean** the room. | The room **is going to be cleaned**. |
| Modals | They **must clean** the room. | The room **must be cleaned**. |

## Continuous passives: *being*

Add **being** between *be* and the participle.

- The road **is being repaired** at the moment.
- When I arrived, dinner **was being served**.

> ⚠️ Typical error: ~~The road is repairing.~~ → A road can't repair: *The road is being repaired.*

## Perfect passives: *been*

Add **been** between *have/has/had* and the participle.

- My bike **has been stolen**!
- By the time we arrived, all the tickets **had been sold**.

> ⚠️ Typical error: ~~My bike has stolen.~~ → *My bike has been stolen.*

## Future and modal passives: *be*

After *will*, *going to* and every modal, use **be** + participle.

- The results **will be announced** on Friday.
- The new stadium **is going to be built** next year.
- Phones **must be switched off**.
- This homework **should be finished** by Monday.

> ⚠️ Typical error: ~~The results will announced.~~ → *will be announced.*

### Modal perfect passive

- The letter **should have been sent** yesterday.
- The window **must have been broken** by the wind.

## Negatives and questions

### The first auxiliary does the work

The first auxiliary makes the negative or the question.

| Negative | Question |
|---|---|
| The room **isn't being** cleaned. | **Is** the room **being** cleaned? |
| The email **hasn't been** sent. | **Has** the email **been** sent? |
| It **won't be** finished. | **Will** it **be** finished? |

## *Being* or *been*?

| | Comes after | Example |
|---|---|---|
| **being** | am / is / are / was / were | It **is being** built. |
| **been** | have / has / had | It **has been** built. |
| **be** | will / modals / to | It **will be** built. |

## Common mistakes

**1. Mixing *being* and *been*.** *~~It has being built~~* → **It has been built.**

**2. Missing *be* after a modal.** *~~It must done~~* → **It must be done.**

**3. Missing *been* in the perfect.** *~~The car has repaired~~* → **The car has been repaired.**

**4. Active continuous instead of passive.** *~~The house is building~~* → **The house is being built.**

**Pro tip:** say the active tense, then put *be* into that tense and add the participle — the rest follows automatically.
'''

GAP = ('Fill in the gaps',
  'Type the passive form of the verb in the tense shown by the clue. Twenty original sentences.',
  [
  ('Present continuous', 'The bridge [[is being repaired]] at the moment.', '(repair)', 'An action in progress now: is being + past participle.'),
  ('Present continuous', 'Our classroom [[is being painted]] this week.', '(paint)', 'Present continuous passive: is being painted.'),
  ('Present continuous', 'New houses [[are being built]] near the station.', '(build)', 'Plural subject: are being + built.'),
  ('Past continuous', 'When we arrived, dinner [[was being served]].', '(serve)', 'In progress in the past: was being + served.'),
  ('Past continuous', 'The car [[was being washed]] when it started to rain.', '(wash)', 'Past continuous passive: was being washed.'),
  ('Present perfect', 'My bike [[has been stolen]]!', '(steal)', 'Recent past with a present result: has been + stolen.'),
  ('Present perfect', 'All the tickets [[have been sold]].', '(sell)', 'Plural, present perfect: have been sold.'),
  ('Present perfect', 'The email [[hasn’t been sent]] yet.', '(not send)', 'Negative present perfect passive: hasn’t been sent.'),
  ('Present perfect', '[[Has]] the parcel been delivered?', 'has / is', 'Question: Has + subject + been + participle?'),
  ('Past perfect', 'By the time we got there, the cake [[had been eaten]].', '(eat)', 'Before another past moment: had been + eaten.'),
  ('Past perfect', 'The thief [[had been caught]] before the police arrived.', '(catch)', 'Past perfect passive: had been caught.'),
  ('Future', 'The results [[will be announced]] on Friday.', '(announce)', 'Future passive: will be + announced.'),
  ('Future', 'You [[will be met]] at the airport.', '(meet)', 'Future passive: will be met.'),
  ('Going to', 'The old cinema [[is going to be demolished]].', '(demolish)', 'Planned future passive: is going to be + participle.'),
  ('Modal', 'Phones [[must be switched]] off during the exam.', '(switch)', 'Modal passive: must be + participle.'),
  ('Modal', 'This form [[should be signed]] by a parent.', '(sign)', 'Modal passive: should be signed.'),
  ('Modal', 'The project [[can be done]] in pairs.', '(do)', 'Modal passive: can be done.'),
  ('Modal perfect', 'The letter [[should have been sent]] last week.', '(send)', 'Modal perfect passive: should have been sent.'),
  ('Being or been', 'The car has [[been]] repaired. You can collect it.', 'being / been', 'After ‘has’ use ‘been’.'),
  ('Being or been', 'The car is [[being]] repaired. Come back tomorrow.', 'being / been', 'After ‘is’ (continuous) use ‘being’.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each passive sentence — 20 examples across all the tenses.',
  [
  ('Present continuous', 'The road is being repaired.', []),
  ('Present continuous', 'A new school is being built.', []),
  ('Past continuous', 'The room was being cleaned.', []),
  ('Past continuous', 'We were being watched.', []),
  ('Present perfect', 'My phone has been stolen.', []),
  ('Present perfect', 'The tickets have been sold.', []),
  ('Present perfect', 'Has the email been sent?', []),
  ('Present perfect', 'The problem hasn’t been solved.', []),
  ('Past perfect', 'The cake had been eaten.', []),
  ('Past perfect', 'The door had been locked.', []),
  ('Future', 'The winner will be announced tomorrow.', []),
  ('Future', 'You will be told later.', []),
  ('Going to', 'The hotel is going to be closed.', []),
  ('Modal', 'Mobiles must be switched off.', []),
  ('Modal', 'This can be done online.', []),
  ('Modal', 'It should be finished today.', []),
  ('Modal perfect', 'It should have been done yesterday.', []),
  ('Modal perfect', 'The window must have been broken.', []),
  ('Question', 'Will the match be cancelled?', []),
  ('Question', 'Is the house being sold?', []),
  ])

MATCH = {'title': 'Match the active and passive tense', 'subtitle': 'Tap an active verb, then tap the same tense in the passive.',
  'leftLabel': 'Active', 'rightLabel': 'Passive', 'rightLabelSub': '(same tense)', 'reviewArrowPrefix': '',
  'pairs': [
  ('they clean', 'it is cleaned'), ('they are cleaning', 'it is being cleaned'), ('they cleaned', 'it was cleaned'), ('they were cleaning', 'it was being cleaned'),
  ('they have cleaned', 'it has been cleaned'), ('they had cleaned', 'it had been cleaned'), ('they will clean', 'it will be cleaned'), ('they are going to clean', 'it is going to be cleaned'),
  ('they must clean', 'it must be cleaned'), ('they can clean', 'it can be cleaned'), ('they should clean', 'it should be cleaned'), ('they might clean', 'it might be cleaned'),
  ('they should have cleaned', 'it should have been cleaned'), ('they build', 'it is built'), ('they are building', 'it is being built'), ('they have built', 'it has been built'),
  ('they will build', 'it will be built'), ('they had built', 'it had been built'), ('they were building', 'it was being built'), ('they built', 'it was built'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Being after is / was; been after have / has / had; be after will and modals.',
  [
  ('Present continuous', 'Sorry, the lift ___ at the moment.', ['is being repaired', 'is repairing', 'has being repaired', 'is been repaired'],
   ['A lift can’t repair: ‘is repairing’ is active and wrong in meaning.', '‘Has being’ mixes the perfect with the continuous: after ‘has’ use ‘been’.', 'After ‘is’ the continuous passive needs ‘being’, not ‘been’.'],
   'Happening now: is being + past participle.'),
  ('Present perfect', 'Look! My car ___.', ['has been stolen', 'has stolen', 'has being stolen', 'is been stolen'],
   ['‘Has stolen’ is active: the car stole something.', 'After ‘has’ use ‘been’, not ‘being’.', '‘Is been’ is impossible.'],
   'A recent event with a present result: has been + participle.'),
  ('Future', 'The new library ___ next spring.', ['will be opened', 'will opened', 'will being opened', 'will been opened'],
   ['After ‘will’ the passive needs ‘be’.', 'After ‘will’ use ‘be’, not ‘being’.', 'After ‘will’ use ‘be’, not ‘been’.'],
   'Future passive: will be + past participle.'),
  ('Modal', 'All answers ___ in pen.', ['must be written', 'must written', 'must be wrote', 'must being written'],
   ['After a modal the passive needs ‘be’.', '‘Wrote’ is past simple; use the participle ‘written’.', 'After a modal use ‘be’, not ‘being’.'],
   'Modal passive: must be + participle.'),
  ('Past perfect', 'When I got home, the dishes ___ already.', ['had been washed', 'had washed', 'have been washed', 'had being washed'],
   ['‘Had washed’ is active: the dishes washed something.', '‘Have been’ is present perfect; the moment is past.', 'After ‘had’ use ‘been’.'],
   'Earlier than another past moment: had been + participle.'),
  ('Past continuous', 'The film ___ when the power went off.', ['was being shown', 'was showing', 'had been shown', 'is being shown'],
   ['‘Was showing’ is possible for cinemas, but here the passive is needed for ‘the film’ being shown.', '‘Had been shown’ means it was already finished.', '‘Is’ is present.'],
   'In progress in the past: was being + participle.'),
  ('Going to', 'The old factory ___ into flats.', ['is going to be turned', 'is going to turned', 'is going to being turned', 'is going be turned'],
   ['After ‘to’ we need ‘be’ before the participle.', 'After ‘going to’ use ‘be’, not ‘being’.', '‘Going be’ is missing ‘to’.'],
   'Going to passive: is going to be + participle.'),
  ('Being or been', 'The results have ___ published online.', ['been', 'being', 'be', 'were'],
   ['After ‘have’ use ‘been’, not ‘being’.', 'After ‘have’ use ‘been’, not ‘be’.', '‘Have were’ is impossible.'],
   'Perfect passive: have / has / had + been.'),
  ('Being or been', 'The results are ___ checked right now.', ['being', 'been', 'be', 'was'],
   ['After ‘are’ (continuous) use ‘being’.', '‘Are be’ is impossible.', '‘Are was’ is impossible.'],
   'Continuous passive: am / is / are + being.'),
  ('Negative', 'The problem ___ yet.', ['hasn’t been solved', 'hasn’t solved', 'isn’t solved yet been', 'didn’t solved'],
   ['‘Hasn’t solved’ is active.', 'Wrong word order.', 'Passive negatives use ‘be’, and after ‘didn’t’ use the base verb.'],
   'Negative present perfect passive: hasn’t been solved.'),
  ('Question', '___ the room been booked?', ['Has', 'Is', 'Was', 'Did'],
   ['‘Is the room been’ is impossible.', '‘Was the room been’ is impossible.', '‘Did the room been’ is impossible.'],
   'Present perfect passive question: Has + subject + been…?'),
  ('Question', '___ the match be shown on TV?', ['Will', 'Is', 'Has', 'Does'],
   ['‘Is the match be’ is impossible.', '‘Has the match be’ is impossible.', '‘Does the match be’ is impossible.'],
   'Future passive question: Will + subject + be…?'),
  ('Modal perfect', 'This report ___ yesterday. It’s late!', ['should have been sent', 'should have sent', 'should be sent', 'should been sent'],
   ['‘Should have sent’ is active: the report sent something.', '‘Should be sent’ is about now or the future.', '‘Have’ is missing.'],
   'Modal perfect passive: should have been + participle.'),
  ('Modal', 'Tickets ___ online or at the door.', ['can be bought', 'can bought', 'can be buy', 'can been bought'],
   ['After a modal the passive needs ‘be’.', 'After ‘be’ use the participle ‘bought’.', 'After a modal use ‘be’, not ‘been’.'],
   'Modal passive: can be + participle.'),
  ('Tense', 'They are building a new hospital. → A new hospital ___.', ['is being built', 'is built', 'has been built', 'was being built'],
   ['The active is continuous, so the passive must be continuous.', 'The active is not perfect.', 'The tense must stay present.'],
   'Present continuous → is being built.'),
  ('Tense', 'They have cancelled the flight. → The flight ___.', ['has been cancelled', 'was cancelled', 'is being cancelled', 'had cancelled'],
   ['The active is present perfect, so keep it.', 'The active is not continuous.', '‘Had cancelled’ is active past perfect.'],
   'Present perfect → has been cancelled.'),
  ('Tense', 'They will deliver it tomorrow. → It ___ tomorrow.', ['will be delivered', 'will delivered', 'is delivered', 'is being delivered'],
   ['After ‘will’ use ‘be’.', 'The tense must be future.', 'The active uses ‘will’.'],
   'Future → will be delivered.'),
  ('Tense', 'They had locked the gate. → The gate ___.', ['had been locked', 'was locked', 'has been locked', 'had locked'],
   ['The active is past perfect.', 'The active is past perfect, not present perfect.', '‘Had locked’ is active.'],
   'Past perfect → had been locked.'),
  ('Active continuous error', 'Which sentence is correct?', ['The house is being painted.', 'The house is painting.', 'The house is been painted.', 'The house being painted.'],
   ['A house can’t paint.', '‘Is been’ is impossible.', '‘Is’ is missing.'],
   'Continuous passive: is being + participle.'),
  ('Modal', 'Medicines ___ out of reach of children.', ['should be kept', 'should kept', 'should be keep', 'should keeping'],
   ['After a modal the passive needs ‘be’.', 'After ‘be’ use the participle ‘kept’.', 'Wrong form after a modal.'],
   'Modal passive: should be kept.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('Being or been', 'The car has *being* repaired.', 'been', 'After ‘has’ use ‘been’: ‘has been repaired’.'),
  ('Being or been', 'The tickets have *being* sold.', 'been', 'After ‘have’ use ‘been’.'),
  ('Being or been', 'The road is *been* repaired now.', 'being', 'Continuous: ‘is being repaired’.'),
  ('Being or been', 'The room was *been* cleaned when I arrived.', 'being', 'Past continuous: ‘was being cleaned’.'),
  ('Missing be', 'The results will *announced* tomorrow.', 'be announced', 'After ‘will’ add ‘be’: ‘will be announced’.'),
  ('Missing be', 'This must *done* today.', 'be done', 'After a modal add ‘be’: ‘must be done’.'),
  ('Missing been', 'My bike has *stolen*!', 'been stolen', 'Perfect passive: ‘has been stolen’.'),
  ('Missing been', 'The cake had *eaten* before we arrived.', 'been eaten', 'Past perfect passive: ‘had been eaten’.'),
  ('Missing being', 'The house is *built* right now.', 'being built', 'Happening now: ‘is being built’.'),
  ('Active continuous', 'The bridge is *repairing* this month.', 'being repaired', 'A bridge can’t repair: ‘is being repaired’.'),
  ('Wrong participle', 'The letter has been *wrote*.', 'written', 'Participle: ‘written’.'),
  ('Wrong participle', 'It will be *sell* online.', 'sold', 'Participle: ‘sold’.'),
  ('Wrong participle', 'The window must have been *broke* by the wind.', 'broken', 'Participle: ‘broken’.'),
  ('Wrong auxiliary', 'The parcel *have* been delivered.', 'has', '‘The parcel’ is singular: ‘has been’.'),
  ('Wrong auxiliary', 'The rooms *is* being cleaned.', 'are', 'Plural: ‘are being cleaned’.'),
  ('Wrong question', '*Did* the email been sent?', 'Has', 'Perfect question: ‘Has the email been sent?’.'),
  ('Wrong question', '*Is* the match be shown on TV?', 'Will', 'Future question: ‘Will the match be shown?’.'),
  ('Wrong negative', 'The problem *didn’t* been solved.', 'hasn’t', 'Negative perfect: ‘hasn’t been solved’.'),
  ('Going to', 'The cinema is going to *being* closed.', 'be', 'After ‘going to’ use ‘be’.'),
  ('Modal perfect', 'It should have *be* done yesterday.', 'been', 'Modal perfect passive: ‘should have been done’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, being / been / be, multiple choice and spot-the-mistake. In the typing questions write the passive in the tense the sentence needs. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('aux', 'Being, been or be'),
 'fill': [
  ('Present continuous', 'The streets [[are being cleaned]] right now.', 'clean', 'In progress now with a plural subject: are being cleaned.', 'Now → is / are being + participle.'),
  ('Present perfect', 'The thief [[has been arrested]].', 'arrest', 'Recent event: has been + participle.', 'Perfect → has been + participle.'),
  ('Future', 'The winner [[will be chosen]] by the public.', 'choose', 'Future: will be + chosen.', 'Future → will be + participle.'),
  ('Modal', 'This door [[must be kept]] closed.', 'keep', 'Modal passive: must be + kept.', 'Modal → be + participle.'),
  ],
 'order': [
  ('Present continuous', 'It is being fixed.', []),
  ('Present perfect', 'It has been sold.', []),
  ('Future', 'It will be finished.', []),
  ('Modal', 'It can be recycled.', []),
  ],
 'customItems': [
  ('Aux', 'The bridge has ___ closed.', ['been', 'being', 'be', 'is'],
   ['After ‘has’ we never use ‘being’.', 'After ‘has’ we never use ‘be’.', '‘Has is’ is impossible.'],
   'After have / has / had → been.'),
  ('Aux', 'The bridge is ___ repaired.', ['being', 'been', 'be', 'was'],
   ['‘Is been’ is impossible.', '‘Is be’ is impossible.', '‘Is was’ is impossible.'],
   'Continuous after is / are / was → being.'),
  ('Aux', 'The bridge will ___ opened soon.', ['be', 'been', 'being', 'is'],
   ['‘Will been’ is impossible.', '‘Will being’ is impossible.', '‘Will is’ is impossible.'],
   'After will or a modal → be.'),
  ('Aux', 'The bridge should have ___ finished last year.', ['been', 'be', 'being', 'was'],
   ['‘Have be’ is impossible.', '‘Have being’ is impossible.', '‘Have was’ is impossible.'],
   'After have (also in modal perfects) → been.'),
  ],
 'mc': [
  ('Past perfect', 'The museum ___ when we arrived. It was closed.', ['had been closed', 'had closed', 'has been closed', 'was being close'],
   ['‘Had closed’ is active.', '‘Has been’ is present perfect.', 'After ‘being’ use the participle.'],
   'Before a past moment: had been + participle.'),
  ('Present continuous', 'Shh! The baby ___ fed.', ['is being', 'has being', 'is been', 'being'],
   ['After ‘has’ use ‘been’.', '‘Is been’ is impossible.', '‘Is’ is missing.'],
   'Now: is being fed.'),
  ('Going to', 'The park ___ improved next year.', ['is going to be', 'is going to', 'will being', 'is going be'],
   ['‘Going to improved’ is missing ‘be’.', '‘Will being’ is wrong.', '‘Going be’ is missing ‘to’.'],
   'Going to passive: is going to be + participle.'),
  ('Question', '___ the room been cleaned?', ['Has', 'Is', 'Did', 'Was'],
   ['‘Is the room been’ is impossible.', '‘Did the room been’ is impossible.', '‘Was the room been’ is impossible.'],
   'Perfect question: Has…been?'),
  ],
 'error': [
  ('Being or been', 'It has *being* done.', 'been', 'After ‘has’: ‘been’.'),
  ('Missing be', 'It will *finished* soon.', 'be finished', 'After ‘will’ add ‘be’.'),
  ('Active continuous', 'The flat is *decorating* now.', 'being decorated', 'Passive continuous: ‘is being decorated’.'),
  ('Missing been', 'The work has *completed*.', 'been completed', 'Perfect passive: ‘has been completed’.'),
  ],
}
