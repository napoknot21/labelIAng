from src.core import signal as sg
from tkinter import *
from pandas import DataFrame
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.gridspec as gridspec

class SignalUI :

    # Constructor
    def __init__(self, master, signal) :
        self.master = master
        self.signal = signal


    # Block tkinter for the signalUI
    def loadGraphicalBlock (self) :
        block_signal = Label (self.master)
        return block_signal


    def getMaster (self) :
        return self.master


    def getSignal (self) : 
        return self.signal

    
    def plotAGraph (self) :
        mpl.plot(self.signal.getTimer(), self.signal.getValues())
        mpl.show()
    
