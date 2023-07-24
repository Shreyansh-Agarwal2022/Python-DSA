class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
def search(root,key):
    if not root:
        return False
    elif root.data==key:
        return True
    elif root.data>key:
        return(search(root.left,key))
    else:
        return(search(root.right,key))
def insert(root,value):
    if not root:
        return(Node(value))
    elif root.data<=value:
        root.right=insert(root.right,value)
    else:
        root.left=insert(root.left,value)
    return(root)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def levelOrder(root):
    if not root:
        return
    queue=[root]
    while queue:
        temp=queue.pop(0)
        print(temp.data)
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
def findmax(root):
    if root:
        while root.right:
            root=root.right
        return root.data
    return None
def findmin(root):
    if root:
        while root.left:
            root=root.left
        return root.data
    return None
def height(root):
    if not root:
        return(0)
    else:
        l=height(root.left)
        r=height(root.right)
        return(1+max(l,r))
def size(root):
    if not root:
        return(0)
    else:
        l=size(root.left)
        r=size(root.right)
        return(1+l+r)
def delete(root,key):
    if root is None:
        return(None)
    elif root.data<key:
        root.right=delete(root.right,key)
    elif root.data>key:
        root.left=delete(root.left,key)
    else:
        if not root.left and not root.right:
            return None
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            temp=findmin(root.right)
            root.data=temp
            root.right=delete(root.right,temp)
    return root
root=None
choice=1
while choice==1:
    value=int(input("Enter Value to be inserted : "))
    root=insert(root,value)
    choice=int(input("Enter 1 to continue : "))
choice=1
while choice==1:
    value=int(input("Enter Value to be deleted : "))
    root=delete(root,value)
    choice=int(input("Enter 1 to continue : "))
print("Level Order :")
levelOrder(root)
print("Inorder :")
inorder(root)
print(f"Size of tree : {size(root)}")
print(f"Height of tree : {height(root)}")
print(f"Min value : {findmin(root)}\nMax value : {findmax(root)}")