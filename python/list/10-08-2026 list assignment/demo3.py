"""
3.

=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.

7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
153 121 10
370 22 44
407 15 131

Output:
Row 1 Armstrong Count = 1
Row 2 Armstrong Count = 1
Row 3 Armstrong Count = 1

---------------------------------------------------------

Enter your choice: 2

Output:
Column 1 Palindrome Count = 0
Column 2 Palindrome Count = 3
Column 3 Palindrome Count = 2

=========================================================
"""
c=0
usev=0
m=[]
while c!=1:
   print("\nSelect the option from the list :")
   print("1. Count Armstrong Numbers Row-wise")
   print("2. Count Palindrome Numbers Column-wise")  
   print("3. Display Average of Each Row")
   print("4. Exit ")  
   choice=int(input("Enter you choice :"))
   if usev==0:
      rows=int(input("Enter rows"))
      cols=int(input("Enter columns "))
      print("Enter matrix element :")
      for i in range(rows):
        row=[]
        for j in range(cols):
          row.append(int(input()))
        m.append(row)
      usev=1
   match choice :
      case 1 :
         print("\ndispaly  matrix ")
         print(*m)
         x=1
         for ro in m:
            acount=0
            for v in ro:
               org=v
               asum=0
               while v>0:
                 d=v%10
                 v=v//10
                 asum+=d**len(str(org))

               if asum==org:
                  acount+=1
            print("Row",x,"armstrong count :",acount)
            x+=1 
      case 2:
            print("\ndispaly  matrix ")
            print(*m)
            i=0
            while i<cols: 
              j=0
              percount=0
              while j<rows:
                ch=m[j][i]
                rh=int(str(ch)[::-1])
                if rh==ch:
                  percount+=1
                j+=1
              print("column",i+1,"palindrome count ",percount)
              i=i+1
      case 3 :
         print("\ndispaly  matrix ")
         print(*m)
         x=1
         for ro in m:
             print("row",x,"average=",sum(ro)/len(ro))
             x+=1
      case 4 :
         break
print("thanks you for using matrix system :")
