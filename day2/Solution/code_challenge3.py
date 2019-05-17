# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:57:46 2019

@author: user
"""

#Enter a space seprated value
user_input = input("Enter space seprated value : ").split(" ")

#Shorting input length
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
            
#print pallindromic integer
print(pallindromic_integer)