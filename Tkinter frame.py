from tkinter import *
top=Tk()
frame=Frame(top)
frame.pack()
redbutton=Button(frame,text="Red", fg="red")
redbutton.pack(side =LEFT)

greenbutton=Button(frame,text="Green", fg="green")
greenbutton.pack(side=RIGHT)
top.mainloop()
