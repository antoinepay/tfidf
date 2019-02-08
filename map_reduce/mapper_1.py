#!/usr/bin/python

import sys
import os
import re

eng_stopwords = set(['up', 'don', 'that', 'over', 'most', 'aren', 'on', 'this', 'then', 'no', 'y', 'after', 'we',
                     'yourself', 'from', 'him', 'itself', 've', 'herself', 'the', 're', 'didn', 'has', 'each',
                     "didn't", 'as', 'o', "wasn't", 'our', "you've", 'below', 'here', 'them', 'hadn', 'further',
                     'with', 'into', 'you', 'between', 'by', 'too', "needn't", 'they', 'such', 'how', 'through',
                     'been', 'his', 'all', 'do', 'll', 'shan', 'were', 'can', 'did', 'himself', 'isn', 'he', 'any',
                     'me', "you're", 'just', 'doing', 'her', 'what', "hadn't", 'had', 'their', 'being', 'couldn',
                     "she's", 'about', "shan't", 't', "aren't", 'wasn', 'themselves', 'very', 'weren', "don't",
                     'in', 'm', 'during', 'are', 'than', "mightn't", 'why', 'off', 'until', 'and', 'an', 'haven',
                     'few', "couldn't", 'for', 'doesn', 'where', 'down', 'so', 'there', 'who', 'but', 'shouldn',
                     's', "shouldn't", 'she', 'it', 'mightn', "wouldn't", 'whom', "doesn't", 'of', 'needn', 'when',
                     'nor', 'wouldn', 'yourselves', 'before', 'd', 'ourselves', 'am', 'which', 'yours', 'again',
                     "won't", 'i', 'a', 'only', 'having', 'ma', 'myself', "hasn't", "should've", 'ain', 'be', 'other',
                     'at', 'because', 'to', 'out', 'both', "mustn't", 'hers', "weren't", "you'd", 'have', 'against',
                     "haven't", 'those', 'should','theirs', 'own', "it's", 'won', 'while', 'once', 'was', 'ours', 'now',
                     'mustn', 'its', 'or', 'my', 'not', 'does', 'under', 'your', 'hasn', "you'll", 'will', 'above',
                     'some', 'is', 'more', "isn't", 'same', 'if', "that'll", 'these'])

for line in sys.stdin:
    filename = os.environ["map_input_file"]
    words = re.findall(r'[^\s!,.?":;0-9]+', line.lower())
    for word in words:
        if word not in eng_stopwords:
            word_doc = word + ' ' + filename
            print('%s\t%s' % (word_doc, 1))
