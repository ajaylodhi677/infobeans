"""4.Unique Digit Security Scanner


A smart locker accepts only numbers whose all digits are unique.


Write a program using for-else loop to:


- Check every digit

- If any repeated digit found reject

- Else accept


Input:

57294


Output:

Valid Unique Code"""

n= int(input("Enter number :"))
count=0
for i in range(len(str(n))):
     d=n%10
     temp=n//10
     n=n//10
     for i in range(len(str(temp))):
         e=temp%10
         if d==e:
            print("Reject")
            count=count+1
            break
         temp=temp//10
     if count==1:
        break     

else:
    print("accept")

