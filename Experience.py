# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:50:45 2019

@author: yasha
"""


from pymongo import MongoClient 
try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

db = conn.Job_Portal_Group_Dummy
 #Experience
collection02 = db.Experience_Professional
#while Experience not in ("Fresher", "Professional"):
#Experience = input("Are you a Fresher or Professional: ")
#if
#Experience == "Fresher":
Highest_Degree = input("Enter Your Highest Qualification: ")
Degree_Course = input("Enter Your Course Name: ")
University = input("Enter Your University Name: ")
Passing_year = input("Enter Your Year Of Passing: ")
#elif Exp erience == "Professional":
#Highest_Degree = input("Enter Your Highest Qualification:")
#Degree_Course = input("Enter Your Course Name:")
#University = input("Enter Your University Name:")
#Passing_year = input("Enter Your Year Of Passing:")
Current_Company_Name = input("Enter Your Current Company Name: ")
Current_Designation = input("Enter Your Current Designation: ")
Years_Of_Experience = input("Enter Your Years Of Experience: ")
Current_Job_Location = input("Enter Your Current Job Location: ")
Current_Job_Salary = input("Enter Your Salary range (In million: ")
Expected_Job_Salary = input("Enter Your Salary Amount You Expect (In Million): ")
    #else:
     #   print("Please enter value Fresher or Professional")

collection02.insert_many(
        [
                {"Highest_Degree" : Highest_Degree,
                 "Degree_Course" : Degree_Course,
                 "University" : University,
                 "Passing_year" : Passing_year,
                 "Current_Company_Name" : Current_Company_Name,
                 "Current_Designation" : Current_Designation,
                 "Years_Of_Experience" : Years_Of_Experience,
                 "Current_Job_Location" : Current_Job_Location,
                 "Current_Job_Salary" : Current_Job_Salary,
                 "Expected_Job_Salary" : Expected_Job_Salary
                        }]
        )