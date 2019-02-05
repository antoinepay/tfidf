#!/usr/bin/python

import sys

for line in sys.stdin:
    word_doc, count = line.strip().split('\t', 1)
    word, doc = word_doc.split(' ', 1)
    val = word + ' ' + count
    print('%s\t%s' % (doc, val))
