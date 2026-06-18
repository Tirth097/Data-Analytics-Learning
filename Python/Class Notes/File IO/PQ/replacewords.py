# with open("E:\\Material\\Coding\\Python\\File IO\\practic.txt", "r") as f:
#     data = f.read()

# data = data.replace("java", "python")
# with open("E:\\Material\\Coding\\Python\\File IO\\practic.txt", "w") as f:
#     f.write(data)
    
## 2ND METHOD

with open("E:\\Material\\Coding\\Python\\File IO\\practic.txt", "r+") as f:
    data = f.read() # cursor reads data and now it is at end
    f.seek(0) #cursor goes back to start
    f.write(data.replace("java","python"))
    