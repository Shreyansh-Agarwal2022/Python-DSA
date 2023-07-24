class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def empty(self):
        return(self.head==None)
    def push(self,value):
        new=Node(value)
        new.next=self.head
        self.head=new
        return
    def pop(self):
        if(self.empty()):
            return "Stack is empty"
        else:
            value=self.head.data
            self.head=self.head.next
            return(value)
    def top(self):
        if(self.empty()):
            return "Stack is empty"
        else:
            return(self.head.data)
s=Stack()
for i in range(10,21,2): 
    s.push(i)
print("Top : ",s.top())
print("Stack is :")
while not s.empty():
    print(s.pop())