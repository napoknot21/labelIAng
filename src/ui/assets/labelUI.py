from src.core import label as lb
from tkinter import *


class LabelUI :

    # Constructor
    def __init__ (self, master, label):
        """
        Constructor for the LabelUI object

        Parameters
        ----------
            master : Tkinter object
                A Tkinter/Canvas where the graphical label (label.py) should be placed

            label : Label object
                The label to be placed on the master
        """
        self.master = master
        self.label = label


    def loadLabelBlock (self) :
        """
        Loader function for the graphical Label block

        Notes
        -----
            The choice of using a canvas instead of a label is determined by the visualization:
            When scrolling, a label could be not visible on the screen
        """
        label_block = Canvas ( self.master,height=100)
        # id label
        id_label = Label ( label_block, text="ID: " + str(self.label.getId()))
        id_label.place(relwidth=.2, relheight=1, relx=0, rely=0)
        # Specific label for the name block
        name_label = Label (label_block, text="NAME LABEL: " + str(self.label.getName()))
        name_label.place(relwidth=.6, relheight=1, relx=.2, rely=0)
        color_label = Frame(label_block)
        color_label.place(relwidth=.2, relheight=1, relx=.8, rely=0)
        # Canvas for the color label => get color value (string)
        color_canvas = Canvas ( color_label, bg=str(self.label.getColor()))
        color_canvas.place(relx=.5, rely=.5, relwidth=.8, relheight=.8, anchor=CENTER)
        return label_block

    
    # Getter
    def getMaster (self) :
        """Getter fot the master widget """
        return self.master

    # Getter
    def getLabel (self) :
        """Getter for the label widget"""
        return self.label