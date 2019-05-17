# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:05:17 2019

@author: user
"""

# accetping string from user and parsing it into List.
user_input = input("Enter String: ")

character_frequency = {}       # initialising the Dict.

# loop to access every element of the list individually.
for alphabet in user_input:

    # adding every element as a 'key' and its frequency of occurance
    #as 'value' in the Dict.
    character_frequency[alphabet] = character_frequency.get(alphabet,0) + 1
    
print (character_frequency)
