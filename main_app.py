import tkinter as tk
from tkinter import *
from tkinter import StringVar
from tkinter import messagebox
from contacts import con
import os

class window(object):
    def __init__(self):


        self.root = tk.Tk()
        self.root.geometry('400x400')
        self.root.title("Contacts")

        photo = PhotoImage(file="images.png")
        self.root.iconphoto(False, photo)

        C = Canvas(self.root, bg="blue", height=500, width=500)
        filename = PhotoImage(file='communication+connection+contact+contacts+icon-1320196392476038550.png')
        background_label = Label(self.root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        b1 = Button(self.root,text = 'Add Contact',fg='white',bg='red', command=self.add_contact).place(x=160,y=105)
        b2 = Button(self.root, text='Search Contact', fg='white', bg='red', command= self.get_data).place(x=153, y=140)

        self.root.mainloop()

    def add_contact(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry('400x400')
        self.root.title("Contacts")

        photo = PhotoImage(file="images.png")
        self.root.iconphoto(False, photo)

        C = Canvas(self.root, bg="blue", height=500, width=500)
        filename = PhotoImage(file='communication+connection+contact+contacts+icon-1320196392476038550.png')
        background_label = Label(self.root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.a1 = StringVar(self.root,value= 'Name')
        self.a2 = StringVar(self.root,value= 'Phone')
        self.a3 = StringVar(self.root, value= 'Email')
        self.a4 = StringVar(self.root,value= 'Linkdin')



        e1 = Entry(self.root,textvariable=self.a1).place(x=140,y=100)
        e2 = Entry(self.root, textvariable=self.a2).place(x=140,y=120)
        e3 = Entry(self.root, textvariable=self.a3).place(x=140,y=140)
        e4 = Entry(self.root, textvariable=self.a4).place(x=140,y=160)

        b = Button(self.root,text='Submit',bg='red',fg='white',command=self.send_data).place(x=175,y=200)
        self.root.mainloop()

    def send_data(self):
        if self.a1.get()=="Name" or self.a2.get() =="Phone" or self.a1.get()=="" or self.a2.get() =="" :
            messagebox.showwarning('Invalid',"Phone and Number cannot be Empty")
        else:
            s= [self.a1.get(),self.a2.get(),self.a3.get(),self.a4.get()]

            con.insert_row(self.a1.get(),self.a2.get(),self.a3.get(),self.a4.get())
            messagebox.showinfo('Done','Data Added')
    def get_data(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry('400x400')
        self.root.title("Contacts")

        photo = PhotoImage(file="images.png")
        self.root.iconphoto(False, photo)

        C = Canvas(self.root, bg="blue", height=500, width=500)
        filename = PhotoImage(file='communication+connection+contact+contacts+icon-1320196392476038550.png')
        background_label = Label(self.root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.a10 = StringVar(self.root,value='Name')
        e1 = Entry(self.root, textvariable=self.a10).place(x=140, y=100)
        b = Button(self.root, text='Submit', bg='red', fg='white', command=self.data_check).place(x=175, y=130)

        self.root.mainloop()
    def data_check(self):

        data = con.get_row(self.a10.get())
        if data == None:messagebox.showinfo('Sorry!','No Data Found')
        else:
            self.data_window(data)
    def data_window(self,data):

        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry('400x400')
        self.root.title("Contacts")

        photo = PhotoImage(file="images.png")
        self.root.iconphoto(False, photo)

        C = Canvas(self.root, bg="blue", height=500, width=500)
        filename = PhotoImage(file='communication+connection+contact+contacts+icon-1320196392476038550.png')
        background_label = Label(self.root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)


        l = Label(text=data[0],width = 15,fg='white',bg='red').place(x=140,y=100)
        l = Label(text=data[1], width=15,fg='white',bg='red').place(x=140, y=125)
        l = Label(text=data[2], width=15,fg='white',bg='red').place(x=140, y=145)
        l = Label(text=data[3], width=15,fg='white',bg='red').place(x=140, y=165)
        
        self.root.mainloop()





        pass




con.connect()
o = window()

