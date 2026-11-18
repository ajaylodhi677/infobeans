from demo4 import BankAccount,NegativeDepositException,InsufficientBalanceException,InvalidWithdrawalException,InvalidAmountException
acc=input("Enter account number:")
name=input("Enter name:")
bal=int(input("Enter initial balance:"))
p1=BankAccount(acc,name,bal)
while True:
    print("""================================
BANK ACCOUNT SYSTEM
===================

1. Deposit
2. Withdraw
3. Check Balance
4. Display Account Details
5. Exit
""")
    choice=int(input("Enter your chpoice:"))
    match choice:
        case 1:
            try:
                amount=int(input("Enter amount to deposit"))
                p1.deposit(amount)
                print("\nDemposit successful")
                print("Avaliable balnce:",p1.balance) 
            except NegativeDepositException as e:
                print("NegativeDepositException:",e)
            except InvalidAmountException as e:
                print("InvalidAmountException:",e) 
        case 2:
            try:
                amount=int(input("Enter amount :"))
                p1.withdraw(amount)
                print("\nWihdraw succesfully")
                print("Avaliable balnce:",p1.balance) 
            except InvalidWithdrawalException as e:
                print("InvalidWithdrawalException:",e)
            except InvalidAmountException as e:
                print("InvalidAmountException:",e)
            except InsufficientBalanceException as e:
                print("InsufficientBalanceException:",e)                  
        case 3:
            p1.check_balance()
        case 4:
            p1.display_account_details() 
        case 5:
            print("Thank you for using bank account system")
            break 
        case _:
            print("Invalid choice")    