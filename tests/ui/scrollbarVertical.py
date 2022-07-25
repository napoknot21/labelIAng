from tkinter import *

from pyparsing import common_html_entity
from setuptools import Command

root = Tk()

frame = Frame (root)
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

canvas_1 = Canvas (frame, bg="blue")
canvas_1.pack(side=LEFT, fill=BOTH, expand=1, anchor="nw")

sb_y = Scrollbar (frame, orient='vertical')
sb_y.pack (side=RIGHT, fill=Y)

canvas_2 = Canvas (canvas_1, bg="red") #! the main canvas
canvas_2.pack(side=TOP, fill=BOTH, expand=1)

sb_x = Scrollbar (canvas_1, orient='horizontal')
sb_x.pack (side=BOTTOM, fill=X)

canvas_2.config (yscrollcommand=sb_y.set, xscrollcommand=sb_x.set)

canvas_2.bind('<Configure>', lambda e : canvas_2.configure(scrollregion=canvas_2.bbox("all")))

second_frame = Frame (canvas_2)

item = canvas_2.create_window((0, 0), window=second_frame, anchor="nw")

sb_y.config(command=canvas_2.yview)
sb_x.config(command=canvas_2.xview)

def __fill_canvas_signals(event) :
    pass
    #canvas_width = event.width
    #canvas_2.itemconfig(item, width=canvas_width)
    

for i in range (20) :
    label_block = Label (second_frame, text="Test", height=6, bg="red")
    label_block.pack(side=TOP, fill=BOTH, expand=1)


for i in range (50) :
    label_block = Label (second_frame, text="Test", height=6)
    label_block.pack(side=RIGHT, fill=BOTH, expand=1)


root.mainloop()