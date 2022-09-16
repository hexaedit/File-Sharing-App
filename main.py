import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter import *
import subprocess
import os

from PIL import ImageTk, Image


root = Tk()
root.title("file share")
root.geometry("450x560+500+200")
root.resizable(False, False)
root.configure(bg="#f4fdfe")


def connect():
    os.system('fs.py')

def phone():
   window = Toplevel(root)
   window.title("Send")
   window.geometry("450x560+500+200")
   window.configure(bg ="#f4fdfe")
   window.resizable(False,False)
   img_icon = PhotoImage(file="images\\smartphone.png")
   frame = Frame(window, width=80, height=80)
   frame.pack()
   frame.place(anchor='n',x=230,y=260)
   img = ImageTk.PhotoImage(Image.open("myqr.png"))
   label = Label(frame, image = img)
   label.pack()
   sback = PhotoImage(file="images\\sender.png")
   Label(window,text = "Scan to Connect",font=('Acumin Variable',17,'bold'),bg = "#f4fdfe").place (x=135,y=480)
   Label(window,image = sback).place(x=-2,y=0)
   window.iconphoto(False,img_icon)
   window.mainloop()

imageicon = PhotoImage(file="images\\icon.png")

root.iconphoto(False,imageicon)

Label(root,text="file share",font=('Acumin Variable concept',20,'bold')).place (x=20,y=30)
Frame(root,width="400",height="2",bg="#f3f5f6").place(x=25,y=80)

send_image = PhotoImage(file="images\\smartphone.png")

phone = Button(root,image = send_image,bg = "#f4fdfe",bd=0,command=phone)
phone.place (x=50,y=100)

receive_image=PhotoImage(file="images\\computer.png")

computer = Button(root,image = receive_image,bg = "#f4fdfe",bd=0,command =lambda:os.system("py computer.py"))
computer.place (x=300,y=100)

Label(root,text = "Phone",font=('Acumin Variable',17,'bold'),bg = "#f4fdfe").place (x=50,y=200)
Label(root,text = "Computer",font=('Acumin Variable',17,'bold'),bg = "#f4fdfe").place (x=290,y=200)

background = PhotoImage(file = "images\\background.png")

Label(root,image = background).place(x=-2,y=323)

root.mainloop()
