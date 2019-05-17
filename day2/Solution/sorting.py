# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:01:40 2019

@author: user
"""

student_list = []

while True:
    user_input = input("Enter your input:- ") 
    if not user_input:
        break
    
    name, age, marks = user_input.split(",")
  
    student_list.append( (name, int(age), int(marks) ) )

student_list.sort()
print (student_list)