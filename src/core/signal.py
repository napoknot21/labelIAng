from tokenize import String
import numpy as np

class Signal :

    #constructor
    def __init__(self, name, timer, values) :
        self.name = name
        self.timer = np.array(timer)
        self.values = np.array(values)

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


    def toString (self) :
        name = self.name if self.name is not None else self.name
        timer = self.timer if self.timer is not None else self.timer
        values = self.values if self.values is not None else self.values
        return ("singal name: " + name + ", values: " + values + ", timer:" + timer)
