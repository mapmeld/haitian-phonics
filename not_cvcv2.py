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
  ban_phrases = []
  banned = False
  for ban_phrase in ban_phrases:
    if(word.find(ban_phrase) > -1):
      banned = True
      break
  #if (banned):
  #  continue

  if (len(syllables) == 2):
    first_vowel = first_vowel_in(syllables[0])
    second_vowel = first_vowel_in(syllables[1])
    if (len(syllables[0]) > 2) or (len(syllables[1]) > 2):
      if (syllables[0].find(first_vowel) != 2) or (syllables[1].find(second_vowel) !=2):
        if (first_vowel != 'an') and (first_vowel != 'on') and (first_vowel != 'en') and (first_vowel != 'ou'):
          if (second_vowel != 'an') and (second_vowel != 'on') and (second_vowel != 'en') and (second_vowel != 'ou'):
            
            print word
#if (syllables[0].find(first_vowel) == 1) or (syllables[1].find(second_vowel) == 2) and ((len(syllables[0]) != 1 + len(first_vowel)) or (len(syllables[1]) != 1 + len(second_vowel))):
  
      #for syllable in syllables:
        #if (len(syllable) != 1 + len(first_vowel_in(syllable))):
          #letter = syllable[len(first_vowel_in(syllable))+1:]
          #if (letter in common_syllables.keys()):
            #common_syllables[letter] = common_syllables[letter] + 1
          #else:
            #common_syllables[letter] = 1

#syllable_sort = sorted(common_syllables.items(), key=operator.itemgetter(1), reverse = True)
#for syllable, count in syllable_sort:
 # print(syllable + ": " + str(count))
