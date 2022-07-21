from random import random
from tkinter import *
from tkinter.colorchooser import *
from tkinter import messagebox
from matplotlib import widgets
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

        self.initLabelsArray()

        self.loadAndPlaceMainLabels()
        self.loadAndPlaceFooterButtons()
        self.loadAndPlaceSubBodyWidgets()

        self.loadAndPlaceHeaderLabel()
        self.LoadAndPlaceGraphicalLabels()

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.window.mainloop()


    # Initialize main window
    def initWindow(self):
        self.window.title("Video app")
        self.window.geometry("707x500")
        self.window.config(background="white")
        self.loadIconWindow("extras/images/icon.png")
        #self.window.resizable(False, False)


    # Import an images and put it as icon window
    def loadIconWindow(self, filePath):
        p1 = PhotoImage(file=filePath)
        self.window.iconphoto(False, p1)


    # Header initialization
    def initHeaderLabel(self):
        self.header = Label(self.window, text="Enter all labels needed", fg="blue")


    # Body initialization
    def initBodyLabel(self):
        self.body = Frame (self.window, bg="white")


    # Footer initialization
    def initFooterLabel(self):
        self.footer = Label(self.window, fg="blue")


    # Function initialization for all main label initialization functions
    def __loadMainLabels(self):
        self.initHeaderLabel()
        self.initBodyLabel()
        self.initFooterLabel()


    # Function that places all the main labels
    def loadAndPlaceMainLabels(self):
        self.__loadMainLabels()
        self.header.place(relwidth=1, relheight=.159, relx=0, rely=0)
        self.body.place(relwidth=1, relheight=.72, relx=0, rely=0.159 )
        self.footer.place(relwidth=1, relheight=.121, relx=0, rely=0.879 )


    # Load all sub-body labels in the window (scrollbar, canvas)
    def loadAndPlaceSubBodyWidgets(self):
        self.sub_body = Canvas(self.body, bg="white", highlightbackground="white")
        self.sub_body.pack(side=LEFT, fill=BOTH, expand=1)
        
        self.sb = Scrollbar(self.body, orient=VERTICAL, command=self.sub_body.yview)
        self.sb.pack(side=RIGHT, fill=Y)

        self.sub_body.configure(yscrollcommand=self.sb.set)
        self.sub_body.bind('<Configure>', lambda e: self.__fill_canvas(e))
        
        self.labels_frame = Frame(self.sub_body, bg="white")
        self.item = self.sub_body.create_window((0,0), window=self.labels_frame, anchor="nw")
     


    # Load text header for the labels canvas
    def __initHeaderLabel (self) :
        label_header = Label (self.labels_frame,fg="blue", bg="white", height=1)

        id_label = Label (label_header, text="id", fg="blue", bg="white")
        id_label.place(relwidth=.1, relheight=1, relx=0, rely=0)

        name_label = Label( label_header, text="Name", fg="blue", bg="white")
        name_label.place(relwidth=.5, relheight=1, relx=.1, rely=0)
        
        color_label = Label(label_header, text="Color", fg="blue", bg="white")
        color_label.place(relwidth=.2, relheight=1, relx=.6, rely=0)
        
        icon_delete_label = Label(label_header, bg="white")
        icon_delete_label.place(relwidth=.2, relheight=1, relx=.8, rely=0)
        return label_header


    # Load and place the header fot the label canvas
    def loadAndPlaceHeaderLabel (self):
        label_header = self.__initHeaderLabel()
        label_header.pack(side="top", fill="both", expand=1)


    # Initialise the labels array with at least a single label
    def initLabelsArray (self):
        label = lb.Label(None, None, self.generateRandomColors(), 0)
        self.__addLabel(label)


    # Load and generate a graphic label bloc 
    def __loadGraphicLabelBlock (self, label ,defaultID_Var, defaultName_var) :
        label_block = Label (self.labels_frame, height=4, bg="white", fg="blue")
        # Specific label for the id block
        id_label = Label (label_block)
        id_label.place(relwidth=.1, relheight=1, relx=0, rely=0)
        # Entry for the id label => get Id value (integer)
        id_entry = self.__loadEntryText(id_label, var=defaultID_Var)
        id_entry.place(relx=.5, rely=.5, anchor=CENTER)
        id_entry.bind('<Return>', lambda e : self.submitIdValue(widget=id_entry, label=label))
        id_entry.insert(0, str(label.getId()) if label.getId() is not None else "")
        # Specific label for the name block
        name_label = Label(label_block)
        name_label.place(relwidth=.5, relheight=1, relx=.1, rely=0)
        # Entry for the name label => get name value (string)
        name_entry = self.__loadEntryText(name_label, var=defaultName_var, width=35)
        name_entry.place(relx=.5, rely=.5, relwidth=.8, anchor=CENTER)
        name_entry.bind('<Return>', lambda e : self.submitNameValue(widget=name_entry, label=label))
        name_entry.insert(0, label.getName() if label.getName() is not None else "")
        # Specific label for the color block
        color_label = Label(label_block)
        color_label.place(relwidth=.2, relheight=1, relx=.6, rely=0)
        # Canvas for the color label => get color value (string)
        color_canvas = Canvas (color_label, bg=str(label.getColor()))
        color_canvas.place(relx=.5, rely=.2, relwidth=.5, relheight=.6, anchor=CENTER)
        # Button for changing color of the color canvas
        color_button = self.__loadButtonSelectorColor(color_label, color_canvas, label)
        color_button.place(relx=.5, rely=.7, anchor=CENTER)
        # Specific label for the delete button
        icon_delete_label = Label(label_block)
        icon_delete_label.place(relwidth=.2, relheight=1, rely=0, relx=.8)
        # Button for deleting the current label_block 
        button_delete = Button(icon_delete_label, text="Delete label", command=lambda : self.__destroyGraphicalLabelsBlock(label_block, label.getPos() ))#label_block.destroy())#self.__destroyGraphicalLabelsBlock(label_block))
        button_delete["state"] = self.disableButtonLabels()
        button_delete.place(relx=.5, rely=.5, anchor=CENTER)
        
        return label_block


    def testGraphicalsLabels (self) :
        for i in range (5) :
            label = lb.Label(None, None, self.generateRandomColors(), i+1)
            self.__addLabel(label)


    # Grid all labels from the current label array
    def LoadAndPlaceGraphicalLabels (self) :
        #self.testGraphicalsLabels()
        for i in range (len(self.labelsArray)) :
            id_var1  = ''
            name_var1 = ''
            labelGraphical = self.__loadGraphicLabelBlock(self.labelsArray[i], id_var1, name_var1)
            self.graphicsArray.append(labelGraphical)
            if (self.labelsArray[i] is not None) :
                labelGraphical.pack(side="top", fill="both", expand=1)
        self.label_button = self.loadLabelAddButton()
        self.graphicsArray.append(self.label_button)
        self.label_button.pack(side="top", fill="both", expand=1)
    

    def __destroyGraphicalLabelsBlock(self, label_block, id_block) :
        for i, label in enumerate(self.labelsArray) :
            if label.getPos() == id_block :
                self.labelsArray[i] = None
                self.__cleanArray()
        label_block.destroy()
        self.label_button.destroy()
        self.label_button = self.loadLabelAddButton()
        self.graphicsArray.append(self.label_button)
        self.label_button.pack(side="top", fill="both", expand=1)
        #self.LoadAndPlaceGraphicalLabels()
        

    # submit values for the id label
    def submitIdValue (self, widget, label) :
        content = widget.get()
        if not content.isnumeric() :
            messagebox.showerror("Type id value", "Value must be an integer")
        else :
            content = int (widget.get())
            label.setId(content)


    # Check if the name value is valid strning format
    def submitNameValue (self, widget, label) :
        content = widget.get()
        if not isinstance(widget.get(), str) :
            messagebox.showerror("Type name value", "Value must be a string")
        else :
            content = str(widget.get())
            label.setName(content)


    #Check if the label is at least 1, and the disable or enable the deleting button
    def disableButtonLabels (self) :
        if len(self.labelsArray) <= 1 : return DISABLED
        return NORMAL


    def loadLabelAddButton (self) :
        label_addButton = Label (self.labels_frame, height=4,bg="white")
        
        add_button = Button (label_addButton, text="Add a new Label", command=self.addGraphicalLabel)
        add_button.place(relx=.5, rely=.5, anchor=CENTER)
        return label_addButton


    def addGraphicalLabel (self) :
        len_labels = len(self.labelsArray)
        label = lb.Label(None, None, self.generateRandomColors(), len_labels)
        self.__addLabel(label)
        for label_block in self.graphicsArray :
            label_block.destroy()
        """for label in self.labelsArray :
            print(label.toString())"""
        self.label_button.destroy()
        self.LoadAndPlaceGraphicalLabels()


    #################### self.labelsArray fonctions ############################

    def __addLabel (self, label):
        self.labelsArray.append(label)


    def __cleanArray (self) :
        cmpt = 0
        for i in range (len(self.labelsArray)) :
            if self.labelsArray[i] == None : cmpt += 1
        if cmpt == 0 : return self.labelsArray
        newTab = []
        for i in range (len(self.labelsArray)) :
            if self.labelsArray[i] != None : newTab.append(self.labelsArray[i])
        self.labelsArray = newTab
        return self.labelsArray


    def __compareTwoLabels (self, label1, label2):
        if label1.getId() != label2.getId() : return False
        if label1.getName() != label2.getName() : return False
        if label1.getColor() != label2.getColor() : return False
        if label1.getPos() != label2.getPos() : return False
        return True
 

    def __checkAndChangePosition(self) :
        for i in range (len(self.labelsArray)) :
            if self.labelsArray[i].getPos() != i :
                self.labelsArray[i].setPos(i)

    ########################################################################


    # Load and generate a entry for any label (parentWindow )
    def __loadEntryText (self, parentWindow, var, width=3) :
        text = Entry (parentWindow, textvariable=var, width=width)
        return text

    
    # Button selector for changing the canvas color of canvas_colored
    def __loadButtonSelectorColor (self, parentWindow, canvas_colored, label) :
        button_color = Button(parentWindow, text="Change", command=lambda : canvas_colored.configure(bg=self.__colorBrowserChange(label)))
        return button_color


    # Color browser 
    def __colorBrowserChange (self, label):
        color = askcolor(title="Select a new Color")
        if not self.__searchElement(color[1]) :
            label.setColor(color[1])
            return color[1]


    # Generate a new random color
    def generateRandomColors (self) :
        random_color = tuple(np.random.choice(range(255), size=3))
        random_color = "#" + str('%02x%02x%02x' % random_color)
        if not self.__searchElement(random_color) :
            self.colorsArray.append(random_color)
            return random_color
        self.generateRandomColors()


    # Return True if the random color is in the colorsArrays and False else
    def __searchElement (self, random_color) :
        if not self.labelsArray : #if self.colorsArrays has no element
            return False
        for label in self.labelsArray :
            if label.getColor() == random_color : return True
        return False


    def __loadSubLabelFooter(self):
        self.label_exit = Label(self.footer)
        self.label_exit.place(relheight=1, relwidth=.5, relx=0, rely=0)

        self.label_accept = Label(self.footer,)
        self.label_accept.place(relheight=1, relwidth=.5, relx=0.5, rely=0)


    # Initialise the buttons "Accept" and "Exit" for the button_label
    def __initialiseSubLabelButtons(self):
        self.buttons = []
        button_exit = Button(self.label_exit, text="Exit", width=45, command=self.on_closing,
            bg='white', relief='groove')
        self.buttons.append(button_exit)
        button_accept = Button(self.label_accept, text="Next", width=45, command=self.showAllLabels,
            bg='white', relief='groove')
        self.buttons.append(button_accept)


    # Place the "accpet button nexto to the "exit" one
    def loadAndPlaceFooterButtons(self):
        self.__loadSubLabelFooter()
        self.__initialiseSubLabelButtons()
        for button in self.buttons:
            button.place(relx=.5, rely=0.5, anchor=CENTER)


    def on_closing (self):
        if messagebox.askokcancel("Quit", "Do you really want to quit ?"):
            self.window.destroy()


    def showAllLabels (self):
        if self.labelsArray is not None or len(self.labelsArray) != 0:
            for label in self.labelsArray :
                label.toString()
            self.window.destroy()


    def __fill_canvas (self, event) :
        canvas_width = event.width
        self.sub_body.itemconfig(self.item, width=canvas_width)
        self.sub_body.configure(scrollregion=self.sub_body.bbox("all"))


    def getLabels (self) :
        return self.labelsArray