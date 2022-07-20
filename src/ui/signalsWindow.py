from cProfile import label
from tabnanny import check
from tkinter import *
from tkinter import messagebox
import pandas as pd

class SignalsWindow:

    # Constructor
    def __init__(self, filename_csv=None):
        self.values = []
        self.signals_selected = None
        #self.readImportFile()
        self.readSource(filename_csv)  # We suppose the file is already verified
        self.window = Tk()
        self.initialiseWindow()
        # Load properties
        self.loadProperties()
        self.placeMainLabels()
        # Load sub properties
        self.loadSubProperties()
        self.placeButtonsSubLabel()
        # Main loop
        self.window.mainloop()


    # Auxiliary function for reading the data import
    def readImportFile (self) :
        self.data = pd.read_csv("../.data/import/savesSignals.csv")


    # Read the file csv source
    def readSource(self, filename_csv):
        print("Reading source file...")
        if filename_csv.endswith(".csv"):
            self.data = pd.read_csv(filename_csv, index_col=0)
        elif filename_csv.endswith(".xlsx") or filename_csv.endswith(".xls"):
            self.data = pd.read_excel(filename_csv, index_col=0 )
        print("File CSV successfully read")


    # Window init properties 
    def initialiseWindow(self):
        self.window.title("Signals")
        self.window.geometry("707x503")
        self.window.config(background="white")
        self.loadIconWindow("extras/images/icon.png")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)


    # Import an images and put it as icon window
    def loadIconWindow(self, filePath):
        p1 = PhotoImage(file=filePath)
        self.window.iconphoto(False, p1)


    # Load all main window properties
    def loadProperties(self):
        self.initialiseHeaderLabel()
        self.initialiseBodyLabel()
        self.initialiseBottonsLabel()


    # Initialise a label for the window header
    def initialiseHeaderLabel(self):
        self.header = Label(self.window, text="Select all Signals to work with", fg="blue")


    # Initialise a label for the window body (signals)
    def initialiseBodyLabel(self):
        self.body = Frame (self.window, bg="white")


    # Initialise a label for the window buttons
    def initialiseBottonsLabel(self):
        self.footer = Label(self.window, fg="blue")


    # Place by a grid method all main labels (label_text, body, footer)
    def placeMainLabels(self):
        self.header.place(relwidth=1, relheight=.159, relx=0, rely=0)
        self.body.place(relwidth=1, relheight=.72, relx=0, rely=0.159 )
        self.footer.place(relwidth=1, relheight=.121, relx=0, rely=0.879)



    # Load all sub configs in main labels
    def loadSubProperties(self):
        self.initialiseSubLabelBody()
        self.loadSubLabelFooter()
        self.initialiseSubLabelButtons()


    # Load sub label body
    def initialiseSubLabelBody(self):
        self.body_frame = Frame(self.body, bg="white")
        self.body_frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        self.body_canvas = Canvas(self.body_frame, bg="white")
        self.body_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.sb = Scrollbar(self.body_frame, orient=VERTICAL, command=self.body_canvas.yview)
        self.sb.pack(side=RIGHT, fill=Y)

        self.body_canvas.configure(yscrollcommand=self.sb.set)

        self.body_canvas.bind('<Configure>', lambda e : self.__fill_canvas (e))

        self.second_frame = Frame(self.body_canvas, bg="white")
        self.item = self.body_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")
        self._loadCheckbuttonsSignals()


    def _loadCheckbuttonsSignals(self):
        self.signals = []
        for col_name in self.data.columns:
            label_block = Label ( self.second_frame, height=2, bg="white")
            value = IntVar()
            self.values.append(value)
            checkbutton_signal = Checkbutton(label_block, text=col_name, bg="white",
                fg="blue", variable=value, onvalue=1, offvalue=0)
            self.signals.append(checkbutton_signal)
            label_block.pack(side="top", fill="both", expand=1)
            checkbutton_signal.place(relx=0.5, rely=0.5, anchor=CENTER)
        #self.placeSignalsLabel()



    # Place the exit & accept buttons in the fotter label
    def loadSubLabelFooter(self):
        self.label_exit = Label(self.footer)
        self.label_exit.place(relheight=1, relwidth=.5, relx=0, rely=0)

        self.label_accept = Label(self.footer,)
        self.label_accept.place(relheight=1, relwidth=.5, relx=0.5, rely=0)


    # Initialise the buttons "Accept" and "Exit" for the button_label
    def initialiseSubLabelButtons(self):
        self.buttons = []
        button_accept = Button(self.label_exit, text="Exit", width=45, command=self.on_closing,
            bg='white', relief='groove')
        self.buttons.append(button_accept)
        button_exit = Button(self.label_accept, text="Next", width=45, command=self.submitValues,
            bg='white', relief='groove')
        self.buttons.append(button_exit)


    def submitValues (self) :
        self.signals_selected = []
        for i, value in enumerate(self.values) :
            if value.get() == 1 :
                self.signals_selected.append(self.data.columns[i])
                print(self.data.columns[i] + " [SELECTED]")
        self.destroyAndSend()


    # Place all signals on the signal_label
    def placeSignalsLabel(self):
        for j in range(len(self.signals)):
            self.signals[j].grid(column=0, row=j)


    # Place the "accpet button nexto to the "exit" one
    def placeButtonsSubLabel(self):
        for button in self.buttons:
            button.place(relx=.5, rely=0.5, anchor=CENTER)


    # Command function for the "Next" button
    def destroyAndSend(self):
        if self.signals_selected is None :
            messagebox.showerror("Alert Message", message="You need to check at least one signal")
            return
        if len(self.signals_selected) == 0 :
            messagebox.showerror("Alert Message", message="You need to check at least one signal")
            return
        print("Signals loaded and saved successfully")
        self.window.destroy()


    # Alert messages for closing the window
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit ?"):
            exit(0)


    def __fill_canvas (self, event) :
        canvas_width = event.width
        self.body_canvas.itemconfig(self.item, width=canvas_width)
        self.body_canvas.configure(scrollregion=self.body_canvas.bbox("all"))


    # Getter for the signals selected
    def getSignalsSelected (self) :
        return self.signals_selected
