class Person:
    name = "anonymous"
    
    @classmethod
    def changeName(cls,name): # cls insted of self
        cls.name = name # changes name from anonymous
p1 = Person()
p1.changeName("tirth")
print(p1.name)
print(Person.name)