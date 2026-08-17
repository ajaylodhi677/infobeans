""" Project 2
hospital management system"""
#========================= menu ===========================
import random
print("====================================")
print("\tHOSPITAL MANAGEMENT SYSTEM")
print("====================================")
count=0
pid=0
pname =""
gen=""
page=0
fees =0
appoint=0
health=0
df=0
tf=0
gb=0
while True:
   print("Welcome to online hospital services portal ")
   print("1. New Patient Registration")
   print("2. Doctor Appointment")
   print("3. Health Checkup")
   print("4. Final Hospital Bill")
   print("5. About Hospital")
   print("6. Exit")

   choice = input("Enter your choice : ")

   if choice == "":
     print("Please enter your choice.")
     continue

   choice = int(choice)
#==================================patient registration ===================   
   match choice :
      case 1 :
        if count ==1 :
         print("Already registered please user other services :\n")
         print("=================================================")
         continue 
        else : 
           print("=================================================")
           print("\tNew patient registration page")
           print("==========================================\n")
           print("Please fill the details")
           
           while True:
              pname=input("Enter patient Name :")
              if len(pname)>=2:
                 pname=pname
                 break
              else:
                 print(" enter valid name") 
                 continue
           page =int(input("Enter patient age :"))
           while True :
              gen=input("Enter gender :").lower()
              if gen=="male" or gen=="female" or gen=="m" or gen=="f":
                  gen=gen
                  break
              else:
                 print(" Please valid input ")
                 
           print("--------------------------------------------------------")
           print("Registation succecfully ")
           pid=random.randint(100,999)
           print("Patiendt id :",pid,"\n")
           print("--------------------------------------------------------")
           count=1
           continue
#======================================Appointment========================         
      case 2 :
         if count!=1:
            print("--------------------------------------------------------")
            print("Registation is required to book appoitment \n")
            print("--------------------------------------------------------")

            continue
         elif appoint==1:
            print(" already book appointment \n you can go for health checkup\n")
            print("--------------------------------------------------------")
            continue
         else:
            appoint=1   
            print("====================================")
            print("\tDOCTOR APPOINTMENT")
            print("====================================")
            print("Choose Department")
            print("1. General Physician")
            print("2. Orthopedic")
            print("3. Eye Specialist")
            print("4. Dentist")
            while True :
               choice=int(input("Choose department :"))
               if choice<1 or choice>4 :
                  print("Invalid selection : \n")
                  continue
               else :
                  break
            match choice :
               case 1 :
                  print("\nAvailable doctors")
                  a="Dr ashish mehra (mbbs)"
                  b="Dr kabir khan(Md,Mbbs)"
                  print("1.",a)
                  print("2.",b)
                  while True :
                     c=int(input("Choose doctors :"))
                     if c!=1 and c!=2 :
                        print("Invalid selection : \n")
                        continue
                     else :
                        break
                  match c :
                     case 1 :
                        fees =fees+500
                        print("------------------------------------------")
                        print("Appointment Confirmed :\n")
                        print("Doctor :",a)
                        print("Fee : ",fees)
                        print("------------------------------------------")
                        df=df+500
                     case 2 :
                        fees =fees+1000
                        print("------------------------------------------")
                        print("Appointment Confirmed :\n")
                        print("Doctor :",b)
                        print("Fee : ",fees)  
                        print("------------------------------------------")
                        df=df+1000
               case 2 :
                  
                  print("\nAvailable doctors")
                  a="Dr sharma(specialst surgen)"
                  b="Dr hasina malik(orthoprdits) "
                  print("1.",a)
                  print("2.",b)
                  while True :
                     c=int(input("Choose doctors :"))
                     if c!=1 and c!=2 :
                        print("Invalid selection : \n")
                        continue
                     else :
                        break
                  #c=int(input("Choose doctors :"))
                  match c :
                     case 1 :
                        fees =fees+500
                        print("------------------------------------------")
                        print("Appointment Confirmed :\n")
                        print("Doctor :",a)
                        print("Fee : ",fees)
                        print("------------------------------------------")
                        df=df+500
                     case 2 :
                        fees =fees+1000
                        print("------------------------------------------")
                        print("Appointment Confirmed :\n")
                        print("Doctor :",b)
                        print("Fee : ",fees)
                        print("------------------------------------------")
                        df=df+1000
               case 3 :
                  
                  print("\nAvailable doctors")
                  a="Dr ayush(Mbbs)"
                  b="Dr payal sinha(Md) "
                  print("1.",a)
                  print("2.",b)
                  while True :
                     c=int(input("Choose doctors :"))
                     if c!=1 and c!=2 :
                        print("Invalid selection : \n")
                        continue
                     else :
                        break
                  #c=int(input("Choose doctors :"))
                  match c :
                     case 1 :
                        fees =fees+500
                        print("------------------------------------------")
                        print("Appointment Confirmed :\n")
                        print("Doctor :",a)
                        print("Fee : ",fees)
                        print("------------------------------------------")
                        df=df+500
                     case 2 :
                        fees =fees+1000
                        print("------------------------------------------")
                        print("Appointment Confirmed :\n")
                        print("Doctor :",b)
                        print("Fee : ",fees) 
                        print("------------------------------------------")
                        df=df+1000
               case 4 :
                  
                  print("\nAvailable doctors")
                  a="Dr akansha(Md)"
                  b="Dr kiara mittal(Mbbs) "
                  print("1.",a)
                  print("2.",b)
                  while True :
                     c=int(input("Choose doctors :"))
                     if c!=1 and c!=2 :
                        print("Invalid selection : \n")
                        continue
                     else :
                        break
                  #c=int(input("Choose doctors :"))
                  match c :
                     case 1 :
                        fees =fees+500
                        print("------------------------------------------")
                        print("Appointment Confirmed :\n")
                        print("Doctor :",a)
                        print("Fee : ",fees)
                        print("------------------------------------------")
                        df=df+500
                     case 2 :
                        fees =fees+1000
                        print("------------------------------------------")
                        print("Appointment Confirmed :\n")
                        print("Doctor :",b)
                        print("Fee : ",fees)
                        print("------------------------------------------")
                        df=df+1000
            print("--------------------------------------------------------")
            print("\nGo for health checkup up  \nOr collect bill from bill section:")
            print("--------------------------------------------------------")

            continue         
