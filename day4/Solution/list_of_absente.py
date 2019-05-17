# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:35:00 2019

@author: user
"""

file = open('absent_students.txt','w')
file.close()

with open('absent_students.txt','a') as file:
    for i in range(25):
        absent_student_name = raw_input("Enter the absent student name: ")
        if absent_student_name=="":
            break
        file.write(absent_student_name+'\n')
        

file = open('absent_students.txt','r')
print file.readlines()
    