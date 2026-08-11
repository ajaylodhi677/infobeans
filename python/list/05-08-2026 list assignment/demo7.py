"""
7.
Factory Production – Factorial Expansion List

Problem Statement

A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even

Input:
A list of integers

Example 1

Input:
[3, 4, 5]

Processing:
3! = 6
4! = 24
5! = 120

Output:
[6, 24, 120]
Sum = 150
Max = 120
Even Count = 3"""
s=list(map(int,input("Enter list element :").split()))
factl=[]
fc=0
for x in s:
    i=1
    fact=1
    while i<=x:
       fact=fact*i
       i+=1
    if fact%2==0:
       fc+=1
    factl.append(fact)
print(factl)
print("sum =",sum(factl))
print("Max =",max(factl))
print("Even count =",fc)
    
