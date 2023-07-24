s=[0]
q=[0]
visited=[0]
graph=[ [0,1,1,0,0],
        [1,0,0,0,1],
        [1,0,0,1,0],
        [0,0,1,0,0],
        [0,1,0,0,0]
]
while s:
    curr=s.pop()
    print(curr)
    for i in range(0,len(graph[0])):
        if graph[curr][i] and (i not in visited):
            s.append(i)
            visited.append(i)
