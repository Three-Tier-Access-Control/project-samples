
# import the opencv and  library
import cv2
import face_recognition
  
# define a video capture object
vid = cv2.VideoCapture(2) # default webcam  0 , usb camera 4
  
while(True):  
    # Capture the video frame by frame
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_locations = face_recognition.face_locations(frame)

    print(face_locations)

    # Draw a rectangle around the faces
    for (x, y, w, h) in face_locations:
        cv2.rectangle(frame, (h, x), (y, w), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()