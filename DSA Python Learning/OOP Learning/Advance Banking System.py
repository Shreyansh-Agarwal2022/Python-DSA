"""Advanced Banking System

1. Add interest calculation:

Modify the BankAccount class to include an interest rate attribute.
Implement a method calculate_interest() in the BankAccount class that calculates and adds interest to the account balance based on the interest rate.

2. Implement multiple account types:

Create additional classes for different types of bank accounts, such as SavingsAccount and CheckingAccount.
Each account type can have its own unique properties and methods.
For example, a SavingsAccount may have a minimum balance requirement and penalties for going below it.

3. Enhance the Bank class:

Allow the Bank class to handle multiple types of bank accounts.
Maintain separate lists of different account types in the Bank class.
Update the methods in the Bank class to work with different account types.

4. Implement transaction history:

Add a transaction history attribute to the BankAccount class to store a list of transactions (deposits and withdrawals) for each account.
Create a method in the BankAccount class to record transactions.
Implement a method in the Bank class to retrieve the transaction history for a specific account.

#TODO
5. Create user authentication:

Implement a user authentication system to ensure that only authorized users can access their accounts.
Create a User class that represents a bank account holder. Each user can have one or more accounts.
Associate each bank account with a user.

6. Implement account transfer:

Add a method in the Bank class to transfer funds from one account to another.
Perform necessary validations, such as checking if both accounts belong to the same user and if the sender account has sufficient funds.
"""

class BankAccount:
    all=[]
    interest_rate=0.12

    #Constructor
    def __init__(self, name : str, balance=0):
        self.__name=name
        self.balance=balance
        self.number=BankAccount.generate()
        self.history={"Deposit":[],"Withdraw":[],"Interest":[]}
        print(f"Successfully Opened Account : {self.__name} ({self.number})")
        BankAccount.all.append(self)

    #Class Method to generate unique account number
    @classmethod
    def generate(cls):
        flag=True
        num=0
        while flag:
            flag=False
            num+=1
            for object in cls.all:
                if object.number == num:
                    flag=True
        return num
    
    #Getter of name attribute
    @property
    def name(self):
        return self.__name
    
    #Setter of name attribute
    @name.setter
    def name(self, new : str):
        self.__name=new

    #Method to increase balance
    def deposit(self, amount):
        assert amount>=0,"Amount should be non-negative"
        self.balance+=amount
        self.history["Deposit"].append(amount)
        print(f"New Balance : {self.get_balance()}")

    #Method to decrease balance
    def withdraw(self, amount):
        assert amount>=0 and self.balance>amount,"Amount should be non-negative"
        self.balance-=amount
        self.history["Withdraw"].append(amount)
        print(f"New Balance : {self.get_balance()}")

    #Return current balance
    def get_balance(self):
        return f"${self.balance}"
    
    #Method for finding interest
    def calculate_interest(self):
        interest=self.interest_rate*self.balance
        self.balance+=interest
        self.history["Interest"].append(interest)
        print(f"Interest Earned : ${interest}\nNew Balance : {self.get_balance()}")

class SavingAccount(BankAccount):
    all=[]
    minimum=100
    penalty=20

    def __init__(self, name : str, balance=0):
        super().__init__(name,balance)
        self.interest_rate=0.15
        SavingAccount.all.append(self)

    def minimum_balance(self):
        if self.balance < self.minimum:
            self.balance -= self.penalty
            print(f"Your Account Break Minimum Balance Rule, pelaties of ${self.penalty} is imposed.")
            print(f"New Balance : {self.get_balance()}")
        else:
            print("Your Balance is above Minimum Balance Rule, no penalty.")

class BusinessAccount(BankAccount):
    all=[]
    minimum=200
    penalty=30

    def __init__(self, name : str, balance=0):
        super().__init__(name,balance)
        self.interest_rate=0.0
        BusinessAccount.all.append(self)
    
class Bank:
    allBanks=[]

    #Constructor
    def __init__(self):
        self.allAccounts={"BankAccount":[],"Saving":[],"Business":[]}
        print("New Bank is created")
        Bank.allBanks.append(self)
    
    #Method to create New Account
    def create_account(self, name):
        self.allAccounts["BankAccount"].append(BankAccount(name))
    
    #Method to get detail of account
    def get_account(self, account_number):
        for account in self.allAccounts["BankAccount"]:
            if account_number == account.number:
                print(f"Account Details :\nName:{account.name}\nAccount Number:{account.number}\nBalance:{account.get_balance()}\n")
                return account
        print("Account Number not found!")
        return None

    #Method to increase balance of account
    def deposit(self, account_number, amount):
        for account in self.allAccounts["BankAccount"]:
            if account_number == account.number:
                account.deposit(amount)
                print("Done")
                return
        print("Account Number not found!")
    
    #Method to decrease balance of account
    def withdraw(self, account_number, amount):
        for account in self.allAccounts["BankAccount"]:
            if account_number == account.number:
                account.withdraw(amount)
                print("Done")
                return
        print("Account Number not found!")

    #Method to get current balance
    def get_balance(self,account_number):
        for account in self.allAccounts["BankAccount"]:
            if account_number == account.number:
                return account.get_balance()
        print("Account Number not found!")
        return None
    
    def transation_history(self,account_number):
        for account in self.allAccounts["BankAccount"]:
            if account_number == account.number:
                print(f"Account History of {account.name}")
                for i in account.history.keys():
                    print(i,account.history[i])
                return
        print("Account Number not found!")
        return

#One Test Case
def main():
    bank = Bank()

    # Create new accounts
    bank.create_account("Alice")
    bank.create_account("Bob")

    # Deposit funds
    bank.deposit(1, 1000)  # Deposit $1000 into account 1
    bank.deposit(2, 500)   # Deposit $500 into account 2

    # Withdraw funds
    bank.withdraw(1, 300)  # Withdraw $300 from account 1
    bank.withdraw(2, 100)  # Withdraw $100 from account 2

    # Check balance
    print(bank.get_balance(1))  # Output: $700
    print(bank.get_balance(2))  # Output: $400

    bank.transation_history(1)

if __name__=="__main__":
    main()

