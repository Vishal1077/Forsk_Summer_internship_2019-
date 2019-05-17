# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:35:33 2019

@author: user
"""


string = ("ToThohisos isos fofunon")  
vowels = 0
def remove_vowels(string):
    vowels = ("o")
    for x in string.lower():
        if x in vowels:
            string = string.replace(x," ")
print (string)