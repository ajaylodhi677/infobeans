"""
    5
   44
  333
 2222
11111

"""
n=int(input("Enter number of lines :"))

i=n
while i>=1:
     sp=n
     while sp>n-(i-1):
        print("*",end="")
        sp=sp-1
     j=n
     while j>=i:
        print(i,end="")
        j=j-1
     i=i-1
     print() 
