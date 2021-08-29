# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 00:37:08 2019

@author: Ambika
"""
import re
#Problem 3: Return the domain type of given email-ids
#To explain it in simple manner, I will again go with a 
#stepwise approach:

#Solution-1  Extract all characters after “@”
result=re.findall(r'@\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz') 
print(result)

#“.com”, “.in” part is not extracted. 
#To add it, we will go 
result=re.findall(r'@\w+.\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print(result)

#Solution – 2 Extract only domain name using “( )”
result=re.findall(r'@\w+.(\w+)','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print(result)

#Problem 4: Return date from given string
#Here we will use “\d” to extract digit.

result=re.findall(r'\d{2}-\d{2}-\d{4}','Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print(result)

#Problem 5: Return all words of a string those starts with vowel
#   Solution-1  Return each words

result=re.findall(r'\w+','AV is largest Analytics community of India')
print(result)
#Solution-2  Return words starts with alphabets (using [])
result=re.findall(r'[aeiouAEIOU]\w+','AV is largest Analytics community of India')
print(result)

#to avoid “argest” and “ommunity” from the mid of words.
# To drop these two, we need to use “\b” for word boundary
result=re.findall(r'\b[aeiouAEIOU]\w+','AV is largest Analytics community of India')
print (result )
#we can extract words those starts with constant 
#using “^” within square bracket.
result=re.findall(r'\b[^aeiouAEIOU]\w+','AV is largest Analytics community of India')
print (result)

# it has returned words starting with space. 
#To drop it from output, include space in square bracket[].

result=re.findall(r'\b[^aeiouAEIOU ]\w+','AV is largest Analytics community of India')
print( result)











