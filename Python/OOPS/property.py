class Students:
    def __init__(self,phy,che,math):
        self.phy = phy
        self.che = che
        self.math = math
    
    @property
    def percentage(self):
        return((self.che+self.phy+self.math)/3)
s1 = Students(98,96,95)
print(s1.percentage)

s1.phy=98
print(s1.percentage)

    