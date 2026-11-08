TITLE = 'A vs An'
AUX = (['a', 'an'], None, 'an')
NEXT = ('A/An: the indefinite article', '/grammar/articles/indefinite-article-a-an/')
BODY = r'''
## How to choose a or an

The choice depends on the **sound** at the start of the next word — not the letter.

| Use | Before | Examples |
|---|---|---|
| **a** | a consonant **sound** | **a** dog, **a** car, **a** big apple, **a** university |
| **an** | a vowel **sound** (a, e, i, o, u) | **an** apple, **an** egg, **an** island, **an** hour |

## When to use *a*

### 1. Words that start with a consonant sound

- **a** book, **a** pen, **a** teacher, **a** house

### 2. Words that start with a vowel letter but a /j/ or /w/ sound

| Word | Sound | Article |
|---|---|---|
| university | /juː/ "you" | **a** university |
| uniform | /juː/ | **a** uniform |
| European | /jʊə/ | **a** European city |
| one | /w/ "won" | **a** one-way ticket |

> ⚠️ Typical error: ~~an university~~ → It starts with the sound "you": *a university.*

## When to use *an*

### 1. Words that start with a vowel sound

- **an** orange, **an** umbrella, **an** idea, **an** elephant

> ⚠️ Typical error: ~~a orange~~ → Vowel sound: *an orange.*

### 2. Silent *h*

Some words start with **h** but the h is silent, so the first sound is a vowel.

| Word | Sound | Article |
|---|---|---|
| hour | /aʊ/ | **an** hour |
| honest | /ɒ/ | **an** honest man |
| honour | /ɒ/ | **an** honour |

> ⚠️ Typical error: ~~a hour~~ → The *h* is silent: *an hour.*

### 3. Letters and abbreviations

Say the letter's name: if it starts with a vowel sound, use *an*.

- **an** MP3 player ("em"), **an** FBI agent ("ef"), **an** X-ray ("ex")
- **a** UFO ("you"), **a** BBC programme ("bee")

## The adjective decides

The article goes with the word **directly after it**.

| a / an + noun | a / an + adjective + noun |
|---|---|
| **an** apple | **a** big apple |
| **a** house | **an** old house |
| **a** car | **an** expensive car |

## Common mistakes

**1. Looking at the letter, not the sound.** *~~an uniform~~* → **a uniform.**

**2. Pronounced *h*.** *~~an house~~* → **a house** (h is pronounced).

**3. Silent *h*.** *~~a hour~~* → **an hour.**

**4. Forgetting the adjective.** *~~an big egg~~* → **a big egg.**

**Pro tip:** say the word out loud — if your mouth starts with a vowel sound, use **an**.
'''

GAP = ('Fill in the gaps',
  'Type a or an. Listen to the first sound of the next word — not the first letter. Twenty original sentences.',
  [
  ('A', 'My brother wants [[a]] dog for his birthday.', 'a / an', '‘Dog’ starts with a consonant sound /d/, so use ‘a’.'),
  ('An', 'Would you like [[an]] apple?', 'a / an', '‘Apple’ starts with a vowel sound, so use ‘an’. Remember: the first sound of the next word decides — not its first letter.'),
  ('An', 'I saw [[an]] elephant at the zoo.', 'a / an', '‘Elephant’ starts with a vowel sound: an elephant.'),
  ('A', 'She lives in [[a]] small flat.', 'a / an', '‘Small’ starts with a consonant sound: a small flat.'),
  ('An', 'Take [[an]] umbrella — it’s going to rain.', 'a / an', '‘Umbrella’ starts with the vowel sound /ʌ/: an umbrella.'),
  ('An', 'That’s [[an]] interesting idea!', 'a / an', '‘Interesting’ starts with a vowel sound: an interesting idea.'),
  ('A', 'My cousin goes to [[a]] university in Madrid.', 'a / an', '‘University’ starts with the sound “you”, a consonant sound: a university.'),
  ('A', 'We have to wear [[a]] uniform at school.', 'a / an', '‘Uniform’ starts with the sound “you”: a uniform. Remember: the first sound of the next word decides — not its first letter.'),
  ('A', 'Paris is [[a]] European capital.', 'a / an', '‘European’ starts with the sound “you”: a European capital.'),
  ('An', 'The film lasts [[an]] hour and a half.', 'a / an', 'The h in ‘hour’ is silent, so the first sound is a vowel: an hour.'),
  ('An', 'He’s [[an]] honest person — he never lies.', 'a / an', 'The h in ‘honest’ is silent: an honest person. Remember: the first sound of the next word decides — not its first letter.'),
  ('A', 'They live in [[a]] big house near the beach.', 'a / an', 'The h in ‘house’ is pronounced: a house. Remember: the first sound of the next word decides — not its first letter.'),
  ('A', 'Can I have [[a]] hot chocolate, please?', 'a / an', 'The h in ‘hot’ is pronounced: a hot chocolate. Remember: the first sound of the next word decides — not its first letter.'),
  ('An', 'I need [[an]] X-ray of my arm.', 'a / an', '‘X’ is said “ex”, a vowel sound: an X-ray. Remember: the first sound of the next word decides — not its first letter.'),
  ('An', 'He bought [[an]] MP3 player.', 'a / an', '‘M’ is said “em”, a vowel sound: an MP3 player. Remember: the first sound of the next word decides — not its first letter.'),
  ('A', 'Have you ever seen [[a]] UFO?', 'a / an', '‘U’ is said “you”, a consonant sound: a UFO. Remember: the first sound of the next word decides — not its first letter.'),
  ('A', 'She ate [[a]] big orange.', 'a / an', 'The article goes with ‘big’ (consonant sound): a big orange.'),
  ('An', 'They live in [[an]] old house.', 'a / an', 'The article goes with ‘old’ (vowel sound): an old house.'),
  ('An', 'It was [[an]] easy exam.', 'a / an', '‘Easy’ starts with a vowel sound: an easy exam. Remember: the first sound of the next word decides — not its first letter.'),
  ('A', 'I bought [[a]] one-way ticket.', 'a / an', '‘One’ starts with the sound /w/: a one-way ticket.'),
  ])

