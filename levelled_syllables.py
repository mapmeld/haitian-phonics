# -*- coding: utf-8 -*-
# levelled_syllables.py

import operator, json
from word_util import get_syllables, real_len, vowels, is_vowel, is_consonant, consonants, first_vowel_in

wordlist = open('iloom-words.csv', 'r')
lines = wordlist.read().split("\n")
wordlist.close()

words_by_level = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
for level in words_by_level:
  level['n'] = [] # noun
  level['a'] = [] # adjective
  level['adv'] = [] # adverb
  level['v'] = [] # verb
  level['ent'] = [] # interjection
  level['kon'] = [] # conjuctuon ??
  level['konj'] = [] # conjuction ??
  level['pwo'] = [] # ? phrase ?
  level['np'] = [] # proper noun
  level['pre'] = [] # preposition

for line in lines:
  # skip lines which are symbols or proper nouns or multiple word phrases
  if (len(line) == 0) or (line.lower() != line):
    continue

  # reduce to only the letters of the word
  word = line.split(':')[0].split(',')[0]
  if (word.find(' ') > -1):
    continue
  part_of_speech = line.split('~~')[1].replace('[','').replace('"', '').replace('.','').replace(' ','').replace(',','')
  if (part_of_speech == '') or (part_of_speech.find('*') > -1):
    continue

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
    ['ma', 'mi', 'me', 'mo', 'mou', 'men', 'man', 'mon', 'ban', 'bon', 'ben,' 'ran', 'ren', 'ron', 'san', 'sen', 'son', 'lan', 'len', 'lon', 'tan', 'ten', 'ton'],
    ['ka', 'ki', 'ke', 'ko', 'kou', 'ken', 'kan', 'kon'],
    ['pa', 'pi', 'pe', 'po', 'pou', 'pen', 'pan', 'pon'],
    ['da', 'di', 'de', 'do', 'dan', 'don', 'den', 'dou'],
    ['ga', 'gi', 'ge', 'go', 'gan', 'gon', 'gen', 'gou', 'ò', 'gò', 'dò', 'pò', 'kò', 'mò', 'bò', 'rò', 'sò', 'lò', 'tò', 'è', 'gè', 'dè', 'pè', 'kè', 'mè', 'bè', 'rè', 'sè', 'lè', 'tè',],
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

      if (part_of_speech in words_by_level[level_num - 1]) and (word in words_by_level[level_num - 1][part_of_speech]):
        # prevent duplicates
        continue

      if (len(syllables) == 1):
        if (syllables[0] in currently_known):
          words_by_level[level_num - 1][part_of_speech].append(word)
          break
      else:
        if (syllables[0] in currently_known) and (syllables[1] in currently_known):
          words_by_level[level_num - 1][part_of_speech].append(word)
          break

level_num = 0
print("Level 1")
print("~~ent~~")
print("bonjou, komoun, w, m, nicolas, sora")

for level in words_by_level:
  level_num = level_num + 1
  if(level_num == 1):
    continue
  print("")
  print("Level " + str(level_num))
  for part_of_speech in level:
    words = level[part_of_speech]
    if (len(words) > 0):
      print('~~' + part_of_speech + '~~')
      print(", ".join(words))
