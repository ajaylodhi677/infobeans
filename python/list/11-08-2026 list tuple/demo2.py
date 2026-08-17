"""
2.
Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")
"""
n=int(input("Enter size of list :"))
password=[]
print("Enter paswords one by one")
for i in range(n):
     password.append(input())
print(password)
count=0
for i in range(n-1):
    ch=password[i]
    for j in range(i+1,n):
          rh=password[j]
          for x in ch:
              if x in rh:
                  break
          else:
             count+=1
print(count)             
       
   
      