class RankingChoice:
    def __init__(self, name, epcost, spcost, timecost):
        self.name = name
        self.epcost = epcost
        self.spcost = spcost
        self.timecost = timecost # days
    
    def setname(self, name):
        self.name = name
        
    def getname(self):
        return self.name
    
    def setepcost(self,ep):
        self.epcost = ep
        
    def getepcost(self):
        return self.epcost
    
    def setspcost(self,sp):
        self.spcost = sp
        
    def getspcost(self):
        return self.spcost
    
    def settimecost(self,time):
        self.timecost = time
        
    def gettimecost(self):
        return self.timecost