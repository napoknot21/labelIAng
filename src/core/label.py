class Label:

    # Constructor
    def __init__(self, id, name, color, pos):
        """
        Constructor for Label object
        
        Parameters
        ----------
            id : Integer
                The id of the label set by the user

            name : String
                The label name

            color : Tuple
                The label color on RGB format

            pos : Integer
                The position of the label (this argument is useful for labelsUI.py)
        """
        self.id = id
        self.name = name
        self.color = color
        self.pos = pos


    # Setter 
    def setId(self, id):
        """Setter for the ID label"""
        if id is not None:
            if self.id != id:
                if isinstance(id, int) :
                    self.id = id


    # Setter 
    def setName(self, name):
        """Setter for the name label"""
        if name is not None:
            if self.name != name and len(name) != 0:
                self.name = name


    # Setter
    def setColor(self, color):
        """Setter for the color label"""
        if self.checkColor(color):
            if not self.sameColors(color):
                self.color = color


    # Check 
    def checkColor(self, color):
        """
        Function that checks if the format color is ok (array size is 3)
        
        Parameters
        ----------
            color : Tuples
                The color to check its format

        Returns
        -------
            True : Boolean
                If the color attribute is a tuple

            False : Boolean
                If it's not a tuple
        """
        if color is None: return False
        if len(color) != 7:
            return False
        return True if color[0] == '#' else False


    # Setter
    def setPos (self, newPos) :
        """Setter for the position label"""
        if self.pos == newPos :
            return
        self.pos = newPos


    # Checking
    def sameColors(self, color):
        """
        Check if the argument color and the self.Color are the same
        
        Parameters
        ----------
            color : Tuple
                The tuple color to verify

        Returns
        -------
            True : Boolean
                if the self.color equals to the color parameter

            False : 
                else
        """
        return True if color == self.color else False


    # Getter
    def getName(self):
        """Getter function for the Name label"""
        return self.name


    # Getter
    def getId(self):
        """Getter function for the ID label"""
        return self.id


    # Getter
    def getColor(self):
        """Getter function for the color label"""
        return self.color


    # Getter
    def getPos (self):
        """Getter function for the position label"""
        return self.pos 


    # Print
    def toString (self):
        """Function 'toString' that prints all important information about label object"""
        id = self.getId() if self.id is not None else 0
        name = self.getName() if self.name is not None else "None"
        color = self.getColor() if self.color is not None else "No Color"
        pos = self.getPos() if self.pos is not None else "No position"
        print("ID => {}, name =>  {}, color => {}, position => {}".format(str(id), name, color, str(pos)))
