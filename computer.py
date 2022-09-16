from cProfile import label
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter import *
import subprocess
import os
import http.server
import socket
import socketserver


root = Tk()
root.title("File")
root.geometry("450x560+500+200")
root.configure(bg ="#f4fdfe")
root.resizable(False,False)
Label(root,text="file share",font=('Acumin Variable concept',20,'bold')).place (x=20,y=30)
Frame(root,width="400",height="2",bg="#f3f5f6").place(x=25,y=80)


def select():
    global file_name
    file_name = filedialog.askopenfile(initialdir = os.getcwd(),title  = "Select files",filetypes=(('file_type','*.txt'),('all files' , '*.*')))

def send_file():
    s = socket.socket()
    host  = socket.gethostname()
    port = 8180
    s.bind((host,port))
    s.listen(1)
    print(host)
    print("waiting for connection...")
    conn,address = s.accept()
    file = open(file_name,'rb')
    file_data = file.read(1024)
    conn.send(file_data)
    print("Data send")

def send():
    send1 = Toplevel(root)
    send1.title("Send")
    send1.geometry("450x560+500+200")
    send1.config(background = "#f4fdfe")
    send1.resizable(False,False)
    image_iconS = PhotoImage(file="images\\send.png")
    send1.iconphoto(False,image_iconS)
    
    sender_background = PhotoImage(file="images\\sender.png")
    Label(send1,image = sender_background).place(x=-2,y=0)
    m_background= PhotoImage(file="images\\id.png")
    Label(send1,image = m_background , bg = "#f4fdfe").place(x=100,y=260)

    Button(send1,text = "+ select file",width = 10,height =1,font = 'arial 14 bold',bg  = "#fff",fg = "#000",command=select).place(x=160,y=150)
    Button(send1,text =  "SEND",width  = 8,height =1,font = 'arial 14 bold',bg = "#000",fg="#fff",command = send_file).place(x="300",y="150")
    host = socket.gethostname()
    Label(send1,text=f'ID:(host)' , bg = 'white',fg = 'black').place(x = 140,y = 290)
     

    send1.mainloop()

def recieve():
    recieve1 = Toplevel(root)
    recieve1.title("Recieve")
    recieve1.geometry("450x560+500+200")
    recieve1.config(background = "#f4fdfe")
    recieve1.resizable(False,False)

    def receiver():
        ID = senderID.get()
        filenameR  = incoming_file.get()

        s  = socket.socket()
        port = 8180
        s.connect((ID,port))
        file = open(filenameR,'wb')
        file_data  = s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been recieved successfully")


    image_iconR = PhotoImage(file="images\\receive.png")
    recieve1.iconphoto(False,image_iconR)
    Hbackground = PhotoImage(file="images\\receiver.png")
    Label(recieve1, image = Hbackground).place(x = -2, y =0)

    logo = PhotoImage(file = 'Images\\profile.png')
    Label(recieve1,image  = logo , bg ="#f4fdfe").place(x = 10,y =250)
    Label(recieve1,text="Recieve",font = ('arial',20),bg = "#f4fdfe").place(x = 100,y = 280)

    Label(recieve1 , text  = "Input sender id" , font = ('arial',10,'bold'),bg = "#f4fdfe").place(x = 20,y = 340)
    senderID  = Entry(recieve1,width = 25,fg = "black",border = 2,bg ='white',font =('arial',15))
    senderID.place(x = 20, y = 370)
    senderID.focus()

    Label(recieve1 , text  = "Filename" , font = ('arial',10,'bold'),bg = "#f4fdfe").place(x = 20,y = 420)
    incoming_file  = Entry(recieve1,width = 25,fg = "black",border = 2,bg ='white',font =('arial',15))
    incoming_file.place(x = 20, y = 450)

    imageicon = PhotoImage(file = "images\\arrow.png")
    rr = Button(recieve1,text = "Recieve",compound=LEFT,image = imageicon ,width = 130,bg = '#39c790',font  = 'arial 14 bold',command=receiver)
    rr.place(x = 20, y = 500)


    recieve1.mainloop()



imageicon = PhotoImage(file="images\\icon.png")

root.iconphoto(False,imageicon)

Label(root,text="file share",font=('Acumin Variable concept',20,'bold')).place (x=20,y=30)
Frame(root,width="400",height="2",bg="#f3f5f6").place(x=25,y=80)

send_image = PhotoImage(file="images\\send.png")

phone = Button(root,image = send_image,bg = "#f4fdfe",bd=0,command=send)
phone.place (x=50,y=100)

receive_image=PhotoImage(file="images\\receive.png")

computer = Button(root,image = receive_image,bg = "#f4fdfe",bd=0,command =recieve)
computer.place (x=300,y=100)

Label(root,text = "Send",font=('Acumin Variable',17,'bold'),bg = "#f4fdfe").place (x=50,y=200)
Label(root,text = "Recieve",font=('Acumin Variable',17,'bold'),bg = "#f4fdfe").place (x=290,y=200)

background = PhotoImage(file = "images\\background.png")

Label(root,image = background).place(x=-2,y=323)


root.mainloop()