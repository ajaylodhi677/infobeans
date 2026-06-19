seconds =int(input("Enter seconds"))

hours =seconds//3600
rem = seconds%3600
minutes = rem//60
rem = rem%60

print(hours, ":hours", minutes,": minutes",rem,":seconds")