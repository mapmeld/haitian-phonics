# -*- coding: utf-8 -*-
# wordlist_to_phonics.py

from word_util import get_syllables

wordlist = open('wordlist.txt', 'r')
lines = wordlist.read().split("\n")
wordlist.close()

output_list = open('outputlist.txt', 'w')

for line in lines:
  # skip lines which are symbols or proper nouns or multiple word phrases
  if (len(line) == 0) or (line.find('[') > -1) or (line.find(']') > -1) or (line.lower() != line) or (line.find(' ') > -1):
    continue

  # reduce to only the letters of the word
  word = line.replace(':', '').replace('"', '').replace('!', '')
  print word

  syllables = get_syllables(word)

  print '-'.join(syllables)
  output_list.write(word + "\n")
  output_list.write('-'.join(syllables) + "\n\n")
