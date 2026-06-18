# create a student class that takes name & marks of 3 subjects as argumnets in constructor then create a method to print the average 
class Students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avarage is :",sum/3)
s1=Students("Parth",[96,97,98])
s1.get_avg()