ORDER = ('Put it in order',
  'Tap the words to build each sentence — 20 examples with a and an.',
  [
  ('A', 'I have a cat.', []),
  ('A', 'She’s a teacher.', []),
  ('An', 'He ate an apple.', []),
  ('An', 'It’s an elephant.', []),
  ('An', 'Take an umbrella.', []),
  ('An', 'That’s an idea.', []),
  ('A', 'She goes to a university.', []),
  ('A', 'I wear a uniform.', []),
  ('An', 'Wait an hour.', []),
  ('An', 'He’s an honest man.', []),
  ('A', 'They have a house.', []),
  ('A', 'It was a happy day.', []),
  ('A', 'I saw a big egg.', []),
  ('An', 'It’s an old car.', []),
  ('An', 'She’s an amazing singer.', []),
  ('A', 'It’s a useful book.', []),
  ('An', 'I need an X-ray.', []),
  ('A', 'Is that a UFO?', []),
  ('An', 'It was an easy test.', []),
  ('A', 'We had a great time.', []),
  ])

MATCH = {'title': 'A or an?', 'subtitle': 'Tap a word, then tap the article it needs.',
  'leftLabel': 'Word', 'rightLabel': 'Article', 'rightLabelSub': '(a / an)', 'reviewArrowPrefix': '',
  'pairs': [
  ('___ apple', 'an'), ('___ banana', 'a'), ('___ egg', 'an'), ('___ university', 'a'), ('___ hour', 'an'),
  ('___ house', 'a'), ('___ umbrella', 'an'), ('___ uniform', 'a'), ('___ honest man', 'an'), ('___ big apple', 'a'),
  ('___ old car', 'an'), ('___ European city', 'a'), ('___ idea', 'an'), ('___ dog', 'a'), ('___ orange', 'an'),
  ('___ one-way street', 'a'), ('___ MP3 player', 'an'), ('___ UFO', 'a'), ('___ island', 'an'), ('___ happy child', 'a'),
  ]}

