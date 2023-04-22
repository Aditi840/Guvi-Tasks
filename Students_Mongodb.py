# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 02:12:29 2023

@author: Aditi
"""

import pymongo
import json
from scipy import stats

# Creating a connection with MongoClient
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Creating a database
database = client["students_database"]

# Creating a collection
collection = database["students"]

# Drop the existing students collection
database.drop_collection('students')

# Recreate the students collection with a new _id index
collection = database.create_collection('students')
collection.create_index('_id')


# Loading data from JSON file
with open("C:/Users/Aditi/Documents/students.json", 'r') as f:
    # Initialize an empty list to hold the JSON objects
    json_list = []

    # Read each line in the file and append it to the list
    for line in f:
        json_list.append(json.loads(line))

# Convert the list of JSON objects to a JSON array
json_data = json.dumps(json_list)

# Print the JSON data
print(json_data)

#converting JSON string to Python dictionary
data = json.loads(json_data)

# Inserting data into the collection
collection.insert_many(data)


max_score = collection.find_one(sort=[('scores.score', -1)], projection={'name': 1, '_id': 0})

print(max_score['name'])

def avg_score(scores):
    return sum(score['score'] for score in scores)/len(scores)

#find students who scored below average and pass mark is 40%
result = []
for student in collection.find():
    scores = student["scores"]
    student_avg_score = avg_score(scores)
    exam_avg_score = sum(avg_score(s["scores"]) for s in collection.find())
    if student_avg_score < exam_avg_score and any(score["score"] >= 40 for score in scores):
        result.append(student["name"])

for name in result:
    print(name)

#define pass and fail marks
pass_mark = 40
fail_mark = 20

for student in collection.find():
    for score in student["scores"]:
        if score["score"] < pass_mark:
            score["status"] = "fail"
            
        else:
            score["status"] = "pass"
    collection.update_one({"_id": student["_id"]}, {"$set": {"scores": student["scores"]}})
    
#create a new collection for storing total and average scores
stats_collection = database["score_stats"]

#calculate and insert total average scores for each category
for category in ["exam", "quiz", "homework"]:
    total_score = 0
    num_students = collection.count_documents({})
    for student in collection.find():
        scores = [s for s in student["scores"] if s["type"] == category]
        total_score += sum(s["score"] for s in scores)
    avg_score = total_score / (num_students * len(scores))
    stats_collection.insert_one({"category": category, "total_score": total_score, "avg_score": avg_score})
    
#create a new collection for storing students who meet the criteria
new_collection = database["new_students"]

#find students who meet the criteria and insert them into the new collection
for student in collection.find():
    scores = student["scores"]
    avg_score = sum(score["score"] for score in scores) / len(scores)
    if avg_score < exam_avg_score and all(score["score"] >= 40 for score in scores):
        new_collection.update_one({"_id": student["_id"]}, {"$set": student})
        
#create a collection for students who scored below fail marks in all categories
fail_collection = database["fail_students"]

#find students and insert them into the fail collection
for student in collection.find():
    scores = student["scores"]
    if all(score["score"] < fail_mark for score in scores):
        fail_collection.update_one({"_id": student["_id"]}, {"$set": student})

#create a collection for students who scored above pass marks in all categories
pass_collection = database["pass_students"]
#find students and insert them into the pass collection
for student in collection.find():
    scores = student["scores"]
    if all(score["score"] >= pass_mark for score in scores):
        pass_collection.update_one({"_id": student["_id"]}, {"$set": student})
dco1 = collection.find()

    
