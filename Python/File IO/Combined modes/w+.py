f = open("E:\Material\Coding\Python\File IO\demo.txt","w+")
f.write("abc") # cursor reach at override word till c 
print(f.read()) # thus prints words aper c but as turcated there is nothing left after cusror only /n
f.close()