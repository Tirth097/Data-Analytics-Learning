list = [i*i for i in range (6) if i%2 != 0]
# print(list)

#replace -ve to zero and +ve to same val
l = [-2,-4,3,5,2,-1]
l = [0 if i<0 else i for i in l]
# print(l)

# convert lower case to upper case
words = ["hello","python","tirth"]
words = [i.upper() for i in words]
print(words)