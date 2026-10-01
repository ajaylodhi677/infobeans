"""
1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.

The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:

Key → Patient ID
Value → Dictionary containing patient details

Each patient record should contain:

Patient Name
Age
Gender
Disease
Doctor Name
Sample Data Structure
{
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit

Functional Requirements
1. Add New Patient

Accept the following information from the user:

Patient ID
Patient Name
Age
Gender
Disease
Doctor Name

Store the record in the nested dictionary.

Validation:
If the Patient ID already exists, display:

Patient ID already exists.

2. Search Patient

Accept Patient ID from the user.

If the patient exists, display complete information.

Sample Output

Patient ID : 101
Name       : Ajay
Age        : 35
Gender     : Male
Disease    : Fever
Doctor     : Dr. Sharma

If Patient ID is not found:

Patient Record Not Found

3. Update Patient Disease

Accept Patient ID.

If found:

Ask for new disease.
Update the disease information.

Sample Output

Disease Updated Successfully
4. Delete Patient Record

Accept Patient ID.

If found:

Remove the patient record.

Sample Output

Patient Record Deleted Successfully

Otherwise:

Patient Not Found
5. Display All Patients

Display all patient records in a formatted manner.

Sample Output

--------------------------------
Patient ID : 101
Name       : Ajay
Age        : 35
Disease    : Fever
Doctor     : Dr. Sharma
--------------------------------

Patient ID : 102
Name       : Ravi
Age        : 42
Disease    : Diabetes
Doctor     : Dr. Gupta
6. Count Total Patients

Display the total number of patients currently stored.

Sample Output

Total Patients : 25
7. Display Patients By Disease

Accept a disease name from the user.

Display all patients suffering from that disease.

Sample Output

Enter Disease : Fever

101  Ajay
108  Aman
115  Neha

If no patient is found:

No Patient Found
8. Display Oldest Patient

Find and display the patient having the highest age.

Sample Output

Oldest Patient Details

Patient ID : 110
Name       : Ravi
Age        : 68
Disease    : Diabetes
Doctor     : Dr. Gupta
9. Display Youngest Patient

Find and display the patient having the minimum age.

Sample Output

Youngest Patient Details

Patient ID : 121
Name       : Riya
Age        : 4
Disease    : Viral Fever
Doctor     : Dr. Mehta
10. Exit

Terminate the application.

Sample Output

Thank You For Using Hospital Patient Management System
"""
patient={
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}

while True:
  print("=="*20)
  print("HOSPITAL PATIENT MANAGEMENT SYSTEM")
  print("=="*20)
  print("1. Add New Patient")
  print("2. Search patient")
  print("3. Update Patient Disease")
  print("4. Delete Patient Record")
  print("5. Display All Patients")
  print("6. Count Total Patients")
  print("7. Display Patients By Disease")
  print("8. Display Oldest Patient")
  print("9. Display Youngest Patient")
  print("10. Exit")
  print("\nEnter your choice")
  choice=int(input())
  match choice :
      case 1 :
         id=int(input("Enter id of new patient:"))
         if id not in patient:
           name=input("Enter name :")
           age=int(input("Enter age :"))
           gender=input("Enter gender:")
           disease=input("Enter disease :")
           doctor=input("Enter doctor name :")
           patient[id]={"name":name,"age":age,"gender":gender,"disease":disease,"doctor":doctor}
           print("patient details added succesfully ")
         else:
           print("pateient already exist :")
      case 2 :
         x=int(input("Enter user id of the user :"))
         if x in patient:
            details=patient[x]
            for k,v in details.items():
                print(k,":",v) 
         else:
            print("Id not found :")  
      case 3 :
         id=int(input("Enter patient id :"))
         if id in patient:
            print("old disease :",patient[id]["disease"])
            newdisease=input("Enter new diesease :")
            patient[id]["disease"]=newdisease   
            print("disease updated succesfully")
         else:
            print("patient id not found :")  
      case 4 :
         id=int(input("Enter patient id :"))
         if id in patient: 
             del patient[id]
             print("Patient record deleted successfully")
         else:
           print("Id not found")
      case 5 :
         print("patient details ")
         for id,details in patient.items():
             print("---"*8)
             print("Patient Id :",id)
             for k,v in details.items():
                 print(k.ljust(10),":",v)
      case 6 :
         print("Total patient :",len(patient))
      case 7 :
         x=input("Enter disease :")
         c=0
         for id,details in patient.items():
              if details["disease"]==x:
                    c=1
                    print(id," ",patient[id]["name"])
         if c==0:
           print("No patiend found for this disease") 
      case 8 :
           max=0
           d=0
           for id,details in patient.items():
                if details["age"]>max:
                    max=details["age"]
                    d=id
           print("Oldest patient in hospital")
           print("Patient id:",d)
           for k,v in patient[d].items():
                 print(k.ljust(10),":",v)
      case 9 :
           
           min=float('inf')
           d=0
           for id,details in patient.items():
                if details["age"]<min:
                    min=details["age"]
                    d=id
           print("Youngest patient in hospital")
           print("Patient id:",d)
           for k,v in patient[d].items():
                 print(k.ljust(10),":",v)
      
      case 10:
          break
print("Thanks for using hospital management")
  