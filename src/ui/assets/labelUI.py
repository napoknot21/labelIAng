from cProfile import label
from src.core import label as lb
import tkinter as tk
import matplotlib as mt


class LabelUI :

    def __init__ (self, master, label):
        self.master = master
        self.label = label


    def loadLabelBlock (self) :
        label_block = tk.Label (
            self.master,
            height=4, 
            width=60
        )

        id_label = tk.Label (
            label_block,
            text="ID: " + str(self.label.getId())
        )
        id_label.place(relwidth=.02, relheight=1, relx=0, rely=0)
        # Specific label for the name block
        name_label = tk.Label(
            label_block,
            text="NAME LABEL: " + str(self.label.getName())
        )
        name_label.place(relwidth=.09, relheight=1, relx=.02, rely=0)
        color_label = tk.Label(
            label_block
        )
        color_label.place(relwidth=.02, relheight=1, relx=.11, rely=0)
        # Canvas for the color label => get color value (string)
        color_canvas = tk.Canvas (
            color_label,
            bg=str(self.label.getColor())
        )
        color_canvas.place(relx=.5, rely=.5, relwidth=.8, relheight=.8, anchor="CENTER")

        return label_block

    
    def getMaster (self) :
        return self.master


    def getLabel (self) :
        return self.label