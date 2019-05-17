# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:06:33 2019

@author: user
"""

import re

file = open("simpsons_phone_book.txt")
for item in file:
    if re.search(r"J.*Neu",item):
        print(item)
file.close()