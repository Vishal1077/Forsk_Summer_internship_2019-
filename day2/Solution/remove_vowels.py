# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:28:28 2019

@author: user
"""

string = ['lbm', 'clfrn', 'klhm', 'flrd']
def remove_vowels(string):
    vowels = ("a", "e", "i", "o", "o")
    for x in string.lower():
        if x in vowels:
            string = string.replace(x," ")
print (string)
        