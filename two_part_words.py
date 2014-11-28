# -*- coding: utf-8 -*-
# basic_words.py

import operator, json
from word_util import get_syllables, real_len, vowels, is_vowel, is_consonant, consonants, first_vowel_in

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
# you can de-activate nice_consonants entirely by not having any of them:
# nice_consonants = []

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
  #if (banned):
  #  continue

  # word "rabat" becomes syllables ["ra", "bat"]
  # they both have the same vowel, so they go into this if statement
  if (len(syllables) == 2) and (first_vowel_in(syllables[0]) == first_vowel_in(syllables[1])):

    # first_syllable "ra" is split on its vowel "a" to become ["r", ""]
    # second_syllable "bat" is split on its vowel "a" to become ["b", "t"]
    first_syllable = syllables[0].split(first_vowel_in(syllables[0]))
    second_syllable = syllables[1].split(first_vowel_in(syllables[1]))

    # check if first_syllable and second_syllable share common beginning or ending
    # includes starting or ending on a vowel (for example "wa" and "vwa")

    # strictest: beginning or ending matches, excluding beginning or ending on a vowel
    # "bèbè" is accepted because both syllables begin with "b"
    # "kaba" is rejected because their match is ending with "a"
    # "kaskad" is rejected because it believes syllables to be "ka-skad"
    #if (first_syllable[0] == second_syllable[0] and first_syllable[0] != "") or (first_syllable[1] == second_syllable[1] and first_syllable[1] != ""):
    #  print(word)

    # less strict: beginning or ending matches, including beginning or ending with a vowel
    # "kaba" would be accepted because both syllables end with "a"
    # "kaskad" is rejected because it believes syllables to be "ka-skad"
    if (first_syllable[0] == second_syllable[0]) or (first_syllable[1] == second_syllable[1]):
      print(word)

    # different rule: beginning or ending matches, checking just the letter before or after the vowel
    # doesn't count beginning or ending with a vowel
    # "kaskad" is accepted even though it believes syllables to be "ka-skad"
    if first_syllable[0] != "" and second_syllable[0] != "":
      syllable_0_1 = first_syllable[0][ len(first_syllable[0]) - 1]
      syllable_1_1 = second_syllable[0][ len(second_syllable[0]) - 1 ]

    #if (first_syllable[0] != "" and second_syllable[0] != "" and syllable_0_1 == syllable_1_1) or (first_syllable[1] != "" and second_syllable[1] != "" and first_syllable[1][0] == second_syllable[1][0]):
    #  print(word)
