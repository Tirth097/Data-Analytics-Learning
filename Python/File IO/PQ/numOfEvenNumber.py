with open("E:\Material\Coding\Python\File IO\demo.txt","r") as f:
    data = f.read()
    i = 0
    for even in data:
        if (even % 2 == 0):
            i += 1
    print(i)
            
    