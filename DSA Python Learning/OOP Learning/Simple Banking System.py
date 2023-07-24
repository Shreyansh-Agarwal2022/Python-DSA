"""Project: Simple Banking System

Description:
Create a program that simulates a simple banking system. The system should allow users to create bank accounts, deposit and withdraw funds, and check their account balance.

Requirements:

1. Create a BankAccount class that represents a single bank account. It should have the following attributes:

Account number (auto-generated)
Account holder's name
Current balance

2. Implement the following methods in the BankAccount class:

deposit(amount): Add the specified amount to the account balance.
withdraw(amount): Subtract the specified amount from the account balance. Make sure to check if the account has sufficient funds before allowing a withdrawal.
get_balance(): Return the current account balance.

3. Create a Bank class that represents the banking system. It should have the following attributes:

A list to store all the bank accounts.

4. Implement the following methods in the Bank class:

create_account(name): Create a new bank account with the given account holder's name. Generate a unique account number for the account.
get_account(account_number): Retrieve a bank account based on the provided account number.
deposit(account_number, amount): Deposit the specified amount into the account associated with the given account number.
withdraw(account_number, amount): Withdraw the specified amount from the account associated with the given account number.
get_balance(account_number): Get the current balance of the account associated with the given account number.

5. Create a main program that allows users to interact with the banking system by providing a command-line interface. Users should be able to create accounts, deposit and withdraw funds, and check their account balance."""

class BankAccount:
    all=[]

    #Constructor
    def __init__(self, name : str, balance=0):
        self.__name=name
        self.balance=balance
        self.number=BankAccount.generate()
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
        print(f"New Balance : {self.get_balance()}")

    #Method to decrease balance
    def withdraw(self, amount):
        assert amount>=0 and self.balance>amount,"Amount should be non-negative"
        self.balance-=amount
        print(f"New Balance : {self.get_balance()}")

    #Return current balance
    def get_balance(self):
        return f"${self.balance}"
    
class Bank:
    allBanks=[]

    #Constructor
    def __init__(self):
        self.allAccounts=[]
        print("New Bank is created")
        Bank.allBanks.append(self)
    
    #Method to create New Account
    def create_account(self, name):
        self.allAccounts.append(BankAccount(name))
    
    #Method to get detail of account
    def get_account(self, account_number):
        for account in self.allAccounts:
            if account_number == account.number:
                print(f"Account Details :\nName:{account.name}\nAccount Number:{account.number}\nBalance:{account.get_balance()}\n")
                return account
        print("Account Number not found!")
        return None

    #Method to increase balance of account
    def deposit(self, account_number, amount):
        for account in self.allAccounts:
            if account_number == account.number:
                account.deposit(amount)
                print("Done")
                return
        print("Account Number not found!")
    
    #Method to decrease balance of account
    def withdraw(self, account_number, amount):
        for account in self.allAccounts:
            if account_number == account.number:
                account.withdraw(amount)
                print("Done")
                return
        print("Account Number not found!")

    #Method to get current balance
    def get_balance(self,account_number):
        for account in self.allAccounts:
            if account_number == account.number:
                return account.get_balance()
        print("Account Number not found!")
        return None

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

if __name__=="__main__":
    main()

