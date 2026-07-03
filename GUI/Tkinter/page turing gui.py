from tkinter import *
#window size:
HEIGTH=500
WIDTH=100

def display(pa):
    pa.tkraise()



def p1():
    f=Frame(a)
    Label(f,text="on page 1:").pack()
    return f
def p2():
    f=Frame(a)
    Label(f,text="on page 2:").pack()
    return f
def p3():
    f=Frame(a)
    Label(f,text="on page 3:").pack()
    return f
def p4():
    f=Frame(a)
    Label(f,text="on page 4:").pack()
    return f
def p5():
    f=Frame(a)
    Label(f,text="on page 5:").pack()
    return f

a=Tk()
index=0
def add():
    global index
    index +=1
    bq["state"]="active"
    if index >=4:
       bu["state"]="disabled"

    display(fs[index])
def sub():
    global index
    index-=1
    if index<=0:
        bq["state"]="disabled"
    else:
        bu["state"]="active"
        
    display(fs[index])



fs=(p1(),p2(),p3(),p4(),p5())
for v in fs:
    v.grid(row=0,column=0,sticky="nsew")
display(fs[0])

bu=Button(a,text="NEXT",state="active" ,command=add)
bu.grid(row=2,column=1)

bq=Button(a,text="BACK",state="disabled" ,command=sub)
bq.grid(row=2,column=0)






a.mainloop()
