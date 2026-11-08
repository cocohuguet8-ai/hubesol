TITLE = 'Order of Adjectives'
AUX = (['opinion', 'size', 'age', 'colour'], None, 'size')
NEXT = ('All nouns & determiners', '/grammar/nouns-determiners/')
BODY = r'''
## The basic order

When we use two or more adjectives **before a noun**, they usually follow this order:

| 1 Opinion | 2 Size | 3 Age | 4 Shape | 5 Colour | 6 Origin | 7 Material | 8 Purpose | **Noun** |
|---|---|---|---|---|---|---|---|---|
| lovely | big | old | round | red | Italian | wooden | dining | **table** |

- a **beautiful old** house
- a **small black** cat
- an **expensive Italian leather** bag

Short memory trick: **OSASCOMP** (Opinion, Size, Age, Shape, Colour, Origin, Material, Purpose).

## Opinion first, facts after

### 1. Opinion adjectives

What you **think**: *nice, lovely, ugly, amazing, boring, delicious*

### 2. Fact adjectives

What **is** true: *big, new, round, blue, French, cotton*

- a **delicious** hot soup — a **boring** long film

> ⚠️ Typical error: ~~a red lovely dress~~ → Opinion first: *a lovely red dress.*

## Size, age, shape

- a **big old** car (size → age)
- a **small round** table (size → shape)
- a **long thin** face (size → shape)

> ⚠️ Typical error: ~~an old big house~~ → *a big old house.*

## Colour, origin, material

- a **white Spanish** wine (colour → origin)
- a **Japanese silk** scarf (origin → material)
- a **blue cotton** shirt (colour → material)

## Purpose: next to the noun

The purpose word says **what it's for** and goes right before the noun:

- **running** shoes, a **sleeping** bag, a **wine** glass

## Commas and *and*

### 1. Before the noun: usually no comma between different types

- a **tall young** man (~~a tall, young man~~ is possible but less common)

### 2. Two adjectives of the same type: comma or *and*

- a **cheap, comfortable** hotel (two opinions)

### 3. After the verb (*be, look, seem*): use *and*

- The house is **old and beautiful**. — She looks **tired and happy**.

## How many adjectives?

In real English, we rarely use more than **three** adjectives before a noun. Too many sounds unnatural.

## Common mistakes

**1. Colour before size.** *~~a black small dog~~* → **a small black dog**.

**2. Material before colour.** *~~a wooden brown box~~* → **a brown wooden box**.

**3. Opinion after facts.** *~~a new nice phone~~* → **a nice new phone**.

**4. No *and* after *be*.** *~~The film was long boring.~~* → **long and boring**.

**Pro tip:** start with what you **think**, finish with what it's **made of** or **for**.
'''

