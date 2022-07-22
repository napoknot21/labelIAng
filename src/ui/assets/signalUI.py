from src.core import signal as sg
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt
import numpy as np


class SignalUI :

    # Constructor
    def __init__(self, master, signal) :
        self.master = master
        self.signal = signal


    # Block tkinter for the signalUI
    def loadGraphicalBlock (self) :
        block_signal = Canvas (self.master, height=200, bg="white")
        
        buttons_side = Label (block_signal, bg="white", text=self.signal.getName(), fg="blue")
        buttons_side.place(relheight=1, relwidth=.2, relx=0, rely=0)

        signal_side = Canvas (block_signal, bg="white")
        signal_side.place(relheight=1, relwidth=.8, relx=.2, rely=0)
        self.plotAGraph(signal_side)

        return block_signal


    def getMaster (self) :
        return self.master


    def getSignal (self) : 
        return self.signal

    
    def plotAGraph (self, master) :
        axe_x = self.signal.getTimer()
        axe_y = self.signal.getValues()
        figure = plt.figure(figsize=(2, 5), dpi=100)
        figure.add_subplot(111).plot(axe_x,axe_y)
        chart = FigureCanvasTkAgg(figure, master)
        #plt.subplot(axe_x, axe_y)
        chart.get_tk_widget().place(relheight=1, relwidth=1, relx=0, rely=0)
        plt.grid()
    
