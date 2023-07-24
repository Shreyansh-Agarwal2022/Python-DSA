class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.rear=None
        self.front=None
    def enqueue(self,item):
        new=Node(item)
        if self.front==None:
            self.front=new
            self.rear=self.front
            return
        else:
            self.rear.next=new
            self.rear=new
    def isempty(self):
        if self.front==None:
            return True
        else:
            return False
    def dequeue(self):
        if self.isempty():
            return "---Empty---"
        else:
            value=self.front.data
            self.front=self.front.next
            return(value)
    def peek(self):
        if self.isempty():
            print("Empty")
            return
        return(self.front.data)
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())
print(q.peek())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())