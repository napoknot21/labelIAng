import pandas as pd
from ui import browserFileWindow as br
from ui import signalsWindow as sg
from core import connexion as cn

class Model :

    #Constructor
    def __init__(self) :
        data = br.BrowserFileWindow().getFileVideoAndCsvPath()
        self.filename_video = data[0] #filename_video
        self.filename_csv = data[1] #filename_csv
        self.T = cn.Connexion(self.filename_video, self.filename_csv)
        self.SW = sw.SignalsWindow(self.filename_csv)
        
