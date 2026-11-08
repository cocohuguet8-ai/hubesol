TITLE = 'Countable & Uncountable Nouns'
AUX = (['a', 'an', 'some', 'many', 'much'], None, 'some')
NEXT = ('Some & Any', '/grammar/nouns-determiners/some-any/')
BODY = r'''
## Countable vs uncountable

| Countable | Uncountable |
|---|---|
| can be counted: one, two, three… | can't be counted one by one |
| singular and plural | only one form (no plural) |
| **a** chair, two **chairs** | **furniture** |
| **an** apple, **apples** | **fruit** |
| **a** job, **jobs** | **work** |

## Countable nouns

### 1. Singular: need *a / an / the / my…*

- I've got **a** bike. — ~~I've got bike.~~

### 2. Plural: add *-s / -es*

- two **books**, three **boxes**, many **people**

### 3. Words that go with countables

- **many**, **a few**, **few**, **a number of**, numbers (*three*, *ten*)

## Uncountable nouns

### 1. No *a / an*, no plural

- ~~an information~~, ~~informations~~ → **information**, **some information**

> ⚠️ Typical error: ~~I need an advice.~~ → *I need some advice / a piece of advice.*

### 2. Singular verb

- The news **is** good. — My hair **is** long. — Money **doesn't** grow on trees.

### 3. Words that go with uncountables

- **much**, **a little**, **little**, **an amount of**

## Common uncountable nouns

| Group | Examples |
|---|---|
| Food & drink | water, milk, bread, rice, cheese, sugar |
| Materials | wood, glass, paper, plastic |
| Abstract ideas | love, advice, information, help, news |
| Collections | furniture, luggage, money, homework |
| Weather | weather, rain, snow, traffic |

> ⚠️ Typical error: ~~The weather are nice.~~ → *The weather is nice.*

## Counting uncountables

Use a **unit word** + *of*:

| Unit | Example |
|---|---|
| a piece of | a piece of advice / furniture / cake |
| a slice of | a slice of bread / pizza |
| a glass / bottle of | a glass of water, a bottle of milk |
| a loaf of | a loaf of bread |
| a cup of | a cup of tea |

## Both countable and uncountable

Some nouns change meaning:

- **Coffee** is expensive. (the drink) — Two **coffees**, please. (two cups)
- I don't have **time**. — I've been there three **times**. (occasions)
- The window is made of **glass**. — I need my **glasses**. (spectacles)

## Common mistakes

**1. Plural uncountables.** *~~furnitures, advices, homeworks~~* → **furniture, advice, homework**.

**2. *A / an* with uncountables.** *~~a bread~~* → **a loaf of bread / some bread**.

**3. Plural verb.** *~~The news are bad.~~* → **The news is bad.**

**4. *Much* with countables.** *~~much cars~~* → **many cars**.

**Pro tip:** ask *"Can I put a number in front?"* — yes → countable; no → uncountable.
'''

