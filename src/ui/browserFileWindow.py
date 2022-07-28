from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class BrowserFileWindow:

    # Constructor
    def __init__(self):
        """
        Constructor for the BrowserFileWindow
        
        Notes
        -----
            'filename_csv' : string
                The csv file path

            'filename_video' : string
                the video file path
        """
        self.filename_csv = None
        self.filename_video = None
        # Window settings
        self.window = Tk()
        self.initWindow()
        # Main label settings (header, body, footer)
        self.loadAndPlaceMainLabels()
        # Buttons and sub label settings
        self.loadAndPlaceBodyLabels()
        self.loadAndPlaceFooterButtons()
        #Window warnign about to close it
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()


    # Initialize
    def initWindow(self):
        """Function that initializes the BrowserFileWindow properties"""
        self.window.title("Video app")
        self.window.geometry("707x500")
        self.window.config(background="white")
        self.loadIconWindow("extras/images/icon.png")
        self.window.resizable(False, False)


    # Import an images and put it as icon window
    def loadIconWindow(self, filePath):
        """
        Function that loads an image as a window icon
        
        Parameters
        ----------
            filePath : String
                The image path
        """
        p1 = PhotoImage(file=filePath)
        self.window.iconphoto(False, p1)


    # Header initialization
    def initHeaderLabel(self):
        """Initialize the header label window"""
        self.header = Label(self.window, text="VIDEO APP [BETA]", fg="blue")


    # Body initialization
    def initBodyLabel(self):
        """Initialize the body label window"""
        self.body = Label(self.window, bg="white", fg="blue")


    # Footer initialization
    def initFooterLabel(self):
        """Initialize the footer label window for buttons"""
        self.footer = Label(self.window, fg="blue")


    # Loading and place
    def loadAndPlaceMainLabels(self) :
        """Function that loads and runs all load labels functions with the 'place' method"""
        self.initHeaderLabel()
        self.initBodyLabel()
        self.initFooterLabel()
        self.header.place(relwidth=1, relheight=.159, relx=0, rely=0)
        self.body.place(relwidth=1, relheight=.72, relx=0, rely=0.159 )
        self.footer.place(relwidth=1, relheight=.121, relx=0, rely=0.879)


    # Explorer label 
    def loadLabelExplorerVideo(self):
        """Function that loads and places the file explorer label for the Video file with the 'place' method"""
        self.label_window_explorer_video = Label(
            self.body,
            text="Select a video File",
            fg="blue",
            bg="white"
        )
        self.label_window_explorer_video.place(relwidth=1, relheight=.15, relx=0, rely=0.20)
        # Button browser 
        buttonBrowser = self.browserButtonVideo()
        buttonBrowser.place(rely=0.38, relx=0.5, anchor=CENTER)


    # Explorer label for the csv file
    def loadLabelExplorerCsv(self):
        """Function that loads and places the file explorer label for the CSV File with the 'place' method"""
        self.label_window_explorer_csv = Label(
            self.body,
            text="Select a CSV File",
            fg="blue",
            bg="white"
        )
        self.label_window_explorer_csv.place(relwidth=1, relheight=0.15, relx=0, rely=0.6)
        # Button browser
        buttonBrowser = self.browserButtonCsv()
        buttonBrowser.place(rely=.78, relx= 0.5, anchor=CENTER)


    # Browser button for the video file
    def browserButtonVideo(self):
        """
        Function that loads and returns a button for the video file

        Returns
        ----------
            browserButton : Button (tkinter)
                The browser button widget 
        """
        browserButton = Button(self.body, text="Browse Files", command=self.openFileBrowserVideo, relief='groove', height=1)
        return browserButton


    # Browser button for the csv file
    def browserButtonCsv(self):
        """Function that loads and returns a button for the CSV file

        Returns
        ----------
            browserButton : Button (tkinter)
                The browser button widget 
        """
        browserButton = Button(self.body, text="Browse Files", command=self.openFileBrowserCsv, relief='groove', height=1)
        return browserButton


    # File browser for the video file
    def openFileBrowserVideo(self):
        """Function that loads the browser window and print on the window the video file path"""
        filename = filedialog.askopenfilename(
            initialdir="./",
            title="Select a Video file",
            filetypes=(
                ("AVI videos", "*.avi"),
                ("mp4 videos", "*.mp4"),
                ("All files", "*.*")
            )
        )
        self.setFilePathVideo(filename)
        if self.filename_video is not None:
            if len(self.filename_video) != 0:
                self.printLabelContentVideo()


    # File browser for the video file
    def openFileBrowserCsv(self):
        """Function that loads the browser and prints on the window the csv file path"""
        filename = filedialog.askopenfilename(
            initialdir="./",
            title="Select a CSV file",
            filetypes=(
                ("csv files", "*.csv"),
                ("Excel files", "*.xls"),
                ("All files", "*.*")
            )
        )
        self.setFilePathCsv(filename)
        if self.filename_csv is not None :
            if len(self.filename_csv) != 0:
                self.printLabelContentCsv()


    # Empty labels 
    def loadSpacesBody(self, text=""):
        """
        Function that loads the separator labels (aesthetics goal)
        
        Returns
        -------
            spaceLabel : Label (Tkinter)
                A empty space label for separating the other labels
        """
        spaceLabel = Label(self.body, text=text, bg="white", fg="blue")
        return spaceLabel


    # loading and place 
    def loadAndPlaceBodyLabels(self):
        """Function that load and places the labels (tkinter) widgets on the body label """
        self.loadSpacesBody("Select and open the files needed to start").place(relwidth=1, relheight=.20, relx=0, rely=0)
        self.loadLabelExplorerVideo()
        self.loadSpacesBody().place(relwidth=1, relheight=.18, relx=0, rely=.42)
        self.loadLabelExplorerCsv()
        self.loadSpacesBody().place(relwidth=1, relheight=.18, relx=0, rely=0.82)


    # Placing
    def loadSubLabelFooter(self):
        """Function that loads and place the 'accept' & 'exit' buttons in the footer label """
        # Exit label
        self.label_exit = Label(self.footer)
        self.label_exit.place(relheight=1, relwidth=.5, relx=0, rely=0)
        # Accept label
        self.label_accept = Label(self.footer,)
        self.label_accept.place(relheight=1, relwidth=.5, relx=0.5, rely=0)


    # Loading
    def loadButtons(self):
        """Function that loads buttons exit and next (accept) in 'buttons' array"""
        self.buttons = []
        button_exit = Button(self.label_exit, text="Exit", command=self.on_closing, relief='groove', bg="white", width=40)
        self.buttons.append(button_exit)
        button_accept = Button(self.label_accept, text="Next", command=self.destroyAndSend, relief='groove', bg="white", width=40)
        self.buttons.append(button_accept)


    # Placing
    def placeFooterButtons(self):
        """Function that places all footer buttons on their current label"""
        for button in self.buttons:
            button.place(relx=.5, rely=0.5, anchor=CENTER)


    # Calling
    def loadAndPlaceFooterButtons(self):
        """Function loading and placing all sub function for the footer label"""
        self.loadSubLabelFooter()
        self.loadButtons()
        self.placeFooterButtons()


    # Showing
    def printLabelContentVideo(self):
        """Function that prints on the video explorer window when a file is selected"""
        self.label_window_explorer_video.configure(text="Video selected: " + self.filename_video)


    # Change 
    def printLabelContentCsv(self):
        """Function that print on the label CSV file explorer window when a file is selected"""
        self.label_window_explorer_csv.configure(text="File csv selected: " + self.filename_csv)


    # Action
    def destroyAndSend(self):
        """Event function for the 'Next' button (submit values)"""
        if (self.filename_video is None or self.filename_csv is None) or (
                len(self.filename_csv) == 0 or len(self.filename_video) == 0):
            messagebox.showerror("Alert Message", message="You need to enter two files !")
            return
        self.window.destroy()


    # Warnings
    def on_closing(self):
        """ Warning/Alert function for the closing action/event of the window"""
        if self.filename_csv is not None or self.filename_video is not None :
            if messagebox.askokcancel("Quit", "Do you really want to quit ?"):
                self.window.destroy()
        else :
            self.window.destroy()


    # Getter 
    def getFileVideoAndCsvPath(self):
        """
        Getter for the 'filename_video' and 'filename_csv' paths and prints them on the terminal
        
        Return
        ------
            self.filename_video, self.filename_csv : String list
                An array containing the video and CSV files paths. 
                That allows the (model.py) to recuperate both values with only one function call
        """
        video = self.filename_video if self.filename_video is not None else "None"
        csv = self.filename_csv if self.filename_csv is not None else "None"
        print("File video: " + video)
        print("Csv File: " + csv)
        return self.filename_video, self.filename_csv


    # Setter 
    def setFilePathVideo (self, filename_video):
        """Setter for the video file path"""
        if filename_video is not None :
            if len(filename_video) != 0 :
                self.filename_video = filename_video


    # Setter 
    def setFilePathCsv (self, filename_csv) :
        """Setter for the csv file path"""
        if filename_csv is not None :
            if len(filename_csv) != 0 :
                self.filename_csv = filename_csv 
