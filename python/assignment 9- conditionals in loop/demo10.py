"""3. Smart Scholarship Allocation System

A scholarship is provided based on marks, family income, and category.

If marks are 85 or above, then check income. If income is less than or equal to 300000, then check category. If category is not general, give Full Scholarship; otherwise give 75% Scholarship. If income is above 300000, give 50% Scholarship.

If marks are between 70 and 84, then check income. If income is less than or equal to 200000, give 50% Scholarship; otherwise give 25% Scholarship.

If marks are below 70, no scholarship is given.

Input:
Marks = 88
Income = 250000
Category = OBC

Output:
Scholarship = Full Scholarship"""

marks =int(input("marks :"))
income=int(input("income annual :"))
cate =input("cateagory :").lower()

if marks>=85:
    if income<300000:
       if cate!='general':
          print("Scholarship : Full scholarship")
       else:
          print("Scholarship : 75% scholarship")
    else:
       print("Scholarship : 50% scholarship")
elif marks>=70:
    if income<=200000:
       print("Scholarship : 50% scholarship")
    else:
       print("Scholarship : 25% scholarship")
else:
    print("no scholarship given")