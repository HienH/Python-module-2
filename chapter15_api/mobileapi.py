#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:17:28 2019

@author: hienh
"""

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox0d7a2303963940c09c1e18562e8ee54e.mailgun.org/messages",
        auth=("api", "d53425e230f1f63d12dc7171bc049178-060550c6-0bad2ab1"),
        data={"from": "Excited User <mailgun@sandbox0d7a2303963940c09c1e18562e8ee54e.mailgun.org>",
              "to": ["hiienhang@example.com", "YOU@sandbox0d7a2303963940c09c1e18562e8ee54e.mailgun.org"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
    

    
send_simple_message()
