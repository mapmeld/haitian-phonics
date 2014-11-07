# -*- coding: utf-8 -*-
# word_util.py

# split by vowel
vowels = ['an', 'en', 'on', 'a','à','e','è','i','o','ò','u']
# TODO: plus Y at end of words

def first_vowel_in(word):
  min_vowel = None
  min_index = len(word)
  for vowel in vowels:
    if (word.find(vowel) > -1) and (word.find(vowel) < min_index):
      #if (vowel == 'an') or (vowel == 'en') or (vowel == 'on'):
        # ann / enn / onn ?
        # if (word.find(vowel + 'n') == word.find(vowel)):
        #  continue

        # a-ban-do-ne

      min_vowel = vowel
      min_index = word.find(vowel)
  return min_vowel

def get_syllables(remainder):
  syllables = []
  while first_vowel_in(remainder) is not None:
    first_vowel = first_vowel_in(remainder)
    if (remainder.find(first_vowel) == 0) and (len(syllables) > 0):
      # multiple vowels chain together?
      # a-ban-do-ne
      last_syllable = syllables[len(syllables) - 1]
      if (last_syllable[len(last_syllable) - 1] == 'n'):
        syllables[len(syllables) - 1] = last_syllable[0: len(last_syllable) - 1]
        remainder = 'n' + remainder
      else:
        syllables[len(syllables) - 1] = last_syllable + remainder[0]
        remainder = remainder[1:]
        continue
    if (remainder[0] == 'b') and (len(syllables) > 0):
      if (remainder.find(first_vowel) > 1) and (remainder[1] != 'r') and (remainder[1] != 'w'):
        last_syllable = syllables[len(syllables) - 1]
        syllables[len(syllables) - 1] = last_syllable + 'b'
        remainder = remainder[1:]
        continue
    syllables.append(remainder[0 : remainder.find(first_vowel) + len(first_vowel)])
    remainder = remainder[remainder.find(first_vowel) + len(first_vowel) : ]
  if (len(syllables) > 0):
    syllables[len(syllables) - 1] = syllables[len(syllables) - 1] + remainder
  else:
    syllables = [remainder]
  return syllables
