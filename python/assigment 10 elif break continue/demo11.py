""" automorphic number

n=int(input("Enter number"))
s=n*n

for i in range(len(str(n))):
    d= n%10
    e= s%10
    n=n//10
    s=s//10
    if d!=e:
       print("not autoumorphic ")
       break
else:
    print("automorphic number")"""

n = int(input("Enter number :"))

for i in range(len(str(n))):
    d=n%10
    n=n//10
    if d==0:
       print("duck number")
       break
else:
    print("not duck number")
       