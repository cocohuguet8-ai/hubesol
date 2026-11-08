TITLE = 'Reported Statements & Backshift'
AUX = (['said', 'that', 'had', 'would', 'was'], None, 'said')
NEXT = ('Changes in Reported Speech', '/grammar/reported-speech/reported-speech-changes/')
BODY = r'''
## How to report a statement

| Direct speech | Reported speech |
|---|---|
| "I **am** tired," she said. | She said (that) she **was** tired. |

When the reporting verb is in the **past** (*said, told*), the tense of the original words usually moves **one step back**. This is called **backshift**. *That* is optional.

## The backshift table

| Direct speech | → | Reported speech |
|---|---|---|
| present simple: "I **live** here." | → | past simple: she **lived** there |
| present continuous: "I'**m working**." | → | past continuous: he **was working** |
| past simple: "I **saw** it." | → | past perfect: she **had seen** it |
| present perfect: "I'**ve finished**." | → | past perfect: he **had finished** |
| past continuous: "I **was sleeping**." | → | past perfect continuous: she **had been sleeping** |
| *will*: "I'**ll help**." | → | *would*: he **would help** |
| *can*: "I **can** swim." | → | *could*: she **could** swim |
| *may*: "I **may** come." | → | *might*: he **might** come |
| *must*: "I **must** go." | → | *had to* (or *must*): she **had to** go |

The **past perfect** doesn't change: "I **had** left." → She said she **had left**.

## When to use backshift

### 1. Reporting after *said* / *told*

- "I **love** pizza." → Pau said he **loved** pizza.
- "We **are** late." → They told me they **were** late.

> ⚠️ Typical error: ~~Pau said he loves pizza yesterday.~~ → After *said*, move the tense back: *Pau said he loved pizza.*

### 2. Past actions → past perfect

- "I **lost** my keys." → She said she **had lost** her keys.
- "We**'ve been** to Rome." → They said they **had been** to Rome.

> ⚠️ Typical error: ~~She said she has lost her keys.~~ → *had lost.*

### 3. Future and modals

- "I**'ll call** you." → He said he **would call** me.
- "You **can** stay." → She said I **could** stay.

> ⚠️ Typical error: ~~He said he will call me.~~ → After *said*: *would call.*

## Modals that don't change

*Would, could, might, should* and *ought to* stay the same.

- "You **should** rest." → The doctor said I **should** rest.
- "I **could** help." → She said she **could** help.

## Pronouns and possessives change too

Change *I, my, we, our* to match the new speaker.

- "**I**'m tired of **my** job." → Marta said **she** was tired of **her** job.

More in [Changes in Reported Speech](/grammar/reported-speech/reported-speech-changes/).

## When backshift is optional

If the reporting verb is **present** (*says, has said*), don't backshift: *She says she **is** tired.* If the fact is still true, backshift is optional. See [Reported Speech without Backshift](/grammar/reported-speech/reported-speech-no-backshift/).

## Common mistakes

**1. No backshift after *said*.** *~~He said he is hungry~~* → **He said he was hungry.**

**2. Past simple instead of past perfect.** *~~She said she saw it~~* (possible in speech, but formally) → **She said she had seen it.**

**3. *Will* instead of *would*.** *~~They said they will come~~* → **They said they would come.**

**4. Forgetting to change pronouns.** *~~She said I am tired~~* → **She said she was tired.**

**Pro tip:** go one step back on the timeline — present → past, past → past perfect, *will* → *would*.
'''

