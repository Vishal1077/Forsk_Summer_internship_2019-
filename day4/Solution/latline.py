# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:29:43 2019

@author: user
"""

filename = ("words.txt")
f = open(filename)
for line in open(filename):
    print(len(line))
for line in open(filename):
    pass
print(open(filename).readlines()[-1])