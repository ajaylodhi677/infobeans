"""
10.

=========================================
EMAIL DOMAIN COUNTER
====================

emails = [
"[ajay@gmail.com](mailto:ajay@gmail.com)",
"[ravi@yahoo.com](mailto:ravi@yahoo.com)",
"[neha@gmail.com](mailto:neha@gmail.com)",
"[aman@outlook.com](mailto:aman@outlook.com)",
"[abc@gmail.com](mailto:abc@gmail.com)"
]

Write a program to:

* Count users belonging to each email domain.

Sample Output:
{
'gmail.com':3,
'yahoo.com':1,
'outlook.com':1
}

"""
s=input("Enter gmail id :").split()
d={}
for x in s:
    i=x.index("@")
    cut=x[i+1:]
    d[cut]=d.get(cut,0)+1
for k,v in d.items():
    print(k,":",v)