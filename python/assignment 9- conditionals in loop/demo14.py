"""7. University Result Classification System

A university assigns final class based on marks, backlog, and project score.

If marks are 75 or above, then check backlog. If backlog is 0, then check project score. If project score is 80 or above, assign First Class with Distinction; otherwise First Class. If backlog is not 0, assign First Class.

If marks are between 60 and 74, then check backlog. If backlog is less than or equal to 2, assign Second Class; otherwise Pass Class.

If marks are between 50 and 59, assign Pass. Otherwise Fail.

Input:
Marks = 78
Backlogs = 0
Project = 85

Output:
Result = First Class with Distinction"""

marks =int(input(" Marks :"))
back =int(input("backlog :"))
pro =int(input("project :"))

if marks>=75:
    if back==0:
       if pro>=80:
          print("Result : First class with distinction")
       else:
          print("Result : First class")
    else:
       print("Result : First class")
elif marks>=60:
    if back<=2:
       print("Result : second class")
    else:
       print("Result : Pass class")
elif marks>50:
    print("Result : pass class")
else:
    print("Result : Fail")
