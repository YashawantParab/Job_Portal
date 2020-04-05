# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:53:02 2019

@author: yasha
"""

from pymongo import MongoClient 
try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

db = conn.Job_Portal_Group_Dummy
#Jobs by Skills

collection05 = db.Jobs
Jobs_by_skills1 = input("Select skills: C++, Python ,JAVA, SQL, MySQL: ")
Jobs_by_skills2 = input("Add some more skills: C++, Python ,JAVA, SQL, MySQL: ")
Jobs_by_skills3 = input("Add some more  skills: C++, Python ,JAVA, SQL, MySQL: ")
Jobs_by_skills4 = input("Add some more  skills: C++, Python ,JAVA, SQL, MySQL: ")
Jobs_by_skills5 = input("Add some more  skills: C++, Python ,JAVA, SQL, MySQL: ")

#collection06 = db.Jobs.Location
Jobs_by_location1 = input("Select Preferred Location: Heidelberg, Frankfrut: ")
Jobs_by_location2 = input("Select Preferred Location: Heidelberg, Frankfrut: ")

#collection07 = db.Jobs.Industry
Job_by_Industry1 = input("Select Preferred Industry: IT, Automobile: ")
Job_by_Industry2 = input("Select Preferred Industry: IT, Automobile: ")


collection05.insert_many(
        [
                {"Jobs_by_skills1" : Jobs_by_skills1,
                 "Jobs_by_skills2" : Jobs_by_skills2,
                 "Jobs_by_skills3" : Jobs_by_skills3,
                 "Jobs_by_skills4" : Jobs_by_skills4,
                 "Jobs_by_skills5" : Jobs_by_skills5,
                 "Jobs_by_location1" : Jobs_by_location1,
                 "Jobs_by_location2" : Jobs_by_location2,
                 "Job_by_Industry1" : Job_by_Industry1,
                 "Job_by_Industry2" : Job_by_Industry2
                        }])

"""
collection05.insert_many(
        [
                {"Jobs_by_location1" : Jobs_by_location1,
                 "Jobs_by_location2" : Jobs_by_location2
                        }])

collection05.insert_many(
        [
                {"Job_by_Industry1" : Job_by_Industry1,
                 "Job_by_Industry2" : Job_by_Industry2
                        }])
"""
    