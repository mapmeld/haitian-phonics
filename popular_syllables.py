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

  # remove words with complex vowels
  ban_phrases = ['an', 'on', 'en', 'ou', 'ui', 'ch', 'y', 'w']
  banned = False
  for ban_phrase in ban_phrases:
    if(word.find(ban_phrase) > -1):
      banned = True
      break
  if (banned):
    continue

  # count popularity of syllables used in two-syllable words
  if (len(syllables) == 2):
    for syllable in syllables:
      if (syllable in common_syllables.keys()):
        common_syllables[syllable] = common_syllables[syllable] + 1
      else:
        common_syllables[syllable] = 1
        started_with[syllable] = []
        ended_with[syllable] = []
    started_with[syllables[0]].append(word)
    ended_with[syllables[1]].append(word)

syllable_sort = sorted(common_syllables.items(), key=operator.itemgetter(1), reverse = True)

pop = open('popular-syllables.txt', 'w')

for syllable, index in syllable_sort:
  if common_syllables[syllable] > 10:
    print("Syllable: " + syllable + " (" + str(common_syllables[syllable]) + ")")
    pop.write("Syllable: " + syllable + " (" + str(common_syllables[syllable]) + ")\n")
    for word in started_with[syllable]:
      pop.write(word + "\n")
    for word in ended_with[syllable]:
      pop.write(word + "\n")
