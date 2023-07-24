def heapify(arr,n,i):
    largest=i
    lc=2*i+1
    rc=2*i+2
    if lc<n and arr[lc] > arr[largest]:
        largest=lc
    if rc<n and arr[rc] > arr[largest]:
        largest=rc
    if i!=largest:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
def heapsort(arr):
    n=len(arr)
    for i in range(n//2 - 1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,-1,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)
ls=[10,-1,2,33,-4,5,66,-7,8,99,-10,11]
heapsort(ls)
print(ls)