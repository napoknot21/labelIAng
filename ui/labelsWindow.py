from tkinter import *

class LabelsWindow:

    def __init__(self):
        self.window = Tk()
        self.initWindow()
        self.loadAndPlaceMainLabels()
        self.loadAndPlaceFooterButtons()
        self.subSelectLabelsNumber()
        self.loadAndPLaceBodylabels()
        self.menuSelector()


        self.window.mainloop()


    # Initialize main window
    def initWindow(self):
        self.window.title("Video app")
        self.window.geometry("707x500")
        self.window.config(background="white")
        self.loadIconWindow("ui/.images/icon.png")
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
    def loadMainLabels(self):
        self.initHeaderLabel()
        self.initBodyLabel()
        self.initFooterLabel()


    # Function that places all the main labels
    def loadAndPlaceMainLabels(self):
        self.loadMainLabels()
        self.header.grid(column=0, row=0)
        self.body.grid(column=0, row=1)
        self.footer.grid(column=0, row=2)


    def subSelectLabelsNumber(self):
        self.labelsNumber = Label(
            self.body,
            bg='white',
            width=100,
            height=4,
        )
        self.labelsNumber.grid()


    def subBodyLabelTextAndMenu (self) :
        self.text_body = Label(
            self.labelsNumber,
            text="Select number of labels",
            fg="blue",
            bg="white"
        )
        self.text_body.grid(column=0, row=0)
        self.menu_body = Label (
            self.labelsNumber,
            fg="blue",
            bg="white"
        )
        self.menu_body.grid(column=1, row=0)

    def menuSelector (self) :
        self.optionList = []
        for i in range (100) :
            self.optionList += [i]
        var = StringVar(self.menu_body)
        var.set(self.optionList[0])
        self.optionMenu = OptionMenu(
            self.menu_body,
            var,
            *self.optionList
        )
        self.optionMenu.pack()

    def loadAndPLaceBodylabels (self) :
        self.subBodyLabelTextAndMenu()








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