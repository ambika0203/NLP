# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 02:03:23 2019

@author: Ambika
"""
#Package gensim - installation :conda install -c conda-forge gensim

#Topic Modeling - LDA
#Preparing Docs
doc1 = "Sugar is bad to consume. My sister likes to have sugar, but not my father."
doc2 = "My father spends a lot of time driving my sister around to dance practice."
doc3 = "Doctors suggest that driving may cause increased stress and blood pressure."
doc4 = "Sometimes I feel pressure to perform well at school, but my father never seems to drive my sister to do better."
doc5 = "Health experts say that Sugar is not good for your lifestyle."

# compile documents
doc_complete = [doc1, doc2, doc3, doc4, doc5]

#Cleaning and Preprocessing
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string
stop = set(stopwords.words('english'))
exclude = set(string.punctuation) 
lemma = WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in doc_complete]  
#Preparing document term matrix
import gensim
from gensim import corpora
'''
# Creating the term dictionary of our corpus, 
where every unique term is assigned an index.''' 
dictionary = corpora.Dictionary(doc_clean)
'''
# Converting list of documents (corpus) into Document Term Matrix 
using dictionary prepared above.'''
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
# Creating the object for LDA model using gensim library
Lda = gensim.models.LdaModel
# Running and Training LDA model on the document term matrix.
ldal = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)
# passes how many times the algorithm is supposed to pass over the whole corpus. 
print(ldal.print_topics(num_topics=3, num_words=3))
