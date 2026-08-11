"""
6.

A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0"""
s=list(map(int,input("Enter  list element :").split()))
prime=[]
for x in s:
   if x<2:
     pass
   else:
      i=2
      while i<=x//2:
         if x%i==0:
            break
         i=i+1
      else:
         prime.append(x)

print("Prime IDs =",prime)
if len(prime)==0:
   print("max = -1")
else:
   print("Max =",max(prime))
print("sum =",sum(prime))
print("total prime =",len(prime))