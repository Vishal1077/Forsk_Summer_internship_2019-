 # -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:35:00 2019

@author: user
"""



users = {} 
with open("C:/Users/user/OneDrive/Desktop/Summer Internship/day4/passwd") as f:
    for line in f:
        if not line.startswith("#"):
            user_info = line.split(":")
            users[user_info[0]] = user_info[2]
 
for username in sorted(users):
    print("{}:{}".format(username, users[username]))