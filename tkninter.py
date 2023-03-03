import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox

win = Tk()

#M E N U S

def nothing():
    file = Toplevel(win)
    button = Button(file,text='do nothing')
    button.pack()

menubar = Menu(win)
filemenu = Menu(menubar)

filemenu.add_command(label="New Window",command = nothing)
filemenu.add_command(label="New File",command = nothing)
filemenu.add_command(label="Open",command = nothing)
filemenu.add_command(label="Close",command = nothing)
filemenu.add_separator()
filemenu.add_command(label="Save",command = nothing)
filemenu.add_command(label="Save as",command = nothing)
filemenu.add_separator()
filemenu.add_command(label="Close tab",command = nothing)
filemenu.add_separator()
filemenu.add_command(label="Exit",command = win.quit)

menubar.add_cascade(label="File",menu = filemenu)

editmenu = Menu(menubar)
filemenu = Menu(menubar)

filemenu.add_command(label="Undo",command = nothing)
filemenu.add_command(label="Redo",command = nothing)
filemenu.add_separator()
filemenu.add_command(label="Cut",command = nothing)
filemenu.add_command(label="Copy",command = nothing)
filemenu.add_command(label="Paste",command = nothing)
filemenu.add_command(label="Select all",command = nothing)
filemenu.add_separator()
filemenu.add_command(label="Exit",command = win.quit)

menubar.add_cascade(label="Edit",menu = filemenu)


win.config(menu = menubar)

#mb = Menubutton(win,text='file')
#mb.grid()
#mb.menu = Menu(mb)
#mb['menu'] = mb.menu

#x1 = IntVar()
#x2 = IntVar()

#mb.menu.add_checkbutton(label='open',variable=x1)
#mb.menu.add_checkbutton(label='close',variable=x2)

#mb.pack()



















#W I N D O W  C O N F I G

#def hello():
    #messagebox.showinfo('from computer','hey there!')
#b = Button(win,text = 'click pls',command = hello)
#b.pack()


#win.title("first")
#top = Toplevel()
#top.title('second')
#win.mainloop()




#lb = Listbox(win)
#lb.insert(1,'python')
#lb.insert(2,'c')
#lb.insert(3,'c++')
#lb.insert(4,'jquery')
#lb.insert(5,'ruby')

#lb.pack()



#frame = Frame(win)
#frame.pack()

#frame2 = Frame(win)
#frame2.pack(side=BOTTOM)

#rb = Button(frame,text='Red',fg='red')
#rb.pack(side=RIGHT)

#bb = Button(frame,text='Blue',fg='blue')
#bb.pack(side=TOP)

#blb = Button(frame,text='Black',fg='black')
#blb.pack(side=BOTTOM)

#gb = Button(frame,text='Green',fg='green')
#gb.pack(side=LEFT)


#C A N V A S


#l1 = Label(win,text="First Number")
#l1.grid(row=1,column=0)

#l2 = Label(win,text="Second Number")
#l2.grid(row=2,column=0)

#label = Label(win)
#label.grid(row=6,column=2)

#x1 = StringVar()
#x2 = StringVar()

#e1 = Entry(win,textvariable=x1)
#e1.grid(row=1,column=2)
#e2 = Entry(win,textvariable=x2)
#e2.grid(row=2,column=2)

#def sum(label,x1,x2):
    #n1 = (x1.get())
    #n2 = (x2.get())
    #sum = int(n1) + int(n2)
    #label.config(text='sum is :%d'%sum)
    #return

#sum= partial(sum,label,x1,x2)
#button = Button(win,text = "Calculate", command=sum)
#button.grid(row=3,column=0)


#B U T T O N S


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


#W I N D O W


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

