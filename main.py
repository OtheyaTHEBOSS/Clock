from tkinter import *
from datetime import datetime
from time import strftime
from PIL import ImageTk,Image

w=Tk()
w.geometry('480x320')
w.minsize(375,100)
w.title("Digital Clock")


#Extracting day
a=datetime.today().strftime('%A')
b=(a.upper())
c=(b[0:2])

#setting background
img1=Image.open("g3.jpg")
img2= ImageTk.PhotoImage(img1)
Label(w,image=img2).place(x=-2,y=0)


f1=Frame(w,width=450, height=80,bg='#0e1013')
f1.pack(expand=True)

#Mechenism
def time():
    a=strftime('%H : %M : %S')  #%H   %M   %S
    l1.config(text=a)
    l1.after(1000,time)

l1=Label(f1, font=('Century Gothic',40),
          bg='#0e1013',
          foreground='#d3d3d3')

l1.place(x=130,y=10)
time()

l2=Label(f1, font=('Century Gothic',40),
          bg='#0e1013',
          foreground='#d3d3d3')
l2.config(text=c+" |")
l2.place(x=10,y=10)

#5Required labels
'''def labels():
    l3=Label(f1, font=('Century Gothic',8),bg='#0e1013',fg='#7f7f7f',text='DAY')
    l3.place(x=10,y=130)

    l4=Label(f1, font=('Century Gothic',8),bg='#0e1013',fg='#7f7f7f',text='HOURS')
    l4.place(x=150,y=130)

    l5=Label(f1, font=('Century Gothic',8),bg='#0e1013',fg='#7f7f7f',text='MINUTES')
    l5.place(x=300,y=130)

    l3=Label(f1, font=('Century Gothic',8),bg='#0e1013',fg='#7f7f7f',text='SECONDS')
    l3.place(x=450,y=130)

labels()
'''
w.mainloop()