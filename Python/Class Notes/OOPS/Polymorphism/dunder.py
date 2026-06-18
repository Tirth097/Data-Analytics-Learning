class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def show_num(self):
        print(self.real,"i +",self.img,"j")
    
    def __add__(self,num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return complex(newreal,newimg)

n1 = complex(5,7)
n1.show_num()
n2 = complex(3,2)
n2.show_num()
n3 = n1 + n2
n3.show_num()
         