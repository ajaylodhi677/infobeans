"""2. Hospital Emergency Priority System

A hospital assigns treatment priority based on age, severity, and insurance.

If severity is critical, then check age. If age is 60 or above, assign Immediate ICU; otherwise assign Emergency Ward.

If severity is moderate, then check insurance. If insured, assign Priority Treatment; otherwise assign General Queue.

If severity is low, then check age. If age is less than 10, assign Pediatric Priority; otherwise assign Wait.

Input:
Age = 65
Severity = critical
Insurance = yes

Output:
Treatment = Immediate ICU"""

age = int(input("Enter age :"))
severity=input("Severity :").lower()

if severity=='critical':
    if age>=60:
       print("Treatement : Immediate ICU")
    else:
       print("Treatement : emergency ward")
elif severity=='moderate':
    insurance=input("do you hava insurance :").lower()
    if insurance=='yes':
       print("Treatement : priority treatement")
    else:
        print("Treatement : General Queue")
elif age<10:
    print("Treatement : pediatric priority")
else:
     print("Treatement : wait")

    







