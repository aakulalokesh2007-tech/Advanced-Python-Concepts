from tkinter import *
import time

def update_clock():
    tim=time.strftime("%I:%M:%S %p")
    b.config(text=tim)
    tim=time.strftime("%x")
    d.config(text=tim)
    tim=time.strftime("%A")
    da.config(text=tim)
    a.after(200,update_clock)

a=Tk()
a.geometry("700x500")
Label(a,text="TIME:",font=("Arial",50)).grid(row=0,column=0)
Label(a,text="DAY:",font=("Arial",50)).grid(row=1,column=0)
Label(a,text="DATE:",font=("Arial",50)).grid(row=2,column=0)
b=Label(a,font=("Arial",50),fg="#00FF00")
b.grid(row=0,column=1)
da=Label(a,font=("Arial",50))
da.grid(row=1,column=1)
d=Label(a,font=("Arial",50),fg="red")
d.grid(row=2,column=1)
update_clock()
a.mainloop()
