#Iterative
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(data)
                    break
                else:
                    current = current.right

    def inorder(self):
        if self.root is None:
            return
        stack = []
        current = self.root
        while True:
            while current is not None:
                stack.append(current)
                current = current.left
            if len(stack) == 0:
                return
            node = stack.pop()
            print(node.data)
            current = node.right

    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, data):
        if self.root is None:
            return None
        parent = None
        current = self.root
        while current is not None:
            if data == current.data:
                if current.left is None and current.right is None:
                    if parent is None:
                        self.root = None
                    elif parent.left == current:
                        parent.left = None
                    else:
                        parent.right = None
                elif current.left is None:
                    if parent is None:
                        self.root = current.right
                    elif parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                elif current.right is None:
                    if parent is None:
                        self.root = current.left
                    elif parent.left == current:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                else:
                    successor_parent = current
                    successor = current.right
                    while successor.left is not None:
                        successor_parent = successor
                        successor = successor.left
                    current.data = successor.data
                    if successor_parent.left == successor:
                        successor_parent.left = successor.right
                    else:
                        successor_parent.right = successor.right
                return
            elif data < current.data:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right
root=BinaryTree()
root.insert(10)
root.insert(20)
root.insert(15)
root.insert(12)
root.insert(17)
root.insert(16)
root.insert(1)
root.insert(2)
root.insert(3)
root.insert(10)
root.delete(15)
root.delete(10)
root.inorder()

#Recursive
def insert(root,data):
    if not root:
        return(Node(data))
    else:
        if root.data<=data:
            root.right=insert(root.right,data)
        else:
            root.left=insert(root.left,data)
    return(root)
def levelorder(root):
    print("Level Order : ")
    if not root:
        return([])
    else:
        result=[]
        queue=[root]
        while queue:
            current=queue.pop(0)
            print(current.data)
            result.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return(result)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def search(root,data):
    while root:
        if root.data==data:
            return(True)
        elif root.data<data:
            root=root.right
        else:
            root=root.left
    return(False)
def delete(root,value):
    if not root:
        return(None)
    if root.data>value:
        root.left=delete(root.left,value)
    elif root.data<value:
        root.right=delete(root.right,value)
    else:
        if not root.left:
            root=root.right
        elif not root.right:
            root=root.left
        elif root.left and root.right:
            min=root.right
            while min.left:
                min=min.left
            root.data=min.data
            root.right=delete(root.right,min.data)
    return(root)
tree=None
tree=insert(tree,10)
tree=insert(tree,15)
tree=insert(tree,10)
tree=insert(tree,30)
tree=insert(tree,5)
tree=insert(tree,2)
tree=insert(tree,7)
tree=insert(tree,9)
tree=insert(tree,12)
tree=delete(tree,10)
tree=delete(tree,15)
print(levelorder(tree))
print("Inorder : ")
inorder(tree)