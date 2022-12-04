class RankingChoice:
    def __init__(self, name):
        self.name = name
        self.epcost = 0
        self.spcost = 0
        self.timecost = 0 # days
    
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