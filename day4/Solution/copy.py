# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:33:29 2019

@author: user
"""



with open("words.txt","rt") as file1, open("new_file.txt","wt") as file2:
    file2.write(file1.read())