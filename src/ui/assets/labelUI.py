from src.core import label as lb
from tkinter import *
import matplotlib as mt


class LabelUI :

    def __init__ (self, master, label):
        self.master = master
        self.label = label


    def loadLabelBlock (self) :
        label_block = Label ( self.master,height=5)
        id_label = Label ( label_block, text="ID: " + str(self.label.getId()))
        id_label.place(relwidth=.2, relheight=1, relx=0, rely=0)
        # Specific label for the name block
        name_label = Label(label_block, text="NAME LABEL: " + str(self.label.getName()))
        name_label.place(relwidth=.6, relheight=1, relx=.2, rely=0)
        color_label = Label(label_block)
        color_label.place(relwidth=.2, relheight=1, relx=.8, rely=0)
        # Canvas for the color label => get color value (string)
        color_canvas = Canvas ( color_label, bg=str(self.label.getColor()))
        color_canvas.place(relx=.5, rely=.5, relwidth=.8, relheight=.8, anchor=CENTER)
        return label_block

    
    def getMaster (self) :
        return self.master


    def getLabel (self) :
        return self.label