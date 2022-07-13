from calendar import c
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from turtle import ontimer

from pip import main

root = Tk()
root.geometry("700x600")
root.title("Test for the dinamic geometru scrollbar")


"""mainLabel = Label(
    root,
    bg="light blue"
)
mainLabel.place(relx=0, rely=0, relheight=1, relwidth=.97)
mainCanvas = Canvas (
    mainLabel,
    highlightbackground="white"   
)


sb = Scrollbar (
    scrollarLabel,
    orient="vertical",
    command=mainCanvas.yview
)
sb.place(relx=0, rely=0, relheight=1, relwidth=1)

mainCanvas.configure(yscrollcommand=sb.set)
mainCanvas.bind('<Configure>', lambda e: mainCanvas.configure(scrollregion=mainCanvas.bbox("all")))


mainFrame = Frame (
    mainCanvas,
    highlightbackground="white"
)

mainCanvas.create_window((0,0), window=mainFrame, anchor="nw")



def create_block (text=0) :
    blockLabel = Label (
        mainCanvas,
        text=str(text),
        height=5,
        width=300,
        bg="blue"
    )
    blockLabel.place()
    return blockLabel

label = create_block()
label.grid(column=0, row=0)#place(relx=0, rely=0, relwidth=1)
"""
"""
for i in range(10) :
    rely = 0
    label = create_block(i)
    label.place(relx=0, rely=rely, relwidth=1)
    rely += 5
"""

tree_frame = Frame (root, bg="red")
tree_frame.place(relx=0, rely=0, relwidth=1, relheight=1)


tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

my_tree_label = Canvas (tree_frame, yscrollcommand=tree_scroll.set)
my_tree_label.pack(side='top', fill=BOTH, expand=False)

#config scrollbar
tree_scroll.config(command=my_tree_label.yview)

"""def create_block (text=0) :
    blockLabel = Label (
        my_tree_label,
        text=str(text),
        height=5,
        bg="blue"
    )
    blockLabel.pack(fill="both", expand=False)
    return blockLabel

for i in range(10) :
    label = create_block(i)
    label.pack()

"""
root.mainloop()
