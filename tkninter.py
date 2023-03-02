import tkinter
from tkinter import *
from functools import partial

win = Tk()
l1 = Label(win,text="First Number")
l1.grid(row=1,column=0)

l2 = Label(win,text="Second Number")
l2.grid(row=2,column=0)

label = Label(win)
label.grid(row=6,column=2)

x1 = StringVar()
x2 = StringVar()

e1 = Entry(win,textvariable=x1)
e1.grid(row=1,column=2)
e2 = Entry(win,textvariable=x2)
e2.grid(row=2,column=2)

def sum(label,x1,x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sum = int(n1) + int(n2)
    label.config(text='sum is :%d'%sum)
    return

sum= partial(sum,label,x1,x2)
button = Button(win,text = "Calculate", command=sum)
button.grid(row=3,column=0)


#l = Label(win,text='username')
#l.pack(side=LEFT)

#e = Entry(win)
#e.pack(side=RIGHT)

#t = Text(win)
#t.insert(INSERT,'hello')
#t.pack()

#c1 = IntVar()
#cb = Checkbutton(win, text='Music', offvalue=0, onvalue=1, height=5,  width=10, variable=c1)
#cb.pack()

#c2 = IntVar()
#cb2 = Checkbutton(win, text='Video', offvalue=0, onvalue=1, height=5,  width=10,variable=c2)
#cb2.pack()

#var = IntVar()

#r1 = Radiobutton(win, text='option1',variable=var,value=1)
#r1.pack()

#r2 = Radiobutton(win, text='option1',variable=var,value=2)
#r2.pack()

#r3 = Radiobutton(win, text='option1',variable=var,value=3)
#r3.pack()

#win.geometry("800x600")

#c = Canvas(win,height=600,width=800,bg='blue')
#cord = 10,50,240,210
#arc = c.create_arc(cord,start=0,extent=150,fill='black')
#line = c.create_line(10,10,200,200,fill='white')
#c.pack()

#def prnt():
#    print("hello")

#b = Button(win, text="button1",command=prnt, padx=20,pady=20,activeforeground='white',activebackground='red')
#b.place(x=100,y=200)
#b.pack()
#b2 = Button(win, text="button2")
#b2.place(x=200,y=300)
#b2.pack()

win.mainloop()

