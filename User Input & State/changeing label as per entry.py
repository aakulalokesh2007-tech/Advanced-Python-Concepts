from tkinter import *
def fun():
    b["text"]=c.get()
    c.delete(0,END)
a=Tk()
a.title("label changing")
a.geometry("300x300")
b=Label(a,text="DEFAULT")
c=Entry(a)
d=Button(a,text="change label",command=fun)
b.pack()
c.pack()
d.pack()
a.mainloop()
