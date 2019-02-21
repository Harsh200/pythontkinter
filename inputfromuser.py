from tkinter import *

window=Tk()
userwrote = StringVar()
userwrote.trace("w",)
e=Entry(window,fg="Black",bd=5,bg="black",textvariable=userwrote)
e.pack()
window.mainloop()