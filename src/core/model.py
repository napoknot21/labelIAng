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
        self.T = cn.Connexion(self.filename_video, self.filename_csv)

        self.S = sw.SignalsWindow(self.T.getterFilenames()[1]).getSignalsSelected()
        self.LW = lw.LabelsWindow()
        self.MW = mw.MainWindow(self.S, self.T.getterFilenames()[0], None)#self.LW.getLabels())
