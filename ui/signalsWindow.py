from tkinter import *
import pandas as pd

class SignalsWindow:

    # Constructor
    def __init__(self, filename_csv=None):
        self.values = []
        self.readSource(filename_csv)  # We suppose the file is already verified
        self.window = Tk()
        self.initialiseWindow()
        self.window.mainloop()


    # Read the file csv source
    def readSource(self, filename_csv):
        if filename_csv.endswith(".csv"):
            self.data = pd.read_csv(filename_csv, index_col=0)
        elif filename_csv.endswith(".xlsx") or filename_csv.endswith(".xls"):
            self.data = pd.read_excel(filename_csv, index_col=0)
        print("File CSV successfully read")


    # Window init properties
    def initialiseWindow(self):
        self.window.title("Signals")
        self.window.geometry("707x503")
        self.window.config(background="white")
        self.window.resizable(False, False)

        self.loadProperties()
        self.placeMainLabels()

        self.loadSubProperties()
        self.placeButtonsSubLabel()


    # Load all main window properties
    def loadProperties(self):
        self.initialiseHeaderLabel()
        self.initialiseBodyLabel()
        self.initialiseBottonsLabel()


    # Initialise a label for the window header
    def initialiseHeaderLabel(self):
        self.header = Label(
            self.window,
            text="Select all Signals to work with",
            width=100,
            height=5,
            fg="blue",
        )


    # Initialise a label for the window body (signals)
    def initialiseBodyLabel(self):
        self.body = Label(
            self.window,
            width=100,
            height=24,
            bg="white",
            fg="Blue",
        )


    # Initialise a label for the window buttons
    def initialiseBottonsLabel(self):
        self.footer = Label(
            self.window,
            width=100,
            height=3,
            fg="blue"
        )


    # Place by a grid method all main labels (label_text, body, footer)
    def placeMainLabels(self):
        self.header.grid(column=0, row=0)
        self.body.grid(column=0, row=1)
        self.footer.grid(column=0, row=2)


    # Load all sub configs in main labels
    def loadSubProperties(self):
        self.initialiseSubLabelBody()
        self.initialiseSubLabelButtons()


    # Load sub label body
    def initialiseSubLabelBody(self):
        self.main_frame = Frame(self.body)
        self.main_frame.pack(fill=BOTH, expand=1)

        self.sub_canvas = Canvas(self.main_frame, bg="white", height=350, highlightbackground="white")
        self.sub_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.sb = Scrollbar(
            self.main_frame,
            orient=VERTICAL,
            command=self.sub_canvas.yview
        )
        self.sb.pack(side=RIGHT, fill=Y)
        self.configSubCanvas()

        self.second_frame = Frame(self.sub_canvas, bg="white", height=350, highlightbackground="white")
        self.sub_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")
        self._loadCheckbuttonsSignals()


    def configSubCanvas(self):
        self.sub_canvas.configure(yscrollcommand=self.sb.set)
        self.sub_canvas.bind('<Configure>', lambda e: self.sub_canvas.configure(scrollregion=self.sub_canvas.bbox("all")))



    def _loadCheckbuttonsSignals(self):
        self.signals = []
        for col_name in self.data.columns:
            value = IntVar()
            self.values.append(value)
            checkbutton_signal = Checkbutton(
                self.second_frame,
                text=col_name,
                #var=cb,
                variable=value,
                onvalue=1,
                offvalue=0
            )
            self.signals.append(checkbutton_signal)
        self.placeSignalsLabel()


    # Initialise the buttons "Accept" and "Exit" for the button_label
    def initialiseSubLabelButtons(self):
        self.buttons = []
        button_accept = Button(
            self.footer,
            text="Exit",
            width=45,
            command=exit,
            bg='white',
            relief='groove'
        )
        self.buttons.append(button_accept)
        button_exit = Button(
            self.footer,
            text="Next",
            width=45,
            command=self.submitValues,
            bg='white',
            relief='groove'
        )
        self.buttons.append(button_exit)


    def submitValues (self) :
        self.signals_selected = []
        i = 0
        for value in self.values :
            if value.get() == 1 :
                self.signals_selected.append(self.signals[i])
                print(self.data.columns[i] + " [SELECTED]")
            i+=1
        print("Signals loaded and save it successfully")
        self.window.destroy()


    # Place all signals on the signal_label
    def placeSignalsLabel(self):
        for j in range(len(self.signals)):
            self.signals[j].grid(column=0, row=j)


    # Place the "accpet button nexto to the "exit" one
    def placeButtonsSubLabel(self):
        i = 0
        for button in self.buttons:
            button.grid(column=i, row=0, padx=15, pady=15)
            i += 1


    def getSignalsSelected (self) :
        return self.signals_selected
