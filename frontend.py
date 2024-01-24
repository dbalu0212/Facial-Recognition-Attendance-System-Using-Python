import tkinter as tk
from tkinter import Message ,Text
#import cv2,os
#import shutil
#import csv
#import numpy as np
#from PIL import Image, ImageTk
#import pandas as pd
#import datetime
#import time
#import tkinter.ttk as ttk
#import tkinter.font as font
#import urllib.request
window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("Face_Recogniser")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
#answer = messagebox.askquestion(dialog_title, dialog_text)
 
window.geometry('1280x1280')
window.configure(background='grey')

#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
message = tk.Label(window, text="         Face-Recognition-Based-Attendance-Management-System"  ,fg="black", bg="white"  ,font=('times', 30, 'italic bold ')) 

message.place(x=200, y=20)

lbl = tk.Label(window, text="Enter ID",width=20  ,height=2, bg="grey"  ,font=('times', 15, ' bold ') ) 
lbl.place(x=400, y=200)

txt = tk.Entry(window,width=20  ,bg="white" ,font=('times', 15, ' bold '))
txt.place(x=700, y=215)

lbl2 = tk.Label(window, text="Enter Name",width=20  ,bg="grey"    ,height=2 ,font=('times', 15, ' bold ')) 
lbl2.place(x=400, y=300)

txt2 = tk.Entry(window,width=20  ,bg="white"  ,font=('times', 15, ' bold ')  )
txt2.place(x=700, y=315)

lbl3 = tk.Label(window, text="Notification : ",width=20  ,bg="grey"  ,height=2 ,font=('times', 15, ' bold ')) 
lbl3.place(x=400, y=400)

message = tk.Label(window, text="" ,bg="grey"  ,width=30  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
message.place(x=700, y=400)

lbl3 = tk.Label(window, text="Attendance : ",width=20  ,bg="grey"  ,height=2 ,font=('times', 15, ' bold  underline')) 
lbl3.place(x=400, y=600)


message2 = tk.Label(window, text="" ,bg="grey",activeforeground = "green",width=30  ,height=2  ,font=('times', 15, ' bold ')) 
message2.place(x=700, y=600)
def clear():
    txt.delete(0, 'end')    
   
def clear2():
    txt2.delete(0, 'end')    

def TakeImages():        
    Id=(txt.get())
  
def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    
def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()


clearButton = tk.Button(window, text="Clear", command=clear  ,width=5  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=950, y=210)
clearButton2 = tk.Button(window, text="Clear", command=clear2  ,width=5  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton2.place(x=950, y=310)    
takeImg = tk.Button(window, text="Take Images", command=TakeImages  ,width=10  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
takeImg.place(x=200, y=500)
trainImg = tk.Button(window, text="Train Images", command=TrainImages  ,width=10  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
trainImg.place(x=500, y=500)
trackImg = tk.Button(window, text="Track Images", command=TrackImages  ,width=10  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
trackImg.place(x=800, y=500)
quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,width=10  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=1100, y=500)

