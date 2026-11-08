TITLE = 'Some & Any'
AUX = (['some', 'any'], None, 'any')
NEXT = ('Much, Many & A lot of', '/grammar/nouns-determiners/much-many-a-lot-of/')
BODY = r'''
## The basic rule

| | **some** | **any** |
|---|---|---|
| Positive | I've got **some** money. | — |
| Negative | — | I haven't got **any** money. |
| Question | Would you like **some** tea? (offer) | Have you got **any** tea? |
| Nouns | plural countable + uncountable | plural countable + uncountable |

## When to use *some*

### 1. Positive sentences

- There are **some** apples in the bowl. — I need **some** help.

### 2. Offers

- Would you like **some** cake?

### 3. Requests

- Can I have **some** water, please? — Could you lend me **some** money?

> ⚠️ Typical error: ~~Would you like any coffee?~~ → In offers use *some*: *Would you like some coffee?*

## When to use *any*

### 1. Negative sentences

- There aren't **any** eggs. — I don't have **any** time.

### 2. Most questions

- Are there **any** questions? — Did you buy **any** bread?

### 3. With negative words: *never, without, hardly*

- He left **without** **any** money. — I **never** have **any** free time.

> ⚠️ Typical error: ~~I don't have some friends here.~~ → *I don't have any friends here.*

### 4. *Any* in positives = "it doesn't matter which"

- Take **any** seat you like. — **Any** student can join the club.

## Compounds

| | some- | any- |
|---|---|---|
| people | **someone / somebody** | **anyone / anybody** |
| things | **something** | **anything** |
| places | **somewhere** | **anywhere** |

- There's **someone** at the door. — Is there **anyone** at home?
- I didn't see **anything**. — Let's go **somewhere** nice.

## *Some / any* vs *no*

*No* = *not any*. Use it with a **positive** verb.

| not … any | no |
|---|---|
| There aren't **any** chairs. | There are **no** chairs. |
| I haven't got **any** money. | I've got **no** money. |

> ⚠️ Typical error: ~~I haven't got no money.~~ → Double negative: *I haven't got any money / I've got no money.*

## Common mistakes

**1. *Some* in negatives.** *~~We don't have some milk.~~* → **any milk**.

**2. *Any* in offers.** *~~Do you want any help? (offering)~~* → **Would you like some help?**

**3. Double negative.** *~~I didn't buy nothing.~~* → **I didn't buy anything.**

**4. *Some* / *any* with singular countables.** *~~some book~~* → **a book**.

**Pro tip:** expect a *yes*? → **some**. Negative or real question? → **any**.
'''

