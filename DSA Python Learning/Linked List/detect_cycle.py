class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def cycle(self):
        slow=self.head
        fast=self.head
        while True:
            slow=slow.next
            fast=fast.next.next
            if (slow==self.head or fast==None):
                break
            if (slow==fast):
                return True
        return False

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.head.next.next.next.next = llist.head.next
print(llist.cycle())

#We can also do exception handeling in cycle function for fast becoming None and giving 
# AttributeError: 'NoneType' object has no attribute 'next' for fast
# try : ... except AttributeError : ...

# In cycle function,
#        try:
#            while True:
#                # Move slow by one step and fast by two steps
#                slow = slow.next
#                fast = fast.next.next
#                # If slow and fast are the same, there is a cycle
#                if slow == fast:
#                    return True
#        except AttributeError:
#            # If fast reaches the end, there is no cycle
#            return False

#or by -> while fast and fast.next: ...