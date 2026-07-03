from  tkinter import *
bg=["black","blue"]
def display(pa):
    pa.tkraise()

def create(x,num):
    def lam():
        display(pags[2-num])
    b=Frame(x,bg=bg[num-1])
    c=Label(b,text=f"page :{num}")
    c.pack()
    d=Button(b,text="next" if num==1 else "previous",command=lam)
    d.pack()
    return b



a=Tk()
a.title("frame pages")
pags=[create(a,i) for i in range(1,3)]



for v in pags:
    v.grid(row=0,column=0,sticky="nsew")
    
display(pags[0])

a.mainloop()
    
