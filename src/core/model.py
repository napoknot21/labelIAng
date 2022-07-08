from src.ui import browserFileWindow as br
from src.ui import signalsWindow as sw
from src.ui import labelsWindow as lw
from src.ui import mainWindow as mw
from src.core import connexion as cn

class Model :

    def __init__(self):
        data = br.BrowserFileWindow().getFileVideoAndCsvPath()
        self.filename_video = data[0]
        self.filename_csv = data[1]
        if self.filename_video is None or self.filename_csv is None :
            print("The video file or the csv file is None")
            exit(1)
        data_connexion = cn.Connexion(self.filename_video, self.filename_csv).getterFilenames()
        if data_connexion[0] is None or data_connexion[1] is None :
            print("Not possible to connect to the video and/or the csv file")
            exit(1)
        self.S = sw.SignalsWindow(data_connexion[1]).getSignalsSelected()
        data_labels = lw.LabelsWindow().getLabels()
        if data_labels is None :
            print("Impossible to get labels")
            exit(1)
        self.MW = mw.MainWindow(self.S, data_connexion[0], data_labels)#self.LW.getLabels())
