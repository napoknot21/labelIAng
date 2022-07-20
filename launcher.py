from re import L
import sys, subprocess
subprocess.check_call([sys.executable, 'extras/setup.py'])

from src.core import model as md
from src.ui import mainWindow as mw
from src.ui import labelsWindow as lw
from src.core import label as lb

class Launcher :

	#Constructor
	def __init__(self) :
		#self.M = md.Model()
		self.LW = lw.LabelsWindow()
		"""signals = ["Signal1", "Signal2", "Signal3", "Signal4"]
		labels = [
			lb.Label(0, "name1", "#ffffff", 0),
			lb.Label(1, "name2", "#ffff5d", 1),
			lb.Label(2, "name3", "#fff5fe", 2),
			lb.Label(3, "name4", "#fdefff", 3),
			lb.Label(4, "name5", "#fdefff", 4),
			lb.Label(5, "name6", "#fdefff", 5),
			lb.Label(6, "name7", "#fdefff", 6),
			lb.Label(7, "name8", "#fdefff", 7),
		]
		self.MW = mw.MainWindow(
			signals,
			"C:/Users/cmartin-/Desktop/app-pycharm-edition/MobEyeQ3.avi",
			labels_entered=labels
		)"""



#Main function 
def main () :
	Launcher()


if __name__ == '__main__':
	main()
