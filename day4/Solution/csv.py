# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:35:00 2019

@author: user
"""


import csv

with open('data/passwd') as passwd, open("C:/Users/user/OneDrive/Desktop/Summer Internship/day4/zoo.csv", 'w') as output:
    r = csv.reader(passwd, delimiter=':')
    w = csv.writer(output, delimiter='\t')
    for record in r:
        if len(record) > 1:
            w.writerow((record[0], record[2]))