# -*- coding: utf-8 -*-
# word_to_phonics.py

from word_util import get_syllables

my_word = raw_input("what word?")

lines = [my_word]

for line in lines:
  # skip lines which are symbols or proper nouns or multiple word phrases
  if (len(line) == 0) or (line.find('[') > -1) or (line.find(']') > -1) or (line.lower() != line) or (line.find(' ') > -1):
    continue

  # reduce to only the letters of the word
  word = line.replace(':', '').replace('"', '').replace('!', '')
  print(word)

  syllables = get_syllables(word)

  print('-'.join(syllables))

  # only do a* for now
  if word == 'dirab':
    break
