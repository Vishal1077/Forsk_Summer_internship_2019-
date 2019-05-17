# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:15:55 2019

@author: user
"""

import requests

url = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=b84c88aea5f03d0a1138"

response = requests.get(url)
response.content

json_data = response.json()

print("USD to INR :- "+str(json_data['USD_INR']))