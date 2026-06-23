value = int(input("Enter cart value"))
type=input("Enter user type premium/regular").lower()

if value>=5000:
    if type=='premium':
       value =value*0.80
       print("final amount :",value)
    else:
       value = value*0.90
       print("final amount :",value)
else:
    if value>=2000:
       value =value*0.95
       print("final amount :",value)
    else:
       print("No discount is applied")