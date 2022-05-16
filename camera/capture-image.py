
import cv2

cam = cv2.VideoCapture(2)

while True:
	ret, image = cam.read()
	cv2.imshow('Image Test',image)
	# k = cv2.waitKey(1)
	# if k != -1:
	# 	break

	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.imwrite('/home/ashley/projects/project-samples/images/testimage.jpg', image)
		break

cam.release()
cv2.destroyAllWindows()