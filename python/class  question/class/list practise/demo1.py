""" list practise :"""
size=int(input("Enter size of list :"))
nums=[]

for i in range(size):
    print("Which type of data you want to enterc :\n1.for int\n2.for float\n3.complex\n4.for string :\n5.fir boolean")
    choice=int(input("Enter choice :"))
    match choice :
       case 1 :
          x=int(input("Enter numbers :"))
          nums.append(x) 
       case 2 :
          x=float(input("Enter float :"))
          nums.append(x)
       case 3 :
          x=complex(input("Enter cmplex :"))
          nums.append(x)                   
       case 4 :
          x=(input("Enter string :"))
          nums.append(x)
       case 5 :
          x=bool(input("Enter blloen :"))
          nums.append(x)
       case _ :
          nums.append("Invalid choice")
       
print(nums)