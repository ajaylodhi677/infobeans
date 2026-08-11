"""
66Count number of sentences in a paragraph. 
P = "This. Is. Test." 3
"""
s=input("Enter the string :").split()
count=0
for x in s:
    if x.endswith("."):
        count+=1
print(count)

 

