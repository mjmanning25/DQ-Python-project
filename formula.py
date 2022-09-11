class Formula:
    def __init__(self, thing, equation):
        self.thing = thing
        self.equation = equation

    def setThing(self, thing):
        self.thing = thing

    def getThing(self):
        return self.thing

    def setEquation(self, equation):
        self.equation = equation

    def getEquation(self):
        return self.equation

    def calcTotal(self):
        return True
        #calculate Formula
        #read the self.formula Value
        #split it
        #assign values based on what is enterred
        #reconstruct the formula
        #output the result
