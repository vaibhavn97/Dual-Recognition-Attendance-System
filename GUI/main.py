# http://10.40.19.177:8000/
from tkinter import *
from tkinter.messagebox import Message 
from _tkinter import TclError
import tkinter as tk
from PIL import ImageTk,  Image
root = tk.Tk()
import numpy as np
import cv2
import face_recognition
import os
from op import *
import requests
import datetime
import serial
import threading
# Data tramissted to other function
data = {}

# Event Handling 
def setSubject(event):
    text = event.widget.cget("value")
    data['subject'] = text
    print(text, " is Selected")


def setStaff(event):
    text = event.widget.cget("value")
    data['staff'] = text
    print(text, ' staff is selected ')




def getRfidCode():
    ser = serial.Serial()
    ser.port = 'COM3'
    ser.baudrate = 9600
    ser.open()
    name = ""
    while 1:
        while ser.in_waiting:
            data_in = str(ser.read())[2:3]
            name += str(data_in)
            if len(name) == 7: return name
    return "Invalid"

def logic(event):
    threading.Thread(target=submit).start()

def customMessage(m):
    rt = tk.Tk()
    rt.after(2000, rt.destroy) 
    rt.withdraw()
    Message(title="Dual Recognition Attendance System", message=m, master=rt).show()

def submit():
    # tkinter.messagebox.showinfo('Dual Recognitation Attendance System','Scan ID CARD')
    customMessage("Scan Your ID CARD")
    for count in range(3):
        # rfid_code = input("Enter STUDENT PRN") #RFID 
        print(data)
        rfid_code = getRfidCode()
        print(rfid_code)
        respo = requests.get(url="http://10.40.19.177:8000/attendance/is_enroll/", data={
            "rfid_code": rfid_code,
            "subject" : data['subject'],
        })
        code = respo.json()
        print(code)
        if code == "NS":
            customMessage(f'Not a valid Student')    
            f = open("details.txt", "a")
            f.write("Not a Valid Student\n")
            f.close()
        elif code == "NE":
            customMessage(f"Student not enrolled on "+data['subject'])    
            f = open("details.txt", 'a')
            f.write("Student not enrolled for course\n")
        else :
            customMessage(f' Hello {code}, Scanning Face')    
            detected_name = detectFace()
            student_name = code
            print(f"RFID Name is {student_name} and detected name is {detected_name}")
            if detected_name == student_name:
                customMessage(f'Attendace Marked for {code}')    
                requests.post(url='http://10.40.19.177:8000/attendance/get/', data={
                    "student_id":detected_name,
                    "teacher_id":data['staff'],
                    "subject":data['subject']
                })
            elif detected_name == "NSD":
                customMessage("No Face Detected")
            else:
                customMessage("Face Not Matched with PRN")

    


# # Configuring App
root.resizable(0,0)
root.title("Smart Attendance System")
bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(root, image=bgImage)
bgLabel.grid(row=0, column=0)
bgLabel.pack()

heading=Label(root,text='Attendance System',font=('Microsoft Yahei UI Light',18,'bold'),bg='ghost white',fg='grey10')
heading.place(x=570,y=100)
heading=Label(root,text='Select Subject',font=('Microsoft Yahei UI Light',12,'bold'),bg='ghost white',fg='blue')
heading.place(x=570,y=150)


# For Subjects
var = IntVar()
button1=Radiobutton(text="EME", variable=var,value="EME", fg='grey6',bg='ghost white')
button1.pack(anchor=tk.W)
button1.place(x=600,y=190)
button1.bind("<Button-1>",setSubject)

button2=Radiobutton(text="FPGA",variable=var, value="FPGA", fg='grey6',bg='ghost white')
button2.pack(anchor=tk.W)
button2.place(x=600,y=220)
button2.bind("<Button-1>",setSubject)


button3=Radiobutton(text="DAA",variable=var, value="DAA", fg='grey6',bg='ghost white')
button3.pack(anchor=tk.W)
button3.place(x=600,y=250)
button3.bind("<Button-1>",setSubject)


button4=Radiobutton(text="MOBILE",variable=var, value="MOBILE", fg='grey6',bg='ghost white')
button4.pack(anchor=tk.W)
button4.place(x=600,y=280)
button4.bind("<Button-1>",setSubject)



# For Staff 
heading=Label(root,text='Select Teacher',font=('Microsoft Yahei UI Light',12,'bold'),bg='ghost white',fg='blue')
heading.place(x=570,y=310)

var = IntVar()
button1=Radiobutton(text="N.V.Marahe", variable=var, value="nvmarathe", fg='grey6',bg='ghost white')
button1.pack(anchor=tk.W)
button1.place(x=600,y=350)
button1.bind("<Button-1>",setStaff)


button2=Radiobutton(text="R.G.Mevakari", variable=var, value="rgmevekari",fg='grey6',bg='ghost white')
button2.pack(anchor=tk.W)
button2.place(x=600,y=380)
button2.bind("<Button-1>",setStaff)

button3=Radiobutton(text="S.G.Tamhankar", variable=var, value="sgt", fg='grey6',bg='ghost white')
button3.pack(anchor=tk.W)
button3.place(x=600,y=410)
button3.bind("<Button-1>",setStaff)

button4=Radiobutton(text="S.D.Ruikar", variable=var, value="S.U.Ruikar", fg='grey6',bg='ghost white')
button4.pack(anchor=tk.W)
button4.place(x=600,y=440)
button4.bind("<Button-1>",setStaff)


# Final Submit Button
button=Button(text="SUBMIT",font=('Microsoft Yahei UI Light',16,'bold'),bg='navy',fg='snow')
button.place(x=660,y=480)
button.bind("<Button-1>", logic)



root.mainloop()