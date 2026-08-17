income = int(input("Enter your income"))

if income<=250000:
    print(" not payble to tax")
elif income>25000 and income<=500000:
    tax = (income-250000)*0.05
    print("tax :",tax)
elif income>500000 and income<1000000:
    tax = (income-500000)*0.20+(250000*0.05)
    print("tax :",tax)
else:
    tax =(income-1000000)*0.30+(500000*0.20)+(250000*0.05)
    print("tax :",tax)