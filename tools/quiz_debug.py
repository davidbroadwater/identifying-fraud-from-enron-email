#!/usr/bin/python

import pickle

word_data = pickle.load(open("word_data.pkl", "r") )
#from_data = pickle.load(open("your_email_authors.pkl", "r") )

print word_data[2]

### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
sw = stopwords.words("English")

vectorizer = TfidfVectorizer(stop_words=sw)
vectorizer.fit_transform(word_data)
vocab_list = vectorizer.get_feature_names()
print len(vectorizer.get_feature_names())

print vocab_list[34596]
print vocab_list[34597]
print vocab_list[34598]
