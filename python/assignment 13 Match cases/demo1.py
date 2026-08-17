"""1. Utility Toolkit System

You are developing a Utility Toolkit Application for a small office. Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit

Sample Run 1:
Input:
Enter your choice: 1
Enter number: 7

Output:
7 is a Prime Number

Sample Run 2:
Input:
Enter your choice: 2
Enter number: 121

Output:
121 is a Palindrome Number

Sample Run 3:
Input:
Enter your choice: 3
Enter number: 456

Output:
Reversed Number is: 654

Sample Run 4:
Input:
Enter your choice: 4
Enter number: 98765

Output:
Total digits: 5

Sample Run 5 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

Sample Run 6 (Exit):
Input:
Enter your choice: 5

Output:
Exiting program... Thank you!

Requirements:

* Use while loop to repeat menu
* Use match-case for decision making
* Handle negative numbers properly
* Use only loops and conditions"""
import math
while True:
    print("1 → Check Prime Number ")
    print("2 → Check Palindrome Number")
    print("3 → Reverse a Number")
    print("4 → Count Digits")
    print("5 → Exit")
    choice=int(input("Enter choice :"))
    match choice:
       case 1:
           n=int(input("Entr numbr :"))
           n=abs(n)
           m=int(math.sqrt(n))
           if n<2:
              print(" not prime ")
           else:
              i=2
              while i<=m:
                 if n%i==0:
                    print("Not prime ")
                    break
                 i=i+1
              else:
                 print(n," is Prime number ")

       case 2:
           n=int(input("Entr numbr :"))
           n=abs(n)
           temp = n
           rev=0
           while n>0:
              d=n%10
              n=n//10
              rev =rev*10+d
           if rev==temp:
              print(temp," is Palindrome number")
           else:
              print(temp," is Not palindrome number")
       case 3:
           n=int(input("Entr numbr :"))
           n=abs(n)
           temp = n
           rev=0
           while n>0:
              d=n%10
              n=n//10
              rev =rev*10+d
           print("reversed numbr :",rev)
       case 4:
           n=int(input("Enter number "))
           n=abs(n)
           l=len(str(n))
           print("Digit count :",l)
       case 5:
           print("Exiting the program")
           break              
       case _:
           print("invalid choice please try again :")
    print("Want to continue  1.yes/2.no")
    a = int(input("plase choice "))
    match a:
       case 1:
          continue
       case 2:
          print("Exiting...")
          break
       case _:
          print(" invalid input come again")
          break
print("Thanks ")
       
                 
