"""4. Gym Membership Eligibility Checker
   A gym checks multiple conditions:

* If age ≥ 18 → Allowed for gym
* If BMI > 25 → Suggest weight loss program

Input:
Enter age: 25
Enter BMI: 27

Output:
Gym access granted
Enroll in weight loss program"""

age ,BMI = map(int,input("Enter age and BMI respectively").split())

if age>=18:
    if BMI>25:
       print("Gym acces granted\nEnroll in weight loss prigram")
    else:
       print("Gym access granted")
else:
   print("Not allowed in gym...")