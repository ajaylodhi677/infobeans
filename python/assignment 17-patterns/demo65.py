"""
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1




n=int(input("Enter number of lines :"))
i=1
while i<=n:
     sp=n
     while sp>i:
        print(" ",end="")
        sp=sp-1
     j=1
     while j<=i:
        if j==1 or j==i :
           print(1,end=" ")
        elif i==n and j==n//2+1:
           print(n+1,end=" ")
        else:
           print((i-1),end=" ")
        j=j+1
     i=i+1
     print() """
n=int(input("Enter number of lines :"))
i=1
while i<=n:
     sp=n
     while sp>i:
        print(" ",end="")
        sp=sp-1
     rev=0
     if i<=1 :
        pass
     else:
        a=11**(i-1)
        while a>0:
           d=a%10
           rev=rev*10+d
           a=a//10
           #print(d,end=" ")    
     if i<=1 :
        print(i,end=" ")
     else:
        b=rev
        while b>0:
           e=b%10
           b=b//10
           print(e,end=" ")      
     i=i+1
     print()

