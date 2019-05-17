# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:58:43 2019

@author: user
"""

import re 

check1 = r'[456]+(\d{15}|\d{3}-(\d{4}-?){3})'

while True:
    a = input("Enter credit card no. :- ").strip()
    if not a:
        break
    check2 = re.match(check1,a)
    check3 = re.search(r'(\d)\1{3,}',a.replace('-',''))
    if check2 and not check3:
        print ("Valid")
    else:
        print ("Invalid")
        
        