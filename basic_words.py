# -*- coding: utf-8 -*-
# basic_words.py

import operator, unicodedata
from word_util import get_syllables, real_len

wordlist = open('wordlist.txt', 'r')
lines = wordlist.read().split("\n")
wordlist.close()

common_syllables = {}

for line in lines:
  # skip lines which are symbols or proper nouns or multiple word phrases
  if (len(line) == 0) or (line.find('[') > -1) or (line.find(']') > -1) or (line.lower() != line) or (line.find(' ') > -1):
    continue

  # reduce to only the letters of the word
  word = line.replace(':', '').replace('"', '').replace('!', '').replace('.', '')
  if real_len(word) == 1 and word != "w" and word != "m":
    continue
  syllables = get_syllables(word)

  for syllable in syllables:
    if syllable in common_syllables:
      common_syllables[syllable] = common_syllables[syllable] + 1
    else:
      common_syllables[syllable] = 1 

  if (len(syllables) == 1):
    print(word)

# syllable_sort = sorted(common_syllables.items(), key=operator.itemgetter(1))
# print(syllable_sort)
