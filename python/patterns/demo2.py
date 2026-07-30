""" WAP to print squre cube and squre root from 1 to n"""
import math

n=int(input("Enter number "))

i=1
print(" num \tsquare \t squre root \t cube")
while i<=n:
#for i in range(1,n+1):
    print(i,"\t",i*i,"\t",round(math.sqrt(i), 2),"\t\t",i*i*i)
    i=i+1

   
