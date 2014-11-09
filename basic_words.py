# -*- coding: utf-8 -*-
# basic_words.py

import operator, json
from word_util import get_syllables, real_len, vowels, is_vowel, is_consonant, consonants

wordlist = open('wordlist.txt', 'r')
lines = wordlist.read().split("\n")
wordlist.close()

common_syllables = {}

vowel_count = {}
for vowel in vowels:
  vowel_count[vowel] = 0

consonant_count = {}
for consonant in consonants:
  consonant_count[consonant] = 0

nice_consonants = ['t', 'l', 'p', 'k', 's', 'v', 'b', 'd']

for line in lines:
  # skip lines which are symbols or proper nouns or multiple word phrases
  if (len(line) == 0) or (line.find('[') > -1) or (line.find(']') > -1) or (line.lower() != line) or (line.find(' ') > -1):
    continue

  # reduce to only the letters of the word
  word = line.replace(':', '').replace('"', '').replace('!', '').replace('.', '')

  # filter out un-cool one-letter words
  if real_len(word) == 1 and word != "w" and word != "m":
    continue

  syllables = get_syllables(word)

  for syllable in syllables:
    if syllable in common_syllables:
      common_syllables[syllable] = common_syllables[syllable] + 1
    else:
      common_syllables[syllable] = 1 

  # remove words with complex vowels
  ban_phrases = ['an', 'on', 'en', 'ou', 'ui', 'ch', 'y', 'w']
  banned = False
  for ban_phrase in ban_phrases:
    if(word.find(ban_phrase) > -1):
      banned = True
      break
  if (banned):
    continue

  if (len(syllables) == 1):
    # filter to 1-3 letter words
    if (real_len(word) <= 3):
      # ideal words

      if (word.find('v') > -1):
        print(word)
      else:
        continue

      # only print with A and one of the helpful consonants
      if (word.find('i') == 1):
        only_nice_consonants = True

        for consonant in consonants:
          is_a_nice_consonant = False
          for nice_consonant in nice_consonants:
            if consonant.find(nice_consonant) > -1:
              is_a_nice_consonant = True
              break

          if(word.find(consonant) > -1):
            consonant_count[consonant] = consonant_count[consonant] + 1
            if(word.find(consonant) != word.rfind(consonant)):
              consonant_count[consonant] = consonant_count[consonant] + 1

            if is_a_nice_consonant:
              continue
            elif word.find(consonant) > -1:
              only_nice_consonants = False
              break

        if only_nice_consonants:
          print(word)      

      # collect data on these ideal words
      for vowel in vowels:
        if(word.find(vowel) > -1):
          vowel_count[vowel] = vowel_count[vowel] + 1

print(consonant_count['j'])

consonant_sort = sorted(consonant_count.items(), key=operator.itemgetter(1))
print(json.dumps(consonant_sort))

# vowel_sort = sorted(vowel_count.items(), key=operator.itemgetter(1))
# print(json.dumps(vowel_sort))

# syllable_sort = sorted(common_syllables.items(), key=operator.itemgetter(1))
# print(syllable_sort)
