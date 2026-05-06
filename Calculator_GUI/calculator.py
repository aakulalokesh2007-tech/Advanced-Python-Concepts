from tkinter import*
def press(num):
    if v.get()=="0":
        v.set(num)
    elif v.get() == "syntax error" or v.get()=="zero division error" :
            v.set(num)
    else:    
        v.set(str(v.get())+str(num))
def equals():
    try:
        v.set(eval(v.get()))
    except SyntaxError:
        v.set("syntax error")
    except ZeroDivisionError:
        v.set("zero division error")
def clear():
    v.set("0")
a=Tk()


img=PhotoImage(file="cal.png")
a.iconphoto(True,img)
a.title("calculator")
a.geometry("340x350")
v=StringVar()
v.set("0")
Label(a,textvariable=v,height=4,width=40,bg="lightyellow").pack()
f=Frame(a)
f.pack()
Button(f,text="1",height=4,width=10,command=lambda:press(1)).grid(row=0,column=0)
Button(f,text="2",height=4,width=10,command=lambda:press(2)).grid(row=0,column=1)
Button(f,text="3",height=4,width=10,command=lambda:press(3)).grid(row=0,column=2)
Button(f,text="4",height=4,width=10,command=lambda:press(4)).grid(row=1,column=0)
Button(f,text="5",height=4,width=10,command=lambda:press(5)).grid(row=1,column=1)
Button(f,text="6",height=4,width=10,command=lambda:press(6)).grid(row=1,column=2)
Button(f,text="7",height=4,width=10,command=lambda:press(7)).grid(row=2,column=0)
Button(f,text="8",height=4,width=10,command=lambda:press(8)).grid(row=2,column=1)
Button(f,text="9",height=4,width=10,command=lambda:press(9)).grid(row=2,column=2)
Button(f,text="c",height=4,width=10,command=clear).grid(row=3,column=0)
Button(f,text="0",height=4,width=10,command=lambda:press(0)).grid(row=3,column=1)
Button(f,text="=",height=3,width=7,command=equals,font=6).grid(row=3,column=2)

Button(f,text="+",height=3,width=7,command=lambda:press("+"),font=6).grid(row=0,column=3)
Button(f,text="-",height=3,width=7,command=lambda:press("-"),font=6).grid(row=1,column=3)
Button(f,text="*",height=3,width=7,command=lambda:press("*"),font=6).grid(row=2,column=3)
Button(f,text="/",height=3,width=7,command=lambda:press("/"),font=6).grid(row=3,column=3)
a.mainloop()
