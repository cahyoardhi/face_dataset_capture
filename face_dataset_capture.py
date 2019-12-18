# Import Library
import cv2
import numpy as np
import os 

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
        cv2.rectangle(frame, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        #Create box on the top of rectangle for text
        cv2.rectangle(frame, (x-20, y-50), (x+w+25, y-20), (0, 255, 0), -1)
        cv2.putText(frame, 'FACE DETECTED', (x,y-30), cv2.FONT_HERSHEY_SIMPLEX,
        0.5, (0, 0, 0), 2)

        #Increment face image
        count += 1
    
        #Resize the image face capture
        normalisation   = cv2.resize(frame[y:y+h,x:x+w], (200,200))

        #Convert image to grayscale
        # grayscale       = cv2.cvtColor(normalisation, cv2.COLOR_BGR2GRAY)
                
        #Save the captured image into the dataset folder        
        cv2.imwrite('dataset/'+str(count)+".jpg",normalisation)

    #Output the video with frame    
    cv2.imshow('Face Dataset Capture', frame)

    #If press q keyboard, the video capture will end 
    if((cv2.waitKey(1) & 0xFF) == ord('q')):
        cap.release()
        cv2.destroyAllWindows()

    elif count>500:
        cap.release()
        cv2.destroyAllWindows()
        break
