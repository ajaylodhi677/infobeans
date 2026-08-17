#insurance claim approval system

page = int(input("Enter policy age"))
camount = int(input("Enter claim amount"))
type = input("Enter accidident type").lower()


if page>=2:
    if camount<=50000:
       if type=='minor':
          print("Approve the claim")
       else:
          print("Approve with inspection")
    elif camount<200000:
       if type=='major':
          print("Approve with investigation")
       else:
          print("Reject")
    else:
       print("reject")
elif type=='minor':
    print("reject")
else:
    print("mark as review")
    
     
 
    
