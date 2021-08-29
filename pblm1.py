# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:25:03 2019

@author: Ambika
"""
"REGEX  - Methods
#1. re.match() - Match a pattern
import re
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print(result)

#To print the matching string we’ll use method group 
#(It helps to return the matching string). 
#“r” - it designates a python raw string.
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print(result.group(0))

#string is not starting with ‘AV’,return no match
result = re.match(r'Analytics', 'AV Data Science and Analytics AV')
print(result)

#start() and end() -start and end position of matching pattern in the string.
result = re.match(r'AV', 'AV Data Science and Analytics AV')
print(result.start())
print(result.end())


#2. re.search()
result = re.search(r'Analytics', 'AV Data science and Analytics AV')
print(result.group(0))
#3.re.findall()
result = re.findall(r'AV', 'AV Data science and Analytics AV')
print(result)
#4.re.split()
result=re.split(r'y','Analytics')
result
# Maxsplit - Performed all splits
result=re.split(r'i','Data Science and Analytics')
print(result)
# Maxsplit - Performed mentioned split
result=re.split(r'i','Data Science and Analytics',maxsplit=3)
result
#5.re.compile()
pattern=re.compile('AV')
result=pattern.findall('AV Data science and Analytics AV')
print(result)
result2=pattern.findall('AV is largest analytics community of India')
print(result2)







