from time import time
from turtle import width
from src.core import label as lb
from src.ui.assets import videoUI as vdUI
from src.ui.assets import signalUI as sgUI
from src.ui.assets import labelUI as lbUI
from tkinter import *
import time as tm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.gridspec as gridspec

class MainWindow:

    np.random.seed(19680801)

    """C:/Users/cmartin-/Desktop/app-pycharm-edition/MobEyeQ3.avi"""

    def __init__(self, signals_selected=None, filename_video=None, labels_entered=None):
        self.signals_selected = signals_selected
        self.filename_video = filename_video
        self.labels_entered = labels_entered

        self.graphic_video = None
        self.graphic_signals = []
        self.graphic_labels = []

        #Initialize functions window
        self.window = Tk()
        self.initWindow()

        #Load and place main labels (header and Body)
        self.loadAndPlaceMainLabels()

        #Load and place sub labels of HEADER
        self.loadAndPlaceSubLabelsHeader()
        self.graphic_video = vdUI.VideoUI(self.video_canvas, self.filename_video)


        self.__loadAndPlaceLabelFramesAndTime()
        #self.__loadGraphicalLabel()
        self.loadAndPlaceSubLabelsBody()
        #self.video = vd.Video(filename_video)
        self.loadAndPlaceGraphicalLabels()
        
        self.window.mainloop()


    # Initialize the window
    def initWindow(self):
        self.window.title("Video app 1.0")
        self.window.state('zoomed')
        self.window.config(background="white")
        self.window.geometry("960x540")
        self.__loadIconWindow("extras/images/icon.png")


    # Import an images and put it as icon window
    def __loadIconWindow(self, filePath):
        p1 = PhotoImage(file=filePath)
        self.window.iconphoto(False, p1)


    # Load the header label
    def __loadHeader(self):
        self.header = Label(self.window, bg="black")


    # Load the body label
    def __loadBody(self):
        self.body = Label(self.window,bg="blue")


    # Load and place the main labels (header and body labels)
    def loadAndPlaceMainLabels(self):
        self.__loadHeader()
        self.__loadBody()
        self.header.place(x=0, y=0, relwidth=1, relheight=.65)
        self.body.place(relx=0, rely=.65, relwidth=1, relheight=.35)


    #General Video label and general video-info/labels-info Label 
    def __loadAndPlaceSubLabelsHeader(self):
        self.video_label = Label(self.header, bg="light blue")
        self.video_label.place(relx=0, rely=0, relheight=1, relwidth=.65)
        self.labels_label = Label(self.header, bg="green")
        self.labels_label.place(relx=.65, rely=0, relheight=1, relwidth=.35)


    #Video canvas (where the video is located)
    def __loadAndPlaceVideoCanvas(self):
        self.video_canvas = Label (self.video_label,bg="light blue")
        self.video_canvas.place(relx=0.05, rely=0.05, relwidth=0.905, relheight=0.9)


    #Frames for the video-info/ Labels-selector/ video-buttons 
    def __loadAndPlaceLabelsCanvas(self):
        # Video info label: Nb of frames and other informations
        self.video_info = Label(self.labels_label, bg="brown")
        self.video_info.place(relx=.05, rely=.05, relwidth=.905, relheight=.15)
        # Label frames for the entered labels
        self.labels_frame = Frame(self.labels_label, bg="brown")
        self.labels_frame.place(relx=.05, rely=.25, relwidth=.905, relheight=.5)
        # Video controller label for the buttons
        self.buttons_canvas = Label(self.labels_label,bg="brown")
        self.buttons_canvas.place(relx=.05, rely=.8, relwidth=.905, relheight=.15)


    def loadAndPlaceSubLabelsHeader(self):
        self.__loadAndPlaceSubLabelsHeader()
        self.__loadAndPlaceVideoCanvas()
        self.__loadAndPlaceLabelsCanvas()


    def __loadSignalsLabel (self) :
        self.signals_label = Label(self.body, bg="pink" )
        self.signals_label.place(relx=0, rely=0, relwidth=.98, relheight=1)
        self.sub_canvas = Canvas(self.signals_label,bg="light blue", highlightbackground="white")
        self.sub_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.scrollbar_label = Label(self.body)
        self.scrollbar_label.place(relx=.98, rely=0, relwidth=.02, relheight=1)


    def __loadSignalsScrollBar (self):
        self.scrollbar_signals = Scrollbar (
            self.scrollbar_label,
            orient=VERTICAL,
            command=self.sub_canvas.yview
        )
        self.sub_canvas.update()
        self.scrollbar_signals.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.__configSubBodyWidget()
        self.second_frame = Frame(
            self.sub_canvas, bg="white", 
            height=350,
            highlightbackground="white",
            width=self.sub_canvas.winfo_width()
        )
        self.second_frame.place(relx=0, rely=0, relwidth=1)
        self.sub_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")


    #Config for the scrollbar
    def __configSubBodyWidget(self):
        self.sub_canvas.configure(yscrollcommand=self.scrollbar_signals.set)
        self.sub_canvas.bind('<Configure>', lambda e: self.sub_canvas.configure(scrollregion=self.sub_canvas.bbox("all")))


    def __loadLabelsLabel (self) :
        # Canvas for labels 
        self.labels_canvas = Canvas (self.labels_frame, bg="red")
        self.labels_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        # Scrollbar for the labels
        self.labels_scroll = Scrollbar (self.labels_frame, orient=VERTICAL, command=self.labels_canvas.yview)
        self.labels_scroll.pack(side=RIGHT, fill=Y)
        #config for the label canvas
        self.labels_canvas.configure(yscrollcommand=self.labels_scroll.set)
        # config the bind
        self.labels_canvas.bind('<Configure>', lambda e : self.__fill_canvas_labels(e))
        #Second frame (for print the labels blocks)
        self.second_frame = Frame (self.labels_canvas, bg="black")
        self.item = self.labels_canvas.create_window((0,0), window=self.second_frame, anchor="nw")



    def loadAndPlaceSubLabelsBody (self) :
        self.__loadSignalsLabel()
        self.__loadSignalsScrollBar()
        self.__loadLabelsLabel()


    def __loadAndPlaceLabelFramesAndTime (self) :
        self.frame = Label (
            self.video_info,
            text="Total Frames: " + str(self.graphic_video.getTotalNumberFrames()),
            bg="blue"
        )
        self.frame.place(relx=0, rely=0, relwidth=.5, relheight=1)
        self.timer = Label (
            self.video_info,
            bg="black"
        )
        self.timer.place(relx=0.5, rely=0, relwidth=.5, relheight=1)


    # Private function for tranform the label to graphical labels (labelsUI)
    def __loadGraphicalLabels (self) : 
        for i, label in enumerate (self.labels_entered) :
            labelUI = lbUI.LabelUI(self.second_frame, label)
            self.graphic_labels.append(labelUI)
    

    # private funtion for place (grid) all graphical labels
    def __placeGraphicalLabels (self) :
        for labelUI in self.graphic_labels :
            label_block = labelUI.loadLabelBlock()
            label_block.pack(side="top", fill="both", expand=1)


    #Load and place all graphical labels in the main window
    def loadAndPlaceGraphicalLabels (self) :
        self.__loadGraphicalLabels()
        self.__placeGraphicalLabels()




    def __fill_canvas_labels (self, event, ) :
        canvas_width = event.width
        self.labels_canvas.itemconfig(self.item, width=canvas_width)
        self.labels_canvas.configure(scrollregion=self.labels_canvas.bbox("all"))

