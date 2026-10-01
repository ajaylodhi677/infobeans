class Account:
    def __init__(self,account_no,customer_name,balance):
        self.account_no=account_no
        self.customer_name=customer_name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient balance")

    def display(self):
        print(self.account_no,self.customer_name,self.balance)

    def display_all(accounts):
        for account in accounts:
            account.display()

    def search(accounts,account_no):
        for account in accounts:
            if account.account_no==account_no:
                return account
        return None

    def balance_greater_than_50000(accounts):
        for account in accounts:
            if account.balance>50000:
                account.display()

    def highest_balance(accounts):
        high=accounts[0]
        for account in accounts:
            if account.balance>high.balance:
                high=account
        high.display()