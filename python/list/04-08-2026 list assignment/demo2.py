"""
2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []"""

s=list(map(int,input("Enter salary :").split()))
sum=sum(s)
average=sum/len(s)
gav=[]
sm15=[]
for i in s:
    if i>average:
      gav.append(i)
    if i>15000:
      sm15.append(i)
print("original list :",s)
print("average :",average)
print("above average :",gav)
print("remaining list :",sm15)