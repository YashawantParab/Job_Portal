# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:20:09 2019

@author: yasha
"""

from pymongo import MongoClient 
try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

db = conn.Job_Portal
collection = db.Services


_id = input ("Enter _id followed ber Course Name : ")
Cost_Course_Certification = input ("Enter the cost of Certification : ")
Course_Certification = input ("Enter the course name : ")

Sample_Resume = input ("Prepare Resume :" )
Name = input ("Please enter your Name Field :" )
Last_Name = input ("Please enter your Last Name Field :" )
Resume = input("Please enter Resume Content :" )
Email_ID = input ("Please enter Email-Id Field: ")
Contact = input ("Please enter Contact Number Field: ")
Objective = input("Please enter Objective Field: ")
Skill = input("Please enter Skill set Field: ")
Internships = input("Enter Intership Name Field: ")
Workshop = input ("Enter Workshop Name Field: ")
Certification = input("Enter Certification Name Field: ")
Work_experience = input("Enter Work Experience Year Field: ")
Strength = input("Enter Strength Field: ")



collection.insert_many(
        [
                {"_id" : _id, 
                 "Course_Certification" : Course_Certification,
                 "Cost_Course_Certification" : Cost_Course_Certification,
                 "Resume" : [{"Name": Name,
                             "Last_Name" : Last_Name, 
                             "Resume" : Resume,
                             "Email_ID" : Email_ID, 
                             "Contact" : Contact, 
                             "Objective" : Objective,
                             "Skill" : Skill,
                             "Internships" : Internships,
                             "Workshop" : Workshop, 
                            "Certification" : Certification, 
                            "Work_experience" : Work_experience,
                            "Strength" :Strength
                            }]
                 },
                ])