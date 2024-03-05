from tkinter import *
from tkinter import  messagebox

#run command : pip install pyspeedtest

import pyspeedtest


def one():
    speed = pyspeedtest.SpeedTest("www.google.co.in")
    a1 = (str(speed.download()) + "[Bytes per second]")
    messagebox.showinfo("Your download speed",a1)

root = Tk()
root.title("INTERNET SPEED CHECKER")
root.config(bg="LightBlue")
root.geometry("500x200")

label1 = Label(root,
               text="Internet speed checker",
               font=("Arial",30,"bold"),bg ="lightgreen").pack()

button1 = Button(root, text="Click!!",
                 font=("Arial",30,"bold"),bg ="yellow",
                 height = 1,
                 width=10,
                 command=one).pack()

root.mainloop()
