# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:58:07 2019

@author: user
"""



import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

f = map(lambda i: random.choice(code_names),names)
print(list(f))