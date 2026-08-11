s=list(map(int,input("Enter lsit element :").split()))
print(s)
last=s.pop(-1)

s.insert(0,last)
print(s)