GAP = ('Fill in the gaps',
  'Type the reported verb form after said / told: move the tense one step back. Twenty original sentences.',
  [
  ('Present simple', '“I live in Girona.” → She said she [[lived]] in Girona.', '(live)', 'Present simple → past simple after ‘said’: lived.'),
  ('Present simple', '“I like jazz.” → He said he [[liked]] jazz.', '(like)', 'Present simple moves back to past simple: liked.'),
  ('Present simple', '“We don’t eat meat.” → They said they [[didn’t eat]] meat.', '(not eat)', 'Negative present → negative past: didn’t eat.'),
  ('Be', '“I am tired.” → Laia said she [[was]] tired.', '(be)', '‘Am’ moves back to ‘was’.'),
  ('Be', '“We are late.” → They told me they [[were]] late.', '(be)', '‘Are’ moves back to ‘were’.'),
  ('Present continuous', '“I’m studying.” → Pau said he [[was studying]].', '(study)', 'Present continuous → past continuous: was studying.'),
  ('Present continuous', '“We’re waiting for the bus.” → They said they [[were waiting]] for the bus.', '(wait)', 'Plural, present continuous → were waiting.'),
  ('Past simple', '“I saw the film.” → She said she [[had seen]] the film.', '(see)', 'Past simple → past perfect: had seen.'),
  ('Past simple', '“I lost my phone.” → He told me he [[had lost]] his phone.', '(lose)', 'Past simple → past perfect: had lost.'),
  ('Present perfect', '“I’ve finished my homework.” → She said she [[had finished]] her homework.', '(finish)', 'Present perfect → past perfect: had finished.'),
  ('Present perfect', '“We’ve never been to Paris.” → They said they [[had never been]] to Paris.', '(never / be)', 'Present perfect → past perfect: had never been.'),
  ('Past continuous', '“I was sleeping.” → He said he [[had been sleeping]].', '(sleep)', 'Past continuous → past perfect continuous: had been sleeping.'),
  ('Will', '“I’ll help you.” → She said she [[would help]] me.', '(help)', '‘Will’ moves back to ‘would’.'),
  ('Will', '“It won’t rain.” → The forecast said it [[wouldn’t rain]].', '(not rain)', '‘Won’t’ moves back to ‘wouldn’t’.'),
  ('Can', '“I can swim.” → My sister said she [[could]] swim.', 'can / could', '‘Can’ moves back to ‘could’.'),
  ('May', '“I may be late.” → He said he [[might]] be late.', 'may / might', '‘May’ moves back to ‘might’.'),
  ('Must', '“I must leave early.” → She said she [[had to]] leave early.', 'must / had to', '‘Must’ (obligation) usually becomes ‘had to’.'),
  ('No change', '“You should rest.” → The doctor said I [[should]] rest.', 'should / shall', '‘Should’ doesn’t change in reported speech.'),
  ('No change', '“I had already eaten.” → He said he [[had]] already eaten.', 'had / has', 'The past perfect doesn’t change.'),
  ('Going to', '“I’m going to call her.” → He said he [[was going to]] call her.', 'was going to', '‘Am going to’ moves back to ‘was going to’.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each reported statement — 20 examples with backshift.',
  [
  ('Present simple', 'She said she lived in Madrid.', []),
  ('Present simple', 'He said he didn’t like fish.', []),
  ('Be', 'They said they were hungry.', []),
  ('Be', 'She told me she was tired.', []),
  ('Present continuous', 'He said he was working.', []),
  ('Present continuous', 'They said they were leaving.', []),
  ('Past simple', 'She said she had seen him.', []),
  ('Past simple', 'He told us he had lost his keys.', []),
  ('Present perfect', 'She said she had finished.', []),
  ('Present perfect', 'They said they had never met.', []),
  ('Past continuous', 'He said he had been sleeping.', []),
  ('Will', 'She said she would call me.', []),
  ('Will', 'He said it wouldn’t be easy.', []),
  ('Can', 'She said she could help.', []),
  ('May', 'He said he might come.', []),
  ('Must', 'She said she had to go.', []),
  ('No change', 'He said I should rest.', []),
  ('Going to', 'They said they were going to move.', []),
  ('That', 'She said that she was sorry.', []),
  ('Told', 'My dad told me he was proud.', []),
  ])

MATCH = {'title': 'Match the direct and reported tense', 'subtitle': 'Tap a tense from direct speech, then tap the form it becomes after ‘said’.',
  'leftLabel': 'Direct speech', 'rightLabel': 'Reported speech', 'rightLabelSub': '(after said)', 'reviewArrowPrefix': '',
  'pairs': [
  ('I live', 'she lived'), ('I am', 'she was'), ('we are', 'they were'), ('I’m working', 'he was working'), ('I saw', 'she had seen'),
  ('I’ve finished', 'he had finished'), ('I was sleeping', 'she had been sleeping'), ('I’ll help', 'he would help'), ('I won’t go', 'she wouldn’t go'),
  ('I can swim', 'he could swim'), ('I may come', 'she might come'), ('I must go', 'he had to go'), ('I should rest', 'she should rest'),
  ('I had left', 'he had left'), ('I’m going to call', 'she was going to call'), ('I don’t know', 'he didn’t know'), ('I’ve never been', 'she had never been'),
  ('I lost it', 'he had lost it'), ('I can’t come', 'she couldn’t come'), ('I’m leaving', 'he was leaving'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. After said / told, move one step back: present → past, past → past perfect, will → would.',
  [
  ('Present simple', '“I love chocolate.” → She said she ___ chocolate.', ['loved', 'loves', 'had loved', 'is loving'],
   ['After ‘said’, the present simple normally moves back: ‘loves’ isn’t backshifted.', '‘Had loved’ is two steps back: the original was present, not past.', '‘Is loving’ is present continuous and doesn’t backshift.'],
   'Present simple → past simple after a past reporting verb.'),
  ('Be', '“I am hungry.” → Pau said he ___ hungry.', ['was', 'is', 'has been', 'were'],
   ['‘Is’ isn’t backshifted after ‘said’.', '‘Has been’ is present perfect, not the backshifted form.', '‘He’ takes ‘was’, not ‘were’.'],
   '‘Am / is’ → ‘was’ in reported speech. This is the normal backshift of ‘be’ after a past reporting verb.'),
  ('Present continuous', '“I’m watching TV.” → She said she ___ TV.', ['was watching', 'is watching', 'had watched', 'watched'],
   ['‘Is watching’ isn’t backshifted.', '‘Had watched’ is past perfect: wrong time.', '‘Watched’ loses the continuous meaning.'],
   'Present continuous → past continuous. The action was in progress when it was said.'),
  ('Past simple', '“I met him in 2020.” → She said she ___ him in 2020.', ['had met', 'has met', 'meets', 'was meeting'],
   ['‘Has met’ is present perfect and can’t go with ‘in 2020’.', '‘Meets’ is present.', '‘Was meeting’ changes the meaning.'],
   'Past simple → past perfect: had met. The action was already finished when it was reported.'),
  ('Present perfect', '“I’ve broken my arm.” → He told me he ___ his arm.', ['had broken', 'has broken', 'broke', 'was breaking'],
   ['‘Has broken’ isn’t backshifted.', '‘Broke’ is possible in speech, but the backshift is ‘had broken’.', '‘Was breaking’ changes the meaning.'],
   'Present perfect → past perfect: had broken. The time moves one step back into the past.'),
  ('Will', '“I’ll be there at six.” → She said she ___ there at six.', ['would be', 'will be', 'was', 'had been'],
   ['‘Will’ isn’t backshifted after ‘said’.', '‘Was’ loses the future meaning.', '‘Had been’ is past perfect: wrong meaning.'],
   '‘Will’ → ‘would’ in reported speech. The future seen from the past uses ‘would’.'),
  ('Will', '“We won’t tell anyone.” → They promised they ___ anyone.', ['wouldn’t tell', 'won’t tell', 'didn’t tell', 'hadn’t told'],
   ['‘Won’t’ isn’t backshifted.', '‘Didn’t tell’ changes the time.', '‘Hadn’t told’ changes the meaning.'],
   '‘Won’t’ → ‘wouldn’t’. The future seen from the past uses ‘would’.'),
  ('Can', '“I can’t come.” → Marta said she ___ come.', ['couldn’t', 'can’t', 'wouldn’t', 'mustn’t'],
   ['‘Can’t’ isn’t backshifted.', '‘Wouldn’t’ changes the meaning.', '‘Mustn’t’ changes the meaning.'],
   '‘Can’t’ → ‘couldn’t’. Ability moves back from ‘can’ to ‘could’.'),
  ('May', '“I may be a bit late.” → He said he ___ a bit late.', ['might be', 'may be', 'can be', 'will be'],
   ['‘May’ usually becomes ‘might’ after ‘said’.', '‘Can be’ changes the meaning.', '‘Will’ changes the meaning and isn’t backshifted.'],
   '‘May’ → ‘might’. Possibility moves back from ‘may’ to ‘might’.'),
  ('Must', '“I must finish this today.” → She said she ___ finish it that day.', ['had to', 'must to', 'has to', 'musted'],
   ['No ‘to’ after ‘must’.', '‘Has to’ isn’t backshifted.', '‘Musted’ doesn’t exist.'],
   '‘Must’ (obligation) → ‘had to’ (‘must’ can also stay). Obligation in the past is expressed with ‘had to’.'),
  ('No change', '“You should see a doctor.” → My mum said I ___ see a doctor.', ['should', 'shall', 'should have', 'had to'],
   ['‘Shall’ is a different modal.', '‘Should have’ is about the past.', '‘Had to’ changes advice into obligation.'],
   '‘Should’ doesn’t change in reported speech. Some forms are already ‘back’ and can’t move further.'),
  ('No change', '“I had already left.” → He said he ___ already left.', ['had', 'has', 'had had', 'was'],
   ['‘Has’ is present perfect.', '‘Had had’ is wrong: the past perfect doesn’t move back.', '‘Was left’ is passive.'],
   'The past perfect stays the same. Some forms are already ‘back’ and can’t move further.'),
  ('Going to', '“I’m going to move to Berlin.” → She said she ___ move to Berlin.', ['was going to', 'is going to', 'will', 'had gone to'],
   ['‘Is going to’ isn’t backshifted.', '‘Will’ isn’t backshifted.', '‘Had gone to’ changes the meaning.'],
   '‘Am going to’ → ‘was going to’. Only the ‘be’ part of ‘going to’ moves back.'),
  ('Pronoun', '“I’m tired of my job.” → Joan said ___ was tired of ___ job.', ['she / her', 'I / my', 'she / my', 'her / her'],
   ['The pronouns must change to match Joan.', '‘My’ must change to ‘her’.', '‘Her’ can’t be the subject.'],
   'Change pronouns and possessives to match the speaker. The speaker is now someone else, so pronouns change.'),
  ('Negative', '“I don’t know the answer.” → He said he ___ the answer.', ['didn’t know', 'doesn’t know', 'hadn’t known', 'not knew'],
   ['‘Doesn’t know’ isn’t backshifted.', '‘Hadn’t known’ is two steps back.', 'The negative needs ‘didn’t’ + base verb.'],
   'Negative present → didn’t + base verb. The auxiliary ‘do’ moves back to ‘did’.'),
  ('Past continuous', '“I was reading.” → She said she ___ reading.', ['had been', 'was', 'has been', 'is'],
   ['‘Was’ is common in speech, but the full backshift is ‘had been’.', '‘Has been’ is present perfect.', '‘Is’ is present.'],
   'Past continuous → past perfect continuous: had been reading.'),
  ('That', 'Which sentence is correct?', ['She said that she was ill.', 'She said that she is ill yesterday.', 'She said me that she was ill.', 'She told that she was ill.'],
   ['After ‘said’ and with ‘yesterday’, backshift is needed.', '‘Said me’ is wrong.', '‘Told’ needs a person.'],
   'Reported statement: said (that) + backshifted verb. ‘That’ is optional, but the backshift is needed.'),
  ('Told', '“We’ve won!” → They told us they ___.', ['had won', 'have won', 'won', 'were winning'],
   ['‘Have won’ isn’t backshifted.', '‘Won’ is acceptable in speech, but the backshift is ‘had won’.', '‘Were winning’ changes the meaning.'],
   'Present perfect → past perfect. ‘Told’ + person works like ‘said’ for backshift.'),
  ('Will', '“It will be cold tomorrow.” → The forecast said it ___ cold the next day.', ['would be', 'will be', 'was', 'is'],
   ['‘Will’ isn’t backshifted.', '‘Was’ loses the future meaning.', '‘Is’ isn’t backshifted.'],
   '‘Will’ → ‘would’. The future seen from the past uses ‘would’.'),
  ('Present simple', '“My brother works in a bank.” → She said her brother ___ in a bank.', ['worked', 'work', 'had worked', 'was work'],
   ['‘Work’ needs to be past.', '‘Had worked’ is two steps back.', '‘Was work’ is wrong.'],
   'Present simple → past simple: worked. The original words were in the present.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('No backshift', 'Yesterday she said she *is* tired.', 'was', 'After ‘said’: ‘she was tired’.'),
  ('No backshift', 'He told me he *likes* jazz.', 'liked', 'After ‘told’: ‘he liked jazz’.'),
  ('No backshift', 'They said they *are* waiting outside.', 'were', 'After ‘said’: ‘they were waiting’.'),
  ('Will', 'She said she *will* call me later.', 'would', '‘Will’ → ‘would’.'),
  ('Will', 'He promised he *won’t* be late.', 'wouldn’t', '‘Won’t’ → ‘wouldn’t’.'),
  ('Can', 'Pau said he *can* come to the party.', 'could', '‘Can’ → ‘could’.'),
  ('Present perfect', 'She said she *has* finished her work.', 'had', 'Present perfect → past perfect: ‘had finished’.'),
  ('Past simple', 'He said he had *saw* the film twice.', 'seen', 'Past perfect needs the participle: ‘had seen’.'),
  ('Past simple', 'She told me she had *went* to Rome.', 'gone', 'Participle: ‘had gone’.'),
  ('Going to', 'They said they *are* going to move house.', 'were', '‘Are going to’ → ‘were going to’.'),
  ('Must', 'She said she had *leave* early.', 'to leave', '‘Must’ → ‘had to’: ‘she had to leave early’.'),
  ('May', 'He said he *may* be late.', 'might', '‘May’ → ‘might’.'),
  ('Pronoun', 'Marta said *I* was tired of her job.', 'she', 'Change the pronoun: ‘Marta said she was tired’.'),
  ('Possessive', 'Joan said she had lost *my* keys.', 'her', 'She lost her own keys: ‘her keys’.'),
  ('Negative', 'He said he *doesn’t* know the answer.', 'didn’t', 'Negative backshift: ‘didn’t know’.'),
  ('Negative', 'She said she didn’t *knew* him.', 'know', 'After ‘didn’t’ use the base verb: ‘know’.'),
  ('Past perfect', 'He said he had already *ate*.', 'eaten', 'Past perfect needs the participle: ‘had already eaten’.'),
  ('Said or told', 'She *said* me she was leaving.', 'told', 'Person after the verb: ‘told me’.'),
  ('Said or told', 'He *told* that he was hungry.', 'said', 'No person: ‘He said that…’.'),
  ('Continuous', 'She said she was *study* for an exam.', 'studying', 'Past continuous: ‘was studying’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, which tense, multiple choice and spot-the-mistake. In the typing questions write the backshifted verb after said / told. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('tense', 'Which tense?'),
 'fill': [
  ('Present simple', '“I speak Italian.” → He said he [[spoke]] Italian.', 'speak', 'Present simple moves back to past simple after ‘said’: spoke.', 'Present → past simple.'),
  ('Present perfect', '“I’ve lost my wallet.” → She said she [[had lost]] her wallet.', 'lose', 'Present perfect moves back to past perfect: had lost.', 'Present perfect → past perfect.'),
  ('Will', '“I’ll phone you.” → He said he [[would phone]] me.', 'phone', '‘Will’ becomes ‘would’ in reported speech.', '‘Will’ → ‘would’.'),
  ('Can', '“I can’t swim.” → She said she [[couldn’t]] swim.', 'can / could', '‘Can’t’ becomes ‘couldn’t’ after ‘said’.', '‘Can’t’ → ‘couldn’t’.'),
  ],
 'order': [
  ('Be', 'He said he was busy.', []),
  ('Past simple', 'She said she had called.', []),
  ('Will', 'They said they would wait.', []),
  ('Can', 'He said he couldn’t come.', []),
  ],
 'customItems': [
  ('Tense', '“I saw her.” In reported speech this becomes…', ['he had seen her', 'he has seen her', 'he sees her', 'he was seeing her'],
   ['‘Has seen’ is present perfect: not backshifted.', '‘Sees’ is present.', '‘Was seeing’ changes the meaning.'],
   'Past simple moves back to past perfect.'),
  ('Tense', '“I’m cooking.” In reported speech this becomes…', ['she was cooking', 'she is cooking', 'she had cooked', 'she cooked'],
   ['‘Is cooking’ isn’t backshifted.', '‘Had cooked’ changes the meaning.', '‘Cooked’ loses the continuous.'],
   'Present continuous moves back to past continuous.'),
  ('Tense', '“I’ve been to Japan.” In reported speech this becomes…', ['he had been to Japan', 'he has been to Japan', 'he was to Japan', 'he went to Japan'],
   ['‘Has been’ isn’t backshifted.', '‘Was to Japan’ is wrong.', '‘Went’ is acceptable in speech but not the full backshift.'],
   'Present perfect moves back to past perfect.'),
  ('Tense', 'Which modal does NOT change in reported speech?', ['should', 'will', 'can', 'may'],
   ['‘Will’ becomes ‘would’.', '‘Can’ becomes ‘could’.', '‘May’ becomes ‘might’.'],
   'Should, would, could, might and ought to stay the same.'),
  ],
 'mc': [
  ('Be', '“We are lost.” → They said they ___ lost.', ['were', 'are', 'was', 'had'],
   ['‘Are’ isn’t backshifted.', '‘They’ takes ‘were’.', '‘Had lost’ changes the meaning.'],
   '‘Are’ moves back to ‘were’.'),
  ('Will', '“I’ll help.” → She said she ___.', ['would help', 'will help', 'helped', 'had helped'],
   ['‘Will’ isn’t backshifted.', '‘Helped’ loses the future meaning.', '‘Had helped’ changes the meaning.'],
   '‘Will’ moves back to ‘would’.'),
  ('Must', '“I must go.” → He said he ___ go.', ['had to', 'has to', 'must to', 'musted'],
   ['‘Has to’ isn’t backshifted.', 'No ‘to’ after ‘must’.', '‘Musted’ doesn’t exist.'],
   '‘Must’ often becomes ‘had to’.'),
  ('Pronoun', '“I love my dog.” → Pau said ___ loved ___ dog.', ['he / his', 'I / my', 'he / my', 'him / his'],
   ['Pronouns must change.', '‘My’ must become ‘his’.', '‘Him’ can’t be a subject.'],
   'Change I → he, my → his.'),
  ],
 'error': [
  ('No backshift', 'She said she *lives* in Lleida.', 'lived', 'After ‘said’: ‘she lived in Lleida’.'),
  ('Will', 'He said he *will* be late.', 'would', '‘Will’ → ‘would’.'),
  ('Present perfect', 'They said they *have* finished.', 'had', 'Present perfect → past perfect.'),
  ('Said or told', 'She *said* us she was leaving.', 'told', 'Person after: ‘told us’.'),
  ],
}