GAP = ('Fill in the gaps',
  'Type some, any, or a compound (someone, anything…). Twenty original sentences.',
  [
  ('Positive', 'There are [[some]] biscuits in the tin.', 'some / any', 'Positive sentence: ‘some’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Positive', 'I bought [[some]] fruit at the market.', 'some / any', 'Positive + uncountable: ‘some fruit’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Negative', 'There aren’t [[any]] tomatoes left.', 'some / any', 'Negative sentence: ‘any’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Negative', 'I don’t have [[any]] homework today.', 'some / any', 'Negative + uncountable: ‘any homework’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Question', 'Have you got [[any]] brothers or sisters?', 'some / any', 'Real question: ‘any’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Question', 'Is there [[any]] milk in the fridge?', 'some / any', 'Question about existence: ‘any’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Offer', 'Would you like [[some]] orange juice?', 'some / any', 'Offers use ‘some’: we expect a yes. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Request', 'Can I have [[some]] paper, please?', 'some / any', 'Requests use ‘some’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Request', 'Could you give me [[some]] advice?', 'some / any', 'Polite request: ‘some advice’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Negative word', 'She left without [[any]] money.', 'some / any', '‘Without’ is negative: ‘any’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Negative word', 'He never has [[any]] free time.', 'some / any', '‘Never’ makes the sentence negative: ‘any’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Any = no matter which', 'You can sit in [[any]] chair you like.', 'some / any', '‘Any’ in a positive = it doesn’t matter which. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Compound', 'There’s [[someone|somebody]] at the door.', 'someone / anyone', 'Positive: ‘someone’ (or ‘somebody’). Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Compound', 'Is there [[anyone|anybody]] at home?', 'someone / anyone', 'Question: ‘anyone’ (or ‘anybody’). Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Compound', 'I didn’t see [[anything]] strange.', 'something / anything', 'Negative: ‘anything’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Compound', 'I want to eat [[something]] sweet.', 'something / anything', 'Positive: ‘something’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Compound', 'Let’s go [[somewhere]] quiet.', 'somewhere / anywhere', 'Positive suggestion: ‘somewhere’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Compound', 'I can’t find my keys [[anywhere]].', 'somewhere / anywhere', 'Negative: ‘anywhere’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('No', 'There are [[no]] buses after midnight.', 'any / no', 'Positive verb + ‘no’ = there aren’t any. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Offer', 'Would you like [[something]] to drink?', 'something / anything', 'Offers use some-compounds: ‘something’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with some and any.',
  [
  ('Positive', 'I have some money.', []),
  ('Positive', 'There are some eggs.', []),
  ('Negative', 'I don’t have any time.', []),
  ('Negative', 'There isn’t any milk.', []),
  ('Question', 'Have you got any pets?', []),
  ('Question', 'Is there any bread?', []),
  ('Offer', 'Would you like some tea?', []),
  ('Request', 'Can I have some water?', []),
  ('Negative word', 'He left without any money.', []),
  ('Any = no matter which', 'Take any seat.', []),
  ('Compound', 'Someone is calling you.', []),
  ('Compound', 'Is anyone there?', []),
  ('Compound', 'I didn’t see anything.', []),
  ('Compound', 'Let’s go somewhere nice.', []),
  ('Compound', 'I can’t find it anywhere.', []),
  ('No', 'There are no chairs.', []),
  ('No', 'I have no idea.', []),
  ('Offer', 'Do you want something to eat?', []),
  ('Negative', 'We didn’t buy any bread.', []),
  ('Positive', 'I need some help.', []),
  ])

MATCH = {'title': 'Some or any?', 'subtitle': 'Tap a sentence, then tap the word that fills the gap.',
  'leftLabel': 'Sentence', 'rightLabel': 'Word', 'rightLabelSub': '(some / any)', 'reviewArrowPrefix': '',
  'pairs': [
  ('I’ve got ___ sweets.', 'some'), ('I haven’t got ___ sweets.', 'any'), ('Have you got ___ sweets?', 'any'),
  ('Would you like ___ sweets?', 'some'), ('There’s ___ rice left.', 'some'), ('There isn’t ___ rice left.', 'any'),
  ('Can I have ___ salt?', 'some'), ('Did you meet ___ new friends?', 'any'), ('She went out without ___ coat.', 'any'),
  ('Choose ___ colour you like.', 'any'), ('We need ___ more chairs.', 'some'), ('They never eat ___ meat.', 'any'),
  ('Could you buy ___ bread?', 'some'), ('Are there ___ good films on?', 'any'), ('I made ___ mistakes.', 'some'),
  ('I didn’t make ___ mistakes.', 'any'), ('Would you like ___ help?', 'some'), ('Is there ___ sugar?', 'any'),
  ('He gave me ___ flowers.', 'some'), ('We don’t have ___ plans.', 'any'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Positive, offers, requests → some. Negatives and real questions → any.',
  [
  ('Negative', 'We didn’t see ___ dolphins on the trip.', ['any', 'some', 'no', 'a'],
   ['Negatives use ‘any’, not ‘some’.', '‘Didn’t’ + ‘no’ is a double negative.', '‘A’ doesn’t go with plurals.'],
   'Negative: any. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Offer', 'Would you like ___ more soup?', ['some', 'any', 'no', 'a'],
   ['Offers use ‘some’ because we expect a yes.', '‘No’ doesn’t fit an offer.', '‘Soup’ here is uncountable.'],
   'Offer: some. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Question', 'Are there ___ good restaurants near here?', ['any', 'some', 'no', 'a'],
   ['A real question normally uses ‘any’.', '‘No’ doesn’t fit a question like this.', '‘A’ doesn’t go with plurals.'],
   'Real question: any. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Positive', 'I’ve got ___ good news for you!', ['some', 'any', 'a', 'many'],
   ['Positive sentences use ‘some’.', '‘News’ is uncountable: no ‘a’.', '‘Many’ goes with countables.'],
   'Positive + uncountable: some. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Request', 'Could you pass me ___ napkins, please?', ['some', 'any', 'no', 'a'],
   ['Requests use ‘some’.', '‘No’ doesn’t fit a request.', '‘A’ doesn’t go with plurals.'],
   'Request: some. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Negative word', 'She did the test without ___ help.', ['any', 'some', 'no', 'a'],
   ['‘Without’ is negative: use ‘any’.', '‘Without no’ is a double negative.', '‘Help’ is uncountable.'],
   'Without + any. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Any = no matter which', 'Call me ___ time — I’m always free.', ['any', 'some', 'no', 'a'],
   ['‘Some time’ means at a certain time, not ‘whenever’.', '‘No time’ means never.', '‘A time’ doesn’t give this meaning.'],
   '‘Any’ = it doesn’t matter which. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Compound', 'Did ___ phone me while I was out?', ['anyone', 'someone', 'no one', 'anything'],
   ['A real question normally uses ‘anyone’.', '‘Did no one phone me?’ changes the meaning.', '‘Anything’ is for things, not people.'],
   'Question about people: anyone. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Compound', 'I’m bored. Let’s do ___ fun.', ['something', 'anything', 'nothing', 'somewhere'],
   ['Positive suggestion: ‘something’.', '‘Do nothing fun’ is the opposite.', '‘Somewhere’ is for places.'],
   'Positive: something. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Compound', 'I looked everywhere, but I couldn’t find it ___.', ['anywhere', 'somewhere', 'nowhere', 'anything'],
   ['Negative: ‘anywhere’.', '‘Couldn’t … nowhere’ is a double negative.', '‘Anything’ is for things.'],
   'Negative + place: anywhere. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('No', 'There’s ___ milk left — we need to buy some.', ['no', 'any', 'some', 'none'],
   ['‘There’s any milk’ is wrong in a positive.', '‘Some milk’ contradicts ‘we need to buy some’.', '‘None’ can’t go before a noun.'],
   'Positive verb + no = there isn’t any. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Double negative', 'I didn’t say ___ to her.', ['anything', 'nothing', 'something', 'no'],
   ['‘Didn’t … nothing’ is a double negative.', '‘Something’ is for positives.', '‘No’ needs a noun.'],
   'Negative + anything. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Offer', 'Can I get you ___ to drink?', ['something', 'anything', 'nothing', 'some'],
   ['Offers usually use ‘something’.', '‘Nothing’ doesn’t fit an offer.', '‘Some’ needs a noun after it.'],
   'Offer: something. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Question', 'Do you have ___ questions?', ['any', 'some', 'no', 'a'],
   ['Real question: ‘any’.', '‘No’ doesn’t fit.', 'No ‘a’ with plurals.'],
   'Question: any. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Singular countable', 'I need ___ pen. Can you lend me one?', ['a', 'some', 'any', 'no'],
   ['‘Some’ doesn’t go with a singular countable here.', '‘Any’ doesn’t fit a positive request.', '‘No’ changes the meaning.'],
   'Singular countable: a pen. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Negative', 'They haven’t got ___ children.', ['any', 'some', 'no', 'a'],
   ['Negatives use ‘any’.', '‘Haven’t … no’ is a double negative.', 'No ‘a’ with plurals.'],
   'Negative: any. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Which', 'Which sentence is correct?', ['I don’t have any money.', 'I don’t have some money.', 'I don’t have no money.', 'I have any money.'],
   ['Negatives use ‘any’.', 'Double negative.', '‘Any’ doesn’t go in this positive.'],
   'Negative: any money. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Which', 'Which sentence is correct?', ['Would you like some cake?', 'Would you like any cake?', 'Would you like no cake?', 'Would you like a some cake?'],
   ['Offers use ‘some’.', '‘No’ doesn’t fit an offer.', '‘A some’ isn’t English.'],
   'Offer: some cake. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Compound', 'There’s ___ in my eye!', ['something', 'anything', 'nothing', 'anyone'],
   ['Positive: not ‘anything’.', '‘Nothing’ is the opposite meaning.', '‘Anyone’ is for people.'],
   'Positive: something. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Compound', 'There isn’t ___ in the box. It’s empty.', ['anything', 'something', 'nothing', 'anywhere'],
   ['Negative: not ‘something’.', '‘Isn’t … nothing’ is a double negative.', '‘Anywhere’ is for places.'],
   'Negative: anything. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('Some in negative', 'We don’t have *some* eggs.', 'any', 'Negatives use ‘any’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Some in negative', 'There isn’t *some* sugar in my coffee.', 'any', 'Negative sentence: ‘any’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Some in negative', 'I didn’t buy *some* presents this year.', 'any', 'Negative: ‘any presents’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Some in question', 'Are there *some* problems with the computer?', 'any', 'A real question normally uses ‘any’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Any in positive', 'I’ve got *any* sweets in my pocket.', 'some', 'Positive sentence: ‘some’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Any in positive', 'There are *any* birds in the tree.', 'some', 'Positive: ‘some birds’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Any in offer', 'Would you like *any* biscuits?', 'some', 'Offers use ‘some’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Any in request', 'Can I have *any* water, please?', 'some', 'Requests use ‘some’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Negative word', 'He went out without *some* money.', 'any', '‘Without’ is negative: ‘any’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Negative word', 'She never eats *some* meat.', 'any', '‘Never’ is negative: ‘any’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Double negative', 'I haven’t got *no* friends here.', 'any', 'Double negative: ‘haven’t got any’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Double negative', 'They didn’t say *nothing*.', 'anything', 'Double negative: ‘didn’t say anything’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Double negative', 'We couldn’t find it *nowhere*.', 'anywhere', 'Double negative: ‘couldn’t find it anywhere’.'),
  ('Compound', 'Is there *someone* in the bathroom?', 'anyone', 'A real question: ‘anyone’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Compound', 'I didn’t hear *something*.', 'anything', 'Negative: ‘anything’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Compound', '*Anybody* is knocking at the door.', 'Somebody', 'Positive with a specific person: ‘Somebody’.'),
  ('Compound', 'Let’s go *anywhere* warm this summer.', 'somewhere', 'Positive suggestion: ‘somewhere’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Some + singular', 'Can you lend me *some* pen?', 'a', 'Singular countable: ‘a pen’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('No + negative', 'There aren’t *no* buses today.', 'any', 'Double negative: ‘aren’t any’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Any in offer', 'I’m making pasta — would you like *any*?', 'some', 'Offers use ‘some’: ‘would you like some?’'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, which situation, multiple choice and spot-the-mistake. In the typing questions write one word. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('situation', 'Which situation?'),
 'fill': [
  ('Negative', 'I haven’t got [[any]] cousins.', 'some / any', 'Negative sentence: ‘any’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.', 'Negative → any.'),
  ('Offer', 'Would you like [[some]] popcorn?', 'some / any', 'Offers use ‘some’.', 'Offer → some.'),
  ('Compound', 'Did you buy [[anything]] at the shop?', 'something / anything', 'Real question: ‘anything’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.', 'Question → any-.'),
  ('Compound', '[[Someone|Somebody|someone|somebody]] left a bag here.', 'someone / anyone', 'Positive: ‘someone’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.', 'Positive → some-.'),
  ],
 'order': [
  ('Negative', 'I don’t want any cake.', []),
  ('Offer', 'Would you like some juice?', []),
  ('Compound', 'Someone called you.', []),
  ('No', 'There is no time.', []),
  ],
 'customItems': [
  ('Situation', 'Why ‘some’ in ‘Can I have some water?’', ['it’s a request', 'it’s negative', 'it’s a real question', 'water is countable'],
   ['There’s no negative.', 'It’s a request, not a neutral question.', 'Water is uncountable — but that’s not why.'],
   'Requests use ‘some’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Situation', 'Why ‘any’ in ‘Take any book you want’?', ['it doesn’t matter which', 'it’s negative', 'it’s a question', 'it’s an offer of food'],
   ['There’s no negative.', 'It isn’t a question.', 'It isn’t about food.'],
   '‘Any’ in a positive = no matter which. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Situation', 'Why ‘any’ in ‘He left without any food’?', ['‘without’ is negative', 'it’s an offer', 'food is plural', 'it’s a request'],
   ['It isn’t an offer.', '‘Food’ isn’t plural.', 'It isn’t a request.'],
   'Negative words take ‘any’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Situation', '‘I’ve got no money’ means…', ['I haven’t got any money', 'I’ve got some money', 'I’ve got a little money', 'I want money'],
   ['It’s the opposite.', '‘No’ means zero.', 'It’s about having, not wanting.'],
   'No = not any. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ],
 'mc': [
  ('Question', 'Have you got ___ plans for Saturday?', ['any', 'some', 'no', 'a'],
   ['Real question: ‘any’.', '‘No’ doesn’t fit.', 'No ‘a’ with plurals.'],
   'Question: any. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Positive', 'We saw ___ beautiful birds in the park.', ['some', 'any', 'a', 'no'],
   ['Positive: ‘some’.', 'No ‘a’ with plurals.', '‘No’ changes the meaning.'],
   'Positive: some. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Compound', 'I’m not hungry. I don’t want ___.', ['anything', 'something', 'nothing', 'any'],
   ['Negative: ‘anything’.', 'Double negative.', '‘Any’ alone needs a noun here.'],
   'Negative: anything. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Request', 'Could I have ___ ketchup, please?', ['some', 'any', 'no', 'a'],
   ['Requests use ‘some’.', '‘No’ doesn’t fit a request.', '‘Ketchup’ is uncountable.'],
   'Request: some. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ],
 'error': [
  ('Some in negative', 'I don’t have *some* money.', 'any', 'Negative: ‘any’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Any in offer', 'Would you like *any* tea?', 'some', 'Offers use ‘some’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Double negative', 'I didn’t do *nothing*.', 'anything', 'Double negative. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ('Any in positive', 'I need *any* help.', 'some', 'Positive: ‘some’. Expect a yes (positive, offer, request)? → some. Negative or real question? → any.'),
  ],
}
