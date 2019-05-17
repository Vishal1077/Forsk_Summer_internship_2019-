# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:40:28 2019

@author: user
"""



user_input = input("Enter space seprated value : ").split(" ")

input_length = len(user_input)

count = 0
pallindromic_integer = False

for num in user_input:
    if int(num) > 0:
        count += 1

if count == input_length:
    for positive_num in user_input:
        if positive_num == positive_num[::-1]:
            pallindromic_integer = True
            
print(pallindromic_integer)