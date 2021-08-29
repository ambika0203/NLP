# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:56:31 2019

@author: Ambika
"""

   
# create sample documents
doc1 = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
doc2 = "My mother spends a lot of time driving my brother around to baseball practice."
doc3 = "Some health experts suggest that driving may cause increased tension and blood pressure."
doc4 = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
doc5 = "Health professionals say that brocolli is good for your health." 
doc_complete = [doc1, doc2, doc3, doc4, doc5]


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
doc_term_matrix



# Creating the object for LDA model using gensim library
Lda = gensim.models.LdaModel
# Running and Training LDA model on the document term matrix.
ldal = Lda(doc_term_matrix, num_topics=2, id2word = dictionary, passes=50)
# passes how many times the algorithm is supposed to pass over the whole corpus. 
print(ldal.print_topics(num_topics=2, num_words=3))