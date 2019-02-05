#!/usr/bin/python

import sys

current_doc = None
current_word = None
current_count = 0
word = None
doc = None

for line in sys.stdin:
    line = line.strip()
    word_doc, count = line.split('\t', 1)

    word, doc = word_doc.split(' ', 1)

    if current_doc == doc and current_word == word:
        current_count += 1
    elif current_word is None:
        current_word = word
        current_doc = doc
        current_count = 1
    else:
        print('%s %s\t%s' % (word, doc, current_count))
        current_count = 1
        current_word = word
        current_doc = doc

if current_word == word:
    print('%s %s\t%s' % (word, doc, current_count))
