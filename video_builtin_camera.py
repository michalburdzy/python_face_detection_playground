# pip freeze > requirements.txt

import cv2
cv2.__version__

import numpy as np
import sys

show_frame = False
show_live_transmission = False

if len(sys.argv) == 1:
    print('Usage: python video_builtin_camera.py [show_frame (True/False)] [show_live_transmission (True/False)]')
    quit()

if len(sys.argv) > 1:
    if str(sys.argv[1]) == 'True':
        show_frame = True

    if len(sys.argv) > 2 and str(sys.argv[2]) == 'True':
        show_live_transmission = True


face_cascade= cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# smile_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')
eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')

video_capture_size = 160
face_position_threshod = 30
min_threshold = video_capture_size / 2- face_position_threshod
max_threshold = video_capture_size / 2 + face_position_threshod

print(min_threshold, max_threshold)

video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, video_capture_size)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, video_capture_size)

if show_live_transmission: 
    cv2.namedWindow("Live Transmission", cv2.WINDOW_AUTOSIZE)

def move_to_target(x,y):
    if (x > min_threshold and x < max_threshold and y > min_threshold and y < max_threshold):
        print('CENTER')
        return
    print(x,y)
    if(x >= max_threshold):
        print('MOVE CAM RIGHT')
    elif(x <= min_threshold):
        print('MOVE CAM LEFT')
    if(y >= max_threshold):
        print('MOVE CAM DOWN')
    elif(y <= min_threshold):
        print('MOVE CAM UP')

    return

while(True):
    ret, frame = video_capture.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    for x,y,w,h in face:
        face_center = (x + w//2, y + h//2)
        move_to_target(*face_center)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        cv2.circle(frame,face_center,1,(255,255,0),3)
        
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in eyes:
        #     roi_color = frame[y:y+h, x:x+w]
        #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
        # smiles = smile_cascade.detectMultiScale(roi_gray, 1.1, 3, 0)
        # for (ex,ey,ew,eh) in smiles:
        #     roi_gray = gray[y:y+h, x:x+w]
        #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
 

    if show_frame: 
        cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

