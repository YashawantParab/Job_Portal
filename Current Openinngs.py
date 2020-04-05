# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:52:56 2019

@author: yasha
"""
from pymongo import MongoClient 
try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

db = conn.Job_Portal_Group_Dummy
#Current Openinngs

collection04 = db.Current_Openings
Current_Designation = input("Enter Your Current Designation: ")
Years_Of_Experience = input("Enter Your Years Of Experience: ")
Current_Job_Location = input("Enter Your Current Job Location: ")
Current_Job_Salary = input("Enter Your Salary range: ")
Expected_Job_Salary = input("Enter Your Salary Amount You Expect: ")

collection04.insert_many(
        [
                {"Current_Designation" : Current_Designation,
                 "Years_Of_Experience" : Years_Of_Experience,
                 "Current_Job_Location" : Current_Job_Location,
                 "Current_Job_Salary" : Current_Job_Salary,
                 "Expected_Job_Salary" : Expected_Job_Salary
                        }])
