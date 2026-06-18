class Students:
    def __init__(self,name):
        self.name = name
        
s1 = Students("Tirth")
print(s1)
print(s1.name)
del s1
print(s1.name)
