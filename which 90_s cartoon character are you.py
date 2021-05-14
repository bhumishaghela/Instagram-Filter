import os
import sys
from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
import time
import random
import cv2
folder=os.getcwd()
cartoonCharacter={}
root = Tk()
root.title("Which 90's Cartoon Charcter Are You?")
root.geometry("1400x1000")
root.resizable(width = True, height = True)
title= Label(root,text="Which 90's Cartoon Character Are You? ",font='planet_benson 18')
title.pack()
newsize = (200, 168)
lmain = Label(root)
def video_capture():
    
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    video_capture = cv2.VideoCapture(0)
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
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
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.place(relx=0.25,rely=0.1)
    return faces
    
faces=video_capture()
for filename in os.listdir(folder):
    if filename.endswith('.jpg') or filename.endswith('.png'): 
        
        for (x, y, w, h) in faces:
            if w<newsize[0] and h<newsize[1]:
                newsize=(w,h)
            img = Image.open(os.path.join(folder,filename))
            img=img.resize(newsize)
            img = ImageTk.PhotoImage(img)
            filename=filename.replace(".jpg","")
            filename=filename.replace(".png","")
            cartoonCharacter[filename]=img
        
faces=video_capture()
for cartoonname in cartoonCharacter:
    img=cartoonCharacter[cartoonname]
    video_capture()
    for (x, y, w, h) in faces:
        panel = Label(root,image=img)
        panel.image = img
        panel.place(x=2*x+62,y=y-((1/2)*h))
        root.update()
        
        time.sleep(0.21)
    
        panel.destroy()
        root.update()
    
    


    
for (x, y, w, h) in faces:
    names=list(cartoonCharacter.keys())
    choice=random.choice(names)
    img=cartoonCharacter[choice]
    title.config(text="You Are")
    title.pack()

    panel = Label(root,image=img)
    panel.image = img
    panel.place(x=2*x+62,y=y-((1/2)*h))
    root.update()
    
time.sleep(5)
panel.destroy()
title.destroy()
root.update()
root.after(5,root.destroy())   
        
    
