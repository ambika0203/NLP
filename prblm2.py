# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 00:34:11 2019

@author: Ambika
"""

#Problem 2: Return the first two character of each word
#Solution-1  Extract consecutive two characters of each word, 
#excluding spaces (using “\w“)
import re
result=re.findall(r'\w\w','AV is largest Analytics community of India')
print(result)
#Solution-2  Extract consecutive two characters those available 
#at start of word boundary (using “\b“)
result=re.findall(r'\b\w.','AV is largest Analytics community of India')
print(result)


