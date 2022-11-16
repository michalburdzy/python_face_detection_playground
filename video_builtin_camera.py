import cv2
import numpy as np

f_cas= cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# smile_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')
eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
cv2.namedWindow("Live Transmission", cv2.WINDOW_AUTOSIZE)

while(True):
    ret, frame = cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=f_cas.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    for x,y,w,h in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
        # smiles = smile_cascade.detectMultiScale(roi_gray, 1.1, 3, 0)
        # for (ex,ey,ew,eh) in smiles:
        #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
 

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break