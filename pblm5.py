# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 00:53:17 2019

@author: Ambika
"""

#Problem 7: Split a string with multiple delimiters
import re
line = 'asdf fjdk;afed,fjek,asdf,foo' # String has multiple delimiters (";",","," ").
result= re.split(r'[;,\s]', line)
print(result)
#We can also use method re.sub() to replace these 
#multiple delimiters with one as space ” “.
import re
line = 'asdf fjdk;afed,fjek,asdf,foo'
result= re.sub(r'[;,\s]',' ', line)
print(result)


