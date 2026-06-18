class Students:
    def __init__(self,fullname): #fullname  -> parameter
        self.name = fullname  #name -> attribute/variable of class
        print(self.name)
    def hello(self):
        print("hello",self.name)
    
s1 = Students("tirth") #we assin value to parameter
s1.hello()
