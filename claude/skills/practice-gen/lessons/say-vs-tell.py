TITLE = 'Say vs Tell'
AUX = (['said', 'told', 'say', 'tell'], None, 'told')
NEXT = ('Reported Statements & Backshift', '/grammar/reported-speech/reported-statements-backshift/')
BODY = r'''
## How to use say and tell

| Verb | Pattern | Example |
|---|---|---|
| **say** | say + (that) + words | She **said** (that) she was tired. |
| **say** | say + something + **to** someone | He **said** hello **to** me. |
| **tell** | tell + **person** + (that) + words | She **told me** (that) she was tired. |
| **tell** | tell + person + something | He **told us** a story. |

The key rule: **tell** needs a **person** straight after it. **Say** does not — if you add a person, use **to**.

| ✗ | ✓ |
|---|---|
| ~~She said me the news.~~ | She **told me** the news. / She **said** the news **to** me. |
| ~~He told that he was ill.~~ | He **said** that he was ill. / He **told us** that he was ill. |
| ~~Tell to him.~~ | **Tell him**. |

Past forms: say → **said**, tell → **told**.

## When to use *say*

### 1. Reporting words without saying who heard them

- Laia **said** she was hungry.
- The teacher **said** that the exam was easy.

> ⚠️ Typical error: ~~Laia said me she was hungry.~~ → No person after *say*: *Laia said she was hungry.*

### 2. Direct speech (quotes)

- "I'm ready," she **said**.
- He **said**, "Let's go!"

### 3. Fixed phrases with *say*

| say hello / goodbye | say sorry | say yes / no | say a word | say a prayer |
|---|---|---|---|---|

- Don't leave without **saying goodbye**.

## When to use *tell*

### 1. Reporting to a specific person

- She **told me** she was hungry.
- **Tell your mum** I'll be late.

> ⚠️ Typical error: ~~She told she was hungry.~~ → *Tell* needs a person: *She told me she was hungry.*

### 2. Instructions and orders: *tell* + person + *to*

- The teacher **told us to** sit down.
- **Tell him not to** worry.

See [Reported Commands & Requests](/grammar/reported-speech/reported-commands-requests/).

### 3. Fixed phrases with *tell*

| tell the truth | tell a lie | tell a story | tell a joke | tell the time | tell the difference |
|---|---|---|---|---|---|

- He always **tells the truth**. (no person needed in these phrases)

> ⚠️ Typical error: ~~She said a lie.~~ → *She told a lie.*

## *Say* + *to* vs *tell*

Both are correct, but *tell* is much more common.

- She **said to me** that she was tired. (correct, less common)
- She **told me** that she was tired. (more natural)

## Questions

| Question | Note |
|---|---|
| What did she **say**? | no person |
| What did she **tell** you? | person after *tell* |

## Common mistakes

**1. Person after *say*.** *~~He said me~~* → **He told me** / **He said to me**.

**2. No person after *tell*.** *~~She told that…~~* → **She said that…** / **She told me that…**

**3. *Tell to* + person.** *~~Tell to Pau~~* → **Tell Pau.**

**4. Wrong fixed phrase.** *~~say the truth, tell hello~~* → **tell the truth, say hello.**

**Pro tip:** ask "Who heard it?" If you name the person, use **tell** — *tell someone something*.
'''

