from tkinter import *
def printvalue():
    print*userwrote.get())

window=Tk()
userwrote = StringVar()
userwrote.trace("w",lambda name,index,mode:printvalue)
e=Entry(window,fg="Black",bd=5,bg="black",textvariable=userwrote)
e.pack()
window.mainloop()