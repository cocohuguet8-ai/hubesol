TITLE = "Possessives: 's vs of"
AUX = (["'s", 'of'], None, "'s")
NEXT = ('Reflexive Pronouns', '/grammar/nouns-determiners/reflexive-pronouns/')
BODY = r'''
## Two ways to show possession

| **'s** (people & animals) | **of** (things & places) |
|---|---|
| **Anna's** bag | the door **of** the car |
| my **dad's** car | the end **of** the film |
| the **dog's** bowl | the name **of** the street |

## How to form *'s*

### 1. Singular noun + *'s*

- **Maria's** phone, my **brother's** room, the **teacher's** desk

### 2. Plural noun ending in *-s* + *'*

- my **parents'** house, the **students'** books, the **girls'** team

### 3. Irregular plural + *'s*

- the **children's** toys, **women's** clothes, **people's** opinions

> ⚠️ Typical error: ~~the childrens' toys~~ → *Children* has no -s: *the children's toys.*

### 4. Names ending in *-s*

- **James's** car / **James'** car (both are correct)

## When to use *'s*

### 1. People and animals

- **Joan's** sister, the **cat's** tail

### 2. Time expressions

- **today's** news, **next week's** meeting, **a day's** work

### 3. Places as organisations / shops

- **Spain's** economy, at the **doctor's**, at **Sara's** (= Sara's house)

## When to use *of*

### 1. Things and parts of things

- the top **of** the page, the legs **of** the table

### 2. Long phrases

- the name **of** the woman who lives next door

> ⚠️ Typical error: ~~the car's door~~ sounds unnatural → *the door of the car / the car door.*

### 3. Places and abstract ideas

- the centre **of** the town, the history **of** Europe

## Two owners: *'s* once or twice

| Shared (one thing) | Separate (two things) |
|---|---|
| **Pau and Nil's** house (they live together) | **Pau's and Nil's** bikes (one each) |

## Noun + noun (compound) as an alternative

For things, we often just put two nouns together:

- the **kitchen door**, a **car key**, the **bus stop** (not *the bus's stop*)

## *'s* is not always possession!

| Form | Meaning |
|---|---|
| He**'s** tall. | he **is** |
| She**'s** got a cat. | she **has** |
| **Tom's** bike | possession |

## Common mistakes

**1. Missing apostrophe.** *~~my sisters car~~* → **my sister's car**.

**2. Apostrophe in plurals without possession.** *~~I have two cat's.~~* → **two cats**.

**3. Wrong position.** *~~the students's books~~* → **the students' books**.

**4. *'s* with things.** *~~the film's end~~* is possible but *the end of the film* is more natural.

**Pro tip:** **who** owns it? a person → **'s**. **What** is it part of? a thing → **of**.
'''

