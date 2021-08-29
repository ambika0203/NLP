# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 00:53:03 2019

@author: Ambika
"""
#Problem 6: Validate a phone number
# (phone number must be of 10 digits and starts with 8 or 9) 
#list phone numbers in list “li” and here we will validate phone numbers 
#using regular expression
import re
li=['9999999999','999999-999','99999x9999']
for val in li:
 if re.match(r'[8-9]{1}[0-9]{9}',val) and len(val) == 10:
     print('yes')
 else:
     print('no')
