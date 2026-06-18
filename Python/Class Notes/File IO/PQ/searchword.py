with open("E:\\Material\\Coding\\Python\\File IO\\practic.txt", "r") as f:
    data = f.read()
    if(data.find("learning")!=-1):
        print("found at index",data.find("learning"))
    else:
        print("not found")
## or make the word a variable then enter in .find(word)
## word=="learning"
