# Import Library
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
scaling_factor = 1

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=scaling_factor,
                       fy=scaling_factor, interpolation=cv2.INTER_AREA)

    face_rects = face_cascade.detectMultiScale(
        frame, scaleFactor=1.3, minNeighbors=3)
    for (x, y, w, h) in face_rects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow('Face Detector', frame)

    if((cv2.waitKey(1) & 0xFF) == ord('q')):
        kamera.release()
        cv2.destroyAllWindows()
