#character can have 1 or many colleges
#make a college
#name
#requirements
#gk spells
#gk rituals
#sk spells
#sk rituals

class College:
    def __init__(self, char, name):
        self.name = name

    def getName(self):
        return self.name

    def getGKSpells(self):
        return self.gkspells

    def getGKRituals(self):
        return self.gkrituals

    def getSKSpells(self):
        return self.skspells

    def getSKRituals(self):
        return self.skrituals

    #setup a bunch of shit here
    #build the whole college list of tallents and generals
    #gk counter too
    #use name as a flag, if flag return different sets of spells
    #use a file to show what is known, read file


# add spells per college
