# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 03:44:58 2019

@author: Ambika
"""

# Load Corpus
sentence_stream = gensim.models.word2vec.LineSentence(corpus_path)
# Generate Bigrams
bigram = gensim.models.Phrases(sentence_stream)
term_list = list(bigram[sentence_stream])
# Build Model
model = gensim.models.Word2Vec(term_list)
model.save(model_backup_path)
# Use Model
model = gensim.models.Word2Vec.load(model_backup_path)
model.most_similar(positive= ["predident"])
