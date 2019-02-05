#!/usr/bin/python

import sys
import os
import re
from nltk.corpus import stopwords

eng_stopwords = set(stopwords.words('english'))

for line in sys.stdin:
    filename = os.environ["map_input_file"]
    words = re.findall(r'[^\s!,.?":;0-9]+', line.lower())
    for word in words:
        if word not in eng_stopwords:
            print('%s %s\t%s' % (word, filename, 1))
