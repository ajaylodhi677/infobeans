# mobile EMI 

price= int(input("Enter price of the mobile"))
down= int(input(" what is the amount yor make for downpayment"))
rate = int(input("Enter rate of interst"))
months= int(input("enter no of months"))

remain = price-down
inst = remain/100*10
print("Remaining amount :",remain)
print("total with interst: ",int(remain+inst))
print("Monthly Emi you have to pay ",(remain+inst)/months)