MC = ('Beat the clock',
  '15 seconds per question. Listen to the first SOUND of the next word: consonant sound → a, vowel sound → an.',
  [
  ('An', 'I’d like ___ ice cream, please.', ['an', 'a', 'the', '—'],
   ['‘Ice’ starts with a vowel sound, so ‘a’ is wrong here.', '‘The’ refers to a specific ice cream we both know.', 'A singular countable noun needs an article.'],
   '‘Ice’ starts with a vowel sound, so we use ‘an’. Remember: the first sound of the next word decides — not its first letter.'),
  ('A', 'My dad drives ___ taxi.', ['a', 'an', 'the', '—'],
   ['‘Taxi’ starts with a consonant sound, so not ‘an’.', '‘The taxi’ refers to a specific one.', 'A singular job object needs an article.'],
   '‘Taxi’ starts with the consonant sound /t/: a taxi. Remember: the first sound of the next word decides — not its first letter.'),
  ('University', 'My sister studies at ___ university in London.', ['a', 'an', 'the', '—'],
   ['‘University’ starts with a vowel letter but the sound “you” — a consonant sound.', '‘The’ would refer to a specific university we know.', 'A singular noun needs an article here.'],
   'Sound “you” → a university. Remember: the first sound of the next word decides — not its first letter.'),
  ('Hour', 'The train was ___ hour late.', ['an', 'a', 'the', '—'],
   ['The h in ‘hour’ is silent, so the first sound is a vowel.', '‘The hour’ changes the meaning.', 'An article is needed.'],
   'Silent h → an hour. Remember: the first sound of the next word decides — not its first letter.'),
  ('House', 'They bought ___ house by the sea.', ['a', 'an', 'the', '—'],
   ['The h in ‘house’ is pronounced, so ‘an’ is wrong.', '‘The house’ refers to a specific one.', 'An article is needed.'],
   'Pronounced h → a house. Remember: the first sound of the next word decides — not its first letter.'),
  ('Adjective', 'She’s got ___ amazing voice.', ['an', 'a', 'the', '—'],
   ['The article goes with ‘amazing’, which starts with a vowel sound.', '‘The amazing voice’ refers to a specific one.', 'An article is needed.'],
   'The next word ‘amazing’ decides: an. Remember: the first sound of the next word decides — not its first letter.'),
  ('Adjective', 'It was ___ big elephant.', ['a', 'an', 'the', '—'],
   ['The article goes with ‘big’, not ‘elephant’.', '‘The big elephant’ is a specific one.', 'An article is needed.'],
   'The next word ‘big’ decides: a. Remember: the first sound of the next word decides — not its first letter.'),
  ('Uniform', 'Do you wear ___ uniform at your school?', ['a', 'an', 'the', '—'],
   ['‘Uniform’ starts with the sound “you”.', '‘The uniform’ is a specific one.', 'An article is needed.'],
   'Sound “you” → a uniform. Remember: the first sound of the next word decides — not its first letter.'),
  ('Honest', 'He gave me ___ honest answer.', ['an', 'a', 'the', '—'],
   ['The h in ‘honest’ is silent.', '‘The honest answer’ is specific.', 'An article is needed.'],
   'Silent h → an honest answer. Remember: the first sound of the next word decides — not its first letter.'),
  ('European', 'Lisbon is ___ European capital.', ['a', 'an', 'the', '—'],
   ['‘European’ starts with the sound “you”.', '‘The European capital’ suggests only one.', 'An article is needed.'],
   'Sound “you” → a European capital. Remember: the first sound of the next word decides — not its first letter.'),
  ('Letter', 'She’s got ___ MBA from a US university.', ['an', 'a', 'the', '—'],
   ['‘M’ is said “em”, a vowel sound.', '‘The MBA’ is specific.', 'An article is needed.'],
   'Letter names: “em” → an MBA. Remember: the first sound of the next word decides — not its first letter.'),
  ('Letter', 'They saw ___ UFO over the lake.', ['a', 'an', 'the', '—'],
   ['‘U’ is said “you”, a consonant sound.', '‘The UFO’ is specific.', 'An article is needed.'],
   'Letter names: “you” → a UFO. Remember: the first sound of the next word decides — not its first letter.'),
  ('An', 'My grandma lives on ___ island.', ['an', 'a', 'the', '—'],
   ['‘Island’ starts with a vowel sound.', '‘The island’ is specific.', 'An article is needed.'],
   'Vowel sound → an island. Remember: the first sound of the next word decides — not its first letter.'),
  ('A', 'It was ___ horrible day.', ['a', 'an', 'the', '—'],
   ['The h in ‘horrible’ is pronounced.', '‘The horrible day’ is specific.', 'An article is needed.'],
   'Pronounced h → a horrible day. Remember: the first sound of the next word decides — not its first letter.'),
  ('One', 'This is ___ one-way street.', ['a', 'an', 'the', '—'],
   ['‘One’ starts with the sound /w/.', '‘The one-way street’ is specific.', 'An article is needed.'],
   '‘One’ sounds like “won”: a one-way street. Remember: the first sound of the next word decides — not its first letter.'),
  ('An', 'I’ve got ___ idea!', ['an', 'a', 'the', '—'],
   ['‘Idea’ starts with a vowel sound.', '‘The idea’ is specific.', 'An article is needed.'],
   'Vowel sound → an idea. Remember: the first sound of the next word decides — not its first letter.'),
  ('Which', 'Which is correct?', ['an hour', 'a hour', 'an house', 'a honest'],
   ['Silent h → an.', 'Pronounced h → a house.', 'Silent h → an honest.'],
   'Silent h takes ‘an’; pronounced h takes ‘a’. Remember: the first sound of the next word decides — not its first letter.'),
  ('Which', 'Which is correct?', ['a university', 'an university', 'an uniform', 'a umbrella'],
   ['Sound “you” → a.', 'Sound “you” → a.', '‘Umbrella’ starts with a vowel sound → an.'],
   'Look at the sound, not the letter. Remember: the first sound of the next word decides — not its first letter.'),
  ('A', 'She’s ___ doctor at the hospital.', ['a', 'an', 'the', '—'],
   ['‘Doctor’ starts with a consonant sound.', '‘The doctor’ is specific.', 'Jobs need an article in English.'],
   'Consonant sound → a doctor. Remember: the first sound of the next word decides — not its first letter.'),
  ('An', 'He’s ___ engineer.', ['an', 'a', 'the', '—'],
   ['‘Engineer’ starts with a vowel sound.', '‘The engineer’ is specific.', 'Jobs need an article in English.'],
   'Vowel sound → an engineer. Remember: the first sound of the next word decides — not its first letter.'),
  ])

