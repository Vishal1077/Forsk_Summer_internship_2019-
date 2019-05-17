# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:49:29 2019

@author: user
"""
nums = input("Enter your no.:- ")
def centered_average(nums):
    items = len(nums)
    total = 0
    high = max(nums)
    low = min(nums)
    for num in nums:
        total += num
        aveg = (total-high-low)/(item-2)
        return num
centered_average = 3    
print(centered_average)