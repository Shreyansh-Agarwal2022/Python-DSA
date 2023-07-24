stack=[]
stack2=[]
infix=input("Enter : ")
postfix=""
pre={"+":1,"-":1,"*":2,"/":2}
for i in infix:
    if i=="(":
        stack2.append("(")
    elif i==")":
        while(stack2[-1]!="("):
            postfix+=stack2.pop()
        stack2.pop()
    elif i.isalnum():
        postfix+=i
    else:
        while stack2 and stack2[-1]!="(" and pre[stack2[-1]]>=pre[i]:
            postfix+=stack2.pop()
        stack2.append(i)
while stack2:
    postfix+=stack2.pop()
print("Postfix : "+postfix)
for i in postfix:
    if i.isalnum():
        stack.append(int(i))
    elif i=="+":
        op2=stack.pop()
        op1=stack.pop()
        op3=op1+op2
        stack.append(op3)
    elif i=="-":
        op2=stack.pop()
        op1=stack.pop()
        op3=op1-op2
        stack.append(op3)
    elif i=="*":
        op2=stack.pop()
        op1=stack.pop()
        op3=op1*op2
        stack.append(op3)
    elif i=="/":
        op2=stack.pop()
        op1=stack.pop()
        op3=op1/op2
        stack.append(op3)
    else:
        print("Error")
print("Evaluation : "+str(stack.pop()))