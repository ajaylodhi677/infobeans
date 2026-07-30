"""QNo 8:--
SMART TEXT PROCESSING SYSTEM

A software company is developing a Smart Text Processing System for
handling user messages. Different users require different text
transformations. To avoid creating separate applications, the company
wants a menu-driven program where users can select operations according
to their requirements.

The system should continue executing until the user selects Exit.

====================================================== MENU
======================================================

===== Smart Text Processing System =====

1.  Reverse Complete String
2.  Reverse Every Word
3.  Reverse Word Order
4.  Exit

====================================================== Choice 1 :

Conditions: - Reverse the complete string - Ignore extra spaces - Keep
special characters (@,#,$,%) in their original positions - Do not use
built-in reverse functions

Example: Input: ja@va#py

Output: yp@av#aj

Test Case 1: ab@cd#ef Output: fe@dc#ba

Test Case 2: py@th#on Output: no@ht#yp

Test Case 3: java@proOutput : orpa@vaj

====================================================== Choice 2 :

Conditions: - Reverse every word separately - Words containing digits
should not be reversed - Ignore extra spaces between words - First
letter of each reversed word should become uppercase

Example: Input: java is easy123 programming

Output: Avaj Si easy123 Gnimmargorp

Test Case 1: python full stack22 developer Output: Nohtyp Lluf stack22
Repoleved

Test Case 2: hello java99 world Output: Olleh java99 Dlrow

====================================================== Choice 3 :

Conditions: - Reverse order of words - Remove duplicate words - Ignore
case while checking duplicates - Keep only first occurrence

Example: Input: Java python Java react Python

Output: React Python Java

Test Case 1: HTML CSS HTML Java CSS Output: Java CSS HTML

Test Case 2: Python React Java Python React Output: Java React Python

====================================================== Choice 4
======================================================

Program Closed Successfully"""
while True:
   print("=" * 54)
   print("                     MENU")
   print("=" * 54)
   
   print("\n===== Smart Text Processing System =====\n")
   
   print("1. Reverse Complete String")
   print("2. Reverse Every Word")
   print("3. Reverse Word Order")
   print("4. Exit")
   
   choice=int(input("Enter your choice :")).replace(" ","")
   match choice:
      case 1 :
         n=input("Enter String ")
         s=""
         i=0
         p=len(n)-1
         while i<len(n):
            ch=n[i]
            if ch in "@#$%" :
               s=s+ch  
               p=p+1
            else:
               if n[p] in "@#$%":
                  p=p-1 
                  continue 
               else:
                  s=s+n[p]
            i=i+1
            p=p-1
         print(s)
      case 2 :
         s=input("Enter String :")
         word=s.split()
         result=""
         for w in word:
            if any(ch.isdigit() for ch in w):
                 result=result+w+" "
                #print(w,end=" ")
            else:
                 result=result+w[::-1].capitalize()+" "
                #print(w1.capitalize(),end=" ")
         print(result)
      case 3 :
         s=input("Enter string :")
         word=s.split()
         vis=""
         i=0
         while i<len(word):
           if word[i].lower()+" " not in vis:
              res= res+word[i]
              vis=vis+word[i].lower()+" "
           i=i+1
         res=" ".join(res.split()[::-1])
         print(res)
           
      case 4 :
         break
      case _ :
         print("invalid input")
   print("\nwant to continue or exit :")
   c=int(input("1.continue\n2.exit"))
   match c:
      case 1 :
         continue
      case 2 :
         break
      case _ :
         print("invalid choice ")      
print("thank you")