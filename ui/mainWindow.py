from tkinter import *


class MainWindow:

    def __init__(self, signals_selected=None, filename_video=None, labels_entered=None):
        self.signals_selected = signals_selected
        self.filename_video = filename_video
        self.labels_entered = labels_entered
        self.window = Tk()
        self.initWindow()
        self.loadAndPlaceMainLabels()
        self.loadSubLabelsHeader()
        self.loadAndPlaceSubLabelsHeader()
        self.loadAndPlaceSignalsLabels(3)
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
    def loadHeader(self):
        self.header = Label(
            self.window,
            bg="black"
        )
        self.header.place(x=0, y=0, relwidth=1, relheight=.65)


    # Load body label
    def loadBody(self):
        self.body = Label(
            self.window,
            bg="blue"
        )
        self.body.place(relx=0, rely=.65, relwidth=1, relheight=.35)


    # Load and place the main labels (header and body labels)
    def loadAndPlaceMainLabels(self):
        self.loadHeader()
        self.loadBody()


    def loadSubLabelsHeader(self):
        self.video_label = Label(
            self.header,
            bg="yellow"
        )
        self.video_label.place(relx=0, rely=0, relheight=1, relwidth=.65)
        self.labels_label = Label(
            self.header,
            bg="green"
        )
        self.labels_label.place(relx=.65, rely=0, relheight=1, relwidth=.35)


    def loadAndPlaceSubLabelsHeader(self):
        self.loadAndPlaceVideoCanvas()
        self.loadAndPlaceLabelsCanvas()


    def loadAndPlaceVideoCanvas(self):
        self.video_canvas = Canvas(
            self.video_label,
            bg="white"
        )
        self.video_canvas.place(relx=0.05, rely=0.05, relwidth=0.905, relheight=0.9)


    def loadAndPlaceLabelsCanvas(self):
        self.video_info = Label(
            self.labels_label,
            bg="brown"
        )
        self.video_info.place(relx=.05, rely=.05, relwidth=.905, relheight=.15)
        self.labels_canvas = Label(
            self.labels_label,
            bg="brown"
        )
        self.labels_canvas.place(relx=.05, rely=.25, relwidth=.905, relheight=.5)
        self.buttons_canvas = Label(
            self.labels_label,
            bg="brown"
        )
        self.buttons_canvas.place(relx=.05, rely=.8, relwidth=.905, relheight=.15)


    def loadAndPlaceSignalsLabels (self, signalsLength):
        self.signals = []
        space = 0.01
        rely = 0
        height = (1 - ((signalsLength + 1) * space)) / signalsLength
        for i in range(signalsLength):
            signal_label = Label (
                self.body,
                bg="pink"
            )
            signal_label.place(relx=0.003, rely=space + rely, relwidth=.985, relheigh=height)
            space += space
            rely += height
