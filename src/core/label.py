class Label:

    # Constructor
    def __init__(self, id, name, color):
        self.id = id
        self.name = name
        self.color = color  # color in hexadecimal format


    # Setter for the ID
    def setId(self, id):
        if id is not None:
            if self.id != id:
                self.id = id


    # Setter for the Name
    def setName(self, name):
        if name is not None:
            if self.name != name and len(name) != 0:
                self.name = name


    # Setter for the Color
    def setColor(self, color):
        if self.checkColor(color):
            if not self.sameColors(color):
                self.color = color


    # Check if the format color is ok (array size is 3)
    def checkColor(self, color):
        if color is None: return False
        if len(color) != 7:
            return False
        return True if color[0] == '#' else False


    # Return True if the argument color and the self.Color are the same, else False
    def sameColors(self, color):
        return True if color == self.color else False


    def getName(self):
        return self.name


    def getId(self):
        return self.id


    def getColor(self):
        return self.color


    def toString (self):
        id = self.getId() if self.id is not None else 0
        name = self.getName() if self.name is not None else "None"
        color = self.getColor() if self.color is not None else "No Color"
        print("ID => {}, name =>  {}, color => {}".format(str(id), name, color))
