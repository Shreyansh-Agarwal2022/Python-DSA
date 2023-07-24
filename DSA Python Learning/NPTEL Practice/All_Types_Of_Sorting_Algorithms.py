import sys
sys.setrecursionlimit(20000)
#Selection Sort
def ssort(a):
    n=len(a)
    for i in range(n):
        min=i
        for j in range(i,n):
            if a[min]>a[j]:
                min=j
        a[min],a[i]=a[i],a[min]

#Insertion Sort
def isort(a):
    n=len(a)
    for i in range(1,n):
        pos=i
        while pos>0 and a[pos]<a[pos-1]:
            a[pos],a[pos-1]=a[pos-1],a[pos]
            pos-=1

#Quick Sort
def qsort(a,l,r):
    if (r-l)<=1:
        return
    orange=l+1
    for green in range(l+1,r):
        if a[green]<=a[l]:
            a[orange],a[green]=a[green],a[orange]
            orange+=1
    a[orange-1],a[l]=a[l],a[orange-1]
    qsort(a,l,orange-1)
    qsort(a,orange,r)

#Merge Sort
def merge(a,b):
    (c,m,n)=([],0,0)
    while m<len(a) and n<len(b):
        if a[m]<=b[n]:
            c.append(a[m])
            m+=1
        else:
            c.append(b[n])
            n+=1
    c.extend(a[m:])
    c.extend(b[n:])
    return c
def msort(a,l,r):
    if (r-l)<=1:
        return(a[l:r])
    else:
        mid=(l+r)//2
        L=msort(a,l,mid)
        R=msort(a,mid,r)
        return(merge(L,R))

#A sample array/list for checking.
ls=[1,22,-3,4,-4,66,7,-8,99,10,-11,120,13,-14,150,-5]
#ls=list(range(10000,-1,-1))
print("Old Array :",ls)
#newl=msort(ls,0,len(ls))
#print("New Array :",newl)
#isort(ls)
#ssort(ls)
#ls.sort()
qsort(ls,0,len(ls))
print("New Array :",ls)