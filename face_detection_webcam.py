import numpy as np
import cv2

!pip install mtcnn

import mtcnn
from mtcnn.mtcnn import MTCNN

cap=cv2.VideoCapture(0)

while(True):
    ret,frame=cap.read()
    detector=MTCNN()
    faces=detector.detect_faces(frame)
    for face in faces:
      print(face)
      x,y,w,h=face['box']
      cv2.rectangle(frame,(x,y),(x+w,y+h),color=(255,0,0),thickness=2)

    cv2.imshow('frame',frame)
    if cv2.waitKey(20) &0xFF==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()