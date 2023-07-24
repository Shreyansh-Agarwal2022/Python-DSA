def maximum(l):
    length=len(l[0])
    ans=[0 for _ in range(length+1)]
    ans[0]=abs(l[0][0]-l[1][0])
    for i in range(1,length):
        y=abs(l[0][i]-l[1][i])+ans[i-1]
        x=abs(l[0][i-1]-l[0][i])+abs(l[1][i-1]-l[1][i])+ans[i-2]
        ans[i]=max(x,y)
    return(ans[length-1])

col=int(input())
l=[None,None]
l[0]=list(map(int,input().split()))
l[1]=list(map(int,input().split()))
print(maximum(l))

#Test Case :

#4
#8 6 2 3
#9 7 1 2

#Output : 12
