class a:
    colour = "black"
    def __init__(self):
        print("hello i am a, perent class")
class b:
    age = "24"
    def __init__(self):
        print("hello i am b, perent class")
class c(a,b):
    def __init__(self):
        print("hello i am c, child of a,b")

s1 = c()
print(s1.colour)
print(s1.age)