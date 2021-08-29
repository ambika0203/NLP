"""String matching in python.

e.g x.match('pattern')

First, a re.match matches the
pattern only at the beginning of the string.
"""
import re

# recompile regular expression.
patt = re.compile(r'<HTML>')
patt.match("HTML")
# or you could just as well do this
print re.match(r'<html>', "<html>")
# this returns None if string does not start with 'html'
another_one = re.match(r'html', 'SOMETHINGhtmlcowpig')
print another_one

# optional pos parameter specifies where to start searching
pattern = re.compile(r'html')
result = pattern.match('__html', 2)
print result.group() # prints html

# we can use slicing to match the characters
slicer = pattern.match("__html"[2:])
# or use the endpos to specify the last index of the string to check.
sliced = pattern.match("html", 0, 4)
some_slice = pattern.match("html"[:4])
print slicer.group(), sliced.group(), some_slice.group()
