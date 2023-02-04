# Write a program to build a Digital Clock.

from time import strftime
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Clock')


def time():
    string = strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=('calibri', 40, 'bold'))

label.pack()
time()

mainloop()
