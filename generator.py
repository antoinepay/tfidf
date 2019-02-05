import os
import random
import sys
import requests

WORDS = random.choices(list(map(lambda x: x.strip(), open('words_en.txt', 'r'))), k=500)

line = 1

n_words = 10000

if not os.path.exists('corpus'):
    os.mkdir('corpus')

for i in range(5):
    if not os.path.exists('corpus/' + str(i)):
        os.mkdir('corpus/' + str(i))
    for j in range(10):
        count = n_words
        with open('corpus/' + str(i) + '/text_' + str(j) + '.txt', 'w') as file:
            while count > 0:
                words = ' '.join(random.choices(WORDS, k=10))
                file.write(words + '\n')
                count -= 10
    n_words *= 2

