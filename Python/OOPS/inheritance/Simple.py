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
    
c1 = BMW("M4")
print(c1.name)
c1.start() # inherted method
print(c1.colour) # inherted property