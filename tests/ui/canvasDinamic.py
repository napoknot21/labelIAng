from tkinter import *
#from tkinter import scrolledtext
#from tkinter import ttk

root = Tk()
root.geometry("700x600")
root.title("Test for the dinamic geometry scrollbar")

tree_frame = Frame (root, bg="red")
tree_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

my_tree_canvas = Canvas (tree_frame, bg="white")
my_tree_canvas.pack(side=LEFT, fill=BOTH, expand=1)

tree_scroll = Scrollbar(tree_frame, orient=VERTICAL, command=my_tree_canvas.yview)
tree_scroll.pack(side=RIGHT, fill=Y)

my_tree_canvas.configure(yscrollcommand=tree_scroll.set)

my_tree_canvas.bind('<Configure>', lambda e : __fill_canvas(e))#my_tree_canvas.configure(scrollregion=my_tree_canvas.bbox("all")))
#, anchor=CENTER)

second_frame = Frame (my_tree_canvas, bg="black")#.pack(side='top', fill="both")#.place(relx=0, rely=0, relwidth=1, relheight=1)
item = my_tree_canvas.create_window((0,0), window=second_frame, anchor="nw")

def create_block (text=0) :
    blockLabel = Label (
        second_frame,
        text=str(text),
        height=5,
        #width=98,
        bg="blue"
    )
    return blockLabel

def __fill_canvas (event) :
    canvas_width = event.width
    my_tree_canvas.itemconfig(item, width=canvas_width)
    my_tree_canvas.configure(scrollregion=my_tree_canvas.bbox("all"))


for i in range(10) :
    label = create_block(i)
    label.pack(side="top", fill="both", expand=1)

root.mainloop()
