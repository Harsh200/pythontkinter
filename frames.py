from tkinter import *

window=Tk()
ftop=Frame(window)
ftop.pack()
fbot = Frame(window)
fbot.pack(side=BOTTOM)
lb1=Label(ftop,text="I am harsh")
lb2=Label(ftop,text="i work on python")
lb3=Label(fbot,text="what are you waiting for")
lb1.pack(side=LEFT)
lb2.pack(side=RIGHT)
lb3.pack()

window.mainloop()
#end of program