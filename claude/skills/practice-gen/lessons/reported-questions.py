TITLE = 'Reported Questions'
AUX = (['asked', 'if', 'whether', 'where', 'what'], None, 'asked')
NEXT = ('Reported Commands & Requests', '/grammar/reported-speech/reported-commands-requests/')
BODY = r'''
## How to report a question

| Type | Direct question | Reported question |
|---|---|---|
| Yes/No | "**Are you** tired?" | She asked **if / whether I was** tired. |
| Wh- | "**Where do you** live?" | He asked **where I lived**. |

Two big changes:

1. The word order becomes a **statement**: subject + verb. No *do / does / did*, no question mark.
2. The tense **moves back** after *asked*, like reported statements.

| ✗ | ✓ |
|---|---|
| ~~She asked where did I live.~~ | She asked where **I lived**. |
| ~~He asked was I tired?~~ | He asked **if I was** tired. |
| ~~They asked what time is it.~~ | They asked what time **it was**. |

## Yes/No questions: *if* or *whether*

Use **if** or **whether** (more formal). Both mean the same.

- "**Do you** like sushi?" → She asked **if I liked** sushi.
- "**Have you** finished?" → He asked **whether I had** finished.
- "**Can you** swim?" → They asked **if I could** swim.

> ⚠️ Typical error: ~~She asked do I like sushi.~~ → No *do*, add *if*: *She asked if I liked sushi.*

## Wh- questions: keep the question word

- "**What** are you doing?" → He asked **what I was doing**.
- "**When** does the film start?" → She asked **when the film started**.
- "**Why** did you leave?" → They asked **why I had left**.

> ⚠️ Typical error: ~~He asked what was I doing.~~ → Statement order: *what I was doing.*

### Question word as the subject

If *who / what* is the **subject**, the order doesn't change.

- "**Who** broke the window?" → She asked **who had broken** the window.
- "**What** happened?" → He asked **what had happened**.

## Reporting verbs for questions

| Verb | Pattern | Example |
|---|---|---|
| ask | ask + (person) + if / wh- | She **asked me** where I lived. |
| want to know | want to know + if / wh- | He **wanted to know** if I was OK. |
| wonder | wonder + if / wh- | I **wondered** why she was late. |

> ⚠️ Typical error: ~~She asked to me where I lived.~~ → No *to*: *She asked me…*

## Tense and other changes

### Backshift, pronouns, time and place

The usual changes apply: tense, pronouns, time and place.

- "**Will you** come **tomorrow**?" → She asked if I **would** come **the next day**.
- "Where **is your** car?" → He asked where **my** car **was**.

## No question mark

A reported question is a statement — finish with a **full stop**.

- He asked where I lived**.** (not ~~lived?~~)

## Common mistakes

**1. Question word order.** *~~She asked where was the station~~* → **She asked where the station was.**

**2. Keeping *do / did*.** *~~He asked what did I want~~* → **He asked what I wanted.**

**3. Missing *if* in yes/no questions.** *~~She asked I was hungry~~* → **She asked if I was hungry.**

**4. Question mark at the end.** Reported questions end with a full stop.

**Pro tip:** after *asked*, write it like a normal sentence — subject first, then verb.
'''

