text=input("enter string")
seen=set()
repeating=set()

for char in text:
   if char in seen:
         repeating.add(char)
   else:
          seen.add(char)

for char in text:
     if char in seen and char not in repeating:
           print("first non rep",char)
           break
else:
     print("NO non rep characters")