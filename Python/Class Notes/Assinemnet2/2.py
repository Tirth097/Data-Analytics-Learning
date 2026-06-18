# Q2. Write a function that takes two integers a and b and prints all even
# numbers between them (inclusive).

def even_num(a,b):
   list = [i for i in range (a,b+1) if i % 2 == 0] 
   print(list)

a = int(input("a :"))
b = int(input("b :"))
even_num(a,b)