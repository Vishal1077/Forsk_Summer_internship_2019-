# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:31:26 2019

@author: user
"""

import csv

def print_file():
    with open("zoo.csv","rt") as zoo:
        file = zoo.readlines()
        print(file)
    
print_file()





def list_of_animal():
    list1 = []
    with open('zoo.csv') as anim:
        file_read = csv.reader(anim, delimiter =',')
        next(file_read)
        for i in file_read:
            if i[0] not in list1:
                list1.append(i[0])
        print(list1)

list_of_animal()







def every_animal_water_need():
    with open('zoo.csv','rt') as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')
        
        total_water_needed_elephant = 0
        total_water_needed_tiger = 0
        total_water_needed_zebra = 0
        total_water_needed_lion = 0
        total_water_needed_kangaroo = 0
    
        next(csv_read) 
        for column in csv_read:
            if column[0]=="elephant":
                total_water_needed_elephant = int(column[2])+total_water_needed_elephant
            if column[0]=="tiger":
                total_water_needed_tiger = int(column[2])+total_water_needed_tiger
            if column[0]=="zebra":
                total_water_needed_zebra = int(column[2])+total_water_needed_zebra
            if column[0]=="lion":
                total_water_needed_lion = int(column[2])+total_water_needed_lion
            if column[0]=="kangaroo":
                total_water_needed_kangaroo = int(column[2])+total_water_needed_kangaroo
                
        animal_dictionary = {}
        
        animal_dictionary["elephant"]=total_water_needed_elephant
        animal_dictionary["tiger"]=total_water_needed_tiger
        animal_dictionary["zebra"]=total_water_needed_zebra
        animal_dictionary["lion"]=total_water_needed_lion
        animal_dictionary["kangaroo"]=total_water_needed_kangaroo
        
        print (animal_dictionary)
        
every_animal_water_need()






def total_water_need():
    with open("zoo.csv","rt") as csv_file:
        csv_read = csv.reader(csv_file, delimiter = ',')
        total_water_needed = 0
        next(csv_read)
        for column in csv_read:
            total_water_needed = int(column[2])+total_water_needed         
print(total_water_needed)

total_water_need()
            