"""Findall regex operations in python.

findall(string[, pos[, endpos]])

Returns a list:
not like search and match which returns objects
Otherwise, it returns an empty list.
"""
import re

# look for every word in a string
pattern = re.compile(r"\w+")
result = pattern.findall("hey bro")
result

patt = re.compile(r"a*b")
# returns ['ab', 'ab', 'ab', 'b']
res = patt.findall("abababb")
res

# match a group of words onto a tuple
p = re.compile(r"(\w+) (\w+)")
rv = p.findall("Hello world, i lived")
rv