GAP = ('Fill in the gaps',
  'Type the missing word: a, an, some, many, much, is, are, or the correct form of the noun. Twenty original sentences.',
  [
  ('Singular countable', 'I bought [[a]] new lamp for my room.', 'a / an / some', '‘Lamp’ is countable and singular, so it needs ‘a’.'),
  ('Singular countable', 'She’s got [[an]] umbrella in her bag.', 'a / an / some', 'Singular countable + vowel sound: ‘an umbrella’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Uncountable', 'Can I have [[some]] water, please?', 'a / an / some', '‘Water’ is uncountable: ‘some water’, never ‘a water’ for the substance.'),
  ('Uncountable', 'We need [[some]] information about the course.', 'a / an / some', '‘Information’ is uncountable: no ‘an’, no plural. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Uncountable', 'My teacher gave me [[some]] good advice.', 'a / an / some', '‘Advice’ is uncountable: ‘some advice’ or ‘a piece of advice’.'),
  ('Plural', 'There are three [[books|books]] on the table.', 'book', 'After ‘three’ we need the plural: ‘books’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Plural', 'I saw two [[foxes]] in the garden.', 'fox', 'Nouns ending in -x add -es: ‘foxes’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Plural', 'Many [[people]] came to the party.', 'person', 'The plural of ‘person’ is ‘people’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('No plural', 'We bought some new [[furniture]] for the flat.', 'furniture', '‘Furniture’ is uncountable: no -s. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('No plural', 'I have a lot of [[homework]] tonight.', 'homework', '‘Homework’ is uncountable: never ‘homeworks’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Singular verb', 'The news [[is]] really good today.', 'is / are', '‘News’ is uncountable and takes a singular verb. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Singular verb', 'Your hair [[is]] beautiful.', 'is / are', '‘Hair’ (on your head) is uncountable: singular verb.'),
  ('Singular verb', 'The weather [[is]] terrible this week.', 'is / are', '‘Weather’ is uncountable: ‘is’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Plural verb', 'The children [[are]] in the garden.', 'is / are', '‘Children’ is a plural countable noun: ‘are’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Many / much', 'How [[many]] brothers have you got?', 'many / much', '‘Brothers’ is plural countable: ‘how many’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Many / much', 'How [[much]] money do you need?', 'many / much', '‘Money’ is uncountable: ‘how much’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Many / much', 'There isn’t [[much]] milk in the fridge.', 'many / much', '‘Milk’ is uncountable: ‘much’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Many / much', 'There aren’t [[many]] eggs left.', 'many / much', '‘Eggs’ is plural countable: ‘many’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Unit word', 'Would you like a [[piece]] of cake?', 'piece / slice', 'Use a unit word to count uncountables: ‘a piece of cake’ (‘a slice of cake’ also works).'),
  ('Unit word', 'I’ll have a [[cup]] of tea, please.', 'cup / glass', 'We usually drink tea from a cup: ‘a cup of tea’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with countable and uncountable nouns.',
  [
  ('Singular countable', 'I have a bike.', []),
  ('Plural', 'She has two cats.', []),
  ('Plural', 'Many people live here.', []),
  ('Uncountable', 'I need some help.', []),
  ('Uncountable', 'Can I have some water?', []),
  ('Uncountable', 'He gave me some advice.', []),
  ('No plural', 'We bought new furniture.', []),
  ('Singular verb', 'The news is good.', []),
  ('Singular verb', 'My hair is long.', []),
  ('Singular verb', 'Money is important.', []),
  ('Many / much', 'How many apples are there?', []),
  ('Many / much', 'How much sugar do you want?', []),
  ('Many / much', 'I don’t have much time.', []),
  ('Many / much', 'There aren’t many chairs.', []),
  ('Unit word', 'I ate a slice of bread.', []),
  ('Unit word', 'She drank a glass of milk.', []),
  ('Unit word', 'It’s a piece of advice.', []),
  ('Both', 'Two coffees, please.', []),
  ('Both', 'I don’t have time.', []),
  ('Plural verb', 'The children are tired.', []),
  ])

MATCH = {'title': 'Countable or uncountable?', 'subtitle': 'Tap a noun, then tap its type.',
  'leftLabel': 'Noun', 'rightLabel': 'Type', 'rightLabelSub': '(C / U)', 'reviewArrowPrefix': '',
  'pairs': [
  ('chair', 'countable'), ('furniture', 'uncountable'), ('apple', 'countable'), ('fruit (in general)', 'uncountable'),
  ('job', 'countable'), ('work (= activity)', 'uncountable'), ('suitcase', 'countable'), ('luggage', 'uncountable'),
  ('coin', 'countable'), ('money', 'uncountable'), ('tip', 'countable'), ('advice', 'uncountable'),
  ('exercise (in a book)', 'countable'), ('homework', 'uncountable'), ('car', 'countable'), ('traffic', 'uncountable'),
  ('song', 'countable'), ('music', 'uncountable'), ('report', 'countable'), ('news', 'uncountable'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Can you count it? → a/an, plural, many. Can’t count it? → no plural, much, some.',
  [
  ('Uncountable', 'I need ___ advice about my exams.', ['some', 'an', 'many', 'a'],
   ['‘Advice’ is uncountable, so it can’t take ‘an’.', '‘Many’ goes with plural countable nouns.', '‘Advice’ is uncountable, so it can’t take ‘a’.'],
   'Uncountable: some advice. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('No plural', 'We have a lot of ___ to do this weekend.', ['homework', 'homeworks', 'a homework', 'homework’s'],
   ['‘Homework’ has no plural form.', 'Uncountables don’t take ‘a’.', 'The apostrophe shows possession, not a plural.'],
   '‘Homework’ is uncountable: no -s. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Singular verb', 'The information on the website ___ wrong.', ['is', 'are', 'were', 'have'],
   ['‘Information’ is uncountable: singular verb.', '‘Were’ is plural (or past).', '‘Have’ doesn’t fit the meaning.'],
   'Uncountable + singular verb: is. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Many / much', 'How ___ time do we have?', ['much', 'many', 'few', 'a'],
   ['‘Time’ (= amount) is uncountable: not ‘many’.', '‘Few’ goes with plural countables.', '‘How a’ isn’t English.'],
   'Uncountable: how much. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Many / much', 'How ___ students are in your class?', ['many', 'much', 'little', 'a lot'],
   ['‘Students’ is plural countable: not ‘much’.', '‘Little’ goes with uncountables.', '‘How a lot’ isn’t English.'],
   'Plural countable: how many. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Plural', 'There are five ___ in the photo.', ['women', 'woman', 'womans', 'womens'],
   ['After ‘five’ we need the plural.', '‘Woman’ has an irregular plural.', '‘Womens’ is not a word.'],
   'Irregular plural: women. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Unit word', 'Could I have a ___ of bread?', ['slice', 'bread', 'some', 'many'],
   ['‘A bread of bread’ is wrong.', '‘A some of’ is wrong.', '‘A many of’ is wrong.'],
   'Unit word: a slice of bread. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Uncountable', 'Our hotel room had beautiful old ___.', ['furniture', 'furnitures', 'a furniture', 'furniture’s'],
   ['‘Furniture’ has no plural.', 'Uncountables don’t take ‘a’.', 'The apostrophe isn’t a plural.'],
   '‘Furniture’ is uncountable. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Singular verb', 'Mathematics ___ my favourite subject.', ['is', 'are', 'were', 'have been'],
   ['Subjects ending in -s still take a singular verb.', 'Plural/past form.', 'Wrong tense and number.'],
   'Mathematics is singular. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Both', 'I’ve been to Italy three ___.', ['times', 'time', 'timing', 'a time'],
   ['‘Time’ meaning ‘occasion’ is countable: plural after ‘three’.', '‘Timing’ is a different word.', 'We need the plural.'],
   'Occasion = countable: three times. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Both', 'Two ___, please — with milk.', ['coffees', 'coffee', 'coffee’s', 'coffeeses'],
   ['In a café, ‘coffee’ = a cup, so it’s countable.', 'The apostrophe isn’t a plural.', 'Not a word.'],
   'Two cups: two coffees. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Many / much', 'There isn’t ___ traffic on Sundays.', ['much', 'many', 'a', 'few'],
   ['‘Traffic’ is uncountable.', 'Uncountables don’t take ‘a’.', '‘Few’ goes with countables.'],
   'Uncountable: not much traffic. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Uncountable', 'She has long, dark ___.', ['hair', 'hairs', 'a hair', 'hair’s'],
   ['Hair on your head is uncountable.', 'Uncountable: no ‘a’.', 'Not a plural.'],
   'Head hair: uncountable. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Singular countable', 'I’m looking for ___ job.', ['a', 'some', 'much', '—'],
   ['‘Job’ is countable singular: it needs ‘a’.', '‘Much’ goes with uncountables.', 'A singular countable noun needs an article.'],
   'Singular countable: a job. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Uncountable', 'I’m looking for ___ work.', ['—', 'a', 'many', 'an'],
   ['‘Work’ (activity) is uncountable: no ‘a’.', '‘Many’ goes with countables.', 'No ‘an’ with uncountables.'],
   'Uncountable: work. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Unit word', 'He bought two ___ of milk.', ['bottles', 'milks', 'bottle', 'pieces'],
   ['‘Milk’ is uncountable: count the containers.', 'After ‘two’ we need the plural unit.', 'Milk doesn’t come in pieces.'],
   'Two bottles of milk. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Which', 'Which sentence is correct?', ['The news is surprising.', 'The news are surprising.', 'The new is surprising.', 'A news is surprising.'],
   ['‘News’ takes a singular verb.', '‘The new’ is a different word.', '‘News’ doesn’t take ‘a’.'],
   '‘News’ = uncountable + singular verb. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Which', 'Which sentence is correct?', ['How much luggage have you got?', 'How many luggage have you got?', 'How much luggages have you got?', 'How many luggages have you got?'],
   ['‘Luggage’ is uncountable: not ‘many’.', 'No plural for ‘luggage’.', 'No plural and not ‘many’.'],
   'Uncountable: how much luggage. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Plural', 'I need new ___ — mine are broken.', ['glasses', 'glass', 'a glass', 'glasss'],
   ['‘Glass’ (material) is different from ‘glasses’ (spectacles).', '‘A glass’ is for drinking.', 'Not a word.'],
   'Spectacles: glasses (always plural). Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Uncountable', 'Let me give you ___ help with that.', ['some', 'a', 'an', 'many'],
   ['‘Help’ is uncountable.', '‘Help’ is uncountable.', '‘Many’ goes with countables.'],
   'Uncountable: some help. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('Plural uncountable', 'She gave me some useful *advices*.', 'advice', '‘Advice’ is uncountable: no -s. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Plural uncountable', 'We bought new *furnitures* for the living room.', 'furniture', '‘Furniture’ is uncountable: no -s. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Plural uncountable', 'I have too many *homeworks*.', 'exercises', '‘Homework’ is uncountable; with ‘many’ use a countable noun like ‘exercises’.'),
  ('Plural uncountable', 'Can you give me more *informations*?', 'information', '‘Information’ is uncountable: no -s. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Plural uncountable', 'Our *luggages* are in the car.', 'bags', '‘Luggage’ is uncountable; ‘bags’ is countable and fits ‘are’.'),
  ('A + uncountable', 'Can I have *a* bread, please?', 'some', '‘Bread’ is uncountable: ‘some bread’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('A + uncountable', 'He has *a* good news for you.', 'some', '‘News’ is uncountable: ‘some good news’.'),
  ('A + uncountable', 'We need *an* information.', 'some', '‘Information’ is uncountable: ‘some information’.'),
  ('Plural verb', 'The news *are* on at nine.', 'is', '‘News’ takes a singular verb. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Plural verb', 'The weather *were* lovely yesterday.', 'was', '‘Weather’ is uncountable: singular verb.'),
  ('Plural verb', 'Your money *are* on the table.', 'is', '‘Money’ is uncountable: singular verb. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Much + countable', 'There aren’t *much* chairs in the room.', 'many', '‘Chairs’ is plural countable: ‘many’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Much + countable', 'How *much* friends do you have?', 'many', '‘Friends’ is plural countable: ‘how many’.'),
  ('Many + uncountable', 'I don’t drink *many* water.', 'much', '‘Water’ is uncountable: ‘much’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Many + uncountable', 'There isn’t *many* time left.', 'much', '‘Time’ is uncountable here: ‘much’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Singular after number', 'I have three *brother*.', 'brothers', 'After ‘three’ use the plural: ‘brothers’.'),
  ('Wrong plural', 'Two *childs* are playing outside.', 'children', 'Irregular plural: ‘children’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Wrong plural', 'There are four *persons* waiting.', 'people', 'Normal plural of ‘person’: ‘people’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Singular after number', 'We’ve got two *dog* and a cat.', 'dogs', 'After ‘two’ use the plural: ‘dogs’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Unit word', 'I drank a *bottle* of tea.', 'cup', 'We normally say ‘a cup of tea’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, countable or not, multiple choice and spot-the-mistake. In the typing questions write one word. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('type', 'Countable or not?'),
 'fill': [
  ('Uncountable', 'I need [[some]] help with my project.', 'a / some', '‘Help’ is uncountable, so we use ‘some’, not ‘a’.', 'Uncountable → some.'),
  ('Many / much', 'How [[many]] eggs do we need?', 'many / much', '‘Eggs’ is plural countable: ‘how many’. Ask: can I put a number in front? Yes → countable; no → uncountable.', 'Countable → many.'),
  ('Singular verb', 'The news [[is]] on TV now.', 'is / are', '‘News’ is uncountable: singular verb. Ask: can I put a number in front? Yes → countable; no → uncountable.', 'Uncountable → singular verb.'),
  ('Plural', 'I saw three [[mice]] in the barn.', 'mouse', 'Irregular plural of ‘mouse’: ‘mice’. Ask: can I put a number in front? Yes → countable; no → uncountable.', 'Irregular plural.'),
  ],
 'order': [
  ('Uncountable', 'I need some advice.', []),
  ('Many / much', 'How much money is it?', []),
  ('Unit word', 'I want a slice of pizza.', []),
  ('Plural', 'There are two buses.', []),
  ],
 'customItems': [
  ('Type', 'Which noun is uncountable?', ['luggage', 'suitcase', 'bag', 'ticket'],
   ['‘Suitcase’ is countable: two suitcases.', '‘Bag’ is countable.', '‘Ticket’ is countable.'],
   '‘Luggage’ has no plural. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Type', 'Which noun is countable?', ['coin', 'money', 'cash', 'gold'],
   ['‘Money’ is uncountable.', '‘Cash’ is uncountable.', '‘Gold’ (metal) is uncountable.'],
   'You can count coins: two coins. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Type', 'Which pair is countable + uncountable with the same idea?', ['job / work', 'job / jobs', 'work / homework', 'car / bus'],
   ['That’s singular / plural of one noun.', 'Both are uncountable.', 'Both are countable.'],
   'A job (countable) / work (uncountable). Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Type', 'Why ‘two coffees’ is correct?', ['it means two cups', 'coffee is always countable', 'it’s a mistake', 'it means two kinds of milk'],
   ['Coffee as a drink in general is uncountable.', 'It’s correct in a café.', 'It has nothing to do with milk.'],
   'In a café, ‘a coffee’ = a cup of coffee. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ],
 'mc': [
  ('Uncountable', 'There’s ___ cheese in the fridge.', ['some', 'a', 'many', 'an'],
   ['‘Cheese’ in general is uncountable.', '‘Many’ goes with countables.', 'No ‘an’ with uncountables.'],
   'Uncountable: some cheese. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Many / much', 'We didn’t take ___ photos.', ['many', 'much', 'a', 'little'],
   ['‘Photos’ is plural countable.', 'No ‘a’ with plurals.', '‘Little’ goes with uncountables.'],
   'Plural countable: many photos. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Singular verb', 'Physics ___ difficult for me.', ['is', 'are', 'were', 'have'],
   ['Subjects take a singular verb.', 'Plural/past form.', '‘Have’ doesn’t fit.'],
   'Physics is singular. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Unit word', 'He ate three ___ of chocolate.', ['pieces', 'chocolates', 'piece', 'much'],
   ['‘Three chocolates’ means individual sweets — different meaning.', 'After ‘three’ use the plural.', '‘Much’ doesn’t fit here.'],
   'Count with a unit: three pieces of chocolate.'),
  ],
 'error': [
  ('Plural uncountable', 'I need some *informations*.', 'information', '‘Information’ has no plural. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('A + uncountable', 'She gave me *an* advice.', 'some', '‘Advice’ is uncountable. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Much + countable', 'There are too *much* cars.', 'many', '‘Cars’ is countable: ‘many’. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ('Plural verb', 'My hair *are* wet.', 'is', '‘Hair’ is uncountable: singular verb. Ask: can I put a number in front? Yes → countable; no → uncountable.'),
  ],
}
