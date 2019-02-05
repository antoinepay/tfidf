#!/usr/bin/python

import sys
from collections import Counter

current_doc = None

counter = Counter()
lines = []

for line in sys.stdin:
    doc, val = line.strip().split('\t', 1)
    word, count = val.split(' ', 1)
    counter[doc] += int(count)
    lines.append((doc, word, count))

for line in lines:
    f = int(line[2]) / counter[line[0]]
    print('%s\t%s' % (line[1] + ' ' + line[0], line[2] + ' ' + str(f)))

