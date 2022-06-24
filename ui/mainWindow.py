from tkinter import *

class MainWindow :

    def __init__(self, signals_selected=None, filename_video=None, labels_entered=None):
        self.signals_selected = signals_selected
        self.filename_video = filename_video
        self.labels_entered = labels_entered
        self.window = Tk()
        self.initWindow()
        self.loadAndPlaceMainLabels()
        self.window.mainloop()

    def initWindow(self):
        self.window.title("Video app 1.0")
        self.window.state('zoomed')
        self.window.config(background="white")
        self.window.geometry("960x540")
        self.loadIconWindow("ui/.images/icon.png")


    # Import an images and put it as icon window
    def loadIconWindow(self, filePath):
        p1 = PhotoImage(file=filePath)
        self.window.iconphoto(False, p1)


    # Load header label
    def loadHeader (self) :
        self.header = Label(
            self.window,
            bg="black"
        )
        self.header.place(x=0, y=0, relwidth=1, relheight=.65)


    # Load body label
    def loadBody (self) :
        self.body = Label(
            self.window,
            bg="blue"
        )
        self.body.place(relx=0, rely=.65, relwidth=1, relheight=.35)


    # Load and place the main labels (header and body labels)
    def loadAndPlaceMainLabels(self):
        self.loadHeader()
        self.loadBody()
        self.loadSubLabelsHeader()


    def loadSubLabelsHeader (self) :
        self.video_label = Label (
            self.header,
            bg="yellow"
        )
        self.video_label.place(relx=0, rely=0, relheight=1, relwidth=.65)
        self.labels_label = Label (
            self.header,
            bg="green"
        )
        self.labels_label.place(relx=.65, rely=0, relheight=1, relwidth=.35)






        # ((1920 / 1080) * .8)
