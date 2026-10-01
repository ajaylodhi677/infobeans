'''
Assignment 3: Bank Account Operations
 A bank wants to perform basic operations on a customer's account.

Create a class BankAccount with the following attributes:

Account number
Account holder name
Balance

Create the following methods:

deposit() – Add an amount to the balance.

withdraw() – Subtract an amount from the balance.

display_account() – Display account details and final balance.

Sample data:

Account Number: 1001
Account Holder: Rahul
Opening Balance: 25000
Deposit: 5000
Withdrawal: 3000

Expected result:

Final Balance: 27000

'''
class BankAccount:
    def __init__(self):
        self.acc_no = int(input("Enter Account number:"))
        self.name = input("Enter the Name:")
        self.bal = int(input("Enter Balance:"))
        self.temp = self.bal


    def deposit(self):
        self.d = int(input("Enter Deposit Amount:"))
        self.bal += self.d


    def withdraw(self):
        self.wd = int(input("Enter Withdraw Amount:"))
        self.bal -= self.wd
           

    def display_account(self):
        print("=="*15)
        print("Account Number:",self.acc_no)
        print("Account Holder:",self.name)
        print("Opening Balance:",self.temp)
        print("Deposit:",self.d)
        print("Withdrawal:",self.wd)
        print()
        print("Expected result:")
        print()
        print("Final Balance:",self.bal)



c1 = BankAccount()
c1.deposit()
c1.withdraw()
c1.display_account()