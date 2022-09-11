class Language:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setLevel(self, level):
        self.level = level
    def getLevel(self):
        return self.level

    def isLiterate(self):
        if(self.level >= 6):
            return True
        else: 
            return False
