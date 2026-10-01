from mypackage.perfect import Perfect

   print(
   """========================================
          NUMBER ANALYSIS SYSTEM
   ========================================
   
   1. Check Perfect Number
   2. Check Palindrome Number
   3. Check Strong Number
   4. Check Armstrong Number
   5. Check Prime Number
   6. Check Even or Odd
   7. Find Factorial
   8. Find Sum of Digits
   9. Reverse a Number
   10. Find Number of Digits
   11. Check Automorphic Number
   12. Check Neon Number
   13. Check Spy Number
   14. Check Harshad Number
   15. Exit    
   """)
   choice=int(input("Enter your choice:"))
   match choice:
       case 1:
           n=int(input("Enter number:"))
           print(Perfect(n))
       case 15:
           break
   print("Thanks you for using:")    