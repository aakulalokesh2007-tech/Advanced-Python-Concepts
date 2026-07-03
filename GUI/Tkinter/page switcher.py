from tkinter import *
def do():
    global page
    if page==1:
        b1.pack_forget()
        b3.pack()
        page=2
    elif page==2:
        b3.pack_forget()
        b1.pack()
        page=1
a=Tk()
a.title("Page Switcher")
a.geometry("300x200")

b1=Label(a,text="page 1")
b2=Button(a,text="next",command=do)
b2.pack()
page=1
b1.pack()
b3=Label(a,text="page 2")
a.mainloop()
