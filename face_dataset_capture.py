# Import Library
import cv2
import numpy as np
import os 
import datetime

#Load Model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Check if the folder is exit, if not then make dir
def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

assure_path_exists('dataset/')

#Initialize image counter
count = 0

#Capture video from webcam (0) or video file('videoname.format')
cap = cv2.VideoCapture(0)
scaling_factor = 1

#Loop for capture video
while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, None, fx=scaling_factor,
                       fy=scaling_factor, interpolation=cv2.INTER_AREA)

    #Detect frames from different size
    face_rects = face_cascade.detectMultiScale(
        frame, scaleFactor=1.3, minNeighbors=3)
    for (x, y, w, h) in face_rects:
        
        #Draw rectangle and put into frame
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # cv2.putText(frame, 'HANDSOME PEOPLE', (x, y-15), cv2.FONT_HERSHEY_SIMPLEX,
        # 1.0, (0, 255, 0), 2, lineType=cv2.LINE_AA)

        #Increment face image
        count += 1

        #Resize the image face capture
        normalisation = cv2.resize(frame[y:y+h,x:x+w], (200,200))
                
        #Save the captured image into the dataset folder        
        cv2.imwrite('dataset/'+str(count)+".jpg",normalisation)

    #Output the video with frame    
    cv2.imshow('Face Dataset Capture', frame)

    #If press q keyboard, the video capture will end 
    if((cv2.waitKey(1) & 0xFF) == ord('q')):
        cap.release()
        cv2.destroyAllWindows()

    elif count>100:
        cap.release()
        cv2.destroyAllWindows()
        break
