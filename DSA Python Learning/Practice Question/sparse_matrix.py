#Question : https://www.geeksforgeeks.org/sparse-matrix-representation/

#Solution :

#Here I have used linked list to store a Matrix because Matrix have many 0(zero) entries.
#So its a sparse matrix, so I stored it in linked list for memory efficieny.

#Linked List Node Sturcture
class Node:
    def __init__(self,r,c,data):
        self.data=data
        self.row=r
        self.column=c
        self.next=None

#Class of linked list which is used to store a Sparse Matrix
class LinkedList:
    #Initializing the Linked List
    #We have also stored the last pointer because it help to reduce time complexity of add_end method.
    def __init__(self,rows,columns):
        self.head=None
        self.last=None
        self.rows=rows
        self.columns=columns
    #This method is used to add element to last of Linked List.
    def add_end(self,r,c,data):
        #If Linked List is empty
        if(self.head==None):
            self.head=Node(r,c,data)
            self.last=self.head
        #Else if Linked List is NOT empty
        else:
            self.last.next=Node(r,c,data)
            self.last=self.last.next
    #This method makes the sparse matrix by taking input from user.
    def make_sparse(self):
        for i in range(self.rows):
            for j in range(self.columns):
                data=int(input(f"Enter Data for matrix[{i}][{j}] : "))
                if(data!=0):
                    self.add_end(i,j,data)
    #This method adds element in linked list in sorted order.
    def addSorted(self,r,c,data):
        #If linked list is empty.
        if(self.head==None):
            self.head=Node(r,c,data)
            self.last=self.head
            return
        else:
            #Adding before head of linked list.
            if(self.head.row>r) or (self.head.row==r and self.head.column>c):
                new=Node(r,c,data)
                new.next=self.head
                self.head=new
                return
            #Traversing the Linked List.
            temp=self.head
            prev=None
            while temp is not None:
                if(temp.row<r) or (temp.row==r and temp.column<c):
                    prev=temp
                    temp=temp.next
                elif(temp.row>r) or (temp.row==r and temp.column>c):
                    prev.next=Node(r,c,data)
                    prev.next.next=temp
                    return
                elif(temp.row==r and temp.column==c):
                    temp.data+=data
                    return
            #Adding at last of Linked List.
            if temp is None:
                new=Node(r,c,data)
                prev.next=new
                self.last=new
                return
    #It prints the matrix in normal form.
    def printMatrix(self):
        temp=self.head
        for i in range(self.rows):
            for j in range(self.columns):
                if(temp!=None) and (i==temp.row and j==temp.column):
                    print(f"{temp.data}",end=" ")
                    temp=temp.next
                else:
                    print("0",end=" ")
            print()
        print()
    #It prints the matrix in sparse form by traversing the Linked List.
    def printList(self):
        temp=self.head
        print("Sparse Matrix : ")
        print("Row\tColumn\tValue")
        while(temp!=None):
            print(f"{temp.row}\t{temp.column}\t{temp.data}")
            temp=temp.next
        print()

#Function for merging two sparse matrics/adding two normal matrics in sparse matrix form.  
#It returns the merged sparse matrix.
def merge(head1,head2,rows,columns):
    temp1=head1
    temp2=head2
    head3=LinkedList(rows,columns)
    #Comparing and adding elements to new sparse matrix.
    #This is because sparse matrix is always sorted.
    while(temp1 is not None and temp2 is not None):
        if(temp1.row==temp2.row):
            if(temp1.column==temp2.column):
                value=temp1.data+temp2.data
                head3.add_end(temp1.row,temp1.column,value)
                temp1=temp1.next
                temp2=temp2.next
            elif(temp1.column>temp2.column):
                head3.add_end(temp2.row,temp2.column,temp2.data)
                temp2=temp2.next
            elif(temp1.column<temp2.column):
                head3.add_end(temp1.row,temp1.column,temp1.data)
                temp1=temp1.next
        elif(temp1.row>temp2.row):
            while(temp2!=None) and (temp1.row>temp2.row):
                head3.add_end(temp2.row,temp2.column,temp2.data)
                temp2=temp2.next
        elif(temp1.row<temp2.row):
            while(temp1!=None) and (temp1.row<temp2.row):
                head3.add_end(temp1.row,temp1.column,temp1.data)
                temp1=temp1.next
    #Adding leftover elements.
    while(temp1!=None):
        head3.add_end(temp1.row,temp1.column,temp1.data)
        temp1=temp1.next
    while(temp2!=None):
        head3.add_end(temp2.row,temp2.column,temp2.data)
        temp2=temp2.next
    return(head3)

#This function makes a Transpose matrix from head of sparse matrix.
#It returns new Linked List.
def makeTranspose(head,columns,rows):
    temp=head
    matrix=LinkedList(rows,columns)
    while temp is not None:
        matrix.addSorted(temp.column,temp.row,temp.data)
        temp=temp.next
    return(matrix)

#Our Main function
#Here our functions and methods runs.
def main():
    rows=int(input("Enter Number of rows : "))
    columns=int(input("Enter Number of columns : "))
    matrix1=LinkedList(rows,columns)
    matrix2=LinkedList(rows,columns)
    print("Enter data for Matrix 1 : ")
    matrix1.make_sparse()
    print("Enter data for Matrix 2 : ")
    matrix2.make_sparse()
    print("Displaying Matrix 1 : ")
    matrix1.printMatrix()
    print("Displaying Matrix 2 : ")
    matrix2.printMatrix()

    matrix1.printList()
    matrix2.printList()

    matrix3=merge(matrix1.head,matrix2.head,rows,columns)
    print("Displaying Matrix 3 : ")
    matrix3.printMatrix()
    matrix3.printList()

    print("Transpose of Matrix 3 :")
    matrix4=makeTranspose(matrix3.head,rows,columns)
    matrix4.printMatrix()
    matrix4.printList()

#Executing the Main function
if __name__=="__main__":
    main()

#This was asked in Semester 2 DSA Lab Mid-Term Exam