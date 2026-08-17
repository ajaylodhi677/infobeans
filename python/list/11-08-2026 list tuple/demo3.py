"""
3.

MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 – Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 – Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 – Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45
"""
userv=0
m=[]
while True:
   print("\n==========Welcoem to menu driven==================")
   print("1. Find Employee with Highest Total Score")
   print("2. Find Month with Lowest Average Score")
   print("3. Display Employee-wise Maximum Score")
   print("4. Exit")
   choice=int(input("enter your choice :"))
   if userv==0 and choice!=4:
      rows=int(input("Enter number rows :"))
      cols=int(input("Enter number of columns :"))
      for i in range(rows):
          row=[]
          for j in range(cols):
              row.append(int(input(f"Enter Employee {i+1} performance for months {j+1} value:")))
          m.append(row)
          userv=1
   match choice :
      case 1:
         print("Dispaly matrix :")
         print(*m)
         rsum=0
         x=0
         i=1
         for ro in m:
             s1=sum(ro)
             if rsum<s1:
                rsum=s1
                x=i
             i+=1
         print(f"Employee {x} has highest total score :",rsum) 
      case 2 :
         print("Dispaly matrix :")
         print(*m)
         i=0
         while i<cols:
            j=0
            msum=0
            while j<rows:
               msum+=m[j][i]
               j+=1
            avg=msum/rows
            print(f"month {i+1} Average :",int(avg))
            i+=1
      case 3 :
         print("Dispaly matrix :")
         print(*m)
         x=1
         for ro in m:
           print(f"Employee {x} Max Score :",max(ro))
           x+=1
      case 4:
        break
print("Thanks you for using matrix menu driven system :")      
             
 
           