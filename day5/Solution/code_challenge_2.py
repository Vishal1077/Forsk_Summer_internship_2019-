# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:30:43 2019

@author: user
"""

import re 

user_input = input("Enter your email :- ")
check = re.search(r"[\w.]+@[\w]+\.[a-z]{2,}\b$",user_input)
if (check):
    print(True)
else:
    print(False)