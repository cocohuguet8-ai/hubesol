TITLE = 'Changes in Reported Speech'
AUX = (['that', 'then', 'there', 'the', 'day'], None, 'that')
NEXT = ('Reported Speech without Backshift', '/grammar/reported-speech/reported-speech-no-backshift/')
BODY = r'''
## What changes in reported speech

When we report someone's words **later** or **somewhere else**, three things often change:

| What | Example |
|---|---|
| 1. the **tense** (backshift) | "I **am** here." → She said she **was** there. |
| 2. **pronouns** and **possessives** | "**I** love **my** job." → He said **he** loved **his** job. |
| 3. **time** and **place** words | "I'll do it **tomorrow**." → She said she would do it **the next day**. |

## Pronouns and possessives

Change them to match **who is speaking now** and **who you are talking about**.

| Direct | Reported (about Marta) |
|---|---|
| "**I**'m tired." | Marta said **she** was tired. |
| "This is **my** bag." | Marta said it was **her** bag. |
| "**We** love **our** school." | They said **they** loved **their** school. |
| "I'll call **you**." | She said she would call **me**. |

> ⚠️ Typical error: ~~Pau said I was hungry.~~ (Pau was talking about himself) → *Pau said he was hungry.*

## Time expressions

| Direct speech | Reported speech |
|---|---|
| now | then / at that moment |
| today | that day |
| tonight | that night |
| yesterday | the day before / the previous day |
| tomorrow | the next day / the following day |
| last week | the week before / the previous week |
| next month | the following month / the month after |
| two days ago | two days before |
| this week | that week |

> ⚠️ Typical error: ~~She said she had seen him yesterday.~~ (reported a week later) → *She said she had seen him the day before.*

## Place and demonstratives

| Direct speech | Reported speech |
|---|---|
| here | there |
| this | that |
| these | those |
| come | go (often) |

- "I like **this** café." → She said she liked **that** café.
- "Wait **here**." → He told me to wait **there**.

> ⚠️ Typical error: ~~He said he liked these shoes.~~ (you're not there now) → *He said he liked those shoes.*

## When NOT to change

### 1. Same day, same place

If you report the words **soon** and **in the same place**, keep the original words.

- (Five minutes later) "Pau said he's coming **today**." ✓

### 2. The words are still true

- "The meeting is **tomorrow**." (reported the same day) → She said the meeting is **tomorrow**. ✓

## Putting it all together

> "I **saw** **your** brother **here** **yesterday**," Laia said.
>
> → Laia said **she had seen my** brother **there the day before**.

Four changes: tense, pronoun, possessive, place and time.

## Common mistakes

**1. Not changing pronouns.** *~~She said I was late~~* (she meant herself) → **She said she was late.**

**2. Keeping *yesterday / tomorrow* much later.** → **the day before / the next day.**

**3. Keeping *this / here*.** → **that / there** when the place has changed.

**4. *Ago* in reported speech.** *~~two weeks ago~~* → **two weeks before / earlier.**

**Pro tip:** imagine you are telling the story a week later in a different town — then change *everything* that points to "now" and "here".
'''

