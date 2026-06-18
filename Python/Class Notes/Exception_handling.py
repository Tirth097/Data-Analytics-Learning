try:
    x= int(input("enter a num :"))
    print (5 / x)
except ZeroDivisionError:
    print("zero not allowed")
except ValueError:
    print("invalid input")
else:
    print("great no exeptions")
finally:
    print("executed at end no matter what")
    