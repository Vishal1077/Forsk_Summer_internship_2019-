# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:51:24 2019

@author: user
"""

#Travel in km
travel = float(input("Enter travel in a day - "))
#diesel cost
diesel_cost = 80.0
#vehicle fuel average
fuel_average = 18.0
#during travelling
fuel_consumption = (diesel_cost/fuel_average)
#Cost of driving per day to office
cost_per_day = (diesel_cost*fuel_consumption)
#Printing Cost of Driving per day to office
print ("Cost of driving per day to office is :"+str(round(cost_per_day,2))+" INR")