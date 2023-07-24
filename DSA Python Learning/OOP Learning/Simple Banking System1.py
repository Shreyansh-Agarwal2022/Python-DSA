import random

class BankAccount:

    #Constructor
    def __init__(self, name : str, number : int):
        self.__name=name
        self.balance=0
        self.number=number
        print(f"Successfully Opened Account : {self.__name} ({self.number})")
    
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
        self.allAccounts={}
        print("New Bank is created")
        Bank.allBanks.append(self)
    
    #Method to create New Account
    def create_account(self, name):
        num=self.generate()
        self.allAccounts[num]=BankAccount(name,num)

    #Method to generate unique account number
    def generate(self):
        num=0
        while True:
            num=random.randint(100000, 999999)
            if num not in self.allAccounts.keys():
                return num
    
    #Method to get detail of account
    def get_account(self, account_number):
        account = self.allAccounts[account_number]
        print(f"Account Details :\nName:{account.name}\nAccount Number:{account.number}\nBalance:{account.get_balance()}\n")
        return account               

    #Method to increase balance of account
    def deposit(self, account_number, amount):
        account = self.allAccounts[account_number]
        account.deposit(amount)
        return
    
    #Method to decrease balance of account
    def withdraw(self, account_number, amount):
        account = self.allAccounts[account_number]
        account.withdraw(amount)
        return

    #Method to get current balance
    def get_balance(self,account_number):
        account = self.allAccounts[account_number]
        return account.get_balance()

#One Test Case
def main():
    bank = Bank()

    # Create new accounts
    bank.create_account("Alice")
    bank.create_account("Bob")

    num1,num2=bank.allAccounts.keys()

    # Deposit funds
    bank.deposit(num1, 1000)  # Deposit $1000 into account 1
    bank.deposit(num2, 500)   # Deposit $500 into account 2

    # Withdraw funds
    bank.withdraw(num1, 300)  # Withdraw $300 from account 1
    bank.withdraw(num2, 100)  # Withdraw $100 from account 2

    # Check balance
    print(bank.get_balance(num1))  # Output: $700
    print(bank.get_balance(num2))  # Output: $400

if __name__=="__main__":
    main()