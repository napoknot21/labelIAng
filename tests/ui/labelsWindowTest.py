import os, sys
from tkinter import *

userin = ""

root = Tk()
root.geometry('1080x660')
root.title('Terminal')
root.configure(bg="black")

e = Entry(root, textvariable=userin, fg='lime', bg='black')
e.grid()

def process (event=None) :
    content = e.get()
    print(content)

e.bind('<Return>', process)
root.mainloop()