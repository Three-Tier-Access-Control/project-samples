from pprint import pprint
from pymongo import MongoClient
import numpy as np
import face_recognition

# client = MongoClient('localhost', 27017)


client = MongoClient("mongodb+srv://ashleytshumba:02june1997@cluster0.ie2a2.mongodb.net/?retryWrites=true&w=majority")

db = client['face_db']


faces = db["face"]

# delete all records
# print("Deleting All....")
# faces.delete_many({})
# print("Deleted.")

# count documents
count = faces.count_documents({})

print("Fething....")

all_docs = list(faces.find({}))
first_name, embeddings = [doc["first_name"]
                     for doc in all_docs], [doc["embedding"] for doc in all_docs]

embeddings = np.array(embeddings)


pprint(first_name)
# pprint(embeddings)
pprint(count)

print("Fething Complete....")
