""" Perfect number """
def perfect(num):
   sum=0
   for i in range(1,num//2+1):
      if num%i==0:
           sum+=i
   if sum==num:
      return "perfect number:"
   else:
      return "not a perfect number"
#==============================================
"""palindrome number"""
def palindrome(num):
   if num==int(str(num)[::-1]):
      return "palindrome number"
   else:
      return "non palindrome"
#===============================================
""" Strong knumber"""
def strong(num):
   org=num
   sum=0
   while num>0:
      d=num%10
      fact=1
      for i in range(1,d+1):
          fact=fact*i
      sum+=fact
      num=num//10
   if sum==org:
      return "Strong number"
   else:
      return "Not strong number"
#====================================
"""armsatrong number"""
def armstrong(num):
   org=num
   sum=0
   l=len(str(org))
   while num>0:
      d=num%10
      sum+=d**l
      num=num//10
   if sum==org:
      return "Armstrong number"
   else:
      return "Not Armstrong number"
#========================================
""" prime number"""
def prime(num):
    if num<2:
       return "Not prime" 
    else:
      i=2
      while i<=num//2:
         if num%i==0:
            return "not prime"
         i+=1
      else:
         return "Prime number" 
#========================================
"""even and odd"""
def evenodd(num):
    if num%2==0:
           return "Even"
    else:
       return "Odd"
while True:
  print("""
========================================
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
  match choice :
    case 1:
      print(perfect(int(input("Enter number:"))))
    case 2:
      print(palindrome(int(input("Enter number"))))
    case 3:
      print(strong(int(input("Enter number"))))
    case 4:
      print(armstrong(int(input("Enter number"))))
    case 5:
      print(prime(int(input("Enter number"))))
    case 6:
      print(evenodd(int(input("Enter number:"))))
    case 15:
      break
print("Thanks for using system")