from tkinter import *

def ctof():
    f=float(E1.get())
    c=(f-32)*5/9
    L1.config(text=c)


root=Tk()
root.geometry("500x500")
root.title("C to F Converter")

E1=Entry()
L1=Label(text="")
B1=Button(text="Convert",command=ctof)

E1.place(x=0,y=150)
L1.place(x=0,y=200)
B1.place(x=0,y=220)
    
root.mainloop()
