# Time duration adder
h , m ,s = map(int,input(" enter hours minutes and seconds respectively ").split())

h = h*3600
m =m*60

total = h+m+s
print("total seconds",total)