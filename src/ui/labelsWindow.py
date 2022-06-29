from faulthandler import cancel_dump_traceback_later
from random import random
from tkinter import *
from tkinter.colorchooser import *
from matplotlib.pyplot import title
import numpy as np
from src.core import label as lb

class LabelsWindow:

    def __init__(self):
        self.window = Tk()
        self.initWindow()

        self.colorsArray = []
        self.idsArray = []
        self.namesArray = []

        self.labelsArray = []
        self.graphicsArray = []

        self.loadAndPlaceMainLabels()
        self.loadAndPlaceFooterButtons()
        self.loadAndPlaceSubBodyWidgets()

        self.loadAndPlaceHeaderLabel()

        self.window.mainloop()


    # Initialize main window
    def initWindow(self):
        self.window.title("Video app")
        self.window.geometry("707x500")
        self.window.config(background="white")
        self.loadIconWindow("src/ui/.images/icon.png")
        self.window.resizable(False, False)


    # Import an images and put it as icon window
    def loadIconWindow(self, filePath):
        p1 = PhotoImage(file=filePath)
        self.window.iconphoto(False, p1)


    # Header initialization
    def initHeaderLabel(self):
        self.header = Label(self.window, text="Enter all labels needed", width=100, height=5, fg="blue")


    # Body initialization
    def initBodyLabel(self):
        self.body = Label(self.window, width=100, height=24, bg="white", fg="blue")


    # Footer initialization
    def initFooterLabel(self):
        self.footer = Label(self.window, width=100, height=4, fg="blue")


    # Function initialization for all main label initialization functions
    def __loadMainLabels(self):
        self.initHeaderLabel()
        self.initBodyLabel()
        self.initFooterLabel()


    # Function that places all the main labels
    def loadAndPlaceMainLabels(self):
        self.__loadMainLabels()
        self.header.grid(column=0, row=0)
        self.body.grid(column=0, row=1)
        self.footer.grid(column=0, row=2)


    # Load all sub-body labels in the window (scrollbar, canvas)
    def loadAndPlaceSubBodyWidgets(self):
        self.sub_body = Canvas(
            self.body,
            bg="white",
            height=350,
            width=680,
            highlightbackground="white"
        )
        self.sub_body.pack(side=LEFT, fill=BOTH, expand=1)
        self.sb = Scrollbar(
            self.body,
            orient=VERTICAL,
            command=self.sub_body.yview
        )
        self.sb.pack(side=RIGHT, fill=Y)
        self.__configSubBodyWidget()
        self.labels_frame = Frame(
            self.sub_body,
            bg="white",
            height=350,
            width=680,
            highlightbackground="white"
        )
        self.sub_body.create_window((0,0), window=self.labels_frame, anchor="nw")


    # Canvas config for the sub body label
    def __configSubBodyWidget(self):
        self.sub_body.configure(yscrollcommand=self.sb.set)
        self.sub_body.bind('<Configure>', lambda e: self.sub_body.configure(scrollregion=self.sub_body.bbox("all")))
        


    # Load text header for the labels canvas
    def __initHeaderLabel (self) :
        label_header = Label (
            self.labels_frame,
            width=675,
            height=2,
            fg="blue",
            bg="white"
        )
        id_label = Label (
            label_header,
            text="id",
            height=2,
            fg="blue",
            bg="white"
        )
        id_label.place(relwidth=.02, relx=0, rely=0)
        name_label = Label(
            label_header,
            text="Name",
            height=2,
            fg="blue",
            bg="white"
        )
        name_label.place(relwidth=.09, relx=.02, rely=0)
        color_label = Label(
            label_header,
            text="Color",
            height=2,
            fg="blue",
            bg="white"
        )
        color_label.place(relwidth=.02, relx=.11, rely=0)
        icon_delete_label = Label(
            label_header,
            height=4,
            bg="white"
        )
        icon_delete_label.place(relwidth=.02, rely=0, relx=.13)
        return label_header


    # Load and place the header fot the label canvas
    def loadAndPlaceHeaderLabel (self):
        label_header = self.__initHeaderLabel()
        label_header.grid(column=0, row=0)


    # Load and generate a graphic label bloc 
    def __loadGraphicLabelBlock (self, defaultId, defaultColor) :
        label = lb.Label(id=defaultId, name=None, color=defaultColor)

        label_block = Label (
            self.labels_frame,
            width=675,
            height=3,
            bg="blue",
            fg="blue"
        )

        id_label = Label (
            label_block,
            height=3,
            bg="black"
        )
        id_label.place(relwidth=.02, relx=0, rely=0)
        id_entry = self.__loadEntryText(id_label)
        id_entry.pack()
        id_entry.insert(END, label.getId())
        lambda e : lb.setId(id_entry.get())

        name_label = Label(
            label_block,
            height=3,
            bg="green"
        )
        name_label.place(relwidth=.09, relx=.02, rely=0)
        name_entry = self.__loadEntryText(name_label)
        name_entry.pack()
        name_entry.insert(END, 'Enter the label name' )
        lambda e : lb.setName(name_entry.get())

        color_label = Label(
            label_block,
            height=3,
            bg="red"
        )
        color_label.place(relwidth=.02, relx=.11, rely=0)
        
        color_canvas = Canvas (
            color_label,
            height=2
        )

        

        icon_delete_label = Label(
            label_block,
            height=3,
            bg="pink"
        )
        icon_delete_label.place(relwidth=.02, rely=0, relx=.13)
        return label_block  


    # Load and generate a entry fot any label (parentWindow )
    def __loadEntryText (self, parentWindow, height=1, width=3) :
        text = Text (
            parentWindow,
            height=height,
            width=width
        )
        return text

    
    # Button selector for changing the canvas color of canvas_colored
    def __loadButtonSelectorColor (self, parentWindow, canvas_colored) :
        button_color = Button(
            parentWindow,
            text="Change",
            command=lambda : canvas_colored.configure(bg=self.__colorBrowserChange)
        )
        return button_color


    # Color browser 
    def __colorBrowserChange (self):
        color = askcolor(title="Select a new Color")
        if not self.__searchElement(color[1]) :
            return color[1]


    # Generate a new random color
    def generateRandomColors (self) :
        random_color = list(np.random.choice(range(255), size=3))
        if not self.__searchElement(random_color) :
            self.colorsArray.append(random_color)
            return
        self.generateRandomColors()


    # Return True if the random color is in the colorsArrays and False else
    def __searchElement (self, random_color) :
        if not self.colorsArray: #if self.colorsArrays has no element
            return False
        for color in self.colorsArray :
            if color == random_color : return True
        return False


    def __loadButtons(self):
        self.buttons = []
        button_exit = Button(self.footer, text="Exit", command=exit, width=45, relief='groove', bg="white")
        self.buttons.append(button_exit)
        button_accept = Button(self.footer, text="Next", width=45, command=exit, relief='groove', bg="white")
        self.buttons.append(button_accept)


    # Place the exit & accept buttons in the fotter label
    def __placeFooterButtons(self):
        for i, button in enumerate(self.buttons) :
            button.grid(column=i, row=0, padx=15, pady=15)


    # ensemble function for buttons
    def loadAndPlaceFooterButtons(self):
        self.__loadButtons()
        self.__placeFooterButtons()


    def getLabels (self) :
        return None