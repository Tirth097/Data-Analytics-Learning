# class attributes 
class Students:
    college_name = "mit adt"
    def __init__(self,name):
        self.name = name
        print(self.name,"->[This is an instance attribute]")
        print(Students.college_name,"->[This is an class attribute]")
    
s1 = Students("Tirth")
s2 = Students("Ravi")