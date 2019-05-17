# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:57:00 2019

@author: user
"""

import re

email = input("enter the mail: ")

text = re.findall(r'\w+@\S+\w', email)

print(text)