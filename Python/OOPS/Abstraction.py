class cars:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.acc = True  ## user dosen't need this details so hide them 
        self.clutch = True ## the process only showes whats essential things ## abstraction
        print("car started...")
s1 = cars()
s1.start()