# -*- coding: utf-8 -*-
# levelled_syllables.py

import operator, json
from word_util import get_syllables, real_len, vowels, is_vowel, is_consonant, consonants, first_vowel_in

wordlist = open('wordlist.txt', 'r')
lines = wordlist.read().split("\n")
wordlist.close()

words_by_level = [[], [], [], [], [], []]

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

  levels = [
    ['a', 'e', 'i', 'o'],
    ['ta', 'ti', 'te', 'to'],
    ['la', 'li', 'le', 'lo',], 
    ['sa', 'si', 'se', 'so', 'sou', 'tou', 'lou'],
    ['ra', 'ri', 're', 'ro', 'rou'],
    ['ba', 'bi', 'be', 'bo', 'bou'],
  ]

  if (len(syllables) == 1 or len(syllables) == 2):
    level_num = 0
    currently_known = []
    for level in levels:
      currently_known = currently_known + level
      level_num = level_num + 1
      if (level_num == 1):
        # vowel-only words are obvious
        continue

      if (len(syllables) == 1):
        if (syllables[0] in currently_known):
          words_by_level[level_num -1].append(word)
          break
      else: 
        if (syllables[0] in currently_known) and (syllables[1] in currently_known):
          words_by_level[level_num - 1].append(word)
          break

level_num = 0
for level in words_by_level:
  level_num = level_num + 1
  if(level_num == 1):
    continue
  print("Level " + str(level_num))
  print(", ".join(level))
