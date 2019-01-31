#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 12:06:18 2019

@author: hienh
"""

import requests
endpoint ="https://data.police.uk/api/crimes-at-location?date=2017-02&lat=52.629729&lng=-1.131592"
response = requests.get(endpoint)
print (response)
