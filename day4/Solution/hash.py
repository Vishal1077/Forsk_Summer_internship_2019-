# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:15:46 2019

@author: user
"""

import hashlib
def hash_file(filename):
   h = hashlib.sha1()
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
   return h.hexdigest()
message = hash_file("romeo.txt")
print(message)