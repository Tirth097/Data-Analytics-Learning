# Q1. Write a program that takes salary as input. Using conditional statements,
# calculate the final tax rate based on these rules:

# · If salary < 30,000 > 5%

# · If salary is 30,000-70,000 > 15%

# · If salary > 70,000 > 25%


s = int(input("enter your salary :"))
if(s < 30000):
    print("tax: > 5%")
if(s > 30000 and s < 70000):
    print("tax: > 15%")
if(s > 70000):
    print("tax: > 25%")
    print(f" final salary : {s - (s*0.4)}")
else :
    ("enter valid input")
    