ERR = ('Find the mistake',
  'Each sentence has exactly one mistake. Tap the word you think is wrong (if a word is missing, tap the word right after the gap). Twenty original sentences.',
  [
  ('A for vowel sound', 'I ate *a* orange for breakfast.', 'an', '‘Orange’ starts with a vowel sound: ‘an orange’.'),
  ('A for vowel sound', 'She’s *a* artist.', 'an', '‘Artist’ starts with a vowel sound: ‘an artist’.'),
  ('A for vowel sound', 'Take *a* umbrella with you.', 'an', '‘Umbrella’ starts with a vowel sound: ‘an umbrella’.'),
  ('A for vowel sound', 'It was *a* interesting film.', 'an', '‘Interesting’ starts with a vowel sound: ‘an interesting film’.'),
  ('An for consonant sound', 'He has *an* big dog.', 'a', '‘Big’ starts with a consonant sound: ‘a big dog’.'),
  ('An for consonant sound', 'They bought *an* new car.', 'a', '‘New’ starts with a consonant sound: ‘a new car’.'),
  ('An for /j/ sound', 'She studies at *an* university.', 'a', '‘University’ starts with the sound “you”: ‘a university’.'),
  ('An for /j/ sound', 'We wear *an* uniform.', 'a', '‘Uniform’ starts with the sound “you”: ‘a uniform’.'),
  ('An for /j/ sound', 'Rome is *an* European city.', 'a', '‘European’ starts with “you”: ‘a European city’.'),
  ('Silent h', 'The lesson lasts *a* hour.', 'an', 'Silent h: ‘an hour’. Remember: the first sound of the next word decides — not its first letter.'),
  ('Silent h', 'She’s *a* honest girl.', 'an', 'Silent h: ‘an honest girl’. Remember: the first sound of the next word decides — not its first letter.'),
  ('Pronounced h', 'They live in *an* house.', 'a', 'Pronounced h: ‘a house’. Remember: the first sound of the next word decides — not its first letter.'),
  ('Pronounced h', 'It was *an* happy day.', 'a', 'Pronounced h: ‘a happy day’. Remember: the first sound of the next word decides — not its first letter.'),
  ('Adjective', 'It’s *an* small apple.', 'a', 'The article goes with ‘small’: ‘a small apple’.'),
  ('Adjective', 'He lives in *a* old house.', 'an', 'The article goes with ‘old’: ‘an old house’.'),
  ('Letter', 'I need *a* X-ray.', 'an', '‘X’ is said “ex”: ‘an X-ray’. Remember: the first sound of the next word decides — not its first letter.'),
  ('Letter', 'She saw *an* UFO.', 'a', '‘U’ is said “you”: ‘a UFO’. Remember: the first sound of the next word decides — not its first letter.'),
  ('One', 'Buy *an* one-way ticket.', 'a', '‘One’ sounds like “won”: ‘a one-way ticket’.'),
  ('Job', 'My mum is *a* engineer.', 'an', '‘Engineer’ starts with a vowel sound: ‘an engineer’.'),
  ('Animal', 'There’s *a* insect on your arm!', 'an', '‘Insect’ starts with a vowel sound: ‘an insect’.'),
  ])

