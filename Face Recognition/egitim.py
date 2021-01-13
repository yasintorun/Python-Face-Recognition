import cv2
import numpy as np
from PIL import Image
import os,json

path = 'dataset'
tani = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")


def getImageAndLabels(path):
     faceSamples = []
     ids = []
     labels = []
     dirs = os.listdir(path)
     dictionary = {}

     for i,k in enumerate(dirs):
          dictionary[k] = int(i)

     f = open("ids.json","w")
     a = json.dump(dictionary,f)
     f.close()

     for k in dirs:
         for res in os.listdir(os.path.join(path,k)):
              PIL_img = Image.open(os.path.join(path,k,res)).convert('L')
              img_numpy = np.array(PIL_img,"uint8")
              id=int(dictionary[k])
              faces = detector.detectMultiScale(img_numpy)
              for(x,y,w,h) in faces:
                   faceSamples.append(img_numpy[y:y+h, x:x+w])
                   ids.append(id)
     return faceSamples, ids


faces,ids = getImageAndLabels(path)
tani.train(faces,np.array(ids))
tani.write('data/trainer.yml')
