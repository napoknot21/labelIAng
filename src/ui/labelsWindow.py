from tkinter import *
import numpy as np
from src.core import label as lb

class LabelsWindow:

    def __init__(self):
        self.window = Tk()
        self.initWindow()
        self.loadAndPlaceMainLabels()
        self.loadAndPlaceFooterButtons()
       
        self.colorsArray = []
        self.idsArray = []
        self.namesArray = []

        self.labelsArray = []
        self.graphicsArray = []


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


    def generateRandomColors (self) :
        random_color = list(np.random.choice(range(255), size=3))
        if not self.__searchElement(random_color) :
            self.colorsArray.append(random_color)
            return
        self.generateRandomColors()


    def __searchElement (self, random_color) :
        if not self.colorsArray:
            return False
        for i in range(len(self.colorsArray)):
            cmpt = 0
            for j in range(3):
                if self.colorsArray[i][j] == random_color[j]:
                    cmpt += 1
            if cmpt == 3 :
                return True
        return False


    def loadButtons(self):
        self.buttons = []
        button_exit = Button(self.footer, text="Exit", command=exit, width=45, relief='groove', bg="white")
        self.buttons.append(button_exit)
        button_accept = Button(self.footer, text="Next", width=45, command=exit, relief='groove', bg="white")
        self.buttons.append(button_accept)


    # Place the exit & accept buttons in the fotter label
    def placeFooterButtons(self):
        i = 0
        for button in self.buttons:
            button.grid(column=i, row=0, padx=15, pady=15)
            i += 1


    # ensemble function for buttons
    def loadAndPlaceFooterButtons(self):
        self.loadButtons()
        self.placeFooterButtons()


    def getLabels (self) :
        return None