TITLE = 'The with Names & Places'
AUX = (['the'], None, 'the')
NEXT = ('Zero Article', '/grammar/articles/zero-article/')
BODY = r'''
## The basic rule

Most **single names** take **no article**. Names of **groups, plurals, seas, rivers and some institutions** take **the**.

| No article | **The** |
|---|---|
| Spain, France, Japan | **the** UK, **the** USA, **the** Netherlands |
| Lake Como, Mount Etna | **the** Alps, **the** Andes |
| Europe, Asia, Africa | **the** Atlantic, **the** Mediterranean |
| Oxford Street, Times Square | **the** Thames, **the** Nile |

## Countries and continents

### 1. Most countries and all continents: no article

- I live in **Spain**. — She's travelling around **Asia**.

### 2. Countries with *Republic, Kingdom, States* or a plural name: *the*

- **the** United Kingdom, **the** Czech Republic, **the** United States
- **the** Philippines, **the** Netherlands, **the** Maldives

> ⚠️ Typical error: ~~I visited the France.~~ → *I visited France.*

## Water

### 1. Oceans, seas, rivers and canals: *the*

- **the** Pacific, **the** Red Sea, **the** Danube, **the** Panama Canal

### 2. Lakes: no article

- **Lake** Geneva, **Lake** Victoria

> ⚠️ Typical error: ~~the Lake Garda~~ → *Lake Garda.*

## Mountains and islands

### 1. Mountain ranges and island groups: *the*

- **the** Pyrenees, **the** Himalayas, **the** Canary Islands

### 2. Single mountains and single islands: no article

- **Mount** Everest, **Mallorca**, **Sicily**

## Cities, streets and buildings

### 1. Cities, towns, streets, squares, parks: no article

- **Girona**, **Main Street**, **Central Park**, **Trafalgar Square**

### 2. Hotels, museums, theatres, cinemas: usually *the*

- **the** Ritz, **the** Louvre, **the** National Gallery, **the** Odeon

### 3. Places named after a person (with *'s*): no article

- **McDonald's**, **St Paul's** Cathedral, **Harrods**

## *The … of …* pattern

When a name has **of** in it, use *the*.

| Name | Example |
|---|---|
| the + … + of + … | **the** Tower of London, **the** University of Barcelona |
| no *of* | Barcelona University, London Bridge |

## Common mistakes

**1. *The* with single countries.** *~~the Italy~~* → **Italy**.

**2. No *the* with plural countries.** *~~Netherlands is flat.~~* → **The Netherlands** is flat.

**3. No *the* with rivers.** *~~Thames is long.~~* → **The Thames** is long.

**4. *The* with lakes or single mountains.** *~~the Mount Fuji~~* → **Mount Fuji**.

**Pro tip:** plural, group or water that flows → **the**; one single place → usually no article.
'''

