from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt
import numpy as np


class SignalUI :

    # Constructor
    def __init__(self, master, signal) :
        """
        Constructor for the signalUI object
        
        Parameters
        ----------
            master : Label/Canvas (tkinter)
                master widget where the graphical signal will be displayed

            singal : signal object (signal.py)
                The signal object source
        """
        self.master = master
        self.signal = signal
        self.initMatPlotLibVariables()
        

    # Initialize variables
    def initMatPlotLibVariables (self) :
        """
        Function that initializes the matplotlib variables for the scrolling wheel events
        
        Notes
        -----
            Check the 'zoom_plot' and the 'pan_plot' functions
        """
        self.press = None
        self.cur_xlim = None
        self.cur_ylim = None
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None
        self.xpress = None
        self.ypress = None


    # Loading
    def loadGraphicalBlock (self) :
        """
        Function that loads the graphical Signal block

        Returns
        -------
            'block_signal' : Canvas (tkinter)
                The canvas where the graphical signal will be placed
        """
        block_signal = Canvas (self.master, height=200, bg="white")
        # Label fot the (pottentially) buttons or some informations about the signal
        buttons_side = Label (block_signal, bg="white", text=self.signal.getName(), fg="blue")
        buttons_side.place(relheight=1, relwidth=.2, relx=0, rely=0)
        # Canvas where the signal will be desployed
        signal_side = Canvas (block_signal, bg="white")
        signal_side.place(relheight=1, relwidth=.8, relx=.2, rely=0)
        self.plotAGraph(signal_side)
        # return
        return block_signal


    # 
    def zoom_plot (self, ax, base_scale=2.) :
        """
        Function that changes the zoom level of the plot
        """
        def zoom (event) :
            cur_xlim = ax.get_xlim()
            cur_ylim = ax.get_ylim()

            xdata = event.xdata
            ydata = event.ydata

            if event.button == 'up':
                # deal with zoom in
                scale_factor = 1 / base_scale
            elif event.button == 'down':
                # deal with zoom out
                scale_factor = base_scale
            else:
                # deal with something that should never happen
                scale_factor = 1

            new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
            new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

            relx = (cur_xlim[1] - xdata)/(cur_xlim[1] - cur_xlim[0])
            rely = (cur_ylim[1] - ydata)/(cur_ylim[1] - cur_ylim[0])

            ax.set_xlim([xdata - new_width * (1-relx), xdata + new_width * (relx)])
            #ax.set_ylim([ydata - new_height * (1-rely), ydata + new_height * (rely)])
            ax.figure.canvas.draw()

        fig = ax.get_figure() # get the figure of interest
        fig.canvas.mpl_connect('scroll_event', zoom)
        #return
        return zoom


    # Setting
    def pan_plot (self, ax) :
        """
        Function that manage the events process for the panning plot
        """
        def onPress (event) :
            if event.inaxes != ax: return
            self.cur_xlim = ax.get_xlim()
            self.cur_ylim = ax.get_ylim()
            self.press = self.x0, self.y0, event.xdata, event.ydata
            self.x0, self.y0, self.xpress, self.ypress = self.press

        def onRelease(event):
            self.press = None
            ax.figure.canvas.draw()

        def onMotion(event):
            if self.press is None: return
            if event.inaxes != ax: return
            dx = event.xdata - self.xpress
            dy = event.ydata - self.ypress
            self.cur_xlim -= dx
            self.cur_ylim -= dy
            ax.set_xlim(self.cur_xlim)
            #ax.set_ylim(self.cur_ylim)

            ax.figure.canvas.draw()

        fig = ax.get_figure() # get the figure of interest

        # attach the call back
        fig.canvas.mpl_connect('button_press_event',onPress)
        fig.canvas.mpl_connect('button_release_event',onRelease)
        fig.canvas.mpl_connect('motion_notify_event',onMotion)

        #return the function
        return onMotion

    
    # Plot
    def plotAGraph (self, master) :
        """
        Show the graph and place it in the master

        Parameters
        ----------
            master : master object (master object)
                Parent window for showing the graph
        """
        axe_x = self.signal.getTimer()
        axe_y = self.signal.getValues()
        figure = plt.figure(figsize=(2, 8), dpi=100)
        self.ax = figure.add_subplot(111)
        self.ax.plot(axe_x,axe_y)
        chart = FigureCanvasTkAgg(figure, master)
        chart.get_tk_widget().place(relheight=1, relwidth=1, relx=0, rely=0)
        self.zoom_plot(self.ax)
        self.pan_plot(self.ax)
        plt.grid()
    

    # Getter
    def getAx (self) :
        """Getter for the Ax attribute"""
        return self.ax


    # Getter
    def getMaster (self) :
        """Getter fot the master tkinter label/canvas"""
        return self.master


    # Getter
    def getSignal (self) :
        """Getter for the signal object (signal.py) attribute"""
        return self.signal