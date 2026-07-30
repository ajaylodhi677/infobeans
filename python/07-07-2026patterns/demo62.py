"""
    1
   123
  12345
 1234567
123456789



"""
n=int(input("Enter number of lines :"))
i=1
while i<=n:
     sp=n
     while sp>i:
        print(" ",end="")
        sp=sp-1
     j=1
     while j<=(2*i)-1:
        print(j,end="")
        j=j+1
     i=i+1
     print() 

