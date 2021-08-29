# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:24:17 2019

@author: Ambika
"""

import bs4 as bs ' BeautifulSoup 4. Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree
import urllib.request ' module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.
import re ' Python has a built-in package called re, which can be used to work with Regular Expressions.
import nltk

'The article we are going to scrape is the Wikipedia article on
'Artificial Intelligence. Lets write a 
'Python Script to scrape the article from Wikipedia

scrapped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
article = scrapped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')
paragraphs
article_text = ""

for p in paragraphs:
    article_text += p.text
    
    processed_article = article_text.lower()
processed_article = re.sub('[^a-zA-Z]', ' ', processed_article )
processed_article = re.sub(r'\s+', ' ', processed_article)

# Preparing the dataset
all_sentences = nltk.sent_tokenize(processed_article)

all_words = [nltk.word_tokenize(sent) for sent in all_sentences]

# Removing Stop Words
from nltk.corpus import stopwords
for i in range(len(all_words)):
    all_words[i] = [w for w in all_words[i] if w not in stopwords.words('english')]
from gensim.models import Word2Vec

word2vec = Word2Vec(all_words, min_count=2)
vocabulary = word2vec.wv.vocab
print(vocabulary)
v1 = word2vec.wv['artificial']

sim_words = word2vec.wv.most_similar('intelligence')
sim_words

    
    
    