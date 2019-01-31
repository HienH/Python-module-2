#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:02:06 2019

@author: hienh
"""

from flask import Flask,render_template
from searchdb import * 
app = Flask(__name__)
getDb() 

@app.route("/")
@app.route("/home")
def home():
    
     businesses = getherdatabaseInfo_select()

     search= request.form.get('searchBusiness')
     search = search.lower().title()


    
    
    
     return render_template("index.html", title = "home")


if __name__ == '__main__':
    app.run(debug =True)