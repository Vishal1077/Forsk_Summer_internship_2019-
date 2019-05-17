# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:48:05 2019

@author: user
"""


input_string = input("Enter your string >")

camel_case_string = input_string.title()

upper_case_string = camel_case_string.upper()

lower_case_string = camel_case_string.lower()

print("Camel Case string is {}".format(camel_case_string))

print("Upper Case string is {}".format(upper_case_string))

print("Lower Case string is {}".format(lower_case_string))