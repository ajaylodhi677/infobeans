"""8. E-Commerce Dynamic Pricing System

An e-commerce system gives discount based on demand, stock, user type, and festival.

If demand is 80 or above, then check stock. If stock is less than 50, then check user type. If user is premium, then check festival. If festival is yes, give 20% discount; otherwise 10%. If user is not premium, no discount. If stock is 50 or more, give 5% discount.

If demand is between 40 and 79, then check festival. If yes, give 10% discount; otherwise no discount.

If demand is below 40, then check stock. If stock is greater than 200, give 15% discount; otherwise no discount.

Input:
Demand = 85
Stock = 40
User Type = premium
Festival = yes

Output:
Discount = 20%"""

demand =int(input("Demand :"))
stock =int(input("stock :"))
user =input("User type premium/regular :").lower()
festival =input("Festival :").lower()

if demand>=80:
    if stock<50:
       if user=='premium':
          if festival=='yes':
             print(" 20% discont")
          else:
             print(" 10% discont")
       else:
          print(" no discont")
    else:
       print(" 5% discont")
elif demand>40 and demand<80:
    if festival=='yes':
       print(" 10% discont")
    else:
       print(" NO discont")
elif stock>200:
    print(" 15% discont")
else:
    print("  no discont")  
  