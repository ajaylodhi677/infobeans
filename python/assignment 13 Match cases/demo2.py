"""
2.
 Employee Salary Processor

Scenario:
You are developing an Employee Salary Processing System for a companys HR department. The system is used to manage and calculate employee salary details such as allowances, tax deductions, and final payable salary.

The HR staff may not always follow the correct sequence while using the system. For example, they might try to calculate net salary or tax before entering the basic salary. Your program must handle such situations properly.

👉 Important Condition:
If the Basic Salary is not entered, the system should display:
"Please enter basic salary first"
and should not perform any further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Basic Salary
2 → Calculate HRA (20%) and DA (10%)
3 → Calculate Net Salary
4 → Tax Deduction

* Salary > 50000 → 10% tax
* Otherwise → 5% tax
  5 → Display Salary Slip
  6 → Exit

---

Sample Run 1:
Input:
Enter your choice: 3

Output:
Please enter basic salary first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter Basic Salary: 40000

Output:
Basic Salary recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
HRA: 8000
DA: 4000

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Net Salary (before tax): 52000

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Tax Deduction: 5200

---

Sample Run 6:
Input:
Enter your choice: 5

Output:
----- Salary Slip -----
Basic Salary: 40000
HRA: 8000
DA: 4000
Net Salary: 52000
Tax: 5200
Final Salary: 46800

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 6

Output:
Exiting program... Thank you!"""
salary=0
hra =0
da =0
tax=0
net=0
total=0
while True:
 
  print("1 → Enter Basic Salary")
  print("2 → Calculate HRA (20%) and DA (10%)")
  print("3 → Calculate Net Salary")
  print("4 → Tax Deduction \n")
  print("* Salary > 50000 → 10% tax")
  print("* Otherwise → 5% tax")
  print("5 → Display Salary Slip")
  print("6 → Exit")
  choice =int(input("Enter your chice "))
 
  match choice:
    case 1:
      a=int(input(" Enter your basic sallary"))
      salary=salary+a
      print(" sallery recorded succesfully",salary)
    case 2:
      if salary<1:
        print("\nEnter salary  first ")
      else:
        hra =salary*0.2
        da =salary*0.1
        print("Hra :",hra)
        print("Da :",da)
    case 3:
      if salary<1:
        print("\nEnter salary  first ")
      else: 
        hra =salary*0.2
        da =salary*0.1 
        net=net+hra+da
        print("Net salary (before deduction ):",)
    case 4:
      if salary<1:
        print("\nEnter salary  first ")
      elif salary>50000:
        tax=salary*0.1
        print(" tax deduction ",tax)
      else:
        tax =salary*0.05 
        print(" tax deduction ",tax)
    case 5:
      hra =salary*0.2
      da =salary*0.1
      net=salary+hra+da
      if net>50000:
        tax=net*0.1
      else:
        tax =net*0.05
      if salary<1:
        print("\nEnter salary  first ")
        
      else:
        total=net-tax
        print("--------------Sallery slip-----------------")  
        print("Basic Salary:",salary,"\nHRA:",hra, "\nDA:",da,"\nNet Salary:",net,"\nTax:",tax,"\nFinal Salary:",total)
    case 6:
      print("Exiting program ..... ",end=" ")
      break
    case _:
      print(" invalid input")
  print("\n\n")
print("Thanks you!")    