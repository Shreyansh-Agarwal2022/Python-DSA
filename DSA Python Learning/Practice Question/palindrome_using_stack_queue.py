def palindrome(str):
    stack=[]
    queue=[]
    
    # Better code : stack=list(str) and queue=list(reverse(str))
    for i in str:
        stack.append(i)
        queue.insert(0,i)
    
    #Better Code : return(stack==queue)
    while stack and queue:
        if stack.pop()==queue.pop():
            continue
        else:
            return(False)
    return(True)
    
print(palindrome("racecar"))