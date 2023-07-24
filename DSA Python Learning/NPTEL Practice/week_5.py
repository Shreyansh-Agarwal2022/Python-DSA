
#Sample Test Case :
#Federer:Nadal:2-6,6-7,7-6,6-3,6-1\Nadal:Federer:6-3,4-6,6-4,6-3\Federer:Nadal:6-0,7-6,6-7,6-3\Nadal:Federer:6-4,6-4\Federer:Nadal:2-6,6-2,6-0\Nadal:Federer:6-3,4-6,6-3,6-4\Federer:Nadal:7-6,4-6,7-6,2-6,6-2\Nadal:Federer:7-5,7-5\Halep:Wozniacki:3-6,6-3,6-3
#Djokovic:Zverev:2-6,6-7,7-6,6-3,6-1\Zverev:Djokovic:6-3,4-6,6-4,6-3\Djokovic:Zverev:6-0,7-6,6-7,6-3\Zverev:Djokovic:6-4,6-4\Djokovic:Zverev:2-6,6-2,6-0\Zverev:Djokovic:6-3,4-6,6-3,6-4\Djokovic:Zverev:7-6,4-6,7-6,2-6,6-2\Zverev:Djokovic:7-5,7-5\Williams:Muguruza:3-6,6-3,6-3\Muguruza:Williams:6-4,6-4\Williams:Muguruza:2-6,6-2,6-0\Muguruza:Williams:6-3,4-6,6-4,6-3\Williams:Muguruza:6-0,7-6,6-7,6-3\Muguruza:Williams:6-3,4-6,6-4,6-3\Williams:Muguruza:6-0,7-6,6-7,6-3\Muguruza:Williams:6-3,4-6,6-4,6-3\Williams:Muguruza:6-0,7-6,6-7,6-3
data=input("Enter Data : ")
newd=data.split("\\")
new=[]
for ele in newd:
    new.append(ele.split(":"))
for i in range(len(new)):
    new[i][2]=new[i][2].split(",")
for i in range(len(new)):
    ls=[]
    for j in new[i][2]:
        ls.append(j.split("-"))
    for j in range(len(ls)):
        ls[j][0],ls[j][1]=int(ls[j][0]),int(ls[j][1])
    new[i][2]=ls
d={}
del(newd)
del(data)
#d[player]:
#0 -> best 5 won
#1 -> best 3 won
#2 -> sets won
#3 -> games won
#4 -> sets lost
#5 -> games lost
for ele in new:
    if ele[0] not in d.keys():
        d[ele[0]]=[0 for _ in range(6)]
    if ele[1] not in d.keys():
        d[ele[1]]=[0 for _ in range(6)]

    wins=0 #For how won the 5-set or 3-set game if +ve then 0th won elif -ve then 1th won
    
    for i in range(len(ele[2])):
        d[ele[1]][3]+=ele[2][i][1]
        d[ele[0]][5]+=ele[2][i][1]
        d[ele[0]][3]+=ele[2][i][0]
        d[ele[1]][5]+=ele[2][i][0]
        if ele[2][i][0]>ele[2][i][1]:
            wins+=1
            d[ele[0]][2]+=1
            d[ele[1]][4]+=1
        elif ele[2][i][0]<ele[2][i][1]:
            wins-=1
            d[ele[1]][2]+=1
            d[ele[0]][4]+=1

    if len(ele[2])>=5:
        if wins<0:
            d[ele[1]][0]+=1
        else:
            d[ele[0]][0]+=1
    elif len(ele[2])<3:
        if wins<0:
            d[ele[1]][1]+=1
        else:
            d[ele[0]][1]+=1
    elif len(ele[2])==3:
        if wins==3:
            d[ele[0]][0]+=1
        elif wins==-3:
            d[ele[1]][0]+=1
        elif wins>0:
            d[ele[0]][1]+=1
        elif wins<0:
            d[ele[1]][1]+=1
    elif len(ele[2])==4:
        if wins==2:
            d[ele[0]][0]+=1
        elif wins==-2:
            d[ele[1]][0]+=1
        elif wins>0:
            d[ele[0]][1]+=1
        elif wins<0:
            d[ele[1]][1]+=1

print("\n",new,"\n")
print(d)