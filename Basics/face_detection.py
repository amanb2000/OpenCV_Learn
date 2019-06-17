import cv2
import numpy as np

cap = cv2.VideoCapture(0) # arg is the device index of camera. Usually 0 or -1.

face_cascade = cv2.CascadeClassifier('assets/haarcascade_frontalface_alt.xml')

while True:
	ret, frame = cap.read()
	gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	face_detect = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

	print("Faces found:", len(face_detect))
	print(face_detect)

	for (x, y, w, h) in face_detect:
		cv2.rectangle(gray_image, (x, y), (x+w, y+h), (255, 100, 100), 1)
	cv2.imshow('frame', gray_image)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()