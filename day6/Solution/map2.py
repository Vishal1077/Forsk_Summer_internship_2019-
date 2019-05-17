# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:21:13 2019

@author: user
"""

names = ['Mary', 'Isla', 'Sam']

f = map(lambda x: hash(names[i]),names)

print (list(f))



#or


names = ['Mary', 'Isla', 'Sam']

f = map(lambda x: hash(x),names)

print (list(f))