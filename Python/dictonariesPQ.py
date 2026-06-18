#empty dict -> add sub marks as user input to it
# dict = {}
# dict.update({"Math":input("enter math mark : ")})
# dict.update({"phy":input("enter math phy : ")})
# dict.update({"Chem":input("enter math chem : ")})
# print(dict)


#Figure out a way to store 9 & 9.0 as separate values in the set.
set = {9,"9.0"} # make one string
set = {("int",9),("float",9.0)} # or make two tupples (we cant make dict in set{mutable})
print(set)