GAP = ('Fill in the gaps',
  'Type the missing part of the reported question: if / whether, the question word, or the verb in statement order with backshift. Twenty original sentences.',
  [
  ('Yes/No', '“Are you tired?” → She asked [[if|whether]] I was tired.', 'if / that', 'A yes/no question is reported with ‘if’ or ‘whether’.'),
  ('Yes/No', '“Do you like pizza?” → He asked if I [[liked]] pizza.', '(like)', 'No ‘do’ in reported questions; present simple moves back: liked.'),
  ('Yes/No', '“Can you help me?” → She asked if I [[could]] help her.', 'can / could', '‘Can’ moves back to ‘could’ after ‘asked’.'),
  ('Yes/No', '“Have you finished?” → The teacher asked whether we [[had finished]].', '(finish)', 'Present perfect moves back to past perfect: had finished.'),
  ('Yes/No', '“Will you come tomorrow?” → He asked if I [[would come]] the next day.', '(come)', '‘Will’ moves back to ‘would’.'),
  ('Yes/No', '“Is it raining?” → She asked if it [[was raining]].', '(rain)', 'Present continuous moves back: was raining.'),
  ('Wh-', '“Where do you live?” → He asked where I [[lived]].', '(live)', 'Statement order (I lived) and backshift; no ‘do’.'),
  ('Wh-', '“What are you doing?” → She asked what I [[was doing]].', '(do)', 'Statement order: subject + was doing.'),
  ('Wh-', '“When does the film start?” → He asked when the film [[started]].', '(start)', 'No ‘does’; the subject comes first: the film started.'),
  ('Wh-', '“Why did you leave?” → They asked why I [[had left]].', '(leave)', 'Past simple moves back to past perfect: had left.'),
  ('Wh-', '“How old are you?” → She asked how old I [[was]].', '(be)', 'Statement order: how old I was.'),
  ('Wh-', '“Where is the station?” → A tourist asked me where the station [[was]].', '(be)', 'The verb goes after the subject: the station was.'),
  ('Wh-', '“What time is it?” → He asked what time it [[was]].', '(be)', 'Statement order and backshift: it was.'),
  ('Question word', '“[[Who]] broke the window?” → She asked who had broken the window.', 'who / what', '‘Who’ is the subject here, so the order stays the same.'),
  ('Question word', '“What happened?” → He asked what [[had happened]].', '(happen)', '‘What’ is the subject: no inversion; past simple → past perfect.'),
  ('Reporting verb', 'She [[asked]] me where I had bought my jacket.', 'asked / said', 'Questions are reported with ‘ask’ (+ person).'),
  ('Reporting verb', 'He wanted to [[know]] if the shop was open.', 'know / ask', 'Another reporting phrase for questions: wanted to know.'),
  ('Reporting verb', 'I [[wondered]] why she hadn’t called.', 'wondered / asked to', '‘Wonder’ can report a question you ask yourself.'),
  ('Pronoun', '“Is this your bag?” → She asked if it was [[my]] bag.', '(your)', 'She was speaking to me, so ‘your’ becomes ‘my’.'),
  ('Whether', '“Do you want tea or coffee?” → He asked [[whether]] I wanted tea or coffee.', 'whether / that', '‘Whether’ is common with a choice: tea or coffee.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each reported question — statement order, no question mark.',
  [
  ('Yes/No', 'She asked if I was tired.', []),
  ('Yes/No', 'He asked if I liked jazz.', []),
  ('Yes/No', 'She asked whether I had finished.', []),
  ('Yes/No', 'He asked if I could swim.', []),
  ('Yes/No', 'They asked if we would come.', []),
  ('Yes/No', 'She asked if it was raining.', []),
  ('Wh-', 'He asked where I lived.', []),
  ('Wh-', 'She asked what I was doing.', []),
  ('Wh-', 'He asked when the film started.', []),
  ('Wh-', 'They asked why I had left.', []),
  ('Wh-', 'She asked how old I was.', []),
  ('Wh-', 'He asked where the station was.', []),
  ('Wh-', 'She asked what time it was.', []),
  ('Question word', 'He asked who had called.', []),
  ('Question word', 'She asked what had happened.', []),
  ('Reporting verb', 'He wanted to know where I worked.', []),
  ('Reporting verb', 'I wondered if she was OK.', []),
  ('Pronoun', 'She asked if it was my coat.', []),
  ('Whether', 'He asked whether I wanted tea.', []),
  ('Ask + person', 'She asked me how I was.', []),
  ])

MATCH = {'title': 'Match the direct and reported question', 'subtitle': 'Tap a direct question, then tap its reported version.',
  'leftLabel': 'Direct question', 'rightLabel': 'Reported', 'rightLabelSub': '(asked…)', 'reviewArrowPrefix': '',
  'pairs': [
  ('“Are you hungry?”', 'She asked if I was hungry.'), ('“Where do you live?”', 'She asked where I lived.'), ('“Can you drive?”', 'She asked if I could drive.'),
  ('“What are you doing?”', 'She asked what I was doing.'), ('“Have you eaten?”', 'She asked if I had eaten.'), ('“Why did you leave?”', 'She asked why I had left.'),
  ('“Will you help me?”', 'She asked if I would help her.'), ('“How old are you?”', 'She asked how old I was.'), ('“Do you like cats?”', 'She asked if I liked cats.'),
  ('“When does it start?”', 'She asked when it started.'), ('“Who called?”', 'She asked who had called.'), ('“Is it cold?”', 'She asked if it was cold.'),
  ('“What happened?”', 'She asked what had happened.'), ('“Where is the bank?”', 'She asked where the bank was.'), ('“Did you see it?”', 'She asked if I had seen it.'),
  ('“How do you feel?”', 'She asked how I felt.'), ('“Are you coming?”', 'She asked if I was coming.'), ('“What time is it?”', 'She asked what time it was.'),
  ('“Can I sit here?”', 'She asked if she could sit there.'), ('“Which bus goes to Girona?”', 'She asked which bus went to Girona.'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Statement order, no do / does / did, if or whether for yes/no questions, and backshift.',
  [
  ('Yes/No', '“Are you OK?” → She asked ___ OK.', ['if I was', 'was I', 'if was I', 'that I was'],
   ['Reported questions use statement order, not question order.', 'After ‘if’ the subject comes first: ‘if I was’.', '‘That’ is for statements; a yes/no question needs ‘if’ or ‘whether’.'],
   'Yes/No question: asked + if + subject + verb. Remember: statement order and backshift after ‘asked’.'),
  ('Wh-', '“Where do you work?” → He asked where ___.', ['I worked', 'did I work', 'do I work', 'I did work'],
   ['‘Did’ disappears in a reported question.', 'Question order and no backshift.', '‘I did work’ is emphatic and wrong here.'],
   'Wh- question: question word + subject + backshifted verb.'),
  ('Wh-', '“What are you reading?” → She asked what ___.', ['I was reading', 'was I reading', 'I am reading', 'am I reading'],
   ['Question order is wrong in reported speech.', 'No backshift after ‘asked’.', 'Question order and no backshift.'],
   'Statement order + backshift: I was reading. Remember: statement order and backshift after ‘asked’.'),
  ('Yes/No', '“Do you speak French?” → He asked ___ French.', ['if I spoke', 'do I speak', 'if did I speak', 'that I spoke'],
   ['Question order and ‘do’ are wrong here.', '‘Did’ disappears in reported questions.', '‘That’ is for statements.'],
   'No ‘do’; if + subject + past simple. Remember: statement order and backshift after ‘asked’.'),
  ('Wh-', '“When did you arrive?” → They asked when ___.', ['I had arrived', 'did I arrive', 'I did arrive', 'had I arrived'],
   ['‘Did’ disappears and the order changes.', 'Emphatic and wrong.', 'Question order is wrong.'],
   'Past simple → past perfect, statement order. Remember: statement order and backshift after ‘asked’.'),
  ('Wh-', '“Where is the museum?” → A tourist asked me where the museum ___.', ['was', 'is', 'was it', 'did be'],
   ['After ‘asked’, backshift: ‘was’.', '‘Was it’ is question order.', '‘Did be’ is impossible.'],
   'Statement order: the museum was. Remember: statement order and backshift after ‘asked’.'),
  ('Question word', '“Who ate my sandwich?” → He asked who ___ his sandwich.', ['had eaten', 'did eat', 'ate did', 'has eaten'],
   ['‘Did’ disappears.', 'Wrong order.', 'Present perfect isn’t backshifted.'],
   '‘Who’ is the subject: no inversion; past → past perfect.'),
  ('If or that', 'Which word introduces a reported yes/no question?', ['if', 'that', 'what', 'so'],
   ['‘That’ introduces statements.', '‘What’ is for wh- questions.', '‘So’ shows a result.'],
   'Yes/No questions: if or whether. Remember: statement order and backshift after ‘asked’.'),
  ('Whether', '“Do you want pasta or rice?” → He asked ___ I wanted pasta or rice.', ['whether', 'that', 'what', 'which'],
   ['‘That’ is for statements.', '‘What I wanted pasta’ is wrong.', '‘Which I wanted pasta’ is wrong.'],
   '‘Whether’ is common with a choice of two. Remember: statement order and backshift after ‘asked’.'),
  ('Will', '“Will you be at the party?” → She asked if I ___ at the party.', ['would be', 'will be', 'was being', 'had been'],
   ['‘Will’ isn’t backshifted after ‘asked’.', 'Changes the meaning.', 'Changes the meaning.'],
   '‘Will’ → ‘would’. Remember: statement order and backshift after ‘asked’.'),
  ('Can', '“Can you lend me a pen?” → He asked if I ___ lend him a pen.', ['could', 'can', 'would can', 'could to'],
   ['‘Can’ isn’t backshifted.', 'Two modals can’t go together.', 'No ‘to’ after ‘could’.'],
   '‘Can’ → ‘could’. Remember: statement order and backshift after ‘asked’.'),
  ('Reporting verb', 'She ___ me if I had seen her keys.', ['asked', 'said', 'told', 'asked to'],
   ['‘Said me’ is wrong, and questions use ‘ask’.', '‘Told me if’ is wrong for questions.', 'No ‘to’ after ‘asked’ before a person.'],
   'Report questions with ‘ask’ + person. Remember: statement order and backshift after ‘asked’.'),
  ('Reporting verb', 'He wanted ___ where the toilets were.', ['to know', 'know', 'knowing', 'to knew'],
   ['‘Want’ needs ‘to’.', '‘Wanted knowing’ is wrong.', 'After ‘to’ use the base verb.'],
   'Wanted to know + wh- clause. Remember: statement order and backshift after ‘asked’.'),
  ('Wh-', '“Where have you been?” → Dad asked where I ___.', ['had been', 'have been', 'had I been', 'was been'],
   ['After ‘asked’ the present perfect moves back to the past perfect.', 'Question order is wrong in a reported question.', '‘Was been’ is not a correct form.'],
   'Present perfect → past perfect, in statement order: where I had been.'),
  ('Pronoun', '“Is this your phone?” → He asked if it was ___ phone.', ['my', 'your', 'his', 'our'],
   ['He was speaking to me, so it changes to ‘my’.', 'Only if it was his own phone.', 'Changes the meaning.'],
   '‘Your’ → ‘my’ when the question was to me. Remember: statement order and backshift after ‘asked’.'),
  ('Wh-', '“How much does it cost?” → She asked how much it ___.', ['cost', 'does cost', 'did cost', 'costs did'],
   ['‘Does’ disappears.', '‘Did’ disappears.', 'Wrong order.'],
   'Statement order + backshift: it cost (past of cost). Remember: statement order and backshift after ‘asked’.'),
  ('Wh-', '“Why are you crying?” → Mum asked why I ___.', ['was crying', 'am crying', 'was I crying', 'did cry'],
   ['No backshift.', 'Question order.', 'Wrong structure.'],
   'Statement order + backshift: I was crying. Remember: statement order and backshift after ‘asked’.'),
  ('Yes/No', '“Have you ever been to London?” → She asked if I ___ to London.', ['had ever been', 'have ever been', 'had ever went', 'was ever'],
   ['No backshift.', '‘Went’ is not the participle.', '‘Was ever’ is wrong.'],
   'Present perfect → past perfect. Remember: statement order and backshift after ‘asked’.'),
  ('Wh-', '“Which bus goes to the beach?” → He asked which bus ___ to the beach.', ['went', 'did go', 'goes did', 'does go'],
   ['‘Did’ disappears.', 'Wrong order.', '‘Does’ disappears.'],
   '‘Which bus’ is the subject: which bus went. Remember: statement order and backshift after ‘asked’.'),
  ('Ask + to', 'Which sentence is correct?', ['She asked me where I lived.', 'She asked to me where I lived.', 'She asked me where did I live.', 'She said me where I lived.'],
   ['No ‘to’ after ‘asked’.', 'Question order is wrong.', '‘Said me’ is wrong.'],
   'Ask + person (no ‘to’) + wh- + statement order. Remember: statement order and backshift after ‘asked’.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('Do in reported question', 'He asked when I *did arrive*.', 'had arrived', 'No ‘did’ and backshift: ‘when I had arrived’.'),
  ('Do in reported question', 'He asked what I *did want*.', 'wanted', 'No ‘did’: ‘He asked what I wanted’. Remember: statement order and backshift after ‘asked’.'),
  ('Backshift', 'Last week a tourist asked me where the station *is*.', 'was', 'After ‘asked’, backshift: ‘where the station was’.'),
  ('Backshift', 'Yesterday he asked where I *live*.', 'lived', 'After ‘asked’: ‘where I lived’. Remember: statement order and backshift after ‘asked’.'),
  ('Backshift', 'She asked if I *am* hungry.', 'was', 'After ‘asked’: ‘if I was hungry’. Remember: statement order and backshift after ‘asked’.'),
  ('Backshift', 'He asked if I *will* come.', 'would', '‘Will’ → ‘would’. Remember: statement order and backshift after ‘asked’.'),
  ('Backshift', 'They asked if I *can* swim.', 'could', '‘Can’ → ‘could’. Remember: statement order and backshift after ‘asked’.'),
  ('Backshift', 'She asked why I *have* left early.', 'had', 'Present perfect → past perfect: ‘had left’.'),
  ('If or that', 'He asked *that* I was ready.', 'if', 'Yes/No question: ‘asked if I was ready’.'),
  ('If or that', 'She wanted to know *that* I liked jazz.', 'if', 'Yes/No question: ‘if I liked jazz’. Remember: statement order and backshift after ‘asked’.'),
  ('Wrong verb', 'She *wondered* me where I worked.', 'asked', '‘Wonder’ can’t take a person: ‘She asked me…’.'),
  ('Said or asked', 'He *said* me if I was OK.', 'asked', 'Questions use ‘ask’: ‘He asked me if…’. Remember: statement order and backshift after ‘asked’.'),
  ('Said or asked', 'She *told* me where I lived.', 'asked', 'It was a question: ‘She asked me where I lived’.'),
  ('Pronoun', '“Is this your book?” → She asked if it was *your* book.', 'my', 'She asked me, so ‘my book’. Remember: statement order and backshift after ‘asked’.'),
  ('Wrong question word', '“Where do you live?” → He asked *what* I lived.', 'where', 'Keep the question word: ‘where I lived’.'),
  ('Past participle', 'She asked if I had *saw* the film.', 'seen', 'Participle: ‘had seen’. Remember: statement order and backshift after ‘asked’.'),
  ('Past participle', 'He asked who had *broke* the window.', 'broken', 'Participle: ‘had broken’. Remember: statement order and backshift after ‘asked’.'),
  ('Want to know', 'He wanted *know* where I was.', 'to know', '‘Want’ needs ‘to’: ‘wanted to know’. Remember: statement order and backshift after ‘asked’.'),
  ('Continuous', 'Mum asked what I was *do*.', 'doing', 'Past continuous: ‘was doing’. Remember: statement order and backshift after ‘asked’.'),
  ('Spelling', 'She asked *wether* I was coming.', 'whether', 'Spelling: ‘whether’. Remember: statement order and backshift after ‘asked’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, yes/no or wh-, multiple choice and spot-the-mistake. In the typing questions write if / whether or the verb in statement order with backshift. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('type', 'Yes/No or Wh-'),
 'fill': [
  ('Yes/No', '“Are you coming?” → She asked [[if|whether]] I was coming.', 'if / that', 'A yes/no question is reported with ‘if’ or ‘whether’.', 'Yes/No → if / whether.'),
  ('Wh-', '“Where are you going?” → He asked where I [[was going]].', 'go', 'Statement order and backshift: I was going.', 'Subject first, then verb.'),
  ('Wh-', '“What did you buy?” → She asked what I [[had bought]].', 'buy', 'No ‘did’; past simple moves back to past perfect.', 'Past simple → had + participle.'),
  ('Can', '“Can you drive?” → He asked if I [[could]] drive.', 'can / could', '‘Can’ moves back to ‘could’ after ‘asked’.', '‘Can’ → ‘could’.'),
  ],
 'order': [
  ('Yes/No', 'She asked if I was cold.', []),
  ('Wh-', 'He asked where I worked.', []),
  ('Question word', 'She asked who had called.', []),
  ('Ask + person', 'He asked me what I wanted.', []),
  ],
 'customItems': [
  ('Type', '“Do you like football?” is reported with…', ['if / whether', 'that', 'what', 'who'],
   ['‘That’ is for statements.', '‘What’ would change the question.', '‘Who’ would change the question.'],
   'Yes/No questions → if / whether.'),
  ('Type', '“Where do you live?” is reported with…', ['where', 'if', 'that', 'whether'],
   ['‘If’ is for yes/no questions.', '‘That’ is for statements.', '‘Whether’ is for yes/no questions.'],
   'Wh- questions keep their question word.'),
  ('Type', '“Who called?” → She asked who had called. The word order…', ['doesn’t change, because ‘who’ is the subject', 'changes to who called had', 'needs ‘did’', 'needs ‘if’'],
   ['Wrong order.', '‘Did’ disappears in reported questions.', '‘If’ is for yes/no questions.'],
   'When ‘who / what’ is the subject, keep the order.'),
  ('Type', '“Is it far?” → He asked ___ far.', ['if it was', 'was it', 'it was if', 'that was it'],
   ['Question order is wrong.', 'Wrong order.', '‘That’ is for statements.'],
   'Yes/No: if + subject + verb.'),
  ],
 'mc': [
  ('Wh-', '“What time does the bus leave?” → She asked what time the bus ___.', ['left', 'did leave', 'does leave', 'leaves did'],
   ['‘Did’ disappears.', '‘Does’ disappears and no backshift.', 'Wrong order.'],
   'Statement order + backshift: the bus left.'),
  ('Yes/No', '“Have you got a pen?” → He asked ___ a pen.', ['if I had got', 'had I got', 'have I got', 'that I had got'],
   ['Question order.', 'Question order and no backshift.', '‘That’ is for statements.'],
   'if + subject + backshifted verb.'),
  ('Reporting verb', 'She ___ me how old I was.', ['asked', 'said', 'told', 'asked to'],
   ['‘Said me’ is wrong.', '‘Told’ isn’t used for questions.', 'No ‘to’ before the person.'],
   'Questions → ask + person.'),
  ('Whether', '“Do you want to stay or go?” → She asked ___ I wanted to stay or go.', ['whether', 'that', 'what', 'which'],
   ['‘That’ is for statements, not questions.', '‘What I wanted to stay’ makes no sense.', '‘Which I wanted’ is wrong here.'],
   '‘Whether’ is very common when the question offers a choice.'),
  ],
 'error': [
  ('Do in reported question', 'She asked what I *did want*.', 'wanted', 'No ‘did’: ‘She asked what I wanted’.'),
  ('If or that', 'He asked *that* I was tired.', 'if', 'Yes/No question → ‘if’.'),
  ('Backshift', 'She asked where I *work*.', 'worked', 'After ‘asked’: ‘worked’.'),
  ('Said or asked', 'He *said* me if I was OK.', 'asked', 'Questions are reported with ‘ask’: ‘He asked me…’.'),
  ],
}
