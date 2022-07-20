from src.core import signal as sg
from tkinter import *
from pandas import DataFrame
import matplotlib as mt
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.gridspec as gridspec

class SignalUI :

    def __init__(self, master, signal) :
        self.master = master
        self.signal = signal

    

    def loadGraphicalBlock (self) :
        block_signal = Label (self.master)
        return block_signal


    def getMaster (self) :
        return self.master


    def getSignal (self) : 
        return self.signal
    
