#import pymongo
import pymongo 
import os
from dotenv import load_dotenv
load_dotenv()

# Fetch mongo env vars
# usr = os.environ['MONGO_DB_USER']
# pwd = os.environ['MONGO_DB_PASS']
# mongo_db_name = os.environ['MONGO_DB_NAME']
# mongo_collection_name = os.environ['MONGO_COLLECTION_NAME']
# url = os.environ['MONGO_DB_URL']

# Create a connection to the MongoDB server
#connectionString = "mongodb+srv://User_practice_project:upp99@clusterpracticeproject.mggtnup.mongodb.net/?retryWrites=true&w=majority"
connectionString = os.environ['CONNECTION_STRING']
try:
    client = pymongo.MongoClient(connectionString)
except Exception:
    print ("error" + Exception)

#create a database
db = client['python-mongoDB-CRUD']

#create a collection
collection = db['demo_collection']

#create a document
'''Doc = {
    "name":"Dilini Liyanage",
    "message":"This is the 1st document in python-mongoDB-CRUD"
}

Doc2 = {
    "name":"Dilini Liyanage",
    "message":"This is the 2nd document in python-mongoDB-CRUD"
}

Doc3 = {
    "name":"Dilini Liyanage",
    "message":"This is the 3rd document in python-mongoDB-CRUD"
}

#insert a document
res = collection.insert_one(Doc)
print(res.inserted_id)

collection.insert_one(Doc2)
collection.insert_one(Doc3)'''

print (client.list_database_names())

#read a document
record = collection.find_one()
print(record)

'''#update a document
query = {"message":"This is the 1st document in python-mongoDB-CRUD"}
new_value = {"$set":{"message":"This is the updated document in python-mongoDB-CRUD doc 1"}}
collection.update_one(query, new_value)

#delete a document
query_del = {"message":"This is the updated document in python-mongoDB-CRUD doc 1"}
collection.delete_one(query_del)'''