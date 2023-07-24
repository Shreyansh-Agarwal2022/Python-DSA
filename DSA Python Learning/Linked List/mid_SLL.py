#Ques : Write a function that prints the middle element of a given linked list. If the list has an even number of elements, 
#       print the second middle element. For example, if the input list is 1->2->3->4->5, then the output should be 3. 
#       If the input list is 1->2->3->4->5->6, then the output should be 4.

#Code :

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def append(self,value):
        if self.head is None:
            self.head=Node(value)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=Node(value)
    def mid(self):
        #Exception handeling
        if self.head is None:
            print("Error, list is empty")
            return
        temp=self.head
        length=0
        while temp!=None:
            temp=temp.next
            length+=1
        mid=length//2
        temp=self.head
        i=0
        while(i!=mid):
            temp=temp.next
            i+=1
        print(temp.value)
ls=SLL()
ls.append(1)
ls.append(2)
ls.append(3)
ls.append(4)
ls.append(5)
ls.append(6)
ls.mid()