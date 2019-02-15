import re
import numpy as np

# Create a corpus of document
corpus = sc.wholeTextFiles('hdfs:/Users/Benjamin/Documents/Scolaire/X/Data management/projects/tfidf/corpus/0')

# Create pairs (key= filename, value= words): tokenization of the text
words = corpus.flatMap(lambda x: [(x[0], y) for y in re.split(' |\n', x[1])]) ## ATTENTION enlever l'espace..


# TF-Term-Frequency for corpus of document
counts = words.map(lambda x: ((x[1], x[0]), 1)).reduceByKey(lambda a, b: a + b).map(lambda x: (x[0][1], (x[0][0], x[1])))
total = words.groupByKey().map(lambda x: ((x[0], len(x[1]))))
tf = total.join(counts).map(lambda x: ( x[1][1][0], (x[0], x[1][1][1]/x[1][0])))

# IDF-Inverse-document frequency for a corpus
# Compute the total number of documents in the corpus
docs = corpus.count()

# Number of documents containing a word: pair (word, list of documents in whcih it appears) : count unique times it appears
wordsdocs = words.map(lambda x: (x[1], x[0])).groupByKey().map(lambda x : (x[0], len(np.unique(list(x[1])))))

# Inverse-document frequency
idf = wordsdocs.map(lambda x: (x[0], np.log(docs/x[1])))

# TF-IDF score
tfidf = tf.join(idf).map(lambda x: ((x[0], x[1][0][0]), x[1][0][1]*x[1][1]))

