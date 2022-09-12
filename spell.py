class Spell:
    def __init__(self, name, rank):
        self.rank = rank
        self.name = name

        #spell name
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

        #rank
    def getRank(self):
        return True

    def setRank(self, rank):
        self.rank = rank

        #range
    def getRange(self):
        return self.range

    def setRange(self, range):
        self.range = range

        #duration
    def getDuration(self):
        return self.duration

    def setDuration(self, duration):
        self.duration = duration

        #experience multiple
    def getEM(self):
        return self.em

    def setEM(self, em):
        self.em = em

        #base chance
    def getBC(self):
        return self.bc

    def setBC(self, bc):
        self.bc = bc

        #resist
    def getResist(self):
        return self.resist

    def setResist(self, resist):
        self.resist = resist

        #storage
    def getStorage(self):
        return self.storage

    def setStorage(self, storage):
        self.storage = storage

        #target
    def getTarget(self):
        return self.target

    def setTarget(self, target):
        self.target = target

        #effect
    def getEffect(self):
        return self.effect

    def setEffect(self, effect):
        self.effect = effect

        #cast time
    def getCastTime(self):
        return self.casttime

    def setCastTime(self, casttime):
        self.casttime = casttime

        #actions
    def getAction(self):
        return self.action

    def setAction(self, action):
        self.action = action

        #concentration check
    def getConcentration(self):
        return self.concentration

    def setConcentration(self, concentration):
        self.concentration = concentration

        #material
    def getMaterials(self):
        return self.materials

    def setMaterials(self, materials):
        self.materials = materials

    def addMaterials(self, materials):
        self.materials.append(materials)

        #formula
    def getFormulas(self):
        return self.formulas

    def setFormulas(self, formulas):
        self.formulas = formulas

    def addFormulas(self, formulas):
        self.formulas.append(formulas)

        #import the char so you can read their stats
