class Heap:
    def __init__(self):
        self.arr=[]
    def parent(self,i):
        return (i-1)//2
    def lchild(self,i):
        return 2*i+1
    def rchild(self,i):
        return 2*i+2
    def heapify(self,i,n):
        largest=i
        lc=self.lchild(i)
        rc=self.rchild(i)
        while (lc<n and self.arr[lc]>self.arr[largest]) or (rc<n and self.arr[rc]>self.arr[largest]):
            if lc<n and self.arr[lc]>self.arr[largest]:
                largest=lc
            if rc<n and self.arr[rc]>self.arr[largest]:
                largest=rc
            if largest!=i:
                self.arr[i],self.arr[largest]=self.arr[largest],self.arr[i]
                i=largest
                lc=self.lchild(i)
                rc=self.rchild(i)  
            else:
                break
    def insert(self,data):
        self.arr.append(data)
        i=len(self.arr)-1
        while i>0 and self.arr[self.parent(i)]<self.arr[i]:
            self.arr[self.parent(i)],self.arr[i]=self.arr[i],self.arr[self.parent(i)]
            i=self.parent(i)
    def delete(self):
        if len(self.arr)==0:
            return None
        if len(self.arr)==1:
            return self.arr.pop()
        result=self.arr.pop(0)
        self.heapify(0,len(self.arr))
        return result
    def heapsort(self):
        n=len(self.arr)
        for i in range(n//2-1,-1,-1):
            self.heapify(i,n)
        for i in range(n-1,0,-1):
            self.arr[i],self.arr[0]=self.arr[0],self.arr[i]
            self.heapify(0,i)

heap=Heap()
arr=[10,100,-2,12,111,2]
for i in arr:
    heap.insert(i)
while heap.arr:
    print(heap.delete())
print(heap.arr)