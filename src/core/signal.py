class Signal :

    #constructor
    def __init__(self, name, timer, values) :
        self.name = name
        self.timer = timer
        self.values = values


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
