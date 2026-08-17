""" ATM Note Counter


A bank ATM dispenses ₹100 notes.


Write a program to:


- Read withdrawal amount

- Count how many ₹100 notes needed using loop


Input:

700


Output:

Notes = 7"""

n=int(input("Enter number value in multiole of 100 :"))
if n<100:
    print("only hundred notes availabele")
else:
    d=n//100
    print("Notes :"d)
