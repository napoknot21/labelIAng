import matplotlib
from src.core import model as md
from src.ui import mainWindow as mw
from src.ui import labelsWindow as lw
import sys, subprocess

class Launcher :

	#Constructor
	def __init__(self) :
		self.libraries = ["pandas", "opencv", "matplotlib", "tk"]
		#self.installPackages()
		#self.M = md.Model()
		#self.LW = lw.LabelsWindow()
		self.MW = mw.MainWindow(signals_selected=None, labels_entered=None)


	def installPackages (self) :
		subprocess.check_call([sys.executable, '-m', 'pip', 'intall', 'pandas'])
		"""for libray in self.libraries :
			subprocess.check_call([sys.executable, "-m", "pip", "intall", libray])"""

		

#Main function 
def main () :
	Launcher()


if __name__ == '__main__':
	main()
