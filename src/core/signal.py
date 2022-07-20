from tokenize import String
import numpy as np

class Signal :

    #constructor
    def __init__(self, name, timer, values) :
        self.name = name
        self.timer = np.array([0,2,3])
        self.values = np.array(value for value in values)


    ###########getters and setters###############

    def getName (self) :
        return self.name

    def getTimer (self) :
        return self.timer

    def getValues (self) :
        return self.values

    def setName (self, name) :
        self.name = name

    def setValue (self, values) :
        self.values = values

    def setTimer (self, timer) :
        self.timer = timer

    ##############################################

timer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
values = [1.2, 2.2, 3.2, 4.2, 5.2, 5.4, 6.2, 6.4, 6.0, 10.0]
s = Signal ("Test", timer, values)

print(s.getValues())