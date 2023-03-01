import tkinter
from tkinter import *

win = Tk()
win.geometry("800x600")

def prnt():
    print("hello")

b = Button(win, text="button1",command=prnt, padx=20,pady=20,activeforeground='white',activebackground='red')
b.place(x=100,y=200)
b.pack()
b2 = Button(win, text="button2")
b2.place(x=200,y=300)
b2.pack()

win.mainloop()