GAP = ('Fill in the gaps',
  'Put the two adjectives in brackets in the correct order. Twenty original sentences.',
  [
  ('Opinion + colour', 'She bought a [[lovely red]] dress. (red / lovely)', 'two adjectives', 'Opinion before colour: ‘lovely red’. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Size + colour', 'They have a [[small black]] dog. (black / small)', 'two adjectives', 'Size before colour: ‘small black’. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Size + age', 'We live in a [[big old]] house. (old / big)', 'two adjectives', 'Size before age: ‘big old’. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Opinion + age', 'He has a [[nice new]] phone. (new / nice)', 'two adjectives', 'Opinion before age: ‘nice new’. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Colour + material', 'I need a [[blue cotton]] shirt. (cotton / blue)', 'two adjectives', 'Colour before material: ‘blue cotton’. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Origin + material', 'She wore a [[Japanese silk]] scarf. (silk / Japanese)', 'two adjectives', 'Origin before material: ‘Japanese silk’. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Age + origin', 'They drive an [[old German]] car. (German / old)', 'two adjectives', 'Age before origin: ‘old German’. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Size + shape', 'There’s a [[small round]] table in the corner. (round / small)', 'two adjectives', 'Size before shape: ‘small round’. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Opinion + size', 'What a [[beautiful big]] garden! (big / beautiful)', 'two adjectives', 'Opinion before size. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Colour + origin', 'Would you like some [[white Spanish]] wine? (Spanish / white)', 'two adjectives', 'Colour before origin. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Material + purpose', 'I bought some [[leather walking]] boots. (walking / leather)', 'two adjectives', 'Purpose goes next to the noun: ‘leather walking boots’.'),
  ('Age + colour', 'He wore an [[old grey]] coat. (grey / old)', 'two adjectives', 'Age before colour. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Opinion + origin', 'We had a [[delicious Italian]] meal. (Italian / delicious)', 'two adjectives', 'Opinion before origin. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Size + material', 'It’s a [[tiny plastic]] toy. (plastic / tiny)', 'two adjectives', 'Size before material. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Shape + colour', 'She has a [[long blonde]] ponytail. (blonde / long)', 'two adjectives', 'Shape/length before colour. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Opinion + shape', 'They live in a [[strange square]] house. (square / strange)', 'two adjectives', 'Opinion before shape. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Age + material', 'My grandma has a [[new wooden]] kitchen. (wooden / new)', 'two adjectives', 'Age before material. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Colour + purpose', 'I lost my [[red running]] shoes. (running / red)', 'two adjectives', 'Purpose next to the noun. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('After be', 'The film was long [[and]] boring.', 'and / ,', 'After ‘be’, join adjectives with ‘and’. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('After be', 'Our hotel was cheap [[and]] comfortable.', 'and / ,', 'After ‘be’: ‘cheap and comfortable’. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with adjective order.',
  [
  ('Opinion + colour', 'She has a lovely red dress.', []),
  ('Size + colour', 'I saw a small black cat.', []),
  ('Size + age', 'They live in a big old house.', []),
  ('Opinion + age', 'He bought a nice new car.', []),
  ('Colour + material', 'I want a blue cotton shirt.', []),
  ('Origin + material', 'It’s a Chinese silk scarf.', []),
  ('Age + origin', 'He drives an old French car.', []),
  ('Size + shape', 'We have a small round table.', []),
  ('Opinion + size', 'It’s a beautiful big garden.', []),
  ('Three adjectives', 'It’s a lovely old wooden house.', []),
  ('Three adjectives', 'She wore a long black silk dress.', []),
  ('Three adjectives', 'I bought a small white plastic box.', []),
  ('Purpose', 'I need new running shoes.', []),
  ('Purpose', 'Take your warm sleeping bag.', []),
  ('After be', 'The room was clean and bright.', []),
  ('After be', 'She looks tired and happy.', []),
  ('Opinion + origin', 'We ate delicious Indian food.', []),
  ('Age + colour', 'He wore an old blue jacket.', []),
  ('Size + material', 'It’s a tiny glass bottle.', []),
  ('Opinion + shape', 'What a strange round building!', []),
  ])

MATCH = {'title': 'Which category?', 'subtitle': 'Tap an adjective, then tap its category.',
  'leftLabel': 'Adjective', 'rightLabel': 'Category', 'rightLabelSub': '', 'reviewArrowPrefix': '',
  'pairs': [
  ('beautiful', 'opinion'), ('huge', 'size'), ('ancient', 'age'), ('round', 'shape'), ('purple', 'colour'),
  ('Mexican', 'origin'), ('woollen', 'material'), ('ugly', 'opinion'), ('tiny', 'size'), ('modern', 'age'),
  ('square', 'shape'), ('green', 'colour'), ('Greek', 'origin'), ('metal', 'material'), ('delicious', 'opinion'),
  ('enormous', 'size'), ('young', 'age'), ('oval', 'shape'), ('pink', 'colour'), ('cotton', 'material'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Opinion → size → age → shape → colour → origin → material → purpose → noun.',
  [
  ('Opinion + colour', 'She wore ___ to the party.', ['a gorgeous blue dress', 'a blue gorgeous dress', 'a dress gorgeous blue', 'a gorgeous dress blue'],
   ['Opinion goes before colour.', 'Adjectives go before the noun.', 'Both adjectives go before the noun.'],
   'Opinion → colour: a gorgeous blue dress. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Size + age', 'My grandparents have ___.', ['a big old farmhouse', 'an old big farmhouse', 'a farmhouse big old', 'a big farmhouse old'],
   ['Size goes before age.', 'Adjectives go before the noun.', 'Both adjectives go before the noun.'],
   'Size → age. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Size + colour', 'There’s ___ in the garden.', ['a little white rabbit', 'a white little rabbit', 'a rabbit little white', 'a little rabbit white'],
   ['Size goes before colour.', 'Adjectives go before the noun.', 'Both go before the noun.'],
   'Size → colour. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Colour + material', 'He gave me ___.', ['a black leather wallet', 'a leather black wallet', 'a wallet black leather', 'a black wallet leather'],
   ['Colour goes before material.', 'Adjectives go before the noun.', 'Both go before the noun.'],
   'Colour → material. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Origin + material', 'I bought ___ in Peru.', ['a Peruvian wool hat', 'a wool Peruvian hat', 'a hat Peruvian wool', 'a Peruvian hat wool'],
   ['Origin goes before material.', 'Adjectives go before the noun.', 'Both go before the noun.'],
   'Origin → material. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Opinion + age', 'That’s ___!', ['a cool new bike', 'a new cool bike', 'a bike cool new', 'a cool bike new'],
   ['Opinion goes before age.', 'Adjectives go before the noun.', 'Both go before the noun.'],
   'Opinion → age. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Age + origin', 'We watched ___.', ['an old American film', 'an American old film', 'a film old American', 'an old film American'],
   ['Age goes before origin.', 'Adjectives go before the noun.', 'Both go before the noun.'],
   'Age → origin. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Size + shape', 'She has ___.', ['a small oval mirror', 'an oval small mirror', 'a mirror small oval', 'a small mirror oval'],
   ['Size goes before shape.', 'Adjectives go before the noun.', 'Both go before the noun.'],
   'Size → shape. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Purpose', 'Don’t forget your ___.', ['new swimming costume', 'swimming new costume', 'costume new swimming', 'new costume swimming'],
   ['The purpose word goes next to the noun.', 'Adjectives go before the noun.', 'Purpose goes right before the noun.'],
   'Purpose next to the noun. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Three adjectives', 'They live in ___.', ['a lovely little wooden cottage', 'a wooden lovely little cottage', 'a little wooden lovely cottage', 'a lovely wooden little cottage'],
   ['Material goes near the noun, opinion first.', 'Opinion goes first.', 'Size goes before material.'],
   'Opinion → size → material. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Three adjectives', 'He drives ___.', ['a fast red Italian car', 'a red fast Italian car', 'an Italian fast red car', 'a fast Italian red car'],
   ['Opinion goes before colour.', 'Origin goes after colour.', 'Colour goes before origin.'],
   'Opinion → colour → origin. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('After be', 'The weather was ___.', ['cold and windy', 'cold windy', 'windy cold and', 'and cold windy'],
   ['After ‘be’, join with ‘and’.', 'Wrong position of ‘and’.', 'Wrong position of ‘and’.'],
   'After be: cold and windy. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Opinion + size', 'What ___!', ['a wonderful huge beach', 'a huge wonderful beach', 'a beach wonderful huge', 'a wonderful beach huge'],
   ['Opinion goes before size.', 'Adjectives go before the noun.', 'Both go before the noun.'],
   'Opinion → size. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Age + colour', 'I found ___ in the attic.', ['an old brown suitcase', 'a brown old suitcase', 'a suitcase old brown', 'an old suitcase brown'],
   ['Age goes before colour.', 'Adjectives go before the noun.', 'Both go before the noun.'],
   'Age → colour. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Size + material', 'She keeps her rings in ___.', ['a tiny silver box', 'a silver tiny box', 'a box tiny silver', 'a tiny box silver'],
   ['Size goes before material.', 'Adjectives go before the noun.', 'Both go before the noun.'],
   'Size → material. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Shape + colour', 'He has ___.', ['a long grey beard', 'a grey long beard', 'a beard long grey', 'a long beard grey'],
   ['Shape/length goes before colour.', 'Adjectives go before the noun.', 'Both go before the noun.'],
   'Shape → colour. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Which', 'Which is correct?', ['a nice big blue ball', 'a big nice blue ball', 'a blue big nice ball', 'a nice blue big ball'],
   ['Opinion first.', 'Opinion first.', 'Size before colour.'],
   'Opinion → size → colour. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Which', 'Which is correct?', ['a modern Spanish glass building', 'a glass modern Spanish building', 'a Spanish modern glass building', 'a modern glass Spanish building'],
   ['Material goes last.', 'Age before origin.', 'Origin before material.'],
   'Age → origin → material. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Opinion + material', 'She bought ___.', ['an elegant silk blouse', 'a silk elegant blouse', 'a blouse elegant silk', 'an elegant blouse silk'],
   ['Opinion goes before material.', 'Adjectives go before the noun.', 'Both go before the noun.'],
   'Opinion → material. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Colour + origin', 'We tried ___.', ['some red French wine', 'some French red wine', 'some wine red French', 'some red wine French'],
   ['Colour usually goes before origin.', 'Adjectives go before the noun.', 'Both go before the noun.'],
   'Colour → origin. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake with an adjective. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('Material form', 'I bought a small brown *wood* box.', 'wooden', 'As an adjective, ‘wood’ becomes ‘wooden’: ‘a small brown wooden box’.'),
  ('Material form', 'She wore a lovely red *wool* jumper.', 'woollen', 'The adjective is ‘woollen’: ‘a lovely red woollen jumper’.'),
  ('Material form', 'He has a beautiful old *gold* ring.', 'golden', 'Here we need the adjective ‘golden’ (‘gold ring’ as a compound is also common).'),
  ('Origin form', 'We had a delicious *Italy* dinner.', 'Italian', 'Origin adjective: ‘Italian’, not the country name.'),
  ('Origin form', 'She drives an old *Germany* car.', 'German', 'Origin adjective: ‘German’. Check the adjective’s form: no plural -s, and the right adjective (not the noun or country).'),
  ('Origin form', 'I love this cheap *France* wine.', 'French', 'Origin adjective: ‘French’. Check the adjective’s form: no plural -s, and the right adjective (not the noun or country).'),
  ('Origin form', 'She has a beautiful *China* vase.', 'Chinese', 'Origin adjective: ‘Chinese’. Check the adjective’s form: no plural -s, and the right adjective (not the noun or country).'),
  ('Origin form', 'They live in a lovely old *Spain* village.', 'Spanish', 'Origin adjective: ‘Spanish’. Check the adjective’s form: no plural -s, and the right adjective (not the noun or country).'),
  ('Plural adjective', 'They have two small *blacks* cats.', 'black', 'Adjectives never take -s in English. Check the adjective’s form: no plural -s, and the right adjective (not the noun or country).'),
  ('Plural adjective', 'She bought some lovely *news* shoes.', 'new', 'Adjectives never take -s. Check the adjective’s form: no plural -s, and the right adjective (not the noun or country).'),
  ('Plural adjective', 'We saw three *bigs* old trees.', 'big', 'Adjectives never take -s: ‘three big old trees’.'),
  ('Plural adjective', 'I need two *reds* cotton T-shirts.', 'red', 'Adjectives never take -s: ‘two red cotton T-shirts’.'),
  ('Article', 'It’s *a* old wooden house.', 'an', 'The article goes with the first adjective: ‘old’ starts with a vowel sound → ‘an old wooden house’.'),
  ('Article', 'She has *an* beautiful old car.', 'a', 'The first adjective is ‘beautiful’ (consonant sound) → ‘a beautiful old car’.'),
  ('Missing and', 'The lesson was long *boring*.', 'and boring', 'After ‘be’, join two adjectives with ‘and’: ‘long and boring’.'),
  ('Missing and', 'She seems kind *friendly*.', 'and friendly', 'After ‘seem’, join two adjectives with ‘and’: ‘kind and friendly’.'),
  ('Missing and', 'The room looks clean *bright*.', 'and bright', 'After ‘look’, join two adjectives with ‘and’: ‘clean and bright’.'),
  ('-ed / -ing', 'It was a long and *bored* film.', 'boring', 'The film causes the feeling: ‘boring’ (people feel ‘bored’).'),
  ('-ed / -ing', 'What an *interested* old building!', 'interesting', 'The building causes the feeling: ‘interesting’.'),
  ('-ed / -ing', 'The kids were tired and *exciting* after the trip.', 'excited', 'People feel ‘excited’; a thing is ‘exciting’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, which category, multiple choice and spot-the-mistake. In the typing questions write the two adjectives in the correct order. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('category', 'Which category?'),
 'fill': [
  ('Opinion + colour', 'He has a [[cute brown]] puppy. (brown / cute)', 'two adjectives', 'Opinion before colour. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.', 'Opinion first. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Size + age', 'We stayed in a [[small old]] hotel. (old / small)', 'two adjectives', 'Size before age. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.', 'Size → age.'),
  ('Colour + material', 'She has a [[green glass]] vase. (glass / green)', 'two adjectives', 'Colour before material. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.', 'Colour → material.'),
  ('After be', 'The room was warm [[and]] cosy.', 'and / ,', 'After ‘be’, use ‘and’. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.', 'After be → and.'),
  ],
 'order': [
  ('Size + colour', 'It’s a big red bus.', []),
  ('Opinion + age', 'She has a nice old bike.', []),
  ('Origin + material', 'I love Italian leather shoes.', []),
  ('After be', 'He is tall and thin.', []),
  ],
 'customItems': [
  ('Category', '‘Enormous’ is an adjective of…', ['size', 'opinion', 'age', 'material'],
   ['It describes how big, not what you think.', 'It isn’t about age.', 'It isn’t a material.'],
   'Size. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Category', '‘Woollen’ is an adjective of…', ['material', 'colour', 'origin', 'shape'],
   ['It isn’t a colour.', 'It isn’t a place.', 'It isn’t a shape.'],
   'Material. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Category', 'Which goes FIRST?', ['opinion', 'colour', 'material', 'origin'],
   ['Colour is in the middle.', 'Material is near the end.', 'Origin is near the end.'],
   'Opinion first. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Category', 'Which goes right before the noun?', ['purpose', 'opinion', 'size', 'age'],
   ['Opinion goes first.', 'Size is early.', 'Age is early.'],
   'Purpose: running shoes. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ],
 'mc': [
  ('Size + colour', 'There was ___ on the table.', ['a small green bottle', 'a green small bottle', 'a bottle small green', 'a small bottle green'],
   ['Size before colour.', 'Adjectives before the noun.', 'Both before the noun.'],
   'Size → colour. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Opinion + origin', 'We visited ___.', ['a charming French village', 'a French charming village', 'a village charming French', 'a charming village French'],
   ['Opinion before origin.', 'Adjectives before the noun.', 'Both before the noun.'],
   'Opinion → origin. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('Three adjectives', 'She has ___.', ['a beautiful long white dress', 'a white long beautiful dress', 'a long beautiful white dress', 'a beautiful white long dress'],
   ['Opinion first.', 'Opinion before shape/length.', 'Length before colour.'],
   'Opinion → shape → colour. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ('After be', 'The soup was ___.', ['hot and delicious', 'hot delicious', 'delicious and hot and', 'and hot delicious'],
   ['After ‘be’, use ‘and’.', 'Extra ‘and’.', 'Wrong position.'],
   'After be: hot and delicious. Order: opinion → size → age → shape → colour → origin → material → purpose → noun.'),
  ],
 'error': [
  ('Origin form', 'I love *Japan* food.', 'Japanese', 'Origin adjective: ‘Japanese’. Check the adjective’s form: no plural -s, and the right adjective (not the noun or country).'),
  ('Material form', 'A big *glasses* bottle.', 'glass', 'Material before a noun: ‘glass’ (‘glasses’ are spectacles).'),
  ('Plural adjective', 'Two *whites* rabbits.', 'white', 'Adjectives never take -s. Check the adjective’s form: no plural -s, and the right adjective (not the noun or country).'),
  ('Article', 'It’s *a* amazing old castle.', 'an', '‘Amazing’ starts with a vowel sound: ‘an amazing old castle’.'),
  ],
}
