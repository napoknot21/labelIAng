import pandas

#the label represents the "modes" := types and intesity of lighness
class Label :

	id = 0

	def __init__ (self, name, color, id) :
		self.name = name
		self.color = color
		self.id = id
		id += 1


	def getName (self) :
		return self.name
	
	def getColor (self) :
		return self.color

	def getId (self) :
		return self.id

	def setName (self, name) :
		if not len(name) == 0 and self.name == name :
			self.name = name
	
	def setColor (self, color) :
		if not color is None and self.name == name :
			self.color = color
