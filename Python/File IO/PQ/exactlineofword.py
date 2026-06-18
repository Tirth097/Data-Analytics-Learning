# def findword():
#     word = "learning"
#     with open("E:\\Material\\Coding\\Python\\File IO\\practic.txt", "r") as f:
#         data = f.read()
#         if(data.find(word)!=-1): ## or write (word in data)
#             print("found at index",data.find(word))
#         else:
#             print("not found")

def findline():
    word = "learning"
    with open("E:\\Material\\Coding\\Python\\File IO\\practic.txt", "r") as f:
        i = 1
        for line in f:
            if word in line:
                print("Found at line", i)
                return
            i += 1
    print("Not found")

findline()