#==========================health checkup===================================      
      case 3 :
         if count!=1:
            print("--------------------------------------------------------")
            print("Registation is required to health checkup \n")
            print("--------------------------------------------------------")

            continue
         elif health==1:
            print(" already booked \n you can go for doctor appointment or ither services")
         else:
            health=1
            sc=0
            bc=0
            xc=0
            ec=0
            while True :
               print("====================================")
               print("\tHEALTH CHECKUP")
               print("====================================")
               print("1. Blood Test")
               print("2. Sugar Test")
               print("3. X-Ray")
               print("4. ECG")
               sle =int(input(" select test you want :"))
               
               match sle :
                  case 1 :
                     if bc ==1 :
                        print(" Blood test already added \n")
                     else :   
                        bc=1
                        bf=300
                        tf=tf+bf
                        fees=fees+bf
                        print("Blood test selected :\n")
   
                        print("Fee =",bf)
                        print("Total Fees :",tf)
                        print("\nTest Booked Succesfully\n")
                  case 2 :
                     if sc ==1 :
                        print(" sugar test already added \n")
                     else:   
                        sc=1
                        sf=500
                        tf=tf+sf
                        fees=fees+sf
                        print("Sugar  test selected :\n")
   
                        print("Fee =",sf)
                        print("Total Fees :",tf)
                        print("\nTest Booked Succesfully\n")
                  case 3 :
                     if xc ==1 :
                        print(" Xray  already added \n")
                     else:   
                        xc=1
                        xf=1000
                        tf=tf+xf
                        fees=fees+xf
                        print("Xray  test selected :\n")
   
                        print("Fee =",xf)
                        print("Total Fees :",tf)
                        print("\nTest Booked Succesfully\n")
                  case 4 :
                     if ec ==1 :
                        print(" Egc test already added \n")
                     else:   
                        ec=1
                        ef=700
                        tf=tf+ef
                        fees=fees+ef
                        print("ECG  test selected :\n")
   
                        print("Fee =",ef)
                        print("Total Fees :",tf)
                        print("\nTest Booked Succesfully\n")
                  case _ :
                     print("Invalid input ")   
               print("Wnat to add another test :")    
               print("   +------------+\t+-----------+")
               print("   | 1. Yes     |\t| 2.No      |")
               print("   +------------+\t+-----------+")
            
               c=int(input("Enter your choice :"))
               print()
               if c==1:
                  continue
               elif c==2 :
                  break
               else:
                print("Invalid input")
                break 
            print("========================================================")
            print("health checkup request  successfully captured")
            print("please submit your Diagonistics room\n\n")
            print("========================================================")
         print("\nPlease collect your bill form bill section ") 
         print("========================================================")
         continue
#================================final bill=============================
      case 4 :
         if count!=1 :
            print("========================================================")
            print(" Not registered yet ! \n Please make registered first\n")
            print("========================================================")

            continue
         elif fees==0 :
            print("====================================")
            print("No service availed yet \n") 
            print("====================================")

            continue 
         else : 
            gb=1   
            print("====================================|")
            print("\tFinal Bill       ")
            print("====================================|\n\n")
            print(" Patient Name :",pname,"            |")
            print(" Patient Id   :",pid,"              ")
            print(" Age          :",page,"             ")
            print(" gender       :",gen)
            print("\n\n")
            print("------------------------------------|")
            print(" Doctor Fee     : ",df,"            ")
            print(" test charges   :",tf,"             ")
            print("\n\n")
            print("------------------------------------|")
            print("Total Amount    :",fees)
            print("\n")
            print("====================================|")
            print("Thank you!                          |")
            print("Get well soon                       |")
            print("====================================|")
#=============================about project================            

      case 5 :
         print("====================================")
         print("\tABOUT HOSPITAL")
         print("====================================")
         print("Hospital Name : City Care Hospital")
         print("Project Name  : Hospital Management System")
         print("Developed By  : Ajay Lodhi")
         print("Language      : Python")
         print()
         print("Concepts Used :")
         print("- if-else")
         print("- Nested if-else")
         print("- match-case")
         print("- Nested match-case")
         print("- while loop")
         print("- for loop")
         print("- break")
         print("- continue")
         print()
         print("Version : 1.0")
         print("====================================")
         print("Thank You!")
         print("====================================")
#==================break ==============================         
      case 6 :
         if appoint==1 or health==1:
            if gb==0:
               print("please generate bill first in bill section")
               print("="*25)
               continue
            else:
               #print("uper")
               break 
         else: 
             #print("neeche")    
             break
      case _ :
        print(" Invalid choice please read carefully")
        continue
   print(" Want to use other services ")
   print("   +------------+\t+-----------+")
   print("   | 1. Yes     |\t| 2.No      |")
   print("   +------------+\t+-----------+")

   c=int(input("Enter your choice :"))
   print()
   if c==1:
      continue
   elif c==2 :
      break
   else:
    print("Invalid input")
    break  
print("Thanks for using online portal of hospital ")           