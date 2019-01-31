#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:03:43 2019

@author: hienh
"""



import requests
import json
apikey = '&APPID=f736811e918ca981c13e61311f520686' 


endpoint = http://api.openweathermap.org/data/2.5/weather?q={},uk&APPID=f736811e918ca981c13e61311f520686
city = {"q": "London,UK", "units":"metric", "appid":"YOUR_APP_ID"}
response = requests.get(endpoint, params=payload)
data= response.json()
print(data)
print (response.json)
print (response.status_code)
print (response.headers["content-type"])