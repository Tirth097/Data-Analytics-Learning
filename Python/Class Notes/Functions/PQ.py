## AVERAGE OF THREE FUNCTION 
# def avg(a,b,c):
#     print((a+b+c)/3)
    
# avg(1,2,3)

## print lenght of list (list as perameter)
# def length(list):
#     print(len(list))
# num = [1,2,3,4,5]
# length(num)

## PRINT ELEMNET OF LIST IN SINGLE LINE
num = [1,2,3,4,5,6]
def write(el):
    for i in el:
        if(i == len(num)):
            print(i,end="")
        else:
            print(i,end = ", ")
write(num) 

## FACTORIAL OF N 
# def fact(n):
#     f = 1  
#     for i in range (1,n+1):
#         f *= i
#     print (f)            
# fact(5)

## USD TO INR
# def convertor(USD):
#     print("Rs.",USD*83)
# convertor(8)

## INPUT EVEN ODD
# def dec():
#     n=int(input())
#     if(n%2 == 0):
#         print("even")
#     else:
#         print("odd")
# dec()        
