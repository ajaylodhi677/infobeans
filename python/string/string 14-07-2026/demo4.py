"""
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID"""
n=input("Employee ID:")
#a=n[:3]
#print(n.startswith(a))
if n[0]!="E" or n[1]!="M" or n[2]!="P" or len(n)!=8:
    print("Invalid Employee Id")
else:
  i=3
  while i<len(n):
      ch=n[i]
      if ch not in "0123456789":
          print("Inalid Employee ID")
          break
      i=i+1
  else:
     print("Valid Employee ID ")