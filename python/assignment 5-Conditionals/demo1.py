"""1. Smart Voting & ID Verification System
   A government system verifies whether a citizen can vote and whether they have a valid ID.
* If age ≥ 18 → Eligible to vote
* If ID proof is available → Allowed inside booth

Input:
Enter age: 22
Do you have ID (yes/no): yes

Output:
Eligible to vote
Allowed inside booth"""


age = int(input("Enter your age"))
id = input(" Do you have ID(yes/no)").lower()

if age>=22 :
    if id=='yes':
       print("Eligible to vote\nAllowed inside booth ")
    else:
       print("not allowed inside the booth..")
else :
   print("NOt eligible to vote")	   

