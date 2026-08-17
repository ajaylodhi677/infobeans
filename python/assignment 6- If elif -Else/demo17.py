"""
2. University Admission System

A university decides admission based on marks, entrance score, and category of the student.

If marks are 70 or above, then check entrance score. If entrance score is 80 or above, then check category. If general, admit; otherwise admit with scholarship. If entrance score is less than 80, then check if marks are 85 or above. If yes, admit under management quota; otherwise reject. If marks are below 70, then check if category is not general and marks are at least 60. If yes, check entrance score. If it is 70 or above, waitlist; otherwise reject. If none of these conditions match, reject.

Input:
Marks = 72
Entrance Score = 85
Category = general

Output:
Admission Status = Admitted"""


marks=int(input("Enter marks"))
ent =int(input("enter entrance marks"))
cate =input("Enter your categray").lower()

if marks>=70:
    if ent>=80:
       if cate=='general':
          print("Admitted")
       else:
          print("Admit with scholarship")
    elif marks>=85:
       print("admit under management quota")
    else:
       print("reject")
elif cate!='general' and marks>=60:
    if ent>=70:
       print("waitlist")
    else:
       print("reject")
else:
    print("reject")