LC = {
 'subtitle': '20 mixed questions — typing, word order, sound or letter, multiple choice and spot-the-mistake. In the typing questions write a or an. One pass, then a breakdown of where you’re strong and where to go back and practise.',
 'custom': ('sound', 'Sound, not letter'),
 'fill': [
  ('An', 'I saw [[an]] owl in the garden last night.', 'a / an', '‘Owl’ starts with a vowel sound, so the article is ‘an’.', 'Vowel sound → an. Remember: the first sound of the next word decides — not its first letter.'),
  ('A', 'My uncle is [[a]] pilot.', 'a / an', '‘Pilot’ starts with a consonant sound, so the article is ‘a’.', 'Consonant sound → a. Remember: the first sound of the next word decides — not its first letter.'),
  ('University', 'She works at [[a]] university.', 'a / an', '‘University’ starts with the sound “you”, a consonant sound: a.', 'Sound “you” → a.'),
  ('Hour', 'We waited for [[an]] hour.', 'a / an', 'The h in ‘hour’ is silent, so the first sound is a vowel: an.', 'Silent h → an.'),
  ],
 'order': [
  ('An', 'It’s an egg.', []),
  ('A', 'She’s a nurse.', []),
  ('An', 'Wait an hour.', []),
  ('A', 'It’s a big orange.', []),
  ],
 'customItems': [
  ('Sound', 'Which word takes ‘a’?', ['useful', 'umbrella', 'apple', 'hour'],
   ['‘Umbrella’ starts with a vowel sound → an.', '‘Apple’ starts with a vowel sound → an.', '‘Hour’ has a silent h → an.'],
   '‘Useful’ starts with the sound “you” → a useful book.'),
  ('Sound', 'Which word takes ‘an’?', ['honest', 'house', 'university', 'one-way'],
   ['‘House’ has a pronounced h → a.', '‘University’ starts with “you” → a.', '‘One’ starts with /w/ → a.'],
   'Silent h → an honest person. Remember: the first sound of the next word decides — not its first letter.'),
  ('Sound', 'In ‘___ old car’, which word decides the article?', ['old', 'car', 'the subject', 'the verb'],
   ['The article goes with the word right after it.', 'The subject doesn’t affect the article.', 'The verb doesn’t affect the article.'],
   'The next word (‘old’) decides: an old car. Remember: the first sound of the next word decides — not its first letter.'),
  ('Sound', 'Why ‘an hour’ but ‘a house’?', ['the h is silent in ‘hour’', '‘hour’ is longer', '‘house’ is a building', 'it’s random'],
   ['Length doesn’t matter.', 'The meaning doesn’t matter.', 'It isn’t random: it’s about sound.'],
   'Silent h → vowel sound → an. Remember: the first sound of the next word decides — not its first letter.'),
  ],
 'mc': [
  ('An', 'She’s ___ actress.', ['an', 'a', 'the', '—'],
   ['‘Actress’ starts with a vowel sound.', '‘The actress’ is specific.', 'Jobs need an article.'],
   'Vowel sound → an.'),
  ('A', 'I want ___ new phone.', ['a', 'an', 'the', '—'],
   ['‘New’ starts with a consonant sound.', '‘The new phone’ is specific.', 'An article is needed.'],
   'Consonant sound → a.'),
  ('Adjective', 'It’s ___ expensive restaurant.', ['an', 'a', 'the', '—'],
   ['‘Expensive’ starts with a vowel sound.', '‘The’ is specific.', 'An article is needed.'],
   'The next word decides: an expensive. Remember: the first sound of the next word decides — not its first letter.'),
  ('Letter', 'He’s got ___ FBI badge.', ['an', 'a', 'the', '—'],
   ['‘F’ is said “ef”, a vowel sound.', '‘The’ is specific.', 'An article is needed.'],
   '“ef” → an FBI badge. Remember: the first sound of the next word decides — not its first letter.'),
  ],
 'error': [
  ('A for vowel sound', 'He’s *a* honest man.', 'an', 'Silent h: ‘an honest man’. Remember: the first sound of the next word decides — not its first letter.'),
  ('An for /j/ sound', 'It’s *an* useful tool.', 'a', '‘Useful’ starts with “you”: ‘a useful tool’. Remember: the first sound of the next word decides — not its first letter.'),
  ('Adjective', 'She has *an* beautiful voice.', 'a', '‘Beautiful’ starts with a consonant sound: ‘a’.'),
  ('A for vowel sound', 'I saw *a* eagle.', 'an', '‘Eagle’ starts with a vowel sound: ‘an eagle’.'),
  ],
}
