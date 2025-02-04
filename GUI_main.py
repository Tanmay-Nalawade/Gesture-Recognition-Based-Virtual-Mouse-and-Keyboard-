# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:27:05 2021

@author: om
"""

import tkinter as tk                    #for gui elements
from tkinter import ttk, LEFT, END     # for buttons
from PIL import Image, ImageTk         #for saving many different image file formats
from tkinter.filedialog import askopenfilename       #returns the file name that you selected
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np                  #working with arrays
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
root = tk.Tk()     # is a window with a title bar and other decoration provided by the window manager
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Eye cursor ")

# 43
# video_label =tk.Label(root)
# video_label.pack()
# # read video to display on label
# player = tkvideo("Heart Beats - 4360.mp4", video_label,loop = 1, size = (w, h))
# player.play()
# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('bg.jpg')
image2 = image2.resize((1530, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=70)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="EYE CURSOR",font=("Times New Roman", 35, 'bold'),
                    background="#FFEBCD", fg="black", width=65, height=1)
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

def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
    
 
    
def window():
  root.destroy()


button1 = tk.Button(root, text="LOGIN", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="#FFEBCD", fg="brown")
button1.place(x=20, y=190)

button2 = tk.Button(root, text="REGISTER",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="#FFEBCD", fg="brown")
button2.place(x=20, y=300)

button3 = tk.Button(root, text="EXIT",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="#FFEBCD", fg="brown")
button3.place(x=20, y=500)

root.mainloop()