class Queue:
    def __init__(self,length=50):
        self.front=-1
        self.rear=-1
        self.q=[None for _ in range(length)]
        self.capacity=length
    def enqueue(self,item):
        if (self.rear==self.capacity-1):
            print("Overflow")
            return
        else:
            if(self.rear==-1):
                self.front=self.rear=0
            else:
                self.rear=(self.rear+1)%self.capacity
            self.q[self.rear]=item
            return
    def dequeue(self):
        if(self.front==-1 or self.front>self.rear):
            return "Underflow"
        else:
            value=self.q[self.front]
            if(self.front==self.rear):
                self.front=self.rear=-1
            else:
                self.front=(self.front+1)%self.capacity
            return(value)
        
qu=Queue(3)
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
qu.enqueue(40)              # OverFlow
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())         # UnderFlow
