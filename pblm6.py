# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 00:59:48 2019

@author: Ambika
"""

#Problem 8: Retrieve Information from HTML file
"""if we want to extract information from a HTML file 
(see below sample data). Here we need to extract information 
available between <td> and </td> except the first numerical
 index.  I have assumed here that below html code is stored 
 in a string str. Sample HTML file (str)"""
import re
str=open("F:/Ambika/2018-2019/NLP Workshop/Session I/text.txt","r")
str.read()
result=re.findall(r'<td>\w+</td>\s<td>(\w+)</td>\s<td>(\w+)</td>',str)
print(result)




