# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:05:17 2019

@author: user
"""

from collections import OrderedDict 
user_input = input("Enter string : ")

dict1 = OrderedDict() 
dict1["Digits"] = 0
dict1["Letters"] = 0

for character in user_input:    
    if character.isalpha():  
        dict1["Letters"] = dict1["Letters"] + 1 
    elif character.isdigit():          
        dict1["Digits"] = dict1["Digits"] + 1 
            
for key, value in dict1.items() :
  print ( key, value )