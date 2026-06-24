#cinema ticket booking
age = int(input("Enter your age"))

if age<12:
    print("ticket price :100")
elif age>12 and age<60:
    print("ticket price :200")
else:
    print("ticket price :150")