# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:05:17 2019

@author: user
"""

given_tuple = ('Monday', 'Wednesday', 'Thursday', 'Saturday')

new_tuple = (given_tuple[0],) + ('Tuesday',) + given_tuple[1:3] + ('Friday',) + (given_tuple[-1],) + ('Sunday',)

print (new_tuple)