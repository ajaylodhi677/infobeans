amount = int(input(" Enter ampunt to distribute"))

t =amount//100
rem = amount%100
f = rem//50
rem = rem%50
ten = rem//10

print("100x",t)
print("50X",f)
print("10X",ten)