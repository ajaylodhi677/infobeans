"""10. Mobile Data Plan Advisor


A telecom company suggests the most suitable data plan based on a user’s daily data usage:

* More than 3GB/day → Premium Plan
* 1GB to 3GB/day → Standard Plan
* Less than 1GB/day → Basic Plan

Write a Python program to recommend a plan.

Input:
Enter daily data usage: 0.8

Output:
Recommended Plan: Basic Plan"""

use =float(input("Enter daily usages:"))

if use<1:
    print("recommended plan: Basic plan")
elif use>1 and use<=3:
    print("recommended plan: Standard plan")
else:
    print("recommended plan: Premium plan")

