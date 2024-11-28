import numpy as np
import cv2
xml2 = 'C:/ass/haarcascade_frontalface_default.xml'
xml2'C:/ass/haarcascade_eye1.xml'
face_cascade=cv2.CascadeClassifier(xml1)
eye_cascade=cv2.CascadeClassifier(xml2)

cap = cv2.VideoCapture(0)
cap.set(3.640)
cap.set(4.480)

while(True):
  ret.frame=cap.read()
  frame=cv2.flip(frame.1)
  gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces=face_cascade.detectMultiScale(gray,1.05,5)
  eyes=eye_cascade.detectMultiScale(gray,1.05,5)
  
  if len(faces):
          for (x,y,w,h) in faces:
            face_img=frame[y:y+h, x:x+w]
            face_img=cv2.resize(face_img, dsize=(0,0), fx=0.04, fy=0.04)
            face_img=cv2.resize(face_img, (w,h), interpolation=cv2.INTER_AREA)
            frame[y:y+h, x:x+w]=face_img

  else:
    for (ex,ey,ew,eh) in eyes:
            eye_img=frame[ey:ey+eh, ex:ex+ew]
            eye_img=cv2.resize(eye_img, dsize=(0,0), fx=0.04, fy=0.04)
            eye_img=cv2.resize(eye_img, (ew,eh), interpolation=cv2.INTER_AREA)
            frame[ey:ey+eh, ex:ex+ew]=eye_img

  cv2.imshow('result', frame)
    
  k = cv2.waitKey(30) & 0xff
  if k == 27: # Esc 키를 누르면 종료
      break
    
cap.release()
cv2.destroyAllWindows()
