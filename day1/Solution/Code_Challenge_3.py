# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:04:21 2019

@author: user
"""

#enter marks of assignment
assignment1 = int(input("Enter Marks for Assignment 1: "))
assignment2 = int(input("Enter Marks for Assignment 2: "))
assignment3 = int(input("Enter Marks for Assignment 3: "))
#Enter marks for exams
exam1 = int(input("Enter Marks for Exam 1: "))
exam2 = int(input("Enter Marks for Exam 2: "))
#Calculate weighted_score
weighted_score = ( assignment1 + assignment2 + assignment3 ) * 0.1 + (exam1 + exam2 ) *  0.35
#Print Weighted Score
print("Weighted Score is " + str(weighted_score))
print("Weighted Score is " + str(weighted_score))
