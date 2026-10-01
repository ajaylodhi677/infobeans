"""Wap to sum of unlimited numbers"""
def add(*numbers):
      total=0
      for num in numbers:
          total+=num
      return total
i=1
numbers=[]
while i!=0:
     i=int(input("Enter number :"))
     if i!=0:
       numbers.append(i)
print(add(*numbers))