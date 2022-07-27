from src.core import label as lb
from src.ui.assets import videoUI as vdUI
from src.ui.assets import signalUI as sgUI
from src.ui.assets import labelUI as lbUI
from tkinter import *
import time as tm
import pandas as pd
import numpy as np

class MainWindow:

    np.random.seed(19680801)

    # Constructor 
    def __init__(self, signals_selected=None, filename_video=None, labels_entered=None):
        """
        Constructor for the main window

        Parameters
        ----------
            signals_selected : List

            filename_video : List

            labels_entered : List
        """
        self.signals_selected = np.array(signals_selected)
        self.filename_video = filename_video
        self.labels_entered = np.array(labels_entered)
        # Main list and variables for displaying informations
        self.graphic_video = None
        self.graphic_signals = np.empty(len(self.signals_selected), dtype=sgUI.SignalUI)
        self.graphic_labels = np.empty(len(self.labels_entered), dtype=lbUI.LabelUI)
        #Initialize functions window
        self.window = Tk()
        self.initWindow()
        #Load and place main labels (header and Body)
        self.loadAndPlaceMainLabels()
        #Load and place sub labels of HEADER
        self.loadAndPlaceSubLabelsHeader()
        self.graphic_video = vdUI.VideoUI(self.video_canvas, self.filename_video)
        # Print the number of frames of the video (auxiliary function)
        self.loadAndPlaceSubLabelsBody()

        self.loadAndPlaceGraphicalLabels()
        # Main loop
        self.window.mainloop()


    # Initialize the window
    def initWindow(self):
        """Function to initialize the window properties"""
        self.window.title("Video app 1.0")
        self.window.state('zoomed')
        self.window.config(background="white")
        self.window.geometry("960x540")
        self.__loadIconWindow("extras/images/icon.png")


    # Import an images and put it as icon window
    def __loadIconWindow(self, filePath):
        """Function that loads an image as a window icon"""
        p1 = PhotoImage(file=filePath)
        self.window.iconphoto(False, p1)


    # Load the header
    def __loadHeader(self):
        """Load the header label for the main window"""
        self.header = Label(self.window, bg="white")


    # Load the body
    def __loadBody(self):
        """
        Function that load the body label for the main window
        
        Notes
        ----
            The 'highlightthickness' option is used to hide the border default
        """
        self.body = Frame (self.window,bg="grey", highlightbackground="white",  highlightthickness=0)


    # Load and place
    def loadAndPlaceMainLabels(self):
        """
        Function that load and place the main labels for the main window loading 
        from other private functions with the 'place' method.
        """
        self.__loadHeader()
        self.__loadBody()
        self.header.place(x=0, y=0, relwidth=1, relheight=.65)
        self.body.place(relx=0, rely=.65, relwidth=1, relheight=.35)


    #General Video label and general video-info/labels-info Label 
    def __loadAndPlaceSubLabelsHeader(self):
        """
        Private function that loads the sub widgets of the head.

        Notes
        -----
            'video_label' : The principal label for the video.

            'labels_label' : The principal label for the Label object (Label.py).

            The tkinter labels are placed with the 'place' method.
        """
        self.video_label = Label(self.header)
        self.video_label.place(relx=0, rely=0, relheight=1, relwidth=.65)
        self.labels_label = Label(self.header, bg="white")
        self.labels_label.place(relx=.65, rely=0, relheight=1, relwidth=.35)


    #Video canvas (where the video is located)
    def __loadAndPlaceVideoCanvas(self):
        """
        Private function to load and place the video canvas into the 'video_label' attribute

        Notes
        -----
            'video_canvas' : The canvas (tkinter) where the video is showed
        
            The tkinter canvas is placed with the 'place' method
        """
        self.video_canvas = Label (self.video_label)
        self.video_canvas.place(relx=0.05, rely=0.05, relwidth=0.905, relheight=0.9)


    # Frames for the video-info/ Labels-selector/ video-buttons 
    def __loadAndPlaceLabelsCanvas(self):
        """
        Private function that loads the place the Sub labels for 'labels_label'

        Notes
        -----
            'video_info' : Label (tkinter) where the video information is showed (number of frames, etc)

            'labels_frame" : Frame (tkinter) where the labelsUI will be placed 

            'buttons_canvas' : Label (tkinter) where the buttons video controllers will be placed
        """
        # Video info label: Nb of frames and other information
        self.video_info = Label(self.labels_label, )
        self.video_info.place(relx=.05, rely=.05, relwidth=.905, relheight=.15)
        # Label frames for the entered labels
        self.labels_frame = Frame(self.labels_label, )
        self.labels_frame.place(relx=.05, rely=.25, relwidth=.905, relheight=.5)
        # Video controller label for the buttons
        self.buttons_canvas = Label(self.labels_label)
        self.buttons_canvas.place(relx=.05, rely=.8, relwidth=.905, relheight=.15)


    # Place signalsUI elements
    def __loadAndPlaceSignalsLabel (self) :
        """
        Private function to load and configure the 'labels_frame' for placing the signalsUI elements/objects

        Notes
        -----
            
        """
        # Canvas for the signals blocks
        self.signals_canvas = Canvas (self.body, bg="white", highlightbackground="white",  highlightthickness=0)
        self.signals_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        # Scrollbar to the right side
        self.scrollbar_signal = Scrollbar (self.body, orient=VERTICAL, command=self.signals_canvas.yview)
        self.scrollbar_signal.pack(side=RIGHT, fill=Y)
        # Scrollbar to the button side
        self.scrollbar_signal_bottom = Scrollbar (self.body, orient=HORIZONTAL)
        #self.scrollbar_signal_bottom.pack(side=BOTTOM, fill=X) 
        # config for the signals canvas
        self.signals_canvas.config(yscrollcommand=self.scrollbar_signal.set)
        # bind the signal 
        self.signals_canvas.bind('<Configure>', lambda e : self.__fill_canvas_signals(e))
        # second frame fot signals
        self.second_frame_signal = Frame (self.signals_canvas, highlightbackground="white",  highlightthickness=0)
        self.item_signals = self.signals_canvas.create_window((0,0), window=self.second_frame_signal, anchor="nw")


    # Function called for load and places all sub widgets
    def loadAndPlaceSubLabelsHeader(self):
        """l"""
        self.__loadAndPlaceSubLabelsHeader()
        self.__loadAndPlaceVideoCanvas()
        self.__loadAndPlaceLabelsCanvas()
        self.__loadAndPlaceLabelsLabel()
    

    def __loadAndPlaceLabelsLabel (self) :
        # Canvas for labels 
        self.labels_canvas = Canvas (self.labels_frame)
        self.labels_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        # Scrollbar for the labels
        self.labels_scroll = Scrollbar (self.labels_frame, orient=VERTICAL, command=self.labels_canvas.yview)
        self.labels_scroll.pack(side=RIGHT, fill=Y)
        #config for the label canvas
        self.labels_canvas.configure(yscrollcommand=self.labels_scroll.set)
        # config the bind
        self.labels_canvas.bind('<Configure>', lambda e : self.__fill_canvas_labels(e))
        #Second frame (for print the labels blocks)
        self.second_frame_label = Frame (self.labels_canvas,)
        self.item_labels = self.labels_canvas.create_window((0,0), window=self.second_frame_label, anchor="nw")


    # Load and Place the Frames for the signals/labels blocks
    def loadAndPlaceSubLabelsBody (self) :
        self.__loadAndPlaceSignalsLabel()


    def __loadAndPlaceLabelFramesAndTime (self) :
        self.frames = Label (self.video_info, text="Total Frames: " + str(self.graphic_video.getTotalNumberFrames()))
        self.frames.place(relx=0, rely=0, relwidth=.5, relheight=1)
        self.timer = Label (self.video_info)
        self.timer.place(relx=0.5, rely=0, relwidth=.5, relheight=1)


    # Private function for tranform the label to graphical labels (labelsUI)
    def __loadGraphicalLabels (self) : 
        for i, label in enumerate(self.labels_entered) :
            labelUI = lbUI.LabelUI(self.second_frame_label, label)
            self.graphic_labels[i] = labelUI
    

    # private funtion for place (grid) all graphical labels
    def __placeGraphicalLabels (self) :
        for labelUI in self.graphic_labels :
            label_block = labelUI.loadLabelBlock()
            label_block.pack(side="top", fill="both", expand=1)


    def __loadGraphicalSignals (self) :
        for i, signal in enumerate(self.signals_selected) :
            signalUI = sgUI.SignalUI(self.second_frame_signal, signal)
            self.graphic_signals[i] = signalUI


    def __placeGraphicalSignals (self) :
        for signalUI in self.graphic_signals :
            signal_block = signalUI.loadGraphicalBlock()
            signal_block.pack(side="top", fill="both", expand=1)


    #Load and place all graphical labels in the main window
    def loadAndPlaceGraphicalLabels (self) :
        self.__loadAndPlaceLabelFramesAndTime()
        self.__loadGraphicalLabels()
        self.__placeGraphicalLabels()
        self.__loadGraphicalSignals()
        self.__placeGraphicalSignals()


    # Auxiliary function for dinamic the width of the label block
    def __fill_canvas_labels (self, event) :
        canvas_width = event.width
        self.labels_canvas.itemconfig(self.item_labels, width=canvas_width)
        self.labels_canvas.configure(scrollregion=self.labels_canvas.bbox("all"))


    # Auxiliary function for the dinamic width of the signal block
    def __fill_canvas_signals (self, event, ) :
        canvas_width = event.width
        self.signals_canvas.itemconfig(self.item_signals, width=canvas_width)
        self.signals_canvas.configure(scrollregion=self.signals_canvas.bbox("all"))


    