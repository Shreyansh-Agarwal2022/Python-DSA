class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class CLL:
    def __init__(self):
        self.head=None
        self.last=None

    def append(self,value):
        if(self.head==None):
            self.head=Node(value)
            self.head.next=self.head
            self.last=self.head
        else:
            self.last.next=Node(value)
            self.last=self.last.next
            self.last.next=self.head

    def printlist(self):
        if(self.head==None):
            print("List is Empty")
            return
        temp=self.head
        while(True):
            print(temp.value)
            temp=temp.next
            if(temp==self.last.next):
                break
    
    def insert(self,key,value):
        if(self.head==None):
            print("List is Empty can't find key.")
            return
        elif(self.head.value==key):
            new=Node(value)
            new.next=self.head.next
            self.head.next=new
            return
        elif(self.last.value==key):
            new=Node(value)
            new.next=self.head
            self.last.next=new
            self.last=new
        else:
            temp=self.head.next
            while(temp!=self.head and temp.value!=key):
                temp=temp.next
            if(temp==self.head):
                print("Key Not found.")
                return
            elif(temp.value==key):
                new=Node(value)
                new.next=temp.next
                temp.next=new
        return

ls=CLL()
ls.append(10)
ls.append(20)
ls.append(30)
ls.append(40)
ls.append(50)
ls.append(70)
ls.append(60)
ls.append(80)
ls.insert(80,-1)
ls.insert(10,-2)
ls.insert(40,-3)
ls.printlist()