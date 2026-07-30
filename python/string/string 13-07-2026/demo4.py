"""
4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U """
count=0
n=input("Enter student name :").lower()
for ch in n:
   if ch not in "aeiou ":
      count=count+1
print("Total consonats :",count)
