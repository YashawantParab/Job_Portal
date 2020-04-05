# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:52:16 2019

@author: yasha
"""
from pymongo import MongoClient 
try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

db = conn.Job_Portal_Group_Dummy
#EmployerZone
collection03 = db.EmployerZone
Employer_Company_name = input("Enter Your Company Name: ")
Employer_emailid = input("Enter Your Company email address: ")
Employer_Contact_number = input("Enter Your Contact_number : ")
Employer_Company_Location = input("Enter Your Company Location: ")
Industry_Type = input("Enter Your Industry type: ")
Number_Of_Openings = input ("Enter the Number of Openings: ")
collection03.insert_many([{
        "Employer_Company_name" : Employer_Company_name,
        "Employer_emailid" : Employer_emailid,
        "Employer_Contact_number" : Employer_Contact_number,
        "Employer_Company_Location" : Employer_Company_Location,
        "Industry_Type" : Industry_Type,
        "Number_Of_Openings" : Number_Of_Openings
        }
    ]
    )