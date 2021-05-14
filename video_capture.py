import cv2
import sys
import time
def video_capture():
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    video_capture = cv2.VideoCapture(0)
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = faceCascade.detectMultiScale(
        cv2image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 30),
        #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('My Video',frame)


while True:
    video_capture()
    
  

