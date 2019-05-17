# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:23:59 2019

@author: user
"""

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]


f = list(map(lambda x: x['height'],filter(lambda x:'height' in x,people)))

if len(f) > 0:
    average_height = reduce(lambda a,b:a+b, f) / len(f)
    
print(average_height)



#or


people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

from functools import reduce
from functools import reduce
lst1 = list(filter(lambda x:'height' in x,people))
lst2 = list(map(lambda x: x['height'],lst1))
count = reduce(lambda x,y : x+y,lst2)
len_count = len(lst1)
devide = count/len_count
print(devide)