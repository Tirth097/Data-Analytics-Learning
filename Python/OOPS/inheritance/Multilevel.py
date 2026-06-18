class Car:
    colour = "black"
    @staticmethod
    def start():
        print("car started...")
    @staticmethod
    def stop():
        print("car stoped...")
class BMW(Car):
    def __init__(self,name):
        self.name = name
class M4(BMW):
    def __init__(self,type):
        self.type = type
        print("Multilevel inertance",self.type)
    
c1 = BMW("M4")
print(c1.name)
c1.start() # inherted method
print(c1.colour) # inherted property
c2 = M4("Auto") # inherts all properties from bmw class and bmw class as car's properties
print(c2.colour)
