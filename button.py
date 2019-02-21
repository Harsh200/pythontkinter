from tkinter import *
window=Tk()
def handleClick():
    print("Button click")
btn=Button(window,bd=20,bg="green",fg="red",text="CLick Me",padx=50,pady=80,command=handleClick)

btn.place(x=50,y=50)

window.mainloop()