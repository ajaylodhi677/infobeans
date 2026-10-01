#from patient.patient import addpatient,display,search
#from doctor.doctor_module import adddoc,displaydoc
#from appointment.appoint_module import book_appoinment,show_appointments
#from billing.billing_module import generate_bill
from patient import addpatient,display,search
from doctor import adddoc,displaydoc
from appointment import book_appoinment,show_appointments
from billing import generate_bill
patient=[] 
doctor=[] 
appoinment=[]
bill=[]
while True:
   print("""========== Hospital Management System ==========
   1. Add Patient
   2. Display Patients
   3. Search Patient
   4. Add Doctor
   5. Display Doctors
   6. Book Appointment
   7. Show Appointments
   8. Generate Bill
   9. Exit
   """)
   choice = int(input("Enter your choice:"))
   match choice :
       case 1:
        addpatient(patient)  
        print("Patient added successfuly\n")
       case 2: 
        print("Display patient dettails")    
        display(patient)
       case 3:
        id=int(input("Enter patinet id:"))
        search(id,patient)
       case 4:
        adddoc(doctor)
        print("Doctor added succesfully") 
       case 5:
        print("Dispaly available doctors") 
        displaydoc(doctor)
       case 6:
        book_appoinment(appoinment)
        print("Appointment booked succesfully")
       case 7:
        show_appointments(appoinment)
        print("Appointment list")
       case 8:
        generate_bill(bill,patient)
       case 9:
         break    