"""
29Remove occurrences of a word.
 S = "a test b test c", 
Word = "test", Remove All 
"a b c" """
s=input("Enter String :").split()
word=input("Enter word :")
s1=""
for x in s:
    if x!=word:
      s1=s1+x+" "
print(s1)
