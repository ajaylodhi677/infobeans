#billing system for electricity department

unit = int(input("Enter units"))

if unit<=100:
    print("bill :",unit*5)
elif unit>100 and unit<=200:
    bill = (unit-100)*7+100*5
    print(" bill:",bill)
elif unit>200 :
    bill=(unit-200)*10+(100*7)+(100*5)
    print("bill :",bill)	
    