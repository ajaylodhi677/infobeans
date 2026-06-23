"""5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password"""

user=input("Enter username").lower()
password=input("Enter password").lower()

if user=='admin':
    if len(password)>=8:
      print("Valid user\nStrong password")
    else:
      print(" Please create strong password")
else:
    print("please enter valid user name")
      