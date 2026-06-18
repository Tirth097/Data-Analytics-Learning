class Students:
    __name = "tirth"     # private attribute
    def __pass(self):    # private method
        print("No password")
        
    def name(self):      # accessible only within class
        print(self.__name)
        self.__pass()
    
p1=Students()
# print(p1.__name) --> this will give error 
p1.name() # --> can be done as method is in the class