class maxHeap:
    def __init__(self):
        self.heap=[]
    def LevelOrder(self):
        for i in self.heap:
            print(i)
    def parent(self,i):
        return (i-1)//2
    def leftChild(self,i):
        return 2*i+1
    def rightChild(self,i):
        return 2*i+2
    def insert(self,data):
        self.heap.append(data)
        i=len(self.heap)-1
        parent=self.parent(i)
        while i>0 and self.heap[parent]<self.heap[i]:
            self.heap[parent],self.heap[i]=self.heap[i],self.heap[parent]
            i=parent
            parent=self.parent(i)
    def deleteMax(self):
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        result=self.heap[0]
        self.heap[0]=self.heap.pop()
        i=0
        n=len(self.heap)
        lc=self.leftChild(i)
        rc=self.rightChild(i)
        larget=i
        while (lc<n and self.heap[lc]>self.heap[i]) or (rc<n and self.heap[rc]>self.heap[i]):
            if (lc<n and self.heap[lc]>self.heap[i]):
                self.heap[lc],self.heap[i]=self.heap[i],self.heap[lc]
                larget=lc
            if (rc<n and self.heap[rc]>self.heap[i]):
                self.heap[rc],self.heap[i]=self.heap[i],self.heap[rc]
                larget=rc
            i=larget
            lc=self.leftChild(i)
            rc=self.rightChild(i)
        return result
heap=maxHeap()
heap.insert(10)
heap.insert(-2)
heap.insert(100)
heap.insert(-10)
heap.insert(2)
heap.insert(111)
heap.insert(12)
#print("Max element is ",heap.deleteMax())
#print("Max element is ",heap.deleteMax())
#print("Max element is ",heap.deleteMax())
#print("Max element is ",heap.deleteMax())
#print("Max element is ",heap.deleteMax())
heap.LevelOrder()