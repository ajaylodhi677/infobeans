'''
ASSIGNMENT 2 — BANK ACCOUNT MANAGEMENT SYSTEM
=============================================

A bank provides different types of accounts.

Create the following hierarchy:

Account
|
+-------- SavingsAccount
|
+-------- PremiumSavingsAccount

REQUIREMENTS:

1. Create a parent class Account.

Attributes:

* account_number
* customer_name
* balance

2. SavingsAccount should inherit from Account.

Additional attribute:

* interest_rate

3. PremiumSavingsAccount should inherit from SavingsAccount.

Additional attribute:

* cashback_percentage

4. Parent-class data must be initialized using super().

5. Create the following methods:

display_account()
deposit()
withdraw()

6. Override display_account() in SavingsAccount.

7. Override display_account() again in PremiumSavingsAccount.

8. Each overridden method must call the parent method using super().

9. Demonstrate multilevel inheritance.

10. Balance must be encapsulated using:

@property
@balance.setter
@balance.deleter

11. Balance cannot be negative.

12. Read all data from the user.

INPUT:

Enter Account Number:
Enter Customer Name:
Enter Initial Balance:
Enter Account Type:

1. Savings Account
2. Premium Savings Account

For Savings Account:

Enter Interest Rate:

For Premium Savings Account:

Enter Interest Rate:
Enter Cashback Percentage:

Then ask:

Enter amount to deposit:
Enter amount to withdraw:

SAMPLE INPUT:

Enter Account Number: 1001
Enter Customer Name: Amit
Enter Initial Balance: 25000
Enter Account Type: 2
Enter Interest Rate: 7
Enter Cashback Percentage: 2
Enter amount to deposit: 5000
Enter amount to withdraw: 3000

EXPECTED OUTPUT:

## Account Details

Account Number: 1001
Customer Name: Amit
Balance: 25000

Account Type: Premium Savings Account
Interest Rate: 7%
Cashback Percentage: 2%

After Deposit:
Balance: 30000

After Withdrawal:
Balance: 27000
'''

class Account:
    def __init__(self,account_number,customer_name,balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,balance):
        if balance>=0:
            self.__balance = balance
        else:
            print("Balance can not be negative")

    @balance.deleter
    def balance(self):
        print("Deleting the balance: ")
        del self.__balance

    def display_account(self):
        print(f"""
Account Number: {self.account_number}
Customer Name: {self.customer_name}
Balance: {self.balance}""")
        
    def deposit(self,deposit):
        self.balance = self.balance+deposit
        
    def withdraw(self,withdraw):
        self.balance = self.balance-withdraw

class SavingsAccount (Account):
    def __init__(self,account_number,customer_name,balance,interest_rate):
        super().__init__(account_number,customer_name,balance)
        self.interest_rate = interest_rate

    def display_account(self):
        super().display_account()
        print(f"""Account Type: Savings Account
Interest Rate: {self.interest_rate}""")

class PremiumSavingsAccount (SavingsAccount):
    def __init__(self,account_number,customer_name,balance,interest_rate,cashback_percentage):
        super().__init__(account_number,customer_name,balance,interest_rate)
        self.cashback_percentage = cashback_percentage

    def display_account(self):
        super().display_account()
        print(f"""Account Type: Premium Savings Account
Cashback Percentage: {self.cashback_percentage}""")

account_number = int(input("Enter Account Number:"))
customer_name = input("Enter Customer Name:")
balance = int(input("Enter Initial Balance:"))
print("""
1. Savings Account
2. Premium Savings Account
""")
i = int(input("Enter Account Type:"))
if i == 1:
    interest_rate = float(input("Enter Interest Rate: "))
    acc = SavingsAccount(account_number,customer_name,balance,interest_rate)

    print("\nAccount Details")
    acc.display_account()
    
    deposit = float(input("Enter amount to deposit: "))
    acc.deposit(deposit)
    
    print("\nAfter Deposit:")
    print("Balance:", acc.balance)
    
    withdraw = float(input("Enter amount to withdraw: "))
    acc.withdraw(withdraw)
    
    print("\nAfter Withdrawal:")
    print("Balance:", acc.balance)

elif i == 2:
    interest_rate = float(input("Enter Interest Rate: "))
    cashback_percentage = int(input("Enter Cashback Percentage: "))
    acc = PremiumSavingsAccount(account_number,customer_name,balance,interest_rate,cashback_percentage)

    print("\nAccount Details")
    acc.display_account()
    
    deposit = float(input("\nEnter amount to deposit: "))
    acc.deposit(deposit)
    
    print("After Deposit:")
    print("Balance:", acc.balance)
    
    withdraw = float(input("\nEnter amount to withdraw: "))
    acc.withdraw(withdraw)
    
    print("After Withdrawal:")
    print("Balance:", acc.balance)

else:
    print("Wrong Choice")