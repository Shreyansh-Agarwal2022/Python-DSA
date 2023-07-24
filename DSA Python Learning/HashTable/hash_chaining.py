class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class HashChain:
    def __init__(self,size=11):
        self.size=size
        self.table=[None for _ in range(size)]

    def h(self,key):
        return key%self.size
    
    def insert(self,key,value):
        index=self.h(key)
        if self.table[index] is None:
            self.table[index]=Node(key,value)
            return
        head=self.table[index]
        prev=None
        while(head is not None):
            if(head.key==key):
                head.value=value
                return
            prev=head
            head=head.next
        prev.next=Node(key,value)
        return
    
    def find(self,key):
        index=self.h(key)
        head=self.table[index]
        while(head is not None):
            if head.key==key:
                print("\nValue is",head.value)
                return
            head=head.next
        print("\nNot Found",key)
    
    def delete(self,key):
        index=self.h(key)
        head=self.table[index]
        if head is None:
            print("Not Found")
            return
        elif head.key==key:
            self.table[index]=head.next
        else:
            while(head.next!=None):
                if(head.next.key==key):
                    head.next=head.next.next
                    print("Deleted")
                    return
                else:
                    head=head.next
            print("Not Found")
            return

    def display(self):
        for i in range(len(self.table)):
            print("\nIndex :",i)
            head=self.table[i]
            while(head is not None):
                print(f"({head.key},{head.value}) ->",end=" ")
                head=head.next
            print("None")

t=HashChain(11)

t.insert(11,1)
t.insert(22,2)
t.insert(1,3)
t.insert(110,4)
t.insert(101,5)
t.insert(11,10)
t.insert(2345,6)
t.insert(34,7)
t.insert(7,8)
t.insert(45,9)

t.delete(17)
t.delete(11)

t.display()

t.find(11)
t.find(10)
t.find(34)

