#!/usr/bin/python

import sys
import math

current_word = None
current_doc = None

D = 10

number_of_docs_with_word = 0

buffer = []

for line in sys.stdin:
    word_doc, count_f = line.strip().split('\t', 1)
    word, doc = word_doc.split(' ', 1)
    count, f = count_f.split(' ', 1)

    if current_word is None:
        current_word = word
        current_doc = doc
        number_of_docs_with_word = 1
        buffer.append((word, doc, count, f))
    elif current_word == word and current_doc != doc:
        number_of_docs_with_word += 1
        buffer.append((word, doc, count, f))
    elif current_word != word:
        for b in buffer:
            idf = math.log2(number_of_docs_with_word / D)
            val = doc + ' ' + str(float(b[3]) * idf)
            print('%s\t%s' % (word, val))
        if len(buffer) == 0:
            idf = math.log2(number_of_docs_with_word / D)
            val = doc + ' ' + str(float(f) * idf)
            print('%s\t%s' % (word, val))

        current_word = word
        current_doc = doc
        number_of_docs_with_word = 1
        buffer = []

