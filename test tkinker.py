import tkinter as tk
from tkinter import ttk
from tkinter import *
root = Tk()


a = 50
# this is a function to get the user input from the text input box
canvas = tk.Canvas(root, width = 520, height = 386)
canvas.pack()


# This is the section of code which creates the main window
root.title('Devinette !')


# This is the section of code which creates the a label
Label(canvas, text='Devinette', font=('verdana', 46, 'bold')).place(x=84, y=12)


# This is the section of code which creates the a label
Label(canvas, text='Par enzo', font=('verdana', 36, 'normal')).place(x=140, y=75)


# This is the section of code which creates a text input box
dainput = int(dainput.get())
dainput.place(x=179, y=305)


def Refresh():
    if a < dainput:
        label1 = tk.Label(root, text='Trop grand !', bg='#5F9EA0', font=('helvetica', 20, 'italic')).place(x=39, y=215)
    elif a > dainput:
        label1 = tk.Label(root, text='Trop petit !', bg='#5F9EA0', font=('helvetica', 20, 'italic')).place(x=39, y=215)


# This is the section of code which creates the a label
Label(canvas, text='Devinez un nombre, puis entrez votre nombre après avoir réfléchi!', bg='#5F9EA0', font=('arial', 12, 'normal')).place(x=59, y=265)
Button(root, text='Valider!', bg='#F0F8FF', font=('arial', 12, 'normal'), command=Refresh).place
root.mainloop()