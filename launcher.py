from src.core import model as md
from src.ui import labelsWindow as lw

class Launcher :

	#Constructor
	def __init__(self) :
		#self.M = md.Model()
		self.LW = lw.LabelsWindow()
		

#Main function 
def main () :
	L = Launcher()


if __name__ == '__main__':
	main()
