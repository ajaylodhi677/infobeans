"""
13Get the Unicode code point before index. 
S = "Hello", 
Index = 1 
72 (Unicode for 'H')"""

s=input("Enter String :")
index=int(input("Enter index :"))
print(ord(s[index-1]),"index of ",s[index-1])