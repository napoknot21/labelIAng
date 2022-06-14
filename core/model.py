import pandas as pd
import os, sys

sys.path.insert(0,'./ui')

import browserFileWindow as br
import signalsWindow as sw

sys.path.insert(0,'./core')

import connexion as cn

class Model :

    #Constructor
    def __init__(self) :
        data = br.BrowserFileWindow().getFileNameVideoAndCsvPath()
        self.filename_video = data[0] #filename_video
        self.filename_csv = data[1] #filename_csv
        self.T = cn.Connexion(self.filename_video, self.filename_csv)
        self.SW = sw.SignalsWindow(self.filename_csv)
        
