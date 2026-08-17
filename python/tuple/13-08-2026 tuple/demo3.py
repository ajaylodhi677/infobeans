"""QUESTION 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

---

2. Display all patient details.

---

3. Display patients whose age is above 60 years.

---

4. Search for a patient using Patient ID.

---

5. Count the number of patients suffering from a particular disease.

---

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2

=====================================================================
"""
from collections import namedtuple
patient=namedtuple("patient",["id","name","age","disease"])
n=int(input("Enter number of patient :"))
pat=[]
for i in range(n):
    print("Enter details for patient :",i+1)
    id=input("Enter pariend id :")
    name=input("Enter patient name :")
    dis=input("Enter disease :")
    age =int(input("Enter age :"))
    pat.append(patient(id,name,age,dis))
print("==="*20)
print("showing details")
cfind=input("Which disease you want to filter  :").lower()
pid=input("enter patientd id to find patiend :")
age60=[]
pfound=[]
c=0
for x in pat:
    print(x.id,x.name,x.age,x.disease)
    if x.id==pid:
        pfound=x
    if x.age>60:
       age60.append(x)
    if (x.disease).lower()==cfind:
      c+=1
print("==="*20)
if len(pfound)>0:
    print("Patient founf :")
    print(pfound.id,pfound.name,pfound.age,pfound.disease)
else:
   print("Patiend not found with ;",pid)
print("==="*20)
print("patient above 60:")
for x in age60:
   print(x.id,x.name,x.age,x.disease)
print("==="*20)
print("patient wiht ",cfind)
print(c)

