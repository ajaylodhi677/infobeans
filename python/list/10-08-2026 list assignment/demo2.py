"""
2.

=========================================================
            MATRIX ANALYSIS SYSTEM
=========================================================


A research laboratory stores experimental data in matrix form.
Scientists want a program that can analyze the matrix and provide
different statistics through a menu-driven application.

The application should allow the user to:

1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Prime Numbers Row-wise
   2. Count Perfect Numbers Column-wise
   3. Display Row-wise Sum
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Prime Numbers Row-wise
   ---------------------------------------
   Count and display the number of prime numbers present
   in each row of the matrix.

5. Choice 2 - Count Perfect Numbers Column-wise
   --------------------------------------------
   Count and display the number of perfect numbers present
   in each column of the matrix.

   Note:
   A perfect number is a number that is equal to the sum
   of its proper divisors.

   Examples:
   6  = 1 + 2 + 3
   28 = 1 + 2 + 4 + 7 + 14

6. Choice 3 - Display Row-wise Sum
   --------------------------------
   Calculate and display the sum of each row.

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
2 4 5
6 7 8
11 28 13

Output:
Row 1 Prime Count = 2
Row 2 Prime Count = 1
Row 3 Prime Count = 2

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 2

Output:
Column 1 Perfect Number Count = 1
Column 2 Perfect Number Count = 1
Column 3 Perfect Number Count = 0

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 3

Output:
Row 1 Sum = 11
Row 2 Sum = 21
Row 3 Sum = 52

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Analysis System

========================================================="""
c=0
usev=0
m=[]
while c!=1:
   print("\nSelect the option from the list :")
   print("1. Count Prime Numbers Row-wise")
   print("2. Count Perfect Numbers Column-wise")  
   print("3. Display Row-wise Sum")
   print("4. Exit ")  
   choice=int(input("Enter you choice :"))
   if usev==0 and choice !=4:
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
            pcount=0
            for v in ro:
               if v>1:
                 i=2
                 while i<=v//2:
                    if v%i==0:
                       break
                    i+=1
                 else:
                    pcount+=1
            print("row",x,"prime count =",pcount)
            x+=1
      case 2 :
         print("\ndispaly  matrix ")
         print(*m)
         i=0
         while i<cols:
            j=0
            percount=0
            while j<rows:
               ch=m[j][i]
               k=1
               psum=0
               while k<=ch//2:
                   if ch%k==0:
                     psum+=k
                   k+=1
               if psum==ch:
                  percount+=1
               j+=1
            print("column",i+1,"perfect count ",percount)
            i=i+1
      case 3 :
         print("\ndispaly  matrix ")
         print(*m)
         x=1
         for ro in m:
             print("row",x,"sum=",sum(ro))
             x+=1
      case 4 :
         break
print("thanks you for using matrix system :")

         