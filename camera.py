import cv2
import numpy as np
import os, json

tani = cv2.face.LBPHFaceRecognizer_create()
tani.read('data/trainer.yml')

faceCascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

id = 0
dictionary = {}

names = []
dosya = open("ids.json","r")
dictionary = json.load(dosya)
cam = cv2.VideoCapture(0)

for key, value in dictionary.items():
     names.append(key)

while True:
     ret, frame = cam.read()
     frame = cv2.flip(frame,1)
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

     faces = faceCascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

     for(x,y,w,h) in faces:
          cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
          id,oran = tani.predict(gray[y:y+h, x:x+w])
          print(id)

          if(oran < 70):
               id = names[id]
          else:
               id = "Bilinmiyor"
          cv2.putText(frame, str(id),(x+5,y-5), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
          

     cv2.imshow("Yuz Tanima Sistemi", frame)
     if(cv2.waitKey(10) & 0xFF == 27):
          break
