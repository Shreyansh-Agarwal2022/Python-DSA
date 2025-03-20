class Uni:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [i for i in range(n)]
    
    def check(self, x, y):
        return self.getPar(x) == self.getPar(y)
    
    def getPar(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.getPar(self.parent[x])
            return self.parent[x]
    
    def add(self, x, y):
        p_x = self.getPar(x)
        p_y = self.getPar(y)
        if p_x == p_y:
            return
        if self.rank[p_x] > self.rank[p_y]:
            self.parent[p_y] = p_x
        elif self.rank[p_x] == self.rank[p_y]:
            self.rank[p_x] += 1
            self.parent[p_y] = p_x
        else:
            self.parent[p_x] = p_y

g = Uni(10)
g.add(1, 2)
g.add(2, 3)
g.add(4, 5)
g.add(6, 7)
# Here : 1-2-3   4-5   6-7 
print(g.check(6, 5))


g.add(5, 6)
# Here : 1-2-3   4-5-6-7 
print(g.check(1,7))   
print(g.check(4,7))   
