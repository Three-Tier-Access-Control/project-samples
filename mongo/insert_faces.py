from pprint import pprint
from pymongo import MongoClient
import numpy as np
import face_recognition

# client = MongoClient('localhost', 27017)

client = MongoClient("mongodb+srv://ashleytshumba:02june1997@cluster0.ie2a2.mongodb.net/?retryWrites=true&w=majority")

db = client['face_db']

faces = db["face"]

# Load a sample picture and learn how to recognize it.
ashley_image = face_recognition.load_image_file(
    "face-recognition/known_faces/Ashley_Shumba_0003.png")

ashley_face_encoding = face_recognition.face_encodings(ashley_image)[0]

# Load a second sample picture and learn how to recognize it.
sam_image = face_recognition.load_image_file(
    "face-recognition/known_faces/Sam Phiri.jpg")
sam_face_encoding = face_recognition.face_encodings(sam_image)[0]

# Load a third sample picture and learn how to recognize it.
volition_image = face_recognition.load_image_file(
    "face-recognition/known_faces/Volition Mashamba.jpg")
volition_face_encoding = face_recognition.face_encodings(volition_image)[0]

print("Encoding....")


first_person_name = "Ashley Shumba"
first_sample_face_embedding = ashley_face_encoding.tolist()

second_person_name = "Sam Phiri"
second_sample_face_embedding = sam_face_encoding.tolist()

third_person_name = "Volition Mashamba"
third_sample_face_embedding = volition_face_encoding.tolist()

print("Encoding Complete....")

print("Inserting....")

# faces.insert_one([
#     {"name": first_person_name, "embedding": first_sample_face_embedding},
# ])


faces.insert_many([
    {"name": first_person_name, "embedding": first_sample_face_embedding},
    {"name": second_person_name, "embedding": second_sample_face_embedding},
    {"name": third_person_name, "embedding": third_sample_face_embedding}
])


print("Inserting Complete....")

