"""
5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website"""

n=input("Enter website :").lower()
if " " in n or n[0]!="w" or n[1]!="w" or n[2]!="w" or n[3]!="." or n[-4]!="." or n[-3]!="c" or n[-2]!="o" or n[-1]!="m":
    print(" not valid website")
else:
   print("Valid website")

