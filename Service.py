# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 02:15:30 2019

@author: yasha
"""

from pymongo import MongoClient 
try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

db = conn.Job_Portal_Group
collection = db.Services


_id = input ("Enter _id followed by Services_ : " )
Course_Certification = input ("Enter Course Name : ")
Cost_Course_Certification = input ("Enter the cost of Certification : ")

Sample_Resume = input ("Prepare Resume :" )
Name = input ("Please enter your Name Field :" )
Last_Name = input ("Please enter your Last Name Field :" )
Email_ID = input ("Please enter Email-Id Field: ")
Contact = input ("Please enter Contact Number Field: ")
Objective = input("Please enter Objective Field: ")
Skill = input("Please enter Skill set Field: ")
Internships = input("Enter Intership Name Field: ")
Workshop = input ("Enter Workshop Name Field: ")
Certification = input("Enter Certification Name Field: ")
Work_experience = input("Enter Work Experience Name Field: ")
Strength = input("Enter Strength Field: ")



collection.insert_many(
        [
                {"_id" : _id, 
                 "Course_Certification" : Course_Certification,
                 "Cost_Course_Certification" : Cost_Course_Certification,
                 "Resume" : [{"Name": Name,
                             "Last_Name" : Last_Name, 
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