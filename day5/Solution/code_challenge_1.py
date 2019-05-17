# -*- coding: utf-8 -*-
"""
Created on Sat May 11 14:31:09 2019

@author: user
"""

import re

User_input = input("Enter floating point number :- ")
check = re.search(r"[-+]?\d*\.\d+$",User_input)
if (match):
    print(True)
else:
    print(False)