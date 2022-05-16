import face_recognition
image = face_recognition.load_image_file("/home/ashley/projects/project-samples/images/testimage.jpg")
face_locations = face_recognition.face_locations(image)

print(face_locations)