GAP = ('Fill in the gaps',
  'Type say, says, said, tell, tells or told. Remember: tell + person; say + words (or say + to + person). Twenty original sentences.',
  [
  ('Say', 'Laia [[said]] that she was tired after the trip.', 'said / told', 'No person after the verb, so use ‘said’ + (that) + the words.'),
  ('Tell', 'Laia [[told]] me that she was tired after the trip.', 'said / told', 'A person (me) comes straight after the verb, so use ‘told’.'),
  ('Say', 'The weather forecast [[said]] it would rain all weekend.', 'said / told', 'No person follows, so the verb is ‘said’.'),
  ('Tell', 'Can you [[tell]] me the way to the station?', 'say / tell', '‘Me’ comes right after the verb, so use ‘tell’.'),
  ('Tell', 'Please [[tell]] your parents about the trip.', 'say / tell', 'A person (your parents) follows directly: tell.'),
  ('Say', 'What did he [[say]]? I couldn’t hear him.', 'say / tell', 'No person after the verb in this question: say.'),
  ('Tell', 'What did the doctor [[tell]] you?', 'say / tell', 'A person (you) follows: tell.'),
  ('Say to', 'She said goodbye [[to]] everyone and left.', 'to / —', '‘Say’ + something + to + person.'),
  ('Say', '“I’m ready,” Marc [[said]].', 'said / told', 'Direct speech (quotes) normally uses ‘said’.'),
  ('Tell', 'My grandpa [[tells]] us a story every night.', 'says / tells', 'Present simple with ‘he’: tells + person + a story.'),
  ('Say', 'My dad always [[says]] that I should read more.', 'says / tells', 'Present simple with ‘he’, no person: says.'),
  ('Fixed phrase', 'You should always [[tell]] the truth.', 'say / tell', 'Fixed phrase: tell the truth.'),
  ('Fixed phrase', 'He [[told]] a lie to get out of trouble.', 'said / told', 'Fixed phrase: tell a lie → told a lie.'),
  ('Fixed phrase', 'Don’t forget to [[say]] thank you to your aunt.', 'say / tell', 'Fixed phrase: say thank you.'),
  ('Fixed phrase', 'Can you [[tell]] the difference between these two photos?', 'say / tell', 'Fixed phrase: tell the difference.'),
  ('Fixed phrase', 'She [[said]] sorry for being late.', 'said / told', 'Fixed phrase: say sorry → said sorry.'),
  ('Instructions', 'The teacher [[told]] us to open our books.', 'said / told', 'Instruction: tell + person + to + verb.'),
  ('Instructions', 'Mum [[told]] me not to stay up late.', 'said / told', 'Negative instruction: told + person + not to.'),
  ('Fixed phrase', 'My little brother can’t [[tell]] the time yet.', 'say / tell', 'Fixed phrase: tell the time.'),
  ('Fixed phrase', 'Everybody laughed when he [[told]] a joke.', 'said / told', 'Fixed phrase: tell a joke.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with say and tell.',
  [
  ('Say', 'She said she was tired.', []),
  ('Tell', 'She told me she was tired.', []),
  ('Say', 'He said that the film was great.', []),
  ('Tell', 'He told us that the film was great.', []),
  ('Say to', 'She said hello to me.', []),
  ('Tell', 'Tell me the truth.', []),
  ('Tell', 'Can you tell me the time?', []),
  ('Say', 'What did you say?', []),
  ('Tell', 'What did he tell you?', []),
  ('Say', '“I’m hungry,” she said.', []),
  ('Fixed phrase', 'He always tells jokes.', []),
  ('Fixed phrase', 'Don’t tell lies.', []),
  ('Fixed phrase', 'I said goodbye to my friends.', []),
  ('Fixed phrase', 'She said sorry to her brother.', []),
  ('Fixed phrase', 'I can’t tell the difference.', []),
  ('Instructions', 'The coach told us to run.', []),
  ('Instructions', 'Mum told me not to worry.', []),
  ('Tell', 'Please tell your sister.', []),
  ('Say', 'My dad says I’m lazy.', []),
  ('Tell', 'Grandma tells us stories.', []),
  ])

MATCH = {'title': 'Say or tell?', 'subtitle': 'Tap a phrase, then tap the verb it needs.',
  'leftLabel': 'Phrase', 'rightLabel': 'Verb', 'rightLabelSub': '(say / tell)', 'reviewArrowPrefix': '',
  'pairs': [
  ('___ the truth', 'tell'), ('___ hello', 'say'), ('___ a lie', 'tell'), ('___ goodbye', 'say'), ('___ a story', 'tell'),
  ('___ sorry', 'say'), ('___ a joke', 'tell'), ('___ yes', 'say'), ('___ me the news', 'tell'), ('___ thank you', 'say'),
  ('___ the time', 'tell'), ('___ a prayer', 'say'), ('___ the difference', 'tell'), ('___ no', 'say'), ('___ us a secret', 'tell'),
  ('___ something to her', 'say'), ('___ him to wait', 'tell'), ('___ a word', 'say'), ('___ your mum', 'tell'), ('___ that it’s late', 'say'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Tell + person; say + words (or say + to + person) — and learn the fixed phrases.',
  [
  ('Tell', 'She ___ me she was moving to London.', ['told', 'said', 'says', 'tells to'],
   ['‘Said’ can’t be followed directly by a person like ‘me’.', '‘Says me’ has the same problem — and it’s present, not past.', '‘Tell to me’ is wrong: ‘tell’ takes the person directly.'],
   'A person comes straight after the verb, so ‘tell’ (past: told) is needed.'),
  ('Say', 'She ___ she was moving to London.', ['said', 'told', 'tells', 'told to'],
   ['‘Told’ needs a person after it: ‘told me / us’.', '‘Tells’ is present and still needs a person.', '‘Told to’ is used for instructions, not reported statements.'],
   'No person after the verb, so ‘say’ (past: said) is right.'),
  ('Say to', 'He said goodbye ___ his classmates.', ['to', 'at', '—', 'for'],
   ['‘Say goodbye at’ is wrong: the person needs ‘to’.', 'After ‘say + something’, a person needs ‘to’.', '‘For’ doesn’t introduce the listener.'],
   'With ‘say’, put ‘to’ before the person who hears the words.'),
  ('Fixed phrase', 'Always ___ the truth, even when it’s difficult.', ['tell', 'say', 'speak', 'talk'],
   ['‘Say the truth’ is a very common mistake: the fixed phrase uses ‘tell’.', '‘Speak the truth’ is old-fashioned or literary.', '‘Talk the truth’ is wrong.'],
   'The fixed phrase is ‘tell the truth’.'),
  ('Fixed phrase', 'Don’t forget to ___ thank you to Grandma.', ['say', 'tell', 'speak', 'talk'],
   ['‘Tell thank you’ is wrong: the fixed phrase uses ‘say’.', '‘Speak thank you’ is wrong.', '‘Talk thank you’ is wrong.'],
   'The fixed phrase is ‘say thank you’ (also say hello, goodbye, sorry).'),
  ('Fixed phrase', 'My uncle loves ___ jokes at dinner.', ['telling', 'saying', 'speaking', 'talking'],
   ['‘Saying jokes’ is a common mistake: the phrase is ‘tell jokes’.', '‘Speaking jokes’ is wrong.', '‘Talking jokes’ is wrong.'],
   'The fixed phrase is ‘tell a joke / tell jokes’.'),
  ('Question', 'What did the teacher ___ about the exam?', ['say', 'tell', 'told', 'said'],
   ['‘Tell’ needs a person: ‘tell you about…’.', 'After ‘did’ use the base form, and ‘tell’ needs a person.', 'After ‘did’ use the base form ‘say’, not ‘said’.'],
   'No person in the question, and after ‘did’ the base form: say.'),
  ('Question', 'What did the teacher ___ you about the exam?', ['tell', 'say', 'told', 'said'],
   ['‘Say you’ is wrong: ‘say’ can’t take a person directly.', 'After ‘did’ use the base form ‘tell’.', 'After ‘did’ use the base form.'],
   'A person (you) follows, and after ‘did’ the base form: tell.'),
  ('Instructions', 'The coach ___ us to warm up before the match.', ['told', 'said', 'said to', 'tell'],
   ['‘Said us to’ is wrong: ‘say’ can’t take a person directly.', '‘Said to us to warm up’ is very unnatural.', '‘Tell’ is present; the coach spoke in the past.'],
   'Instructions: tell + person + to + verb.'),
  ('Direct speech', '“We’re going to win,” the captain ___.', ['said', 'told', 'told us', 'tells to'],
   ['‘Told’ needs a person, and direct speech normally uses ‘said’.', 'Possible, but ‘said’ is the normal verb after a quote.', '‘Tells to’ is wrong.'],
   'After a direct quote, ‘said’ is the usual verb.'),
  ('Tell', 'Can you ___ me how to get to the museum?', ['tell', 'say', 'say to', 'speak'],
   ['‘Say me’ is wrong.', '‘Say to me how’ is very unnatural.', '‘Speak me’ is wrong.'],
   '‘Tell me’ = give me information.'),
  ('Say', 'My mum always ___ that breakfast is important.', ['says', 'tells', 'tell', 'say'],
   ['‘Tells’ needs a person after it.', '‘Tell’ needs a person and an -s here.', '‘Say’ needs -s with ‘my mum’.'],
   'No person, third person present: says.'),
  ('Fixed phrase', 'She was upset, so I ___ sorry.', ['said', 'told', 'spoke', 'talked'],
   ['‘Told sorry’ is wrong.', '‘Spoke sorry’ is wrong.', '‘Talked sorry’ is wrong.'],
   'Fixed phrase: say sorry → said sorry.'),
  ('Fixed phrase', 'He ___ a lie and got into trouble.', ['told', 'said', 'spoke', 'did'],
   ['‘Said a lie’ is a common mistake.', '‘Spoke a lie’ is wrong.', '‘Did a lie’ is wrong.'],
   'Fixed phrase: tell a lie → told a lie.'),
  ('Tell to', 'Which sentence is correct?', ['Tell Joan I’ll call her.', 'Tell to Joan I’ll call her.', 'Say Joan I’ll call her.', 'Say to Joan that I’ll call her tell.'],
   ['No ‘to’ after ‘tell’.', '‘Say’ can’t take a person directly.', 'This makes no sense.'],
   '‘Tell’ + person directly: Tell Joan…'),
  ('Said me', 'Which sentence is correct?', ['He told me the news.', 'He said me the news.', 'He told to me the news.', 'He said the news me.'],
   ['‘Said me’ is wrong.', 'No ‘to’ after ‘told’.', 'Wrong word order.'],
   '‘Tell’ + person + thing: told me the news.'),
  ('Fixed phrase', 'I can’t ___ the difference between the twins.', ['tell', 'say', 'speak', 'talk'],
   ['‘Say the difference’ is wrong.', '‘Speak the difference’ is wrong.', '‘Talk the difference’ is wrong.'],
   'Fixed phrase: tell the difference.'),
  ('Say', 'It ___ on the sign that the shop opens at ten.', ['says', 'tells', 'tell', 'said to'],
   ['‘Tells’ would need a person.', '‘Tell’ needs -s and a person.', '‘Said to’ is wrong here.'],
   'Signs and texts ‘say’ something.'),
  ('Tell', 'I ___ Pau about the party, but he forgot.', ['told', 'said', 'said to', 'tell'],
   ['‘Said Pau’ is wrong.', '‘Said to Pau about the party’ is unnatural.', '‘Tell’ is present; this is past.'],
   'Person directly after the verb: told Pau.'),
  ('Fixed phrase', 'Grandma ___ us a story every night.', ['tells', 'says', 'says to', 'speaks'],
   ['‘Says us’ is wrong.', '‘Says to us a story’ is wrong.', '‘Speaks us’ is wrong.'],
   'Tell + person + a story.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('Person after say', 'She *said* me that she was ill.', 'told', 'A person follows: ‘She told me…’.'),
  ('Person after say', 'He *said* us the answer.', 'told', 'A person follows: ‘He told us the answer’.'),
  ('Person after say', 'Can you *say* me the time?', 'tell', 'A person follows: ‘Can you tell me the time?’.'),
  ('No person after tell', 'She *told* that she was ill.', 'said', 'No person follows: ‘She said that…’.'),
  ('No person after tell', 'He *told* he was going home.', 'said', 'No person follows: ‘He said he was going home’.'),
  ('Person after say', 'Please *say* your brother about the party.', 'tell', 'A person follows: ‘tell your brother’.'),
  ('Missing to after say', 'She said goodbye *her* friends.', 'to her', 'Say + something + to + person: ‘goodbye to her friends’.'),
  ('Fixed phrase', 'You must *say* the truth.', 'tell', 'Fixed phrase: ‘tell the truth’.'),
  ('Fixed phrase', 'He *said* a funny joke.', 'told', 'Fixed phrase: ‘tell a joke’.'),
  ('Fixed phrase', 'Don’t *say* lies!', 'tell', 'Fixed phrase: ‘tell lies’.'),
  ('Fixed phrase', 'I *told* hello to the new student.', 'said', 'Fixed phrase: ‘say hello’.'),
  ('Fixed phrase', 'She *told* sorry to her sister.', 'said', 'Fixed phrase: ‘say sorry’.'),
  ('Fixed phrase', 'He can’t *say* the time yet.', 'tell', 'Fixed phrase: ‘tell the time’.'),
  ('Wrong form', 'Yesterday she *telled* me a secret.', 'told', 'Past of ‘tell’: ‘told’.'),
  ('Wrong form', 'He *sayed* he was sorry.', 'said', 'Past of ‘say’: ‘said’.'),
  ('After did', 'What did she *said*?', 'say', 'After ‘did’ use the base form: ‘say’.'),
  ('After did', 'What did he *told* you?', 'tell', 'After ‘did’ use the base form: ‘tell’.'),
  ('Instructions', 'The teacher *said* us to be quiet.', 'told', 'Instruction: ‘told us to be quiet’.'),
  ('Third person', 'My dad always *say* I’m lazy.', 'says', '‘My dad’ needs -s: ‘says’.'),
  ('Third person', 'Grandma *tell* us stories.', 'tells', '‘Grandma’ needs -s: ‘tells’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, fixed phrases, multiple choice and spot-the-mistake. In the typing questions write the right form of say or tell. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('phrase', 'Fixed phrases'),
 'fill': [
  ('Tell', 'He [[told]] us he was leaving.', 'said / told', 'A person (us) follows directly, so the past of ‘tell’: told.', 'Person after → ‘told’.'),
  ('Say', 'He [[said]] he was leaving.', 'said / told', 'No person after the verb, so the past of ‘say’: said.', 'No person → ‘said’.'),
  ('Fixed phrase', 'Don’t [[tell]] lies to your friends.', 'say / tell', 'The fixed phrase is ‘tell lies’, never ‘say lies’.', 'Lies → ‘tell’.'),
  ('Fixed phrase', 'We [[said]] goodbye at the station.', 'said / told', 'The fixed phrase is ‘say goodbye’ → said goodbye.', 'Goodbye → ‘say’.'),
  ],
 'order': [
  ('Tell', 'She told me a secret.', []),
  ('Say', 'He said he was sorry.', []),
  ('Say to', 'I said hello to her.', []),
  ('Instructions', 'Mum told us to hurry.', []),
  ],
 'customItems': [
  ('Phrase', 'Which goes with ‘tell’?', ['a story', 'hello', 'sorry', 'goodbye'],
   ['‘Hello’ goes with ‘say’.', '‘Sorry’ goes with ‘say’.', '‘Goodbye’ goes with ‘say’.'],
   'tell a story, tell a joke, tell a lie, tell the truth.'),
  ('Phrase', 'Which goes with ‘say’?', ['thank you', 'the truth', 'a joke', 'the time'],
   ['‘The truth’ goes with ‘tell’.', '‘A joke’ goes with ‘tell’.', '‘The time’ goes with ‘tell’.'],
   'say thank you, say hello, say sorry, say yes / no.'),
  ('Phrase', 'Grandpa can ___ the difference between real and fake coins.', ['tell', 'say', 'speak', 'talk'],
   ['‘Say the difference’ is wrong.', '‘Speak the difference’ is wrong.', '‘Talk the difference’ is wrong.'],
   'Fixed phrase: tell the difference.'),
  ('Phrase', 'Before you go, ___ goodbye to everyone.', ['say', 'tell', 'speak', 'talk'],
   ['‘Tell goodbye’ is wrong.', '‘Speak goodbye’ is wrong.', '‘Talk goodbye’ is wrong.'],
   'Fixed phrase: say goodbye.'),
  ],
 'mc': [
  ('Tell', 'Can you ___ me your phone number?', ['tell', 'say', 'say to', 'told'],
   ['‘Say me’ is wrong.', '‘Say to me your number’ is unnatural.', 'After ‘can’ use the base form.'],
   'Person after the verb → tell.'),
  ('Question', 'What did your mum ___?', ['say', 'tell', 'said', 'told'],
   ['‘Tell’ needs a person.', 'After ‘did’ use the base form.', 'After ‘did’ use the base form.'],
   'No person, after ‘did’: say.'),
  ('Instructions', 'The doctor ___ me to rest for a week.', ['told', 'said', 'said to', 'tells'],
   ['‘Said me to’ is wrong.', '‘Said to me to rest’ is unnatural.', 'This happened in the past.'],
   'Instructions: told + person + to.'),
  ('Say to', 'She said something ___ me, but I didn’t hear it.', ['to', 'at', 'for', '—'],
   ['‘Say at me’ is wrong.', '‘Say for me’ changes the meaning.', 'With ‘say’, the person needs ‘to’.'],
   'Say + something + to + person.'),
  ],
 'error': [
  ('Person after say', 'He *said* me a secret.', 'told', 'A person follows: ‘He told me a secret’.'),
  ('No person after tell', 'She *told* it was late.', 'said', 'No person: ‘She said it was late’.'),
  ('Fixed phrase', 'Please *say* the truth.', 'tell', 'Fixed phrase: ‘tell the truth’.'),
  ('After did', 'What did you *told* her?', 'tell', 'After ‘did’: ‘tell’.'),
  ],
}