GAP = ('Fill in the gaps',
  'Type the, or — (dash) when no article is needed. Twenty original sentences.',
  [
  ('Country', 'My cousin lives in [[—|-]] Germany.', 'the / —', 'Most countries take no article: ‘Germany’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Country', 'We flew to [[the]] United States last summer.', 'the / —', '‘States’ makes it a group: ‘the United States’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Country', 'Have you ever been to [[the]] Netherlands?', 'the / —', 'Plural country name: ‘the Netherlands’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Country', 'London is the capital of [[the]] UK.', 'the / —', '‘Kingdom’ countries take ‘the’: ‘the UK’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Continent', 'Kenya is in [[—|-]] Africa.', 'the / —', 'Continents take no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Ocean', 'They sailed across [[the]] Atlantic.', 'the / —', 'Oceans take ‘the’: ‘the Atlantic’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Sea', 'We swam in [[the]] Mediterranean.', 'the / —', 'Seas take ‘the’: ‘the Mediterranean’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('River', '[[The|the]] Ebro is the longest river in Catalonia.', 'the / —', 'Rivers take ‘the’: ‘the Ebro’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Lake', 'We had a picnic by [[—|-]] Lake Banyoles.', 'the / —', 'Lakes take no article: ‘Lake Banyoles’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Mountains', 'We go skiing in [[the]] Pyrenees.', 'the / —', 'Mountain ranges take ‘the’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Mountain', 'Have you climbed [[—|-]] Mount Kilimanjaro?', 'the / —', 'Single mountains take no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Islands', 'My grandparents live in [[the]] Balearic Islands.', 'the / —', 'Island groups take ‘the’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Island', 'We spent a week in [[—|-]] Menorca.', 'the / —', 'A single island: no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('City', 'She was born in [[—|-]] Paris.', 'the / —', 'Cities take no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Street', 'There’s a great café on [[—|-]] Oxford Street.', 'the / —', 'Streets take no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Park', 'Let’s go for a walk in [[—|-]] Hyde Park.', 'the / —', 'Parks take no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Museum', 'We saw the Mona Lisa at [[the]] Louvre.', 'the / —', 'Museums usually take ‘the’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Hotel', 'They stayed at [[the]] Hilton.', 'the / —', 'Hotels usually take ‘the’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Of pattern', 'We visited [[the]] Tower of London.', 'the / —', 'Names with ‘of’ take ‘the’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Possessive name', 'Let’s meet at [[—|-]] McDonald’s.', 'the / —', 'Names with ’s take no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with names and places.',
  [
  ('Country', 'I live in Spain.', []),
  ('Country', 'She lives in the USA.', []),
  ('Country', 'The Netherlands is flat.', []),
  ('Continent', 'Japan is in Asia.', []),
  ('Ocean', 'We crossed the Pacific.', []),
  ('Sea', 'I swam in the Red Sea.', []),
  ('River', 'The Nile is very long.', []),
  ('Lake', 'Lake Como is beautiful.', []),
  ('Mountains', 'We hiked in the Alps.', []),
  ('Mountain', 'Mount Etna is a volcano.', []),
  ('Islands', 'We visited the Canary Islands.', []),
  ('Island', 'Sicily is an island.', []),
  ('City', 'Girona is in Catalonia.', []),
  ('Street', 'I work on Main Street.', []),
  ('Park', 'We ran in Central Park.', []),
  ('Museum', 'We went to the Prado.', []),
  ('Hotel', 'They stayed at the Ritz.', []),
  ('Of pattern', 'I study at the University of Girona.', []),
  ('Country', 'He is from the Philippines.', []),
  ('River', 'Paris is on the Seine.', []),
  ])

MATCH = {'title': 'The or no article?', 'subtitle': 'Tap a place name, then tap the article it needs.',
  'leftLabel': 'Place', 'rightLabel': 'Article', 'rightLabelSub': '(the / —)', 'reviewArrowPrefix': '',
  'pairs': [
  ('___ Italy', '—'), ('___ United Kingdom', 'the'), ('___ Europe', '—'), ('___ Atlantic', 'the'),
  ('___ Thames', 'the'), ('___ Lake Geneva', '—'), ('___ Himalayas', 'the'), ('___ Mount Everest', '—'),
  ('___ Bahamas', 'the'), ('___ Ibiza', '—'), ('___ Madrid', '—'), ('___ Baltic Sea', 'the'),
  ('___ Fifth Avenue', '—'), ('___ British Museum', 'the'), ('___ Czech Republic', 'the'), ('___ Australia', '—'),
  ('___ Danube', 'the'), ('___ Times Square', '—'), ('___ Rocky Mountains', 'the'), ('___ Harrods', '—'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Plural names, groups, seas and rivers → the. Single countries, cities, lakes and mountains → no article.',
  [
  ('Country', 'My best friend moved to ___ Canada.', ['—', 'the', 'a', 'an'],
   ['Single country names take no article.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Most countries: no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Country', 'She’s studying in ___ United Kingdom.', ['the', '—', 'a', 'an'],
   ['‘Kingdom’ names need ‘the’.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Kingdom / Republic / States → the. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Country', '___ Maldives are famous for their beaches.', ['The', '—', 'A', 'An'],
   ['Plural country names need ‘the’.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Plural name → the Maldives. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Continent', 'Brazil is the biggest country in ___ South America.', ['—', 'the', 'a', 'an'],
   ['Continents take no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Continents: no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Ocean', '___ Indian Ocean is warm.', ['The', '—', 'A', 'An'],
   ['Oceans need ‘the’.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Oceans → the. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('River', 'Budapest is on ___ Danube.', ['the', '—', 'a', 'an'],
   ['Rivers need ‘the’.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Rivers → the. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Lake', 'We went sailing on ___ Lake Garda.', ['—', 'the', 'a', 'an'],
   ['‘Lake + name’ takes no article.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Lakes: no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Mountains', '___ Andes run through seven countries.', ['The', '—', 'A', 'An'],
   ['Mountain ranges need ‘the’.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Ranges → the Andes. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Mountain', '___ Mount Fuji is the highest mountain in Japan.', ['—', 'The', 'A', 'An'],
   ['‘Mount + name’ takes no article.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Single mountain: no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Islands', 'We’re going to ___ Canary Islands in May.', ['the', '—', 'a', 'an'],
   ['Island groups need ‘the’.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Island groups → the. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Island', 'Have you ever been to ___ Crete?', ['—', 'the', 'a', 'an'],
   ['A single island takes no article.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Single island: no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Street', 'The shop is on ___ Baker Street.', ['—', 'the', 'a', 'an'],
   ['Streets take no article.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Streets: no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Museum', 'Have you visited ___ Guggenheim in Bilbao?', ['the', '—', 'a', 'an'],
   ['Museums usually take ‘the’.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Museums → the. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Of pattern', 'We saw ___ Statue of Liberty.', ['the', '—', 'a', 'an'],
   ['Names with ‘of’ need ‘the’.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'The … of … → the. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Of pattern', 'He studies at ___ Oxford University.', ['—', 'the', 'a', 'an'],
   ['Without ‘of’, this name takes no article.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'No ‘of’: Oxford University. (But: the University of Oxford.)'),
  ('Possessive name', 'I bought these jeans at ___ Harrods.', ['—', 'the', 'a', 'an'],
   ['Names with ’s take no article.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Possessive names: no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Which', 'Which is correct?', ['I live near the Mediterranean.', 'I live near Mediterranean.', 'I live near a Mediterranean.', 'I live near the Mediterranean Lake.'],
   ['Seas need ‘the’.', 'Names don’t take ‘a’.', 'The Mediterranean is a sea, not a lake.'],
   'Seas → the. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Which', 'Which is correct?', ['We visited Lake Tahoe.', 'We visited the Lake Tahoe.', 'We visited a Lake Tahoe.', 'We visited Lake the Tahoe.'],
   ['‘Lake + name’: no article.', 'Names don’t take ‘a’.', 'Wrong word order.'],
   'Lakes: no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('City', '___ Barcelona is famous for its architecture.', ['—', 'The', 'A', 'An'],
   ['Cities take no article.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Cities: no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Country', 'He was born in ___ Czech Republic.', ['the', '—', 'a', 'an'],
   ['‘Republic’ names need ‘the’.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Republic → the. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong. Twenty original sentences.',
  [
  ('The with country', 'I spent a year in *the France*.', 'France', 'Single countries take no article: ‘in France’.'),
  ('The with country', 'They live in *the Portugal* now.', 'Portugal', 'Single countries take no article: ‘in Portugal’.'),
  ('The with continent', 'Peru is in *the South* America.', 'South', 'Continents take no article: ‘in South America’.'),
  ('The with city', 'We visited *the Rome* last spring.', 'Rome', 'Cities take no article: ‘Rome’.'),
  ('The with street', 'Our school is on *the Main* Street.', 'Main', 'Street names usually take no article: ‘on Main Street’.'),
  ('The with lake', 'We swam in *the Lake* Banyoles.', 'Lake', '‘Lake + name’ takes no article: ‘Lake Banyoles’.'),
  ('The with mountain', 'He climbed *the Mount* Everest.', 'Mount', '‘Mount + name’ takes no article: ‘Mount Everest’.'),
  ('The with island', 'We stayed in *the Mallorca* for a week.', 'Mallorca', 'A single island takes no article: ‘in Mallorca’.'),
  ('The with park', 'We had lunch in *the Central* Park.', 'Central', 'Park names take no article: ‘in Central Park’.'),
  ('The with city', 'She grew up in *the London*.', 'London', 'Cities take no article: ‘in London’.'),
  ('A with country', 'My uncle works in *a* USA.', 'the', '‘States’ makes it a group: ‘the USA’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('A with river', 'London is on *a* Thames.', 'the', 'Rivers take ‘the’: ‘the Thames’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('A with sea', 'We sailed on *a* North Sea.', 'the', 'Seas take ‘the’: ‘the North Sea’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('A with ocean', 'Whales live in *an* Arctic Ocean.', 'the', 'Oceans take ‘the’: ‘the Arctic Ocean’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('A with mountains', 'We went hiking in *a* Alps.', 'the', 'Mountain ranges take ‘the’: ‘the Alps’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('A with islands', 'They live on *a* Faroe Islands.', 'the', 'Island groups take ‘the’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('A with country', 'She’s from *a* Netherlands.', 'the', 'Plural country names take ‘the’: ‘the Netherlands’.'),
  ('A with museum', 'We went to *a* Prado on Sunday.', 'the', 'Museums usually take ‘the’: ‘the Prado’.'),
  ('A with of', 'We visited *a* Tower of London.', 'the', 'Names with ‘of’ take ‘the’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('A with kingdom', 'Wales is part of *a* United Kingdom.', 'the', '‘Kingdom’ names take ‘the’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, place type, multiple choice and spot-the-mistake. In the typing questions write the, or — (dash) for no article. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('type', 'Type of place'),
 'fill': [
  ('River', 'Seville is on [[the]] Guadalquivir.', 'the / —', 'Rivers take ‘the’.', 'River → the.'),
  ('Country', 'Have you ever been to [[—|-]] Mexico?', 'the / —', 'Single countries take no article.', 'Single country → no article.'),
  ('Continent', 'The Rockies are in [[—|-]] North America.', 'the / —', 'Continents take no article.', 'Continent → no article.'),
  ('Country', 'Manila is the capital of [[the]] Philippines.', 'the / —', 'Plural country names take ‘the’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.', 'Plural name → the.'),
  ],
 'order': [
  ('River', 'The Thames is in London.', []),
  ('Lake', 'Lake Tahoe is cold.', []),
  ('Country', 'I love Italy.', []),
  ('Islands', 'The Azores are green.', []),
  ],
 'customItems': [
  ('Type', 'Which place type takes ‘the’?', ['rivers', 'lakes', 'cities', 'streets'],
   ['Lakes take no article: Lake Garda.', 'Cities take no article.', 'Streets take no article.'],
   'Rivers → the Rhine, the Nile. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Type', 'Which place type takes NO article?', ['single mountains', 'mountain ranges', 'oceans', 'island groups'],
   ['Ranges take ‘the’: the Alps.', 'Oceans take ‘the’.', 'Island groups take ‘the’.'],
   'Single mountains: Mount Etna. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Type', 'Why ‘the USA’ but ‘Spain’?', ['‘States’ makes it a group', 'the USA is bigger', 'Spain is in Europe', 'it’s random'],
   ['Size doesn’t matter.', 'Location doesn’t matter.', 'It isn’t random.'],
   'Group / plural names take ‘the’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Type', 'Why ‘the University of Girona’ but ‘Girona University’?', ['the ‘of’ pattern takes the', 'universities always take the', 'Girona is a city', 'it’s random'],
   ['Without ‘of’ there’s no ‘the’.', 'The city isn’t the reason.', 'It isn’t random.'],
   'The … of … → the. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ],
 'mc': [
  ('Sea', 'Venice is on ___ Adriatic Sea.', ['the', '—', 'a', 'an'],
   ['Seas need ‘the’.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Seas → the. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Continent', 'Australia is both a country and ___ continent.', ['a', 'the', '—', 'an'],
   ['Here ‘continent’ is a common noun: one of many.', 'A singular countable noun needs an article.', '‘Continent’ starts with a consonant sound.'],
   'Common noun, one of many: a continent. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('City', 'The Sagrada Família is in ___ Barcelona.', ['—', 'the', 'a', 'an'],
   ['Cities take no article.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Cities: no article. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('Hotel', 'We had tea at ___ Savoy.', ['the', '—', 'a', 'an'],
   ['Hotels usually take ‘the’.', 'Names don’t take ‘a’.', 'Names don’t take ‘an’.'],
   'Hotels → the. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ],
 'error': [
  ('The with country', 'We travelled around *the Japan*.', 'Japan', 'Single countries take no article.'),
  ('A with river', 'Cairo is on *a* Nile.', 'the', 'Rivers take ‘the’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ('The with lake', 'They live near *the Lake* Michigan.', 'Lake', '‘Lake + name’: no article.'),
  ('A with islands', 'We flew to *a* Bahamas.', 'the', 'Plural names take ‘the’. Plural names, groups, seas and rivers take the; single countries, cities, lakes and mountains don’t.'),
  ],
}
