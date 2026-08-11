"""
115Find the edit distance (Levenshtein distance) between two strings. 
S1 = "kitten", 
S2 = "sitting" 3"""
s=input("Enteer string 1 :")
s1=input("Enter string 2 :")

i = 0
count = 0
while i <len(s) and i < len(s1):
	if s[i] != s1[i]:
		count+=1
	i+=1
ans = abs(len(s)-len(s1)) + count
print(ans)
