from tkinter import *

window=Tk()
userwrote=StringVar()
e=Entry(window,fg="Black",bd=5,bg="black",textvariable=userwrote)
e.pack()
window.mainloop()