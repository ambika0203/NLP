# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 03:56:22 2019
@author: Ambika
"""
from nltk.tokenize import sent_tokenize, word_tokenize 
import warnings 

warnings.filterwarnings(action = 'ignore') 
  
#import gensim 
from gensim.models import Word2Vec 
  
#  Reads ‘alice.txt’ file 
sample = open("F:/Ambika/2018-2019/NLP Workshop/session III Exercises/alice.txt", "r") 
s = sample.read() 
  
# Replaces escape character with space 
f = s.replace("\n", " ") 
  
data = []  # Empty list type
  
# iterate through each sentence in the file 
for i in sent_tokenize(f): 
    temp = [] 
      
    # tokenize the sentence into words 
    for j in word_tokenize(i): 
        temp.append(j.lower()) 
  
    data.append(temp)
    # Create CBOW model 
model1 = gensim.models.Word2Vec(data, min_count = 1,  
                              size = 100, window = 5) 
  
# Print results 
print("Cosine similarity between 'alice' " +"and 'wonderland' - CBOW : ",model1.similarity('alice', 'wonderland')) 
      
print("Cosine similarity between 'alice' " +"and 'machines' - CBOW : ",model1.similarity('alice', 'machines')) 
  
    
    