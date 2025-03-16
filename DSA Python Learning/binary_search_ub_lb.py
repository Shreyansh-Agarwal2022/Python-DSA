# Binary Search
def bsearch(arr, target):
    l = 0
    r = len(arr) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    
    return -1
    
# Binary Search Lower-Bound
def bslb(arr, target):
    l = 0
    r = len(arr) - 1
    ans = -1
    
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= target:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    
    return ans
    
# Binary Search Upper-Bound
def bsub(arr, target):
    l = 0
    r = len(arr) - 1
    ans = -1
    
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] <= target:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    
    return ans



while True:
    arr = list(map(int, input("Enter Array : ").split()))
    x = int(input("Enter Target : "))
    
    index = bsearch(arr,x)
    lb = bslb(arr, x)
    ub = bsub(arr, x)
    
    print("\nBinary Search :", index, arr[index], "\nLower Bound :", lb, arr[lb] , "\nUpper Bound :", ub, arr[ub], "\n")


"""
Sample Input-Output

Enter Array : -5 -3 -3 -1 -1 -1 0 0 1 3 4 4 10 31
Enter Target : -1

Binary Search : 4 -1 
Lower Bound : 3 -1 
Upper Bound : 5 -1 

Enter Array : -5 -3 -3 -1 -1 -1 0 0 1 3 4 4 10 31
Enter Target : 0

Binary Search : 6 0 
Lower Bound : 6 0 
Upper Bound : 7 0 

Enter Array : -5 -3 -3 -1 -1 -1 0 0 1 3 4 4 10 31
Enter Target : 2

Binary Search : -1 31 
Lower Bound : 9 3 
Upper Bound : 8 1

"""