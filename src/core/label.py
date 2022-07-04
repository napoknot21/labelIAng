class Label:

    # Constructor
    def __init__(self, id, name, color, pos):
        self.id = id
        self.name = name
        self.color = color
        self.pos = pos  # color in hexadecimal format


    # Setter for the ID
    def setId(self, id):
        if id is not None:
            if self.id != id:
                if isinstance(id, int) :
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



    def setPos (self, newPos) :
        if self.pos == newPos :
            return
        self.pos = newPos


    # Return True if the argument color and the self.Color are the same, else False
    def sameColors(self, color):
        return True if color == self.color else False


    def getName(self):
        return self.name


    def getId(self):
        return self.id


    def getColor(self):
        return self.color


    def getPos (self):
        return self.pos 


    def toString (self):
        id = self.getId() if self.id is not None else 0
        name = self.getName() if self.name is not None else "None"
        color = self.getColor() if self.color is not None else "No Color"
        pos = self.getPos() if self.pos is not None else "No position"
        print("ID => {}, name =>  {}, color => {}, position => {}".format(str(id), name, color, str(pos)))
