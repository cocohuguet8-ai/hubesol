TITLE = 'Reflexive Pronouns'
AUX = (['myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'yourselves', 'themselves'], None, 'myself')
NEXT = ('Compound Nouns', '/grammar/nouns-determiners/compound-nouns/')
BODY = r'''
## The forms

| Subject | Reflexive |
|---|---|
| I | **myself** |
| you (one person) | **yourself** |
| he | **himself** |
| she | **herself** |
| it | **itself** |
| we | **ourselves** |
| you (more than one) | **yourselves** |
| they | **themselves** |

Singular forms end in **-self**; plural forms end in **-selves**.

> ⚠️ Typical error: ~~hisself~~, ~~theirselves~~ → *himself, themselves.*

## When to use reflexive pronouns

### 1. Subject and object are the same person

- I cut **myself**. (I cut me ✗)
- She looked at **herself** in the mirror.
- The cat is washing **itself**.

### 2. Emphasis: "nobody else did it"

- I made this cake **myself**!
- The president **himself** answered the letter.

### 3. *By + reflexive* = alone / without help

- He lives **by himself**. — Did you paint this room **by yourself**?

### 4. Common verbs with reflexives

| Verb | Example |
|---|---|
| enjoy yourself | **Enjoy yourselves** at the party! |
| hurt yourself | Be careful — don't **hurt yourself**. |
| help yourself | **Help yourself** to some cake. |
| introduce yourself | Let me **introduce myself**. |
| behave yourself | **Behave yourselves**, children! |

## When NOT to use reflexive pronouns

### 1. With many everyday verbs

In English we do **not** say *wash/dress/shave/relax/feel myself* in normal situations:

- I get up, **wash**, **get dressed** and have breakfast. (~~wash myself~~)
- I **feel** tired. (~~feel myself tired~~)
- Let's **relax**. (~~relax ourselves~~)

> ⚠️ Typical error: ~~I shower myself every morning.~~ → *I have a shower every morning.*

### 2. After prepositions of place

- She put the bag **next to her**. (~~next to herself~~)

## Reflexive vs *each other*

| Reflexive | Each other |
|---|---|
| They looked at **themselves**. (each one in the mirror) | They looked at **each other**. (A → B, B → A) |
| We blamed **ourselves**. | We blamed **each other**. |

## Common mistakes

**1. Wrong form.** *~~ourself~~, ~~themself~~* → **ourselves, themselves**.

**2. Object pronoun instead.** *~~I hurt me.~~* → **I hurt myself.**

**3. Reflexive with everyday verbs.** *~~I concentrate myself.~~* → **I concentrate.**

**4. Confusing with *each other*.** *~~They love themselves~~* (meaning A loves B) → **each other**.

**Pro tip:** use a reflexive when the **action comes back** to the subject — or to say **"nobody else did it"**.
'''

GAP = ('Fill in the gaps',
  'Type the correct reflexive pronoun. Twenty original sentences.',
  [
  ('Same person', 'I cut [[myself]] while I was cooking.', 'I → ?', 'Subject ‘I’, object is the same person: ‘myself’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Same person', 'She looked at [[herself]] in the mirror.', 'she → ?', 'Subject ‘she’: ‘herself’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Same person', 'He hurt [[himself]] playing football.', 'he → ?', 'Subject ‘he’: ‘himself’ (never ‘hisself’). Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Same person', 'The cat is cleaning [[itself]].', 'it → ?', 'Animal / thing: ‘itself’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Same person', 'We taught [[ourselves]] to play the guitar.', 'we → ?', 'Subject ‘we’: ‘ourselves’ (plural ends in -selves).'),
  ('Same person', 'They blamed [[themselves]] for the accident.', 'they → ?', 'Subject ‘they’: ‘themselves’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Same person', 'Did you burn [[yourself]] on the oven, Marta?', 'you (one) → ?', 'One person: ‘yourself’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Same person', 'Children, look after [[yourselves]]!', 'you (many) → ?', 'More than one person: ‘yourselves’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Emphasis', 'I made this birthday cake [[myself]]!', 'I → ?', 'Emphasis: nobody helped me. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Emphasis', 'The manager [[himself]] came to say sorry.', 'he → ?', 'Emphasis: the manager, not someone else. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Emphasis', 'We painted the whole house [[ourselves]].', 'we → ?', 'Emphasis: we did it, not a painter. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('By + reflexive', 'My grandma lives by [[herself]].', 'she → ?', '‘By herself’ = alone. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('By + reflexive', 'Did you do this puzzle by [[yourself]]?', 'you (one) → ?', '‘By yourself’ = without help. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('By + reflexive', 'The kids went to school by [[themselves]] today.', 'they → ?', '‘By themselves’ = alone. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Enjoy', 'Did you enjoy [[yourselves]] at the party, guys?', 'you (many) → ?', '‘Enjoy yourselves’ — more than one person. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Help', 'Please help [[yourself]] to some coffee.', 'you (one) → ?', '‘Help yourself’ = take what you want. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Introduce', 'Let me introduce [[myself]]. I’m Pau.', 'I → ?', '‘Introduce myself’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Behave', 'The dog behaved [[itself]] at the vet.', 'it → ?', '‘Behave itself’ for an animal. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Talk to', 'He often talks to [[himself]] when he’s nervous.', 'he → ?', '‘Talk to himself’ — the same person. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Be proud', 'You should be proud of [[yourself]], Nil!', 'you (one) → ?', '‘Proud of yourself’ — one person. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with reflexive pronouns.',
  [
  ('Same person', 'I cut myself.', []),
  ('Same person', 'She hurt herself.', []),
  ('Same person', 'He looked at himself.', []),
  ('Same person', 'The dog scratched itself.', []),
  ('Same person', 'We taught ourselves.', []),
  ('Same person', 'They blamed themselves.', []),
  ('Emphasis', 'I made it myself.', []),
  ('Emphasis', 'She did it herself.', []),
  ('Emphasis', 'We built it ourselves.', []),
  ('By + reflexive', 'He lives by himself.', []),
  ('By + reflexive', 'I went by myself.', []),
  ('Enjoy', 'Enjoy yourselves at the party!', []),
  ('Help', 'Help yourself to cake.', []),
  ('Introduce', 'Let me introduce myself.', []),
  ('Behave', 'Behave yourselves, kids!', []),
  ('No reflexive', 'I get dressed at seven.', []),
  ('No reflexive', 'I feel tired.', []),
  ('Each other', 'They looked at each other.', []),
  ('Talk to', 'She talks to herself.', []),
  ('Proud', 'Be proud of yourself.', []),
  ])

MATCH = {'title': 'Who is it?', 'subtitle': 'Tap a subject, then tap its reflexive pronoun.',
  'leftLabel': 'Subject', 'rightLabel': 'Reflexive', 'rightLabelSub': '', 'reviewArrowPrefix': '',
  'pairs': [
  ('I hurt…', 'myself'), ('Anna hurt…', 'herself'), ('Marc hurt…', 'himself'), ('The robot switched…off', 'itself'),
  ('We enjoyed…', 'ourselves'), ('You (Pau) cut…', 'yourself'), ('You (Pau and Nil) cut…', 'yourselves'), ('The girls blamed…', 'themselves'),
  ('My dad shaved… (special effort!)', 'himself'), ('The cat washed…', 'itself'), ('My sister and I taught…', 'ourselves'), ('The students introduced…', 'themselves'),
  ('I said to…', 'myself'), ('My mum made it…', 'herself'), ('You (one person) did it…', 'yourself'), ('The machine cleans…', 'itself'),
  ('Kids, help…', 'yourselves'), ('Joan lives by…', 'himself'), ('They live by…', 'themselves'), ('We did it by…', 'ourselves'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Same person as the subject? Want to say “nobody else did it”? → reflexive.',
  [
  ('Same person', 'Be careful with that knife! Don’t cut ___.', ['yourself', 'you', 'yourselves', 'your'],
   ['‘Cut you’ means you cut another person called ‘you’ — we need the reflexive.', 'One person: not ‘yourselves’.', '‘Your’ needs a noun.'],
   'One person, same subject: yourself. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Same person', 'Marc fell off his bike and hurt ___.', ['himself', 'hisself', 'him', 'herself'],
   ['‘Hisself’ is not a word.', '‘Him’ would be another man.', '‘Herself’ is for a woman.'],
   'He → himself. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Same person', 'The girls took photos of ___.', ['themselves', 'theirselves', 'them', 'themself'],
   ['‘Theirselves’ is not a word.', '‘Them’ would be other people.', '‘Themself’ isn’t the plural form here.'],
   'They → themselves. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Same person', 'We really enjoyed ___ at the concert.', ['ourselves', 'ourself', 'us', 'themselves'],
   ['Plural: ‘-selves’.', '‘Enjoy us’ is wrong.', '‘Themselves’ doesn’t match ‘we’.'],
   'We → ourselves. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Emphasis', 'I didn’t buy this jumper — I knitted it ___.', ['myself', 'me', 'mine', 'by me'],
   ['‘Knitted it me’ is wrong.', '‘Mine’ is possessive.', '‘By me’ isn’t natural here.'],
   'Emphasis: myself. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('By + reflexive', 'She travelled around Asia by ___.', ['herself', 'her', 'hers', 'she'],
   ['‘By her’ means ‘next to her’ or ‘by her (agent)’.', '‘Hers’ is possessive.', 'Subject pronoun after a preposition is wrong.'],
   'By herself = alone. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Help', 'There’s food in the kitchen. Help ___!', ['yourselves', 'you', 'yourself', 'your'],
   ['‘Help you’ isn’t the meaning.', 'Talking to a group → plural.', '‘Your’ needs a noun.'],
   'Talking to a group: help yourselves. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Introduce', 'Can you introduce ___ to the class, please, Sara?', ['yourself', 'you', 'yourselves', 'yours'],
   ['‘Introduce you’ would be someone else introducing you.', 'One person: not plural.', '‘Yours’ is possessive.'],
   'One person: introduce yourself. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('It', 'The door closed by ___.', ['itself', 'it', 'its', 'itselves'],
   ['‘By it’ has a different meaning.', '‘Its’ is possessive.', 'Not a word.'],
   'Thing: by itself. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('No reflexive', 'Every morning I wake up, ___ and have breakfast.', ['get dressed', 'dress myself', 'get myself dressed', 'dressed me'],
   ['Normally we don’t use a reflexive with ‘dress’.', 'Not natural for a daily routine.', 'Not English.'],
   'Daily routine: get dressed. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('No reflexive', 'I ___ much better today.', ['feel', 'feel myself', 'feel me', 'am feeling myself'],
   ['‘Feel’ takes no reflexive.', 'Not English.', 'Not English.'],
   'Feel + adjective: no reflexive. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('No reflexive', 'Let’s sit down and ___.', ['relax', 'relax ourselves', 'relax us', 'relaxing us'],
   ['‘Relax’ doesn’t take a reflexive.', 'Not English.', 'Not English.'],
   'Relax: no reflexive. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Each other', 'Joan and Maria love ___. They’re married.', ['each other', 'themselves', 'theirselves', 'itself'],
   ['‘Themselves’ means each one loves himself/herself.', 'Not a word.', 'Not for people.'],
   'A ↔ B: each other. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Each other', 'The players looked at ___ in the mirror before the match.', ['themselves', 'each other', 'them', 'itself'],
   ['In a mirror, each one sees himself.', '‘Them’ would be other people.', 'Not for people.'],
   'Each one sees himself: themselves. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Preposition of place', 'She put her bag next to ___.', ['her', 'herself', 'she', 'hers'],
   ['After prepositions of place we use the object pronoun.', 'Subject pronoun after a preposition is wrong.', '‘Hers’ is possessive.'],
   'Place: next to her. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Behave', 'Children, behave ___!', ['yourselves', 'yourself', 'you', 'ourselves'],
   ['Talking to several children: plural.', '‘Behave you’ is wrong.', '‘Ourselves’ doesn’t match.'],
   'Group: behave yourselves. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Which', 'Which is correct?', ['They did it themselves.', 'They did it theirselves.', 'They did it themself.', 'They did it them.'],
   ['Not a word.', 'Singular-looking form.', 'Wrong pronoun.'],
   'They → themselves. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Which', 'Which is correct?', ['I have a shower every morning.', 'I shower myself every morning.', 'I wash me every morning.', 'I have myself a shower every morning.'],
   ['Not natural English.', '‘Wash me’ is wrong.', 'Not English.'],
   'Daily routine: no reflexive. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Emphasis', 'The Queen ___ opened the new hospital.', ['herself', 'her', 'she', 'hers'],
   ['‘The Queen her’ is wrong.', 'Double subject.', '‘Hers’ is possessive.'],
   'Emphasis: the Queen herself. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Talk to', 'Grandpa sometimes talks to ___.', ['himself', 'him', 'hisself', 'he'],
   ['‘Him’ would be another man.', 'Not a word.', 'Subject pronoun after a preposition is wrong.'],
   'Same person: himself. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('Wrong form', 'He made the cake *hisself*.', 'himself', 'The correct form is ‘himself’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Wrong form', 'They enjoyed *theirselves* at the beach.', 'themselves', 'The correct form is ‘themselves’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Wrong form', 'We did all the work *ourself*.', 'ourselves', 'Plural: ‘ourselves’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Wrong form', 'You two should be proud of *yourself*.', 'yourselves', 'Two people: ‘yourselves’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Wrong form', 'The dog hurt *himself* — it’s a puppy.', 'itself', 'For an animal we call ‘it’: ‘itself’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Object pronoun', 'I cut *me* with a knife.', 'myself', 'Same person: ‘myself’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Object pronoun', 'She taught *her* to swim. (no teacher)', 'herself', 'Same person: ‘herself’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Object pronoun', 'Did you hurt *you*?', 'yourself', 'Same person: ‘yourself’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Object pronoun', 'They introduced *them* to the new neighbours.', 'themselves', 'Same people: ‘themselves’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Wrong person', 'I looked at *herself* in the mirror.', 'myself', 'Subject ‘I’: ‘myself’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Wrong person', 'We blamed *themselves* for losing.', 'ourselves', 'Subject ‘we’: ‘ourselves’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Wrong person', 'She lives by *himself*.', 'herself', 'Subject ‘she’: ‘herself’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Unnecessary reflexive', 'I *feel myself* very happy today.', 'feel', 'With ‘feel’ we don’t use a reflexive: ‘I feel very happy’.'),
  ('Unnecessary reflexive', 'Sit down and *relax yourself*.', 'relax', '‘Relax’ takes no reflexive: ‘Sit down and relax’.'),
  ('Unnecessary reflexive', 'I need to *concentrate myself* on my exams.', 'concentrate', '‘Concentrate’ takes no reflexive: ‘concentrate on’.'),
  ('Unnecessary reflexive', 'We *met ourselves* at the café.', 'met', '‘Meet’ here takes no reflexive: ‘We met at the café’.'),
  ('Each other', 'Pau and Nil hate *themselves* — they always argue.', 'each other', '‘Each other’ = A ↔ B. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Place', 'He put the bag beside *himself*.', 'him', 'After a preposition of place: ‘beside him’.'),
  ('By + reflexive', 'I went to the cinema by *me*.', 'myself', '‘By myself’ = alone. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Enjoy', 'Enjoy *you* at the party, everyone!', 'yourselves', '‘Enjoy yourselves’ — to a group. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, which use, multiple choice and spot-the-mistake. In the typing questions write the reflexive pronoun. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('use', 'Which use?'),
 'fill': [
  ('Same person', 'Be careful or you’ll burn [[yourself]]!', 'you (one) → ?', 'One person: ‘yourself’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.', 'Same person → reflexive.'),
  ('Emphasis', 'We built this treehouse [[ourselves]].', 'we → ?', 'Emphasis: ‘ourselves’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.', 'Emphasis → reflexive.'),
  ('By + reflexive', 'My uncle lives by [[himself]].', 'he → ?', '‘By himself’ = alone. Use a reflexive when the action comes back to the subject, or to say nobody else did it.', 'By + reflexive = alone.'),
  ('Same person', 'They looked at [[themselves]] in the shop window.', 'they → ?', 'Plural: ‘themselves’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.', 'Plural → -selves.'),
  ],
 'order': [
  ('Same person', 'She cut herself.', []),
  ('Emphasis', 'I did it myself.', []),
  ('By + reflexive', 'They live by themselves.', []),
  ('Enjoy', 'Enjoy yourselves at the party!', []),
  ],
 'customItems': [
  ('Use', 'In ‘I painted it myself’, ‘myself’ shows…', ['emphasis: nobody else did it', 'the same person as object', 'being alone', 'each other'],
   ['The object is ‘it’, not ‘myself’.', 'That’s ‘by myself’.', 'That’s for two people.'],
   'Emphasis. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Use', 'In ‘He cut himself’, ‘himself’ shows…', ['subject = object', 'emphasis', 'being alone', 'possession'],
   ['There’s no ‘nobody else’ idea.', 'There’s no ‘by’.', 'It isn’t possessive.'],
   'Same person. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Use', '‘She went by herself’ means…', ['she went alone', 'she went near herself', 'she hurt herself', 'she went with friends'],
   ['Not English meaning.', 'Nothing about hurting.', 'The opposite.'],
   'By herself = alone. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Use', 'Which verb usually has NO reflexive?', ['relax', 'hurt', 'enjoy', 'introduce'],
   ['‘Hurt yourself’ is common.', '‘Enjoy yourself’ is common.', '‘Introduce yourself’ is common.'],
   '‘Relax’, ‘feel’, ‘concentrate’: no reflexive.'),
  ],
 'mc': [
  ('Same person', 'The baby is looking at ___ in the mirror.', ['herself', 'her', 'she', 'hers'],
   ['‘Her’ would be another person.', 'Subject pronoun is wrong here.', '‘Hers’ is possessive.'],
   'Same person: herself. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Wrong form', 'Which word is correct?', ['themselves', 'theirselves', 'themselfs', 'theirself'],
   ['Not a word.', 'Not a word.', 'Not a word.'],
   'They → themselves. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Each other', 'The two friends hugged ___.', ['each other', 'themselves', 'theirselves', 'itself'],
   ['Each one hugs the other.', 'Not a word.', 'Not for people.'],
   'A ↔ B: each other. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('No reflexive', 'I usually ___ at 7 a.m.', ['get up', 'get myself up', 'get me up', 'up myself'],
   ['Daily routine: no reflexive.', 'Not English.', 'Not English.'],
   'Get up: no reflexive. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ],
 'error': [
  ('Wrong form', 'He hurt *hisself*.', 'himself', 'The form is ‘himself’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Object pronoun', 'We enjoyed *us*.', 'ourselves', 'Same people: ‘ourselves’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ('Unnecessary reflexive', 'I *feel myself* tired.', 'feel', '‘Feel’ takes no reflexive: ‘I feel tired’.'),
  ('Each other', 'They kissed *themselves* goodbye.', 'each other', 'A ↔ B: ‘each other’. Use a reflexive when the action comes back to the subject, or to say nobody else did it.'),
  ],
}
