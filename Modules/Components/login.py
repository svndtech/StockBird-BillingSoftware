from tkinter import *

login_frame = Frame()

def loginComponent():
    login_label = Label(master=login_frame,text="Login")
    login_label.pack()
    login_frame.pack()
    return login_frame