GAP = ('Fill in the gaps',
  'Write the possessive form or of. Twenty original sentences.',
  [
  ('Singular + ’s', 'This is [[Marta’s|Marta\'s]] bike.', 'Marta', 'Singular person: add ’s → ‘Marta’s’. People and animals → ’s; things and parts of things → of.'),
  ('Singular + ’s', 'My [[brother’s|brother\'s]] room is very messy.', 'brother', 'Singular noun + ’s: ‘brother’s’. People and animals → ’s; things and parts of things → of.'),
  ('Singular + ’s', 'The [[dog’s|dog\'s]] bowl is empty.', 'dog', 'Animals take ’s: ‘the dog’s bowl’. People and animals → ’s; things and parts of things → of.'),
  ('Plural + ’', 'My [[parents’|parents\']] house is near the beach.', 'parents', 'Plural ending in -s: just add ’ → ‘parents’’. People and animals → ’s; things and parts of things → of.'),
  ('Plural + ’', 'The [[students’|students\']] books are on the desk.', 'students', 'Plural ending in -s: ‘students’’. People and animals → ’s; things and parts of things → of.'),
  ('Plural + ’', 'The [[girls’|girls\']] team won the match.', 'girls', 'Plural ending in -s: ‘girls’’. People and animals → ’s; things and parts of things → of.'),
  ('Irregular plural', 'The [[children’s|children\'s]] toys are everywhere.', 'children', 'Irregular plural (no -s): add ’s → ‘children’s’. People and animals → ’s; things and parts of things → of.'),
  ('Irregular plural', 'This shop sells [[women’s|women\'s]] clothes.', 'women', 'Irregular plural: ‘women’s’. People and animals → ’s; things and parts of things → of.'),
  ('Irregular plural', 'Other [[people’s|people\'s]] opinions are important.', 'people', 'Irregular plural: ‘people’s’. People and animals → ’s; things and parts of things → of.'),
  ('Time', 'Did you read [[today’s|today\'s]] news?', 'today', 'Time expressions take ’s: ‘today’s news’. People and animals → ’s; things and parts of things → of.'),
  ('Time', '[[Next week’s|next week’s|Next week\'s]] meeting is on Tuesday.', 'next week', 'Time expression: ‘next week’s meeting’. People and animals → ’s; things and parts of things → of.'),
  ('Of', 'I didn’t like the end [[of]] the film.', 'of / ’s', 'Part of a thing: ‘the end of the film’. People and animals → ’s; things and parts of things → of.'),
  ('Of', 'What’s the name [[of]] this street?', 'of / ’s', 'Things: ‘the name of the street’. People and animals → ’s; things and parts of things → of.'),
  ('Of', 'Write your name at the top [[of]] the page.', 'of / ’s', 'Part of a thing: ‘the top of the page’. People and animals → ’s; things and parts of things → of.'),
  ('Of', 'The legs [[of]] the table are broken.', 'of / ’s', 'Parts of things: ‘the legs of the table’. People and animals → ’s; things and parts of things → of.'),
  ('Long phrase', 'That’s the car [[of]] the man who lives next door.', 'of / ’s', 'With a long phrase, use ‘of’. People and animals → ’s; things and parts of things → of.'),
  ('Shop / house', 'I’ve got an appointment at the [[doctor’s|doctor\'s]].', 'doctor', '‘At the doctor’s’ = at the doctor’s surgery. People and animals → ’s; things and parts of things → of.'),
  ('Shop / house', 'We’re having dinner at [[Joan’s|Joan\'s]] tonight.', 'Joan', '‘At Joan’s’ = at Joan’s house. People and animals → ’s; things and parts of things → of.'),
  ('Shared', 'Pau and [[Nil’s|Nil\'s]] flat is in Barcelona. (they share it)', 'Nil', 'Shared ownership: ’s only on the last name. People and animals → ’s; things and parts of things → of.'),
  ('Name in -s', 'Have you seen [[James’s|James’|James\'s|James\']] new car?', 'James', 'Names ending in -s: ‘James’s’ or ‘James’’. People and animals → ’s; things and parts of things → of.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with ’s and of.',
  [
  ('Singular + ’s', 'This is Anna’s bag.', []),
  ('Singular + ’s', 'My dad’s car is red.', []),
  ('Singular + ’s', 'The cat’s tail is long.', []),
  ('Plural + ’', 'My parents’ house is big.', []),
  ('Plural + ’', 'The boys’ bikes are new.', []),
  ('Irregular plural', 'The children’s room is blue.', []),
  ('Irregular plural', 'I like men’s shoes.', []),
  ('Time', 'Today’s lesson is easy.', []),
  ('Time', 'I read yesterday’s paper.', []),
  ('Of', 'I love the end of the book.', []),
  ('Of', 'What is the name of the song?', []),
  ('Of', 'Sit at the back of the bus.', []),
  ('Of', 'The door of the car is open.', []),
  ('Shop / house', 'I am at the dentist’s.', []),
  ('Shop / house', 'We met at Laura’s.', []),
  ('Shared', 'Pau and Nil’s dog is old.', []),
  ('Singular + ’s', 'Where is my sister’s phone?', []),
  ('Of', 'He lives in the centre of town.', []),
  ('Irregular plural', 'People’s lives are busy.', []),
  ('Time', 'It was a day’s work.', []),
  ])

MATCH = {'title': '’s or of?', 'subtitle': 'Tap a phrase, then tap the correct form.',
  'leftLabel': 'Idea', 'rightLabel': 'Correct form', 'rightLabelSub': '', 'reviewArrowPrefix': '',
  'pairs': [
  ('the bag / Maria', 'Maria’s bag'), ('the end / the story', 'the end of the story'), ('the toys / the children', 'the children’s toys'), ('the house / my parents', 'my parents’ house'),
  ('the top / the mountain', 'the top of the mountain'), ('the news / today', 'today’s news'), ('the tail / the dog', 'the dog’s tail'), ('the name / the street', 'the name of the street'),
  ('the room / my brother', 'my brother’s room'), ('the books / the students', 'the students’ books'), ('the centre / the city', 'the centre of the city'), ('the clothes / women', 'women’s clothes'),
  ('the meeting / next week', 'next week’s meeting'), ('the legs / the chair', 'the legs of the chair'), ('the car / my uncle', 'my uncle’s car'), ('the opinions / people', 'people’s opinions'),
  ('the beginning / the film', 'the beginning of the film'), ('the bikes / the girls', 'the girls’ bikes'), ('the bottom / the page', 'the bottom of the page'), ('the phone / the teacher', 'the teacher’s phone'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. People and animals → ’s. Things and parts of things → of.',
  [
  ('Singular + ’s', 'Is this ___?', ["Pere's coat", "the coat of Pere", "Peres coat", "Peres' coat"],
   ['With people we use ’s, not ‘of’.', 'We need an apostrophe.', '‘Pere’ is singular: ’s, not s’.'],
   'Person: Pere’s coat. People and animals → ’s; things and parts of things → of.'),
  ('Plural + ’', 'The ___ room is upstairs.', ["boys'", "boys's", "boy's'", "boyses"],
   ['Plural in -s: only add ’.', 'Not English.', 'Not a word.'],
   'Plural in -s + ’: the boys’ room (more than one boy). People and animals → ’s; things and parts of things → of.'),
  ('Irregular plural', 'Where is the ___ section in this shop?', ["children's", "childrens'", "childrens", "child's'"],
   ['‘Children’ has no -s: add ’s.', 'We need the apostrophe.', 'Not English.'],
   'Irregular plural + ’s: children’s. People and animals → ’s; things and parts of things → of.'),
  ('Of', 'I can’t remember ___.', ["the name of the hotel", "the hotel's name of", "the name hotel's", "the hotel of name"],
   ['Wrong order.', 'Not English.', 'Wrong meaning.'],
   'Thing: the name of the hotel. People and animals → ’s; things and parts of things → of.'),
  ('Of', 'Put the plates on ___.', ["the top of the shelf", "the shelf's top of", "the top shelf's", "the of top shelf"],
   ['Not English.', 'Changes the meaning.', 'Not English.'],
   'Part of a thing: the top of the shelf. People and animals → ’s; things and parts of things → of.'),
  ('Time', 'Have you done ___ homework?', ["tonight's", "tonights", "the tonight of", "tonights'"],
   ['We need the apostrophe.', 'Not English.', 'Singular: ’s, not s’.'],
   'Time: tonight’s homework. People and animals → ’s; things and parts of things → of.'),
  ('Shop / house', 'I bought some bread at the ___.', ["baker's", "baker", "bakers's", "of baker"],
   ['‘At the baker’ is a person, not a shop.', 'Not English.', 'Not English.'],
   'Shop: at the baker’s. People and animals → ’s; things and parts of things → of.'),
  ('Plural + ’', 'My ___ names are Pol and Biel.', ["cousins'", "cousin's", "cousins", "cousins's"],
   ['Two cousins: plural, so not ‘cousin’s’.', 'We need the apostrophe.', 'Not English.'],
   'Plural in -s + ’: cousins’. People and animals → ’s; things and parts of things → of.'),
  ('Shared', 'Anna and ___ wedding is in June. (they’re getting married)', ["Marc's", "Marc", "Marcs", "of Marc"],
   ['Shared: ’s on the last name.', 'Not English.', 'Not English.'],
   'Shared: Anna and Marc’s wedding. People and animals → ’s; things and parts of things → of.'),
  ('Separate', '___ birthdays are in May. (one each)', ["Anna's and Marc's", "Anna and Marc", "Annas and Marcs", "Anna's and Marc"],
   ['We need possession.', 'We need apostrophes.', 'With separate things, both names take ’s.'],
   'Separate: both take ’s. People and animals → ’s; things and parts of things → of.'),
  ('Long phrase', 'That’s the house ___.', ["of the woman I told you about", "the woman's I told you about", "woman's", "of woman"],
   ['A long phrase is clearer with ‘of’.', 'Not English.', 'We need ‘the’.'],
   'Long phrase: of. People and animals → ’s; things and parts of things → of.'),
  ('Name in -s', 'I love ___ new song.', ["Charles's", "Charle's", "Charles", "Charless"],
   ['The name is ‘Charles’.', 'We need possession.', 'Not English.'],
   'Name in -s: Charles’s (or Charles’). People and animals → ’s; things and parts of things → of.'),
  ('Not possession', 'In ‘She’s my teacher’, ’s means…', ['is', 'has', 'possession', 'us'],
   ['‘She has my teacher’ makes no sense.', 'There’s no owner here.', 'Not this.'],
   '’s here = is. People and animals → ’s; things and parts of things → of.'),
  ('Not possession', 'In ‘He’s got a dog’, ’s means…', ['has', 'is', 'possession', 'was'],
   ['‘He is got’ is wrong.', 'There’s no owner noun.', 'Not this.'],
   '’s + got = has. People and animals → ’s; things and parts of things → of.'),
  ('Compound', 'Wait for me at the ___.', ["bus stop", "bus's stop", "stop of the bus", "buses stop"],
   ['Things don’t usually take ’s.', 'Not natural.', 'Not English.'],
   'Noun + noun: bus stop. People and animals → ’s; things and parts of things → of.'),
  ('Animal', 'The ___ ears are very big.', ["elephant's", "elephant", "elephants's", "of elephant"],
   ['We need possession.', 'Not English.', 'Wrong order.'],
   'Animal + ’s. People and animals → ’s; things and parts of things → of.'),
  ('Which', 'Which is correct?', ["my parents' car", "my parent's car (two parents)", "my parents car", "my parents's car"],
   ['For two parents, ’ goes after the -s.', 'We need an apostrophe.', 'Not English.'],
   'Plural in -s: parents’. People and animals → ’s; things and parts of things → of.'),
  ('Which', 'Which is most natural?', ["the end of the film", "the film's end of", "the end's film", "the of film end"],
   ['Not English.', 'Wrong meaning.', 'Not English.'],
   'Thing: the end of the film. People and animals → ’s; things and parts of things → of.'),
  ('Time', 'It’s only ten ___ walk from here.', ["minutes'", "minute's", "minutes", "minutes's"],
   ['‘Ten minutes’ is plural: ’ after -s.', 'We need the apostrophe.', 'Not English.'],
   'Time: ten minutes’ walk. People and animals → ’s; things and parts of things → of.'),
  ('Irregular plural', 'The ___ changing room is on the left.', ["men's", "mens'", "mans", "man's'"],
   ['‘Men’ has no -s: add ’s.', 'Not English.', 'Not English.'],
   'Irregular plural: men’s. People and animals → ’s; things and parts of things → of.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('Missing apostrophe', 'This is my *sisters* phone.', 'sister’s', 'Possession: ‘my sister’s phone’. People and animals → ’s; things and parts of things → of.'),
  ('Missing apostrophe', 'I found *Pauls* keys.', 'Paul’s', 'Possession: ‘Paul’s keys’. People and animals → ’s; things and parts of things → of.'),
  ('Missing apostrophe', 'The *cats* bed is in the kitchen.', 'cat’s', 'One cat: ‘the cat’s bed’. People and animals → ’s; things and parts of things → of.'),
  ('Apostrophe plural', 'I have two *dog’s*.', 'dogs', 'Simple plural: no apostrophe. People and animals → ’s; things and parts of things → of.'),
  ('Apostrophe plural', 'We sell fresh *apple’s*.', 'apples', 'Simple plural: no apostrophe. People and animals → ’s; things and parts of things → of.'),
  ('Wrong position', 'The *students’s* books are new.', 'students’', 'Plural in -s: just add ’. People and animals → ’s; things and parts of things → of.'),
  ('Wrong position', 'My *parent’s* house is big. (mum and dad)', 'parents’', 'Two parents: ‘parents’’. People and animals → ’s; things and parts of things → of.'),
  ('Irregular plural', 'The *childrens’* toys are broken.', 'children’s', '‘Children’ has no -s: ‘children’s’. People and animals → ’s; things and parts of things → of.'),
  ('Irregular plural', 'It’s a *womens* magazine.', 'women’s', 'Irregular plural: ‘women’s’. People and animals → ’s; things and parts of things → of.'),
  ('’s with things', 'The *chair’s* leg is broken.', 'chair', 'For things, use noun + noun or ‘of’: ‘the chair leg’ / ‘the leg of the chair’.'),
  ('’s with things', 'Please close the *car’s* door.', 'car', 'For things, use noun + noun: ‘the car door’.'),
  ('Time', 'Did you see *yesterdays* match?', 'yesterday’s', 'Time expression: ‘yesterday’s match’. People and animals → ’s; things and parts of things → of.'),
  ('Time', '*Tomorrow* weather will be sunny.', 'Tomorrow’s', 'Time + ’s: ‘Tomorrow’s weather’. People and animals → ’s; things and parts of things → of.'),
  ('Shop', 'I’m going to the *chemist*.', 'chemist’s', 'Shop: ‘the chemist’s’. People and animals → ’s; things and parts of things → of.'),
  ('Shared', '*Anna’s* and Marc’s flat is lovely. (they live together)', 'Anna', 'Shared: ‘Anna and Marc’s flat’ (’s only once, on the last name).'),
  ('Its / it’s', 'The dog wagged *it’s* tail.', 'its', 'Possessive ‘its’ has no apostrophe. People and animals → ’s; things and parts of things → of.'),
  ('Its / it’s', 'The company changed *it’s* name.', 'its', 'Possessive ‘its’ has no apostrophe. People and animals → ’s; things and parts of things → of.'),
  ('Whose', '*Who’s* bag is this?', 'Whose', 'Possessive question word: ‘whose’. People and animals → ’s; things and parts of things → of.'),
  ('Name in -s', 'That’s *Jame’s* book.', 'James’s', 'The name is ‘James’: ‘James’s’ / ‘James’’.'),
  ('Compound', 'Meet me at the *bus’s* stop.', 'bus', 'Noun + noun: ‘the bus stop’. People and animals → ’s; things and parts of things → of.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, ’s or of, multiple choice and spot-the-mistake. In the typing questions write the possessive form or of. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('form', '’s or of?'),
 'fill': [
  ('Singular + ’s', 'That’s my [[mum’s|mum\'s]] bag.', 'mum', 'Singular person + ’s. People and animals → ’s; things and parts of things → of.', 'Person → ’s.'),
  ('Plural + ’', 'The [[players’|players\']] shirts are green.', 'players', 'Plural in -s + ’. People and animals → ’s; things and parts of things → of.', 'Plural in -s → ’. People and animals → ’s; things and parts of things → of.'),
  ('Of', 'Look at the colour [[of]] the sky!', 'of / ’s', 'Thing: ‘the colour of the sky’. People and animals → ’s; things and parts of things → of.', 'Thing → of.'),
  ('Irregular plural', 'The [[people’s|people\'s]] choice award went to her.', 'people', 'Irregular plural + ’s. People and animals → ’s; things and parts of things → of.', 'Irregular plural → ’s.'),
  ],
 'order': [
  ('Singular + ’s', 'This is Pau’s cat.', []),
  ('Of', 'It’s the end of the day.', []),
  ('Plural + ’', 'The girls’ room is pink.', []),
  ('Time', 'Today’s weather is cold.', []),
  ],
 'customItems': [
  ('Form', 'the toys / the baby →', ["the baby's toys", "the toys of the baby's", "the babys toys", "the toys' baby"],
   ['Not English.', 'We need the apostrophe.', 'Wrong meaning.'],
   'Person/baby → ’s. People and animals → ’s; things and parts of things → of.'),
  ('Form', 'the roof / the house →', ["the roof of the house", "the house's roof of", "the roofs house", "the house of the roof"],
   ['Not English.', 'Not English.', 'Wrong meaning.'],
   'Thing → of (or ‘the house roof’). People and animals → ’s; things and parts of things → of.'),
  ('Form', 'the room / two sisters →', ["my sisters' room", "my sister's room", "my sisters room", "my sisters's room"],
   ['That’s one sister.', 'We need the apostrophe.', 'Not English.'],
   'Plural in -s → ’.'),
  ('Form', 'the news / today →', ["today's news", "the news of today's", "todays news", "the today news"],
   ['Not English.', 'We need the apostrophe.', 'Not English.'],
   'Time → ’s. People and animals → ’s; things and parts of things → of.'),
  ],
 'mc': [
  ('Singular + ’s', 'I’m wearing my ___ jumper.', ["brother's", "brothers", "brother", "brothers's"],
   ['We need the apostrophe.', 'We need possession.', 'Not English.'],
   'One brother: brother’s. People and animals → ’s; things and parts of things → of.'),
  ('Of', 'He lives at the end ___ the road.', ["of", "'s", "for", "from"],
   ['Thing: ‘of’.', 'Wrong preposition.', 'Wrong preposition.'],
   'Part of a thing: the end of the road. People and animals → ’s; things and parts of things → of.'),
  ('Irregular plural', 'The ___ games are in the box.', ["children's", "childrens'", "childs", "children"],
   ['‘Children’ has no -s.', 'Not English.', 'We need possession.'],
   'Children’s. People and animals → ’s; things and parts of things → of.'),
  ('Its', 'The tree lost ___ leaves.', ["its", "it's", "its'", "it is"],
   ['‘It’s’ = it is.', 'Not English.', 'Wrong meaning.'],
   'Possessive: its. People and animals → ’s; things and parts of things → of.'),
  ],
 'error': [
  ('Missing apostrophe', 'That’s *Annas* pen.', 'Anna’s', 'Possession needs ’s. People and animals → ’s; things and parts of things → of.'),
  ('Apostrophe plural', 'I like *banana’s*.', 'bananas', 'Simple plural: no apostrophe. People and animals → ’s; things and parts of things → of.'),
  ('Its / it’s', 'The cat is eating *it’s* food.', 'its', 'Possessive ‘its’. People and animals → ’s; things and parts of things → of.'),
  ('Irregular plural', 'The *mens* team won.', 'men’s', 'Irregular plural: ‘men’s’. People and animals → ’s; things and parts of things → of.'),
  ],
}
