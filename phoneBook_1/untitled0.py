#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 14:57:49 2019

@author: hienh
"""

#businessname = input('Enter a business category ? ')
#businessname= businessenter.capitalize()
#
#def searchbusinessname(businessname):
#    c.execute('SELECT * FROM businessphonebook WHERE business_name= ?',(businessname,))
#    for row in c.fetchall():
#        id= row[0]
#        businessname = row[1]
#    
#    return id,businessname
#        
##print(searchbusinessname('Ailane'))
#
#businessenter = input('Enter a business category ? ')
#businessenter= businessenter.capitalize()
#
#
#def searchbusinesstype(businesstype):
#    c.execute('SELECT * FROM businessphonebook WHERE business_category= ?',(businesstype,))
#    for row in c.fetchall():
#        print('------------')
#        print(row)
#

    
#searchbusinesstype(businessenter)

#def getherdatabaseInfo_select():
#
#      c.execute(""" SELECT 
#                            businessphonebook.id,
#                            businessphonebook.business_name,
#                            businessphonebook.city,
#                            businessphonebook.country,
#                            businessphonebook.postcode,
#                            
#                            postcodes1.longitude,
#                            postcodes1.latitude,
#                            
#                            businessphonebook.tel,
#                            businessphonebook.business_category
#                            
#                            
#                            FROM businessphonebook
#                            
#                            INNER JOIN postcodes1 ON (businessphonebook.postcode = postcodes1.postcode)
#                                                       
#                            """)
##      for row in c.fetchall():
##          print(row)
##    
#    
#      b_infoDict = {}
#      
##      for b_id, b_name,  city, country, postcode, lat, lon, tel, cat in c.fetchall():
##          b_infoDict[b_id] = b_id, b_name,  city, country, postcode, lat, lon, tel, cat
##
##      return b_infoDict
#      