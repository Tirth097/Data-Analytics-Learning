with open ("E:\Material\Coding\Python\Json module\PQ\ name.txt","w") as f:
    names = [input(f"name {i+1} : ") for i in range (5)]
    for name in names:
        name = f.write(name + "\n")
    
with open ("E:\Material\Coding\Python\Json module\PQ\ name.txt","r") as f:
    na = f.read()
    print(na)
    
    