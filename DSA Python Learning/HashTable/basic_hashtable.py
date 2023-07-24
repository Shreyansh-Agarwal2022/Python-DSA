class HashTable:
    def __init__(self,size=100):
        self.size=size
        self.table = [[None, None] for _ in range(size)]
    def h(self,key):
        return (key % self.size)
    def insert(self,key,value):
        self.table[self.h(key)]=[key,value]
    def display(self):
        print("Index\tKey\tValue\n")
        j=1
        for i in self.table:
            print(f"{j}\t{i[0]}\t{i[1]}")
            j+=1
    def find(self,key):
        result=self.table[self.h(key)]
        print()
        if result[0]==key:
            print("Value is",result[1])
        else:
            print("Not Found ",key)
t=HashTable(11)
t.insert(11,1)
t.insert(101,2)
t.insert(101,20)
t.insert(15,3)
t.insert(21,4)
t.display()
t.find(11)