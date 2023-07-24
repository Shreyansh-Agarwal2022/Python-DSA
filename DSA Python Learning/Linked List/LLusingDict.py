'''items = {
            "data" : "Coke",
            "next" : {
                        "data" : "Cheese",
                        "next" : {
                                    "data" : "Biscuits",
                                    "next" : {
                                                "data" : "Soap",
                                                "next" : {}
                                    }
                        }
            }
         }'''
'''items={}
#Temporary variable used for traversal
traversal=items

#Looping through this temporary variable
while traversal != {}:
    print(traversal["data"])
    traversal=traversal["next"]

def insertEnd(head,value):
    #If linked list is empty
    if head=={}:
        head["data"]=value
        head["next"]={}
        return

    #New node we want to add it our linked list
    new_node={"data" : value, "next" : {}}

    #We will traverse till traversalVariable["next"]!={}
    traversalVariable=head
    while traversalVariable["next"]!={}:
        traversalVariable=traversalVariable["next"]
    traversalVariable["next"]=new_node
    return

def insertBegin(head,value):
    #If linked list is empty
    if head=={}:
        head["data"]=value
        head["next"]={}
        return
    
    #New node at beginning
    new_node={}
    new_node["data"]=head["data"]
    new_node["next"]=head["next"]
    head["next"]=new_node
    head["data"]=value
    return

def insertAfter(head,key,value):
    #If Linked List is empty.
    if head=={}:
        print("Linked List is Empty, Key not found.")
        return
    #Traverse till key not found.
    traversalVariable=head
    while traversalVariable!={} and traversalVariable["data"]!=key:
        traversalVariable=traversalVariable["next"]
    #If Key not found in Linked List.
    if traversalVariable=={}:
        print("Key not found.")
        return
    #If Key found.
    new_node={}
    new_node["data"]=value
    new_node["next"]=traversalVariable["next"]
    traversalVariable["next"]=new_node
    return

def deleteBegin(head):
    if head=={}:
        print("Linked List is empty.")
        return {}
    head=head["next"]
    return head

def deleteIntermediate(head,key):
    #If linked list is empty
    if head=={}:
        print("Linked List is empty.")
        return
    #Traverse till key not found
    traversalVariable=head
    while traversalVariable["next"]!={} and traversalVariable["next"]["data"]!=key:
        traversalVariable=traversalVariable["next"]
    #If key not found
    if traversalVariable["next"]=={}:
        print("Key not found. No deletion happened.")
        return
    #If key found
    else:
        traversalVariable["next"]=traversalVariable["next"]["next"]
        return

insertBegin(items,10)
insertBegin(items,20)
insertBegin(items,30)
insertAfter(items,20,40)
deleteIntermediate(items,10)
print(items)'''

class LinkedList:
    def __init__(self):
        self.head={}
    def insertBegin(self,value):
        if self.head=={}:
            self.head["data"]=value
            self.head["next"]={}
        else:
            new_node={}
            new_node["data"]=value
            new_node["next"]=self.head
            self.head=new_node
    def insertEnd(self,value):
        if self.head=={}:
            self.head["data"]=value
            self.head["next"]={}
            return
        traversalVariable=self.head
        while traversalVariable["next"]!={}:
            traversalVariable=traversalVariable["next"]
        traversalVariable["next"]["data"]=value
        traversalVariable["next"]["next"]={}
    def insertAfter(self,key,value):
        traversalVariable=self.head
        while traversalVariable and traversalVariable["data"]!=key:
            traversalVariable=traversalVariable["next"]
        if traversalVariable=={}:
            print("Key not found. No insertion.")
            return
        else:
            new_node={}
            new_node["data"]=value
            new_node["next"]=traversalVariable["next"]
            traversalVariable["next"]=new_node
            return
    def printList(self):
        traversalVariable=self.head
        while traversalVariable:
            print(traversalVariable["data"])
            traversalVariable=traversalVariable["next"]
    def deleteBegin(self):
        if self.head=={}:
            print("Linked List is Empty.")
            return
        self.head=self.head["next"]
    def deleteIntermediate(self,key):
        if self.head=={}:
            print("Linked List is Empty.")
            return
        if self.head["data"]==key:
            self.head=self.head["next"]
            return
        else:
            traversalVariable=self.head
            while traversalVariable["next"]!={} and traversalVariable["next"]["data"]!=key:
                traversalVariable=traversalVariable["next"]
            if traversalVariable["next"]=={}:
                print("Key not found. No deletion happened.")
                return
            else:
                traversalVariable["next"]=traversalVariable["next"]["next"]
                return

l=LinkedList()
l.insertBegin(1)
l.insertBegin(2)
l.insertBegin(3)
l.insertAfter(2,10)
l.deleteIntermediate(4)
l.printList()