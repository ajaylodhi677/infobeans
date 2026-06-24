"""13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600 """

salary=int(input("Enter salary"))
rating=int(input("Enter rating 1 to 5"))

if rating==5:
    salary1=salary+salary*0.25
elif rating==4:
    salary1=salary+salary*0.20
elif rating==3:
    salary1=salary+salary*0.10
elif rating==2:
    salary1=salary+salary*0.05
else:
    print("No hike")
    salary1=salary
if salary<20000 and rating>=4:
    salary1=salary1+2000

print(" revised salary :",salary1)




