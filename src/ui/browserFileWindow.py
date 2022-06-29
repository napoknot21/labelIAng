from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class BrowserFileWindow:

    # Constructor
    def __init__(self):
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
        self.header = Label(self.window, text="VIDEO APP [BETA]", width=100, height=5, fg="blue")


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
    def loadAndPlaceMainLabels(self) :
        self.loadMainLabels()
        self.header.grid(column=0, row=0)
        self.body.grid(column=0, row=1)
        self.footer.grid(column=0, row=2)


    # Explorer label for the video file
    def loadLabelExplorerVideo(self):
        self.label_window_explorer_video = Label(
            self.body,
            text="Select a video File",
            width=100,
            height=3,
            fg="blue",
            bg="white"
        )
        self.label_window_explorer_video.grid()
        buttonBrowser = self.browserButtonVideo()
        buttonBrowser.grid()


    # Explorer label for the csv file
    def loadLabelExplorerCsv(self):
        self.label_window_explorer_csv = Label(
            self.body,
            text="Select a CSV File",
            width=100,
            height=3,
            fg="blue",
            bg="white"
        )
        self.label_window_explorer_csv.grid()
        buttonBrowser = self.browserButtonCsv()
        buttonBrowser.grid()


    # Browser button for the video file
    def browserButtonVideo(self):
        browserButton = Button(self.body, text="Browse Files", command=self.openFileBrowserVideo, relief='groove')
        return browserButton


    # Browser button for the csv file
    def browserButtonCsv(self):
        browserButton = Button(self.body, text="Browse Files", command=self.openFileBrowserCsv, relief='groove')
        return browserButton


    # File browser for the video file
    def openFileBrowserVideo(self):
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


    # Empty labels for the window aesthetic
    def loadSpacesBody(self, text=""):
        spaceLabel = Label(self.body, text=text, width=100, height=4, bg="white", fg="blue")
        return spaceLabel


    # Function that load and place all sub labels and buttons
    def loadAndPlaceBodyLabels(self):
        self.loadSpacesBody("Select and open the files needed to start").grid()
        self.loadLabelExplorerVideo()
        self.loadSpacesBody().grid()
        self.loadLabelExplorerCsv()
        self.loadSpacesBody().grid()


    # Function for load buttons exit and next (accept)
    def loadButtons(self):
        self.buttons = []
        button_exit = Button(self.footer, text="Exit", command=self.on_closing, width=45, relief='groove', bg="white")
        self.buttons.append(button_exit)
        button_accept = Button(self.footer, text="Next", width=45, command=self.destroyAndSend, relief='groove', bg="white")
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


    # Change the label video explorer window when a file is selected
    def printLabelContentVideo(self):
        self.label_window_explorer_video.configure(text="Video selected: " + self.filename_video)


    # Change the label CSV file explorer window when a file is selected
    def printLabelContentCsv(self):
        self.label_window_explorer_csv.configure(text="File csv selected: " + self.filename_csv)


    # Command function for the "Next" button
    def destroyAndSend(self):
        if (self.filename_video is None or self.filename_csv is None) or (
                len(self.filename_csv) == 0 or len(self.filename_video) == 0):
            messagebox.showerror("Alert Message", message="You need to enter two files !")
            return
        self.window.destroy()


    # Alert messages for closing the window
    def on_closing(self):
        if self.filename_csv is not None or self.filename_video is not None :
            if messagebox.askokcancel("Quit", "Do you really want to quit ?"):
                self.window.destroy()
        else :
            self.window.destroy()


    # Getter for the filenames (video and csv) paths
    def getFileVideoAndCsvPath(self):
        video = self.filename_video if self.filename_video is not None else "None"
        csv = self.filename_csv if self.filename_csv is not None else "None"
        print("File video: " + video)
        print("Csv File: " + csv)
        return self.filename_video, self.filename_csv


    #Setter fot the video file path
    def setFilePathVideo (self, filename_video):
        if filename_video is not None :
            if len(filename_video) != 0 :
                self.filename_video = filename_video


    #Setter for the csv file path
    def setFilePathCsv (self, filename_csv) :
        if filename_csv is not None :
            if len(filename_csv) != 0 :
                self.filename_csv = filename_csv 
