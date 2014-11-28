# -*- coding: utf-8 -*-
# basic_words.py

import operator, json
from word_util import get_syllables, real_len, vowels, is_vowel, is_consonant, consonants, first_vowel_in

wordlist = open('wordlist.txt', 'r')
lines = wordlist.read().split("\n")
wordlist.close()

common_syllables = {}
started_with = {}
ended_with = {}

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

  ideal_syllables = []
  #ideal_syllables = ideal_syllables + ["ra", "rè", "rò", "re", "ri", "ro", "rou", "ran", "ron", "ren"]
  ideal_syllables = ideal_syllables + ["la", "lè", "lò", "le", "li", "lo", "lou", "lan", "lon", "len"]
  ideal_syllables = ideal_syllables + ["ta", "tè", "tò", "te", "ti", "to", "tou", "tan", "ton", "ten"]

  if (len(syllables) == 2 and ((syllables[0] in vowels) or (syllables[0] in ideal_syllables)) and ((syllables[1] in vowels) or syllables[1] in ideal_syllables)) and ((syllables[0] not in vowels) or (syllables[1] not in vowels)):
    print(word)
