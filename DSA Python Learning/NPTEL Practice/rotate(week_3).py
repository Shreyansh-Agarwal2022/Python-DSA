def rot(l):
    new=[]
    for i in range(len(l)):
        temp=[]
        for j in range(len(l)):
            temp.append(l[len(l)-j-1][i])
        new.append(temp)
    return new
    
ls=[[1,2,3], [4,5,6], [7,8,9]]
nl=rot(ls)
print(nl)