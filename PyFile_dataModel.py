# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 12:40:38 2019

@author: yasha
"""

from pymongo import MongoClient 
from getpass import getpass
try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

db = conn.Job_Portal_Group_Dummy
collection = db.User_Credentials

#User Credentials Database
User_Name = input("Enter Your User_Name: ")
Password = getpass ("Enter Your Password: ")
Data= User_Name, Password
#print (Data)

collection.insert_many(
        [
                {"UserName" : User_Name, 
                 "Password" : Password},
                ])

#Register Now
collection01 = db.Register_Now01
First_Name = input("Enter Your First_Name: ")
Last_Name = input("Enter Your Last_Name: ")
Email_id =input("Enter Your Email Address: ")
Phone_Number =input("Enter Your Phone_Number: ")
Date_of_Birth =input("Enter Your Date_of_Birth: ")
Place_of_Birth =input("Enter Your Place_of_Birth: ")
Experience = input("Are you a Fresher or Professional: ")

collection01.insert_many(
        [
                {"First_Name" : First_Name, 
                 "Last_Name" : Last_Name,
                 "Email_id" : Email_id,
                 "Phone_Number" : Phone_Number,
                 "Date_of_Birth" : Date_of_Birth,
                 "Place_of_Birth" : Place_of_Birth,
                 "Experience" :  Experience
                  }])
   



