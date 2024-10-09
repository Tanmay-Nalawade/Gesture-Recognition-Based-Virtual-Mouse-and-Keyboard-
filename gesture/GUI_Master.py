# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:27:05 2021

@author: om
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from tkvideo import tkvideo
'''import detection_emotion_practice as validate'''
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
# root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("GESTURE RECOGNIZATION BASED ON MOUSE AND KEYBOARD")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
video_label =tk.Label(root)
video_label.pack()
# read video to display on label
player = tkvideo("videoplayback (2).mp4", video_label,loop = 1, size = (w, h))
player.play()  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="GESTURE RECOGNIZATION BASED ON MOUSE AND KEYBOARD",font=("Times New Roman", 35, 'bold'),
                    background="#152238", fg="white", width=60, height=2)
label_l1.place(x=0, y=0)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def cap_video():
    
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])

def key():
    from subprocess import call
    call(["python","keyboard_hand.py"])
    
    
def Mouse_events():
    from subprocess import call
    call(["python","Mouse_events.py"])

def face_recognisation():
    from subprocess import call
    call(["python","face_recognisation.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Face Recognisation", command=face_recognisation, width=25, height=1,font=('times', 15, ' bold '), bg="red", fg="white")
button1.place(x=100, y=160)

button2 = tk.Button(root, text="Recognized using Mouse",command=Mouse_events,width=25, height=1,font=('times', 15, ' bold '), bg="red", fg="white")
button2.place(x=100, y=220)
button3 = tk.Button(root, text="Recognized using Keyboard",command=key,width=25, height=1,font=('times', 15, ' bold '), bg="red", fg="white")
button3.place(x=100, y=280)

button3 = tk.Button(root, text="Exit",command=window,width=25, height=1,font=('times', 15, ' bold '), bg="red", fg="white")
button3.place(x=100, y=340)

root.mainloop()