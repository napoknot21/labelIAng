import sys, subprocess
subprocess.check_call([sys.executable, 'extras/setup.py'])

from src.core import model as md
from src.ui import mainWindow as mw
from src.ui import labelsWindow as lw
from src.core import label as lb

class Launcher :

	#Constructor
	def __init__(self) :
		self.M = md.Model()

#Main function 
def main () :
	Launcher()


if __name__ == '__main__':
	main()
