from ui import browserFileWindow as br
from ui import signalsWindow as sw
from core import connexion as cn

class Model :

    def __init__(self):
        data = br.BrowserFileWindow().getFileVideoAndCsvPath()
        self.filename_video = data[0]
        self.filename_csv = data[1]
        self.T = cn.Connexion(self.filename_video, self.filename_csv)
        self.signals = sw.SignalsWindow(self.T.getterFilenames()[1]).getSignalsSelected()
