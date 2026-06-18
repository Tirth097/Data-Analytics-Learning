# dict = {
#     "name":"tirth",
#     "age":19,
#     "sub":["math","os","es","ss"],
#     1:12
# }
# print(dict) #print dictionary
# print(dict["name"]) #print particular element
# print(dict[1]) 
# dict["name"]="Buddy" #can change values
# dict["X"] = "y" # new values added

# null_dict ={} # null dictonaries are allowed as well

# nested dict

# students ={
#     "name" : "tirth",
#     "sub" : {
#         "phy" : 98,
#         "chem" : 95
#     }
# }
# print(students)
# print(students["sub"]["phy"])

# methods in deictionaries

students = {"name":"x","sub":["math","phy","chm"]}
print(students.keys())
print(students.values())
print(students.get("name"))
students.update({"age":19,})
print(students)
 