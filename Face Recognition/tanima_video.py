import cv2
import os

cam = cv2.VideoCapture("2.mp4")

face_detector = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

global user
user = input("ad: ")

print("\n[BILGI] Kameraya bakın ve bekleyin...")
say = 0

os.mkdir('dataset/'+user)

while True:
     ret, frame = cam.read()
     frame = cv2.flip(frame,1)
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     faces = face_detector.detectMultiScale(gray, 1.5, 5,
        minSize=(30, 30),
        flags= cv2.CASCADE_SCALE_IMAGE)

     for(x,y,w,h) in faces:
          cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,0),2)
          say+=1
          path = "dataset/"+user+"/"
          cv2.imwrite(path+str(say)+".jpg",gray[y:y+h,x:x+w])
          cv2.imshow('DATA',frame)

     k = cv2.waitKey(100)&0xFF
     if(k == 27 or say>=50):
          break

cam.release()
cv2.destroyAllWindows()
