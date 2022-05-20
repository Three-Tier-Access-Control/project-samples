from pprint import pprint
from pymongo import MongoClient
import numpy as np


client = MongoClient('localhost', 27017)
db = client['face_db']


faces = db["face"]



first_person_name = "John"
first_sample_face_embedding = np.random.rand(128).tolist() 

second_person_name = "Julia"
second_sample_face_embedding = np.random.rand(128).tolist()

# faces.insert_many([
#     {"name": first_person_name, "embedding": first_sample_face_embedding},
#     {"name": second_person_name, "embedding": second_sample_face_embedding}
# ])

# faces.insert_one([
#     {"name": first_person_name, "embedding": first_sample_face_embedding},
# ])

# 
# faces.delete_many({})

# count documents
# count = faces.count_documents({})

all_docs = list(faces.find({}))
names, embeddings = [doc["name"] for doc in all_docs], [doc["embedding"] for doc in all_docs]

embeddings = np.array(embeddings)


target_embedding = np.random.rand(128)
pprint(names)
pprint(embeddings)
pprint(count)
