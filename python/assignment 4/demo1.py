# Restraurant Bill split 
 
total= int(input("enter total amount"))
gst,service,nof = map(int, input("please enter gst% , service charge and no. of friends respectively").split())

gst =(total/100)*gst
service = (total/100)*service

total = total+gst+service

split = total/nof

print("total bill amount :",total,"\n Each person have to pay ",split)