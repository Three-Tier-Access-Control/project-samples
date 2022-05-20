from pprint import pprint
from pymongo import MongoClient
import numpy as np
import face_recognition

client = MongoClient('localhost', 27017)
db = client['face_db']


faces = db["face"]

# delete all records
# faces.delete_many({})

# count documents
count = faces.count_documents({})

print("Fething....")

all_docs = list(faces.find({}))
names, embeddings = [doc["name"]
                     for doc in all_docs], [doc["embedding"] for doc in all_docs]

embeddings = np.array(embeddings)


pprint(names)
# pprint(embeddings)
pprint(count)

print("Fething Complete....")
