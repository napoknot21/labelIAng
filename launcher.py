import sys, subprocess
subprocess.check_call([sys.executable, 'extras/setup.py'])

from src.core import model as md
#from src.ui import mainWindow as mw
#from src.ui import labelsWindow as lw


class Launcher :

	#Constructor
	def __init__(self) :
		self.M = md.Model()
		#self.LW = lw.LabelsWindow()
		#self.MW = mw.MainWindow(signals_selected=None, labels_entered=None)



#Main function 
def main () :
	Launcher()


if __name__ == '__main__':
	main()