GAP = ('Fill in the gaps',
  'Type the reported version of the word in brackets: a pronoun, a possessive, a time word or a place word. Twenty original sentences.',
  [
  ('Pronoun', '“I’m hungry.” → Pau said [[he]] was hungry.', '(I)', 'Pau is talking about himself, so ‘I’ becomes ‘he’.'),
  ('Pronoun', '“We’re late.” → My friends said [[they]] were late.', '(we)', 'The speakers are now ‘they’, so ‘we’ becomes ‘they’.'),
  ('Pronoun', '“I’ll call you.” → Laia said she would call [[me]].', '(you)', 'Laia was speaking to me, so ‘you’ becomes ‘me’.'),
  ('Possessive', '“This is my coat.” → Joan said it was [[her]] coat.', '(my)', 'Joan’s coat: ‘my’ becomes ‘her’.'),
  ('Possessive', '“We love our new flat.” → They said they loved [[their]] new flat.', '(our)', '‘Our’ becomes ‘their’ when you report about them.'),
  ('Possessive', '“Your bag is on the chair.” → She said [[my]] bag was on the chair.', '(your)', 'She was speaking to me, so ‘your’ becomes ‘my’.'),
  ('Time', '“I’m busy now.” → He said he was busy [[then]].', '(now)', '‘Now’ becomes ‘then’ (or ‘at that moment’).'),
  ('Time', '“I’ll finish it today.” → She said she would finish it [[that]] day.', '(today)', '‘Today’ becomes ‘that day’.'),
  ('Time', '“I’m going out tonight.” → He said he was going out [[that]] night.', '(tonight)', '‘Tonight’ becomes ‘that night’.'),
  ('Time', '“I saw her yesterday.” → He said he had seen her the day [[before]].', '(yesterday)', '‘Yesterday’ becomes ‘the day before’.'),
  ('Time', '“The exam is tomorrow.” → She said the exam was the [[next]] day.', '(tomorrow)', '‘Tomorrow’ becomes ‘the next day’.'),
  ('Time', '“We moved last year.” → They said they had moved the year [[before]].', '(last year)', '‘Last year’ becomes ‘the year before’.'),
  ('Time', '“I’ll visit you next week.” → She said she would visit me the [[following]] week.', '(next week)', '‘Next week’ becomes ‘the following week’.'),
  ('Time', '“I met him two days ago.” → She said she had met him two days [[before]].', '(ago)', '‘Ago’ becomes ‘before’ (or ‘earlier’).'),
  ('Place', '“I live here.” → He said he lived [[there]].', '(here)', '‘Here’ becomes ‘there’ when the place is different.'),
  ('Demonstrative', '“I like this song.” → She said she liked [[that]] song.', '(this)', '‘This’ becomes ‘that’.'),
  ('Demonstrative', '“These shoes are new.” → He said [[those]] shoes were new.', '(these)', '‘These’ becomes ‘those’.'),
  ('Time', '“I’m working this week.” → She said she was working [[that]] week.', '(this week)', '‘This week’ becomes ‘that week’.'),
  ('Combined', '“I lost my keys here yesterday.” → He said he had lost [[his]] keys there the day before.', '(my)', 'He lost his own keys: ‘my’ becomes ‘his’.'),
  ('Combined', '“We’ll come back tomorrow.” → They said they would come back the [[following]] day.', '(tomorrow)', '‘Tomorrow’ can also become ‘the following day’.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each reported sentence — 20 examples with pronoun, time and place changes.',
  [
  ('Pronoun', 'He said he was tired.', []),
  ('Pronoun', 'She said she would call me.', []),
  ('Pronoun', 'They said they were lost.', []),
  ('Possessive', 'She said it was her bag.', []),
  ('Possessive', 'He said his phone was broken.', []),
  ('Possessive', 'They said they loved their school.', []),
  ('Time', 'She said she was busy then.', []),
  ('Time', 'He said he would do it that day.', []),
  ('Time', 'She said she had seen him the day before.', []),
  ('Time', 'He said the match was the next day.', []),
  ('Time', 'They said they had moved the year before.', []),
  ('Time', 'She said she would come the following week.', []),
  ('Time', 'He said he had arrived two days before.', []),
  ('Place', 'She said she lived there.', []),
  ('Place', 'He told me to wait there.', []),
  ('Demonstrative', 'She said she liked that dress.', []),
  ('Demonstrative', 'He said those books were his.', []),
  ('Time', 'She said she was going out that night.', []),
  ('Combined', 'He said he had lost his wallet there.', []),
  ('Combined', 'She said she would see me the next day.', []),
  ])

MATCH = {'title': 'Match the direct and reported word', 'subtitle': 'Tap a word from direct speech, then tap what it usually becomes in reported speech.',
  'leftLabel': 'Direct', 'rightLabel': 'Reported', 'rightLabelSub': '(later / elsewhere)', 'reviewArrowPrefix': '',
  'pairs': [
  ('now', 'then'), ('today', 'that day'), ('tonight', 'that night'), ('yesterday', 'the day before'), ('tomorrow', 'the next day'),
  ('last week', 'the week before'), ('next month', 'the following month'), ('two days ago', 'two days before'), ('this week', 'that week'), ('here', 'there'),
  ('this', 'that'), ('these', 'those'), ('I', 'he / she'), ('we', 'they'), ('my', 'his / her'),
  ('our', 'their'), ('last year', 'the year before'), ('next week', 'the following week'), ('this morning', 'that morning'), ('a week ago', 'a week before'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Change pronouns, possessives, time and place words when you report later or somewhere else.',
  [
  ('Pronoun', '“I’m exhausted,” said Marc. → Marc said ___ was exhausted.', ['he', 'I', 'you', 'him'],
   ['Marc is talking about himself, so ‘I’ must become ‘he’, not stay ‘I’.', '‘You’ would mean the listener was exhausted.', '‘Him’ is an object pronoun and can’t be the subject.'],
   'Change ‘I’ to match the speaker: Marc → he.'),
  ('Possessive', '“That’s my seat,” said Laia. → Laia said it was ___ seat.', ['her', 'my', 'your', 'his'],
   ['Keeping ‘my’ would mean it’s your seat, the reporter’s.', '‘Your’ would mean the listener’s seat.', '‘His’ is for a man; Laia is a woman.'],
   'Change ‘my’ to match the speaker: Laia → her.'),
  ('Pronoun', '“I’ll help you,” Pau told me. → Pau said he would help ___.', ['me', 'you', 'him', 'I'],
   ['‘You’ was me, the person Pau spoke to.', '‘Him’ would mean someone else.', '‘I’ can’t be an object.'],
   'Pau spoke to me, so ‘you’ becomes ‘me’.'),
  ('Time', '“I’ll do it tomorrow.” (reported a week later) → She said she would do it ___.', ['the next day', 'tomorrow', 'yesterday', 'the day before'],
   ['A week later, ‘tomorrow’ no longer makes sense.', '‘Yesterday’ is the wrong direction in time.', '‘The day before’ is the past, not the future.'],
   '‘Tomorrow’ becomes ‘the next day’ (or ‘the following day’).'),
  ('Time', '“I met him yesterday.” → She said she had met him ___.', ['the day before', 'yesterday', 'the next day', 'tomorrow'],
   ['Reported later, ‘yesterday’ is no longer correct.', '‘The next day’ is the future.', '‘Tomorrow’ is the future.'],
   '‘Yesterday’ becomes ‘the day before’ (or ‘the previous day’).'),
  ('Time', '“I’m busy now.” → He said he was busy ___.', ['then', 'now', 'there', 'that'],
   ['‘Now’ is the reporter’s moment, not his.', '‘There’ is a place word.', '‘That’ needs a noun after it here.'],
   '‘Now’ becomes ‘then’ or ‘at that moment’.'),
  ('Time', '“I’m going out tonight.” → She said she was going out ___.', ['that night', 'tonight', 'the night', 'this night'],
   ['‘Tonight’ only works if you report the same day.', '‘The night’ is incomplete.', '‘This night’ isn’t natural English.'],
   '‘Tonight’ becomes ‘that night’.'),
  ('Time', '“We bought it two weeks ago.” → They said they had bought it two weeks ___.', ['before', 'ago', 'after', 'later'],
   ['‘Ago’ counts back from now; in reported speech use ‘before’.', '‘After’ is the wrong direction.', '‘Later’ is the wrong direction.'],
   '‘Ago’ becomes ‘before’ or ‘earlier’.'),
  ('Time', '“I’ll start next month.” → He said he would start ___.', ['the following month', 'next month', 'the month before', 'last month'],
   ['‘Next month’ only works if it’s still in the future now.', '‘The month before’ is the past.', '‘Last month’ is the past.'],
   '‘Next month’ becomes ‘the following month’.'),
  ('Place', '“I love it here.” → She said she loved it ___.', ['there', 'here', 'where', 'then'],
   ['‘Here’ is where you are now, not where she was.', '‘Where’ is a question word.', '‘Then’ is a time word.'],
   '‘Here’ becomes ‘there’.'),
  ('Demonstrative', '“I want this one.” → He said he wanted ___ one.', ['that', 'this', 'these', 'those'],
   ['‘This’ refers to something near you now.', '‘These’ is plural.', '‘Those’ is plural.'],
   '‘This’ becomes ‘that’.'),
  ('Demonstrative', '“These cakes are delicious.” → She said ___ cakes were delicious.', ['those', 'these', 'this', 'that'],
   ['‘These’ refers to things near you now.', '‘This’ is singular.', '‘That’ is singular.'],
   '‘These’ becomes ‘those’.'),
  ('Combined', '“I left my bag here.” → He said he had left ___ bag ___.', ['his / there', 'my / here', 'his / here', 'my / there'],
   ['Both words need to change.', '‘Here’ must change to ‘there’.', '‘My’ must change to ‘his’.'],
   'Change the possessive and the place word.'),
  ('Combined', '“We’ll see you tomorrow.” → They said they would see me ___.', ['the next day', 'tomorrow', 'today', 'the day before'],
   ['Only correct if you report it the same day.', '‘Today’ changes the meaning.', '‘The day before’ is the past.'],
   'Reported later: tomorrow → the next day.'),
  ('No change', 'You report five minutes later, in the same room: “I’m tired.” → She said she ___ tired.', ['’s / was (both possible)', 'had been', 'would be', 'has been'],
   ['‘Had been’ is two steps back.', '‘Would be’ changes the meaning.', '‘Has been’ changes the meaning.'],
   'Reported soon and still true: backshift is optional.'),
  ('No change', 'Same day: “The match is tonight.” → He said the match is ___.', ['tonight', 'that night', 'the next night', 'the night before'],
   ['If it’s still the same day, no change is needed.', '‘The next night’ changes the meaning.', '‘The night before’ changes the meaning.'],
   'Same day, same place: keep the original time word.'),
  ('Possessive', '“Our team won!” → They said ___ team had won.', ['their', 'our', 'your', 'there'],
   ['‘Our’ would include you.', '‘Your’ would mean the listener’s team.', '‘There’ is a place word, not a possessive.'],
   '‘Our’ becomes ‘their’.'),
  ('Time', '“I saw it last week.” → She said she had seen it ___.', ['the week before', 'last week', 'next week', 'the following week'],
   ['Reported later, ‘last week’ may be wrong.', '‘Next week’ is the future.', '‘The following week’ is the future.'],
   '‘Last week’ becomes ‘the week before’ / ‘the previous week’.'),
  ('Pronoun', '“You’re right,” she told me. → She said ___ was right.', ['I', 'you', 'she', 'me'],
   ['‘You’ was me; in my report it becomes ‘I’.', '‘She’ would mean she was right.', '‘Me’ can’t be the subject.'],
   'She spoke to me: ‘you’ → ‘I’.'),
  ('Time', '“I’ll finish it this week.” → He said he would finish it ___.', ['that week', 'this week', 'last week', 'the week before'],
   ['‘This week’ only works if it’s still the same week.', '‘Last week’ changes the meaning.', '‘The week before’ is the past.'],
   '‘This week’ becomes ‘that week’.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences — imagine they are reported a week later.',
  [
  ('Pronoun', 'Pau said *I* was hungry. (Pau meant himself.)', 'he', 'Pau talked about himself: ‘Pau said he was hungry’.'),
  ('Pronoun', 'My friends said *we* were lost. (They meant themselves.)', 'they', 'Change ‘we’ to ‘they’. Pronouns change to match the person you are talking about.'),
  ('Possessive', 'Laia said it was *my* bag. (It was Laia’s bag.)', 'her', 'Laia’s bag: ‘her bag’. Possessives change with the pronouns.'),
  ('Possessive', 'They said they loved *our* new house. (Their house.)', 'their', 'Their house: ‘their new house’. Possessives change with the pronouns.'),
  ('Time', 'Last week she said she would call me *tomorrow*.', 'the next day', 'Reported later: ‘tomorrow’ → ‘the next day’.'),
  ('Time', 'He said he had seen her *yesterday*.', 'the day before', 'Reported later: ‘the day before’. Time words change when you report later.'),
  ('Time', 'She said she was busy *now*.', 'then', '‘Now’ → ‘then’. Time words change when you report later.'),
  ('Time', 'They said they had moved two years *ago*.', 'before', '‘Ago’ → ‘before’. Time words change when you report later.'),
  ('Time', 'He said he was going out *tonight*.', 'that night', '‘Tonight’ → ‘that night’. Time words change when you report later.'),
  ('Time', 'She said she would start *next* month.', 'the following', '‘Next month’ → ‘the following month’. Time words change when you report later.'),
  ('Place', 'He said he lived *here* in Madrid. (We’re in Girona now.)', 'there', '‘Here’ → ‘there’. Place words change when you are somewhere else.'),
  ('Demonstrative', 'She said she wanted *this* dress.', 'that', '‘This’ → ‘that’. Demonstratives change when the thing is no longer near.'),
  ('Demonstrative', 'He said *these* shoes were too small.', 'those', '‘These’ → ‘those’. Demonstratives change when the thing is no longer near.'),
  ('Tense', 'She said she *is* tired that day.', 'was', 'Backshift: ‘was’. After ‘said’ the tense moves back.'),
  ('Tense', 'He said he *will* come the next day.', 'would', 'Backshift: ‘would’. After ‘said’ the tense moves back.'),
  ('Tense', 'They said they *have* seen it the week before.', 'had', 'Backshift: ‘had seen’. After ‘said’ the tense moves back.'),
  ('Said or told', 'She *said* me she would come.', 'told', 'Person after: ‘told me’. ‘Tell’ needs a person; ‘say’ doesn’t.'),
  ('Wrong time word', 'He said he had arrived the day *after*.', 'before', '‘Yesterday’ → ‘the day before’, not ‘after’.'),
  ('Wrong time word', 'She said the exam was the *previous* day. (She said “tomorrow”.)', 'next', '‘Tomorrow’ → ‘the next day’. Check the direction in time.'),
  ('Spelling', 'He said he would come the *folowing* week.', 'following', 'Spelling: ‘following’. Check the original words carefully.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, time and place words, multiple choice and spot-the-mistake. In the typing questions write the reported pronoun, possessive, time or place word. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('timeplace', 'Time and place words'),
 'fill': [
  ('Pronoun', '“I’m late.” → Marta said [[she]] was late.', 'I', 'Marta talked about herself, so ‘I’ becomes ‘she’.', 'Match the speaker: ‘she’.'),
  ('Possessive', '“That’s my pen.” → Pol said it was [[his]] pen.', 'my', 'Pol’s pen, so ‘my’ becomes ‘his’ in the report.', 'Match the speaker: ‘his’.'),
  ('Time', '“I’ll see you tomorrow.” → She said she would see me the [[next]] day.', 'tomorrow', '‘Tomorrow’ becomes ‘the next day’ when reported later.', 'Tomorrow → the next day.'),
  ('Place', '“Stay here.” → He told me to stay [[there]].', 'here', '‘Here’ becomes ‘there’ when the place is different.', 'Here → there.'),
  ],
 'order': [
  ('Pronoun', 'He said he was cold.', []),
  ('Time', 'She said she had left the day before.', []),
  ('Place', 'He said he worked there.', []),
  ('Demonstrative', 'She said that book was hers.', []),
  ],
 'customItems': [
  ('Timeplace', '‘yesterday’ in reported speech becomes…', ['the day before', 'the next day', 'that day', 'tomorrow'],
   ['‘The next day’ is for ‘tomorrow’.', '‘That day’ is for ‘today’.', '‘Tomorrow’ is the future.'],
   'yesterday → the day before / the previous day.'),
  ('Timeplace', '‘next week’ in reported speech becomes…', ['the following week', 'the week before', 'that week', 'last week'],
   ['‘The week before’ is for ‘last week’.', '‘That week’ is for ‘this week’.', '‘Last week’ is the past.'],
   'next week → the following week.'),
  ('Timeplace', '‘these’ in reported speech becomes…', ['those', 'this', 'that', 'them'],
   ['‘This’ is singular and near.', '‘That’ is singular.', '‘Them’ is a pronoun, not a demonstrative.'],
   'these → those.'),
  ('Timeplace', '‘ago’ in reported speech becomes…', ['before', 'after', 'later', 'then'],
   ['‘After’ is the wrong direction.', '‘Later’ is the wrong direction.', '‘Then’ replaces ‘now’.'],
   'ago → before / earlier.'),
  ],
 'mc': [
  ('Pronoun', '“We’re ready.” → They said ___ were ready.', ['they', 'we', 'you', 'them'],
   ['‘We’ would include you.', '‘You’ changes who is ready.', '‘Them’ can’t be the subject.'],
   'we → they.'),
  ('Time', '“I’m leaving today.” → He said he was leaving ___.', ['that day', 'today', 'the next day', 'yesterday'],
   ['Only correct if it’s the same day.', 'Changes the meaning.', 'Changes the meaning.'],
   'today → that day.'),
  ('Demonstrative', '“This is my favourite song.” → She said ___ was her favourite song.', ['that', 'this', 'these', 'those'],
   ['‘This’ points to now and here.', '‘These’ is plural.', '‘Those’ is plural.'],
   'this → that.'),
  ('Combined', '“I saw your sister here.” → He said he had seen ___ sister ___.', ['my / there', 'your / here', 'my / here', 'your / there'],
   ['Both words must change.', '‘Here’ must change.', '‘Your’ must change to ‘my’.'],
   'your → my (he spoke to me); here → there.'),
  ],
 'error': [
  ('Pronoun', 'Joan said *I* was tired. (Joan meant herself.)', 'she', 'Joan → ‘she’.'),
  ('Time', 'He said he had called her *yesterday*.', 'the day before', 'Reported later: ‘the day before’.'),
  ('Place', 'She said she was born *here*. (We’re somewhere else.)', 'there', 'here → there.'),
  ('Demonstrative', 'He said *these* were his keys.', 'those', 'these → those.'),
  ],
}
