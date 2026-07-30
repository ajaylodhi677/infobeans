"""3. Smart Banking System
Scenario:
You are developing a Smart Banking System for a bank to help customers perform basic banking operations such as deposit, withdrawal, balance checking, and interest calculation.
Sometimes, users may try to withdraw money or check balance before depositing any amount. Your system must handle such situations properly.

👉 Important Condition:
If no amount has been deposited yet, the system should display:
"No balance available. Please deposit first"
and should not allow withdrawal, balance check, or interest calculation.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Deposit Money
2 → Withdraw Money
3 → Check Balance
4 → Apply Interest

* Balance > 50000 → 5% interest
* Otherwise → 3% interest
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
No balance available. Please deposit first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter amount to deposit: 10000

Output:
Amount deposited successfully

---

Sample Run 3:
Input:
Enter your choice: 3

Output:
Current Balance: 10000

---

Sample Run 4:
Input:
Enter your choice: 2
Enter amount to withdraw: 15000

Output:
Insufficient balance

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Interest added: 300
Updated Balance: 10300

---

Sample Run 6:
Input:
Enter your choice: 2
Enter amount to withdraw: 5000

Output:
Withdrawal successful

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!"""

print("1 → Deposit Money \n2 → Withdraw Money \n3 → Check Balance \n4 → Apply Interest \n5 → Exit")
dp = 0
while True:
    ch = int(input("Enter Your Choice: "))
    match ch:
       case 1:
            db = int(input("Enter amount to deposit:"))
            dp = db + dp
            print("Amount deposited successfully")

       case 2:
            if dp<=0:
                print("No balance available. Please deposit first")
            else:
                wb = int(input("Enter amount to withdraw"))
                if wb>dp:
                     print("Insufficient Balance")
                else:
                     dp = dp - wb
                     print("Withdraw Successfull")

       case 3:
               print("Current Balance :",dp)
       case 4:
          if dp<=0:
            print("No balance available. Please deposit first")
          else:
            if dp > 50000 :
               int = dp*5//100
               dp = dp+int
               print("Interest added:",int,"\nUpdated Balance:",dp)
            else:
               int = dp*3//100
               dp = dp+int
               print("Interest added:",int,"\nUpdated Balance:",dp)
       case 5:
              print("Exiting system... Thank you!")
              break
       case __:
              print("Invalid choice. Please try again.")