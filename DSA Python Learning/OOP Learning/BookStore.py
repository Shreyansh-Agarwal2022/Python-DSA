"""Online Bookstore project with some additional advanced features:

1. Book:

Attributes: title, author, price, quantity, genre
Methods: getters and setters for attributes, update_quantity(quantity), get_discounted_price()

2. Customer:

Attributes: name, email, address, books_purchased
Methods: getters and setters for attributes, purchase_book(book), view_purchased_books()

3. Administrator:

Attributes: name, email, privileges
Methods: getters and setters for attributes, add_book(book), remove_book(book)

4. OnlineBookstore:

Attributes: books, customers, administrators
Methods: add_customer(customer), add_administrator(administrator), search_book(title), display_books()"""

import random
import csv

class Book:
    allBooks={}
    discount=20

    #Constructor
    def __init__(self, title : str, author : str, price, quantity=0, genre=None):

        assert price>=0,"Price should be non-negative"
        assert quantity>=0,"Quantity should be non-negative"

        self.__title=title
        self.__author=author
        self.price=price
        self.quantity=quantity
        self.genre=genre
        self.id=Book.generate()

        Book.allBooks[self.id]=[self.title,self.author,self.price,self.quantity,self.genre]

    #Class Method to generate unique random ID for book
    @classmethod
    def generate(cls):
        num=random.randint(1000,9999)
        if num in cls.allBooks.keys():
            num=cls.generate()
        return num
    
    #Getter for title attribute
    @property
    def title(self):
        return self.__title
    
    #Getter for author attribute
    @property
    def author(self):
        return self.__author
    
    #Setter for title attribute
    @title.setter
    def title(self,new):
        self.__title=new
    
    #Setter for author attribute
    @author.setter
    def author(self,new):
        self.__author=new

    #Print all Books
    @classmethod
    def printBooks(cls):
        print("ID\tTitle\tAuthor\tPrice\tQuantity\tGenre\n")
        for book in cls.allBooks.keys():
            print(f"{book}",end="\t")
            print(f"{cls.allBooks[book][0]}",end="\t")
            print(f"{cls.allBooks[book][1]}",end="\t")
            print(f"{cls.allBooks[book][2]}",end="\t")
            print(f"{cls.allBooks[book][3]}",end="\t\t")
            print(f"{cls.allBooks[book][4]}")

    #Method to update price
    def update_quantity(self,quantity):
        assert quantity>=0,"Quantity should be non-negative"
        self.quantity=quantity

    #Method to get discounted price
    def get_discounted_price(self):
        return (self.price * (100 - self.discount) / 100)
    
    #Read Books from CSV
    @classmethod
    def readCSV(cls,fileName):
        with open(fileName,"r") as f:
            reader=csv.DictReader(f)
            reader=list(reader)

        for book in reader:
            cls(book["Title"],book["Author"],float(book["Price"]),int(book["Quantity"]),book["Genre"])

    # Write Books to CSV
    @classmethod
    def writeCSV(cls, fileName):
        with open(fileName, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "Author", "Price", "Quantity", "Genre"])  # Write header row
            for book_id, book_info in cls.allBooks.items():
                writer.writerow([book_info[0], book_info[1], book_info[2], book_info[3], book_info[4]])

    #Find ID of book
    @classmethod
    def findID(cls,name):
        for ID,info in cls.allBooks.items():
            if info[0]==name:
                return ID
        return None

class Customer:
    allCustomers=[]

    def __init__(self,name:str,books_purchased=[]):
        self.__name=name
        self.books_purchased=books_purchased
        Customer.allCustomers.append(self)

    #Getter for name attribute
    @property
    def name(self):
        return self.__name
    
    #Setter for name attribute
    @name.setter
    def name(self, new : str):
        self.__name=new

    def purchase_book(self, bookID : int):
        if bookID in Book.allBooks.keys():
            self.book.append([bookID,Book.allBooks[bookID]])
        else:
            print("No book exist of this ID.")

    def view_purchased_books(self):
        for book in self.books_purchased:
            print(f"{book[0]} : {book[1]}")

class Administrator:
    def __init__(self,name:str,email:str,privileges=False):
        self.__name=name
        self.__email=email
        self.__privileges=privileges

    #Getter for Name attribute
    @property
    def name(self):
        return self.__name
    
    #Getter for Email attribute
    @property
    def email(self):
        return self.__email
    
    #Getter for Privileges attribute
    @property
    def privileges(self):
        return self.__privileges
    
    #Setter for Name attribute
    @name.setter
    def name(self,new):
        self.__name=new

    #Setter for Email attribute
    @email.setter
    def email(self,new):
        self.__email=new

    #Setter for Privileges attribute
    @privileges.setter
    def privileges(self,new):
        self.__privileges=new

    #Adding book
    def add_book(self,book):
        if self.privileges == True:
            id = Book.findID(book)
            if id==None:
                print("Book Not Found!")
                return
            OnlineBookstore.books.append(id)
            print("Added!")
            return
        else:
            print("You don't have Privileges!")
            return
        
    #Remove book
    def remove_book(self,book):
        if self.privileges == True:
            id = Book.findID(book)
            if id==None:
                print("Book Not Found!")
            elif id in OnlineBookstore.books:
                OnlineBookstore.books.remove(id)
                print("Removed!")
            else:
                print("Book Not Found in Store")
        else:
            print("You don't have Privileges!")

class OnlineBookstore:
    #Class Variables
    books=[]
    customers=[]
    administrators=[]

    #Add Customer
    @classmethod
    def add_customer(cls,customer : Customer):
        cls.customers.append(customer)

    #Add Administrator
    @classmethod
    def add_administrator(cls,administrator : Administrator):
        cls.administrators.append(administrator)

    #Boolean Function to find if book is present or not
    @classmethod
    def search_book(cls,title):
        id=Book.findID(title)
        if id in cls.books:
            return True
        else:
            print("Currently Book is Not present in Store, Please look next month")
            return False

    #Display All Books in Store
    @classmethod
    def displayBooks(cls):
        print("Title\tAuthor\tPrice\tQuantity Genre")
        for book in cls.books:
            print(*Book.allBooks[book],sep="\t")

#Some Test Functions
def Test1():
    b=Book("a","a",10,10,"a")
    b=Book("b","b",20,10,"a")
    b=Book("a","c",30,10,"a")
    b=Book("d","a",40,10,"a")
    b=Book("e","e",50,12,"hgk")
    Book.writeCSV("Path")

def Test2():
    Book.readCSV("Path")
    Book.printBooks()

def Test3():
    Book.readCSV("Path")
    Book.printBooks()
    admin=Administrator("a","a",True)
    admin.add_book("a")
    admin.add_book("d")
    admin.add_book("f")
    OnlineBookstore.displayBooks()
    admin.remove_book("d")
    admin.remove_book("f")
    OnlineBookstore.displayBooks()

"""Test csv file:

Title,Author,Price,Quantity,Genre
a,a,10,10,a
b,b,20,10,a
c,c,30,10,a
d,a,40,10,a
e,e,50,12,hgk
f,"Rob Mai",12.2,30,ash
"""

#Warning : Personal Info
"""Path to temp csv file : C:\Shreyansh_C\DSA Python practice\OOP Learning\\temp1.csv"""