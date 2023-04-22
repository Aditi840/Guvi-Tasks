# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 19:58:09 2023

@author: Aditi
"""

import pymongo

#connect to mongodb server
client = pymongo.MongoClient("mongodb://localhost:27017/")

#create a new database
db = client["telephone_directory"]

#create a new collection
collection = db["contacts"]

#define a contact document
contact = {
    "name": "John Smith",
    "phone-number": "555-1234",
    "place": "New York"}

#Insert the contact document into the collection
insert_result = collection.insert_one(contact)
print(f"Inserted contact with ID: {insert_result.inserted_id}")

#find the contact document we just created
query = {"name": "John Smith"}
result = collection.find(query)
for r in result:
    print(r)
    
#update the phone number for the contact document
update_query = {"name": "John Smith"}
update_value = {"$set": {"phone-number": "555-5678"}}
update_result = collection.update_one(update_query, update_value)
print(f"Updated {update_result.modified_count} documents. ")

#find the updated contact document
query = {"name": "John Smith"}
result = collection.find(query)
for r in result:
    print(r)
    
#delete the contact document
delete_query = {"name": "John Smith"}
delete_result = collection.delete_one(delete_query)
print(f"Deleted {delete_result.deleted_count} documents.")

#try to find the deleted contact document
query = {"name": "John Smith"}
result = collection.find(query)
for r in result:
    print(r)