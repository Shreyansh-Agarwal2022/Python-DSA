class minHeap:
    def __init__(self):
        self.arr=[]
        
    def parent(self,i):
        return (i-1)//2
        
    def lchild(self,i):
        return 2*i+1
        
    def rchild(self,i):
        return 2*i+2
        
    def heapify(self,index,n):
        smallest=index
        l=self.lchild(index)
        r=self.rchild(index)
        if l<n and self.arr[l]<self.arr[smallest]:
            smallest=l
        if r<n and self.arr[r]<self.arr[smallest]:
            smallest=r
        if smallest!=index:
            self.arr[smallest],self.arr[index]=self.arr[index],self.arr[smallest]
            self.heapify(smallest,n)
            
    def insert(self,data):
        self.arr.append(data)
        i=len(self.arr)-1
        p=self.parent(i)
        while i>0 and self.arr[p]>self.arr[i]:
            self.arr[p],self.arr[i]=self.arr[i],self.arr[p]
            i=p
            p=self.parent(i)
            
    def heapsort(self):
        for i in range((len(self.arr)-1)//2,-1,-1):
            self.heapify(i,len(self.arr))
        for i in range(len(self.arr)-1,0,-1):
            self.arr[0],self.arr[i]=self.arr[i],self.arr[0]
            self.heapify(0,i)
        self.arr.reverse()
        
    def delete(self):
        if len(self.arr)==0:
            return None
        elif len(self.arr)==1:
            return(self.arr.pop())
        self.arr[0],self.arr[-1]=self.arr[-1],self.arr[0]
        result=self.arr.pop()
        self.heapify(0,len(self.arr))
        return result

#Test Case
"""h=minHeap()
h.insert(5)
h.insert(7)
h.insert(6)
h.insert(10)
h.insert(9)
h.insert(12)
h.insert(11)
h.insert(13)
print(h.delete())
print(h.delete())
print(h.arr)"""
