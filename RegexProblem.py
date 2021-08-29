# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 00:25:28 2019

@author: Ambika
"""
#Problem 1: Return the first word of a given string
#Solution-1  Extract each character (using “\w“)
import re
result=re.findall(r'.','AV is largest Analytics community of India')
print(result)
#space is also extracted,
#now to avoid it use “\w” instead of “.“.
result=re.findall(r'\w','AV is largest Analytics community of India')
print(result)
#Solution-2  Extract each word (using “*” or “+“)
result=re.findall(r'\w*','AV is largest Analytics community of India')
print(result)
# it is returning space as a word because “*” 
#returns zero or more matches of pattern to its left. 
#Now to remove spaces we will go with “+“.
result=re.findall(r'\w+','AV is largest Analytics community of India')
print(result)

#Solution-3 Extract each word (using “^“)
result=re.findall(r'^\w+','AV is largest Analytics community of India')
print(result)

#we will use “$” instead of “^”, 
#it will return the word from the end of the string.
result=re.findall(r'\w+$','AV is largest Analytics community of India')
print (result)






