"""
5.
 Student Grade Classification System (Python List Assignment)


A school stores student marks in a list. The system must analyze the marks and generate a *clear performance report*
by grouping students into grade categories.



Write a Python program to:

* Iterate through the list of marks
* Assign grades based on marks:

  * *>= 90 → A*
  * *>= 75 and < 90 → B*
  * *>= 50 and < 75 → C*
  * *< 50 → Fail*
* Store each category in separate lists
* Count students in each category
* Display a *final structured report (important)*

---

## 📌 Output Format (Mandatory)

Your output must be displayed exactly in this format:


===== STUDENT GRADE REPORT =====

A Grade Students   : [list]
B Grade Students   : [list]
C Grade Students   : [list]
Fail Students      : [list]

--------------------------------
A Count   : X
B Count   : X
C Count   : X
Fail Count: X
--------------------------------

Total Students: X


---

 Input

[95, 82, 67, 45, 30]

Output


===== STUDENT GRADE REPORT =====

A Grade Students   : [95]
B Grade Students   : [82]
C Grade Students   : [67]
Fail Students      : [45, 30]

--------------------------------
A Count   : 1
B Count   : 1
C Count   : 1
Fail Count: 2
--------------------------------

Total Students: 5"""
s=list(map(int,input("Enter marks of a students out of 100 :").split()))
al=[]
bl=[]
cl=[]
fl=[]
ac=0
bc=0
cc=0
fc=0
for ch in s:
    if ch>=90:
      al.append(ch)
      ac+=1
    elif ch>=75 and ch<90:
      bl.append(ch)
      bc+=1
    elif ch>=50 and ch<75:
      cl.append(ch)
      cc+=1
    else:
      fl.append(ch)
      fc+=1
print("====== Stundet Grade Report ======")
print("A grade studens :",al)
print("B grade studens :",bl)
print("C grade studens :",cl)
print("fail studens :",fl,"\n")
print("-"*30)
print("A count :",ac)
print("B count :",bc)
print("C count :",cc)
print("fail count :",fc)
print("-"*30)
print("total students :",len(s))

