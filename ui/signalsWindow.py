import pandas as pd
import tkinter as tk

class SignalsWindow :

    #Constructor
    def __init__(self, filename_csv) :
        self.readSource(filename_csv)
        self.initliazeWindow()
        

    
    def readSource(self, filename_csv) :
        pass

    
    def initliazeWindow(self) : 
        self.window = tk.Tk()
        self.window.title("Signals")
        self.window.geometry("707x500")
        self.window.eval('tk::PlaceWindow . center')
        self.window.config(background="white")
        self.window.mainloop()
