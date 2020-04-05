# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 09:41:16 2019

@author: yasha
"""
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

db = conn.Job_Portal_Group_Dummy
collection = db.ServicesDummy


_id = input ("Enter _id followed by Services_ : " )
Course_Certification = input ("Enter Course Name : ")
Cost_Course_Certification = input ("Enter the cost of Certification : ")
Sample_Resume = input ("Prepare Resume :" )
Name = input ("Please enter your Name :" )
Last_Name = input ("Please enter your Last Name :" )
Email_ID = input ("Please enter Email-Id: ")
Contact = input ("Please enter Contact Number : ")
Objective = input("Please enter Objective Field: ")
Skill = input("Please enter Skill set : ")
Internships = input("Enter Intership Name: ")
Workshop = input ("Enter Workshop Name: ")
Certification = input("Enter Certification Name: ")
Work_experience = input("Enter Work Experience Name: ")
Strength = input("Enter Strength: ")



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

