# Import Library
import cv2
import numpy as np
import os 

#Load Model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Capture video from webcam (0) or video file('videoname.format')
cap = cv2.VideoCapture(0)
scaling_factor = 1

#Loop for capture video
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=scaling_factor,
                       fy=scaling_factor, interpolation=cv2.INTER_AREA)

    face_rects = face_cascade.detectMultiScale(
        frame, scaleFactor=1.3, minNeighbors=3)
    for (x, y, w, h) in face_rects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cv2.putText(frame, 'HANDSOME PEOPLE', (x, y-15), cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, (0, 255, 0), 3, lineType=cv2.LINE_AA)

    #Output the video with frame
    cv2.imshow('Face Detector', frame)

    #If press q keyboard, the video capture will end 
    if((cv2.waitKey(1) & 0xFF) == ord('q')):
        kamera.release()
        cv2.destroyAllWindows()
