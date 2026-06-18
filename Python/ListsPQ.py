#input
# list = []
# list.append(input("1:"))
# list.append(input("2:"))
# list.append(input("3:"))
# print(list)

#check if there is a palndrom
list=[1,2,3,2,1]
list1 = list.copy()
list.reverse()
if(list == list1):
    print("yeah")
else:
    print("nahh")