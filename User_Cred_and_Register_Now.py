# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 12:40:38 2019

@author: yash
"""

from pymongo import MongoClient 
from getpass import getpass
try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

db = conn.Job_Portal_DataModel
collection = db.UserDetails


#User Credentials Database
User_Name = input("Enter Your User_Name: ")
Password = getpass ("Enter Your Password: ")
First_Name = input("Enter Your First_Name: ")
Last_Name = input("Enter Your Last_Name: ")
Email_id =input("Enter Your Email Address: ")
Phone_Number =input("Enter Your Phone_Number: ")
Date_of_Birth =input("Enter Your Date_of_Birth: ")
Place_of_Birth =input("Enter Your Place_of_Birth: ")
Experience = input("Are you a Fresher or Professional: ")
Highest_Degree = input("Enter Your Highest Qualification: ")
Degree_Course = input("Enter Your Course Name: ")
University = input("Enter Your University Name: ")
Passing_year = input("Enter Your Year Of Passing: ")
Current_Company_Name = input("Enter Current Company Name: ")
Current_Designation = input("Enter Current Designation: ")
Years_Of_Experience = input("Enter Your Years Of Experience: ")
Current_Job_Location = input("Enter Your Current Job Location: ")
Current_Job_Salary = input("Enter Your Salary range : ")
Expected_Job_Salary = input("Enter Your Salary Amount You Expect : ")
Skills1 = input("Select skills: C++, Python ,JAVA, SQL, MySQL: ")
Skills2 = input("Add some more skills: C++, Python ,JAVA, SQL, MySQL: ")
#Data= User_Name, Password
#print (Data)

collection.insert_many(
        [
                { 
                 "UserName" : User_Name,
                 "Password" : Password,
                 "First_Name" : First_Name, 
                 "Last_Name" : Last_Name,
                 "Email_id" : Email_id,
                 "Phone_Number" : Phone_Number,
                 "Date_of_Birth" : Date_of_Birth,
                 "Place_of_Birth" : Place_of_Birth,
                 "Experience" :  Experience,
                 "Highest_Degree" : Highest_Degree,
                 "Degree_Course" : Degree_Course,
                 "University" : University,
                 "Passing_year" : Passing_year,
                 "Current_Company_Name" : Current_Company_Name,
                 "Current_Designation" : Current_Designation,
                 "Years_Of_Experience" : Years_Of_Experience,
                 "Current_Job_Location" : Current_Job_Location,
                 "Current_Job_Salary" : Current_Job_Salary,
                 "Expected_Job_Salary" : Expected_Job_Salary,
                 "Skills" : [Skills1, Skills2]
                 },
                ])
"""
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

cursor = collection01.find()
for record in cursor: 
    print(record) 
"""