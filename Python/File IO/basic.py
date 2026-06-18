##                                       READ MODE

#READ MODE
# f = open("E:\Material\Coding\Python\File IO\demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

##reads only first 5 letters
# d=f.read(5)
# print(d)

## READ LINE BY LINE
# data = f.readline() ## if already read whole file then you have to close and reopen it
# print(data) ## prints one line from file and one /n
# data = f.readline()
# print(data) ## prints second line from file and one /n (here /n works and give gap of on line)

##                                   WRITE MODE 

#TRUNCATE
# f = open("E:\Material\Coding\Python\File IO\demo.txt","w")
# f.write ("deleted everything first the added this")

#APPEND
# f = open("E:\Material\Coding\Python\File IO\demo.txt","a")
# f.write (". Added this at end by append")

#ENTER A FILE THAT DON'T EXIST IN W OR A MODE , IT CREATES IT FOR YOU
f = open("E:\Material\Coding\Python\File IO\sample.txt","w") # creates file
f.close()
