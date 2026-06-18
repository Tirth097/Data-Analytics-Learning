list = [1,2,3,4,5,6,7,8]
def p(list,idx):
    if(idx==len(list)):
        return
    print(list[idx],end=" ")
    p(list,idx+1)

p(list,0)