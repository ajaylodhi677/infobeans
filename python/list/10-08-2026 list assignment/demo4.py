"""
4.

=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Enter size of matrix: 3

Enter matrix elements:

1 2 3
4 5 6
7 8 9

Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

Enter your choice: 1

Output:
Main Diagonal Elements:
1 5 9

---------------------------------------------------------

Enter your choice: 2

Output:
Secondary Diagonal Elements:
3 5 7

---------------------------------------------------------

Enter your choice: 3

Output:
Main Diagonal Sum = 15
Secondary Diagonal Sum = 15
Both Diagonal Sums are Equal

========================================================="""
userv=0
m=[]
while True:
   print("\n=========Welcome to matrix solutions =========")
   print("1. Display Main Diagonal Elements")
   print("2. Display Secondary Diagonal Elements")
   print("3. Compare Main and Secondary Diagonal Sums")
   print("4. Exit")
   choice = int(input("Enter your choice :"))
   if userv==0 and choice!=4:
      rows=int(input("Enter size of matrix"))
      print("Enter matrix element :")
      for i in range(rows):
        row=[]
        for j in range(rows):
          row.append(int(input()))
        m.append(row)
      userv=1
   match choice :
      case 1:
          print("\ndispaly  matrix ")
          print(*m)
          i=0
          print("Main diagonal elements :")
          while i<rows: 
             print(m[i][i],end=" ")
             i+=1
      case 2:
          print("\ndispaly  matrix ")
          print(*m)
          i=0
          print("secondary diagonal elements ")
          while i<rows: 
             print(m[i][len(m[i])-i-1],end=" ")
             i+=1
      case 3 :
          print("\ndispaly  matrix ")
          print(*m)
          mdsum=0
          sdsum=0
          i=0
          while i<rows:
             sdsum+=m[i][len(m[i])-i-1] 
             mdsum+=m[i][i]
             i+=1
          print("Main diagonal sum :",mdsum)
          print("secondary diaogonal sum :",sdsum)
          if mdsum==sdsum:
              print("Both diagonal are equal :")
          elif mdsum>sdsum:
              print("main diaogonal is greater than secondary")
          else:
              print("secondary diagonal is greater than main")
      case 4 :
         break
print("Thanks you for using matrix system")
