# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:35:00 2019

@author: user
"""
 
filename = input("Enter a filename: ")
 
number_of_characters = 0
number_of_words = 0
unique_words = set()
 
for number_of_lines, line in enumerate(open(filename), 1):
    number_of_characters += len(line)
    number_of_words += len(line.split())
    unique_words.update(line.split())
 
print("Number of lines: {}".format(number_of_lines))
print("Number of characters: {}".format(number_of_characters))
print("Number of words: {}".format(number_of_words))
print("Number of unique words: {}".format(len(unique_words)))
 
