# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:04:53 2019

@author: user
"""


import requests
 
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3

response = requests.get(url)
response.content


json_data = response.json()

print("Latitude :- " + str(json_data['coord']['lat']))
print("Longitude :- " + str(json_data['coord']['lon']))
print("Weather Condition :- " + str(json_data['weather'][0]['main']))
print("Wind speed :- " + str(json_data['wind']['speed']))
print("Sun Rise :- " + str(json_data['sys']['sunrise']))
print("Sun set :- " + str(json_data['sys']['sunset']))