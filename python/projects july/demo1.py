""" project 1"""""
import random
print("=================================================================")
print("\t\t\t WELCOME TO GAMEZONE")
print("=================================================================")
i=1
while True:
    print("CHOOSE A GAME YOU WANT TO PLAY")
    print("1.Guess the number")
    print("2.Rock paper Scissors")
    print("3.Dice rolller")
    print("4.Password Generator")
    print("5.Luckey Wheel")
    print("6.About Project")
    print("7.Exit\n")
    i=i+1
    choice=int(input("Enter your choice :"))
    print()
    
    match choice:
#=================Guesss the number ======================
        case 1 :
            print("==============================================")
            print("Welcome to number guessing game ")
            print("Guess the number between 0 t0 100")
            num=random.randint(1,100)
            print("Start guessing number\n ")
            c=1
            while True:
                print("Attempt :",c)
                value=int(input("Enter Number :"))
                
                if value<0 or value>100:
                   print("please Enter number between 0 to 100")
                   continue
                elif num ==value:
                   print(" ===========================================")
                   print("|| Congratulations you won in" ,c,"Attempts   ||")
                   print("===========================================\n")
                   break
                elif num>value:
                   print("Number is Greater!\n")
                else:
                   print("Number is Smaller!\n")
                c=c+1
#===================Rock paper Scissor===================================
        case 2 :
            print("Welcome to rock paper and Scissor \nplayer I vs computer")
            print(" max in 5 are winner")
            print("1.Rock \n2.Paper \n3.Scissor")
            a=0  
            b=0 
            round =0
            while True:
              robo=random.randint(1,3)
              choice=int(input("your turn :"))
              print(" your choice-||-compuer choice:")
              if choice ==1 and robo==1:
                 print("----------------------------------------")
                 print(" rock\t<---vs-->\trock\n||Result :Tie\t||")
                 print("----------------------------------------")
                 round=round+1
              elif choice ==2 and robo==2:
                 print("----------------------------------------")
                 print(" paper\t<---vs-->\tpaper\n||Result :Tie\t||")
                 print("----------------------------------------")
                 round=round+1
              elif choice ==3 and robo==3:
                 print("----------------------------------------")
                 print(" Scissor<---vs-->Scissor\n||Result :Tie\t||")
                 print("----------------------------------------")
                 round=round+1
              elif choice ==1 and robo==2:
                 print("-----------------------------------------------")
                 print(" rock\t<---vs-->\tpaper\n||Result :You Lost\t||")
                 print("-----------------------------------------------")
                 round=round+1
                 b=b+1
              elif choice ==1 and robo==3:
                 print("------------------------------------------------")
                 print(" rock\t<---vs-->\tScissor\n||Result :You won\t||")
                 print("------------------------------------------------")
                 round=round+1
                 a=a+1
              elif choice ==2 and robo==1:
                 print("-----------------------------------------------")
                 print(" paper\t<---vs-->\trock\n||Result :You won\t||")
                 print("-----------------------------------------------")
                 round=round+1
                 a=a+1
              elif choice ==2 and robo==3:
                 print("--------------------------------------------------")
                 print(" paper\t<---vs-->\tScissor\n||Result :You Lost\t||")
                 print("--------------------------------------------------")
                 round=round+1
                 b=b+1
              elif choice ==3 and robo==1:
                 print("-------------------------------------------------")
                 print(" scissor\t<---vs-->\trock\n||Result :You Lost\t||")
                 print("-------------------------------------------------")
                 round=round+1
                 b=b+1
              elif choice ==3 and robo==2:
                 print("--------------------------------------------------")
                 print(" scissor\t<---vs-->\tpaper\n||Result :You won\t||")
                 print("-------------------------------------------------")
                 round=round+1
                 a=a+1
              else:
                 print(" invalid choice Try again ")
              if round==5:
                 print("You won :",a,"\nComputer won :",b)
                 if a==b:
                    print("=======Match Tie===========\n\tWell tried!\n")
                 elif a>b:
                    print("\n********congratulation you won**********\n")
                    break                    
                 else:
                    print("\n=========you Lost==============\nBetter luck next time!\n")

                    break
#==================Dice roller==========================================
        case 3 :
            print(" <-------------Welcome to Dice roller----------->")
            print("5 times max are winner ")
            sum=0
            sum1=0
            for i in range(1,6):
                robo = random.randint(1,6)
                print("round :",i)
                input("presss Enter to dice :")
                user = random.randint(1,6)
                print("Rolling the dice.......")
                print("...........")
                print("......")
                print("...")
                print("Roliing completer")
                print("robo     user")
                print(robo ,"\t",user,"\n")
                print("------------------------------------")
                if robo==user:
                   print(" Round Tie")
                elif user>robo:
                   print(" you won this round ")
                else:
                   print(" You lost the round ")  
                sum=sum+robo
                print("------------------------------------")
                sum1=sum1+user
            print(" computer total :",sum,"\t your total :",sum1)
            print("===============================================")
            print("              FINAL RESULT\n")
           
            if sum==sum1:
               print(" Match Tie ")
            elif sum>sum1 :
               print("\t \tYou Lost \n")
            else:
               print("\t\tcongratulations you won\n")
            print("===============================================")
#=============================Password generator=========================
        case 4 :
            print(" <-------------Welcome to World of password----------->")  
            print("1. 4 Digit PIN")
            print("2. 6 Digit PIN")
            print("3. 8 Character Password")
            print("4. Strong Password")
            select=int(input("Enter choice of password :"))
            match select :
#============================4 digit password ============================================
               case 1 :
                  print("\t+----------------------------+")
                  print("\t| Welcome to 4 Digit passwrod|")
                  print("\t+----------------------------+")
                  while True:
                     lock=random.randint(1000,9999)
                     input("Press Enter to generate a password :")
                     print("Password generating.....")
                     print("........")
                     print(".....")
                     print("Password generated succesfully\n")
                     print("\t+-----------------+")
                     print("\t| Password =",lock,"|")
                     print("\t+-----------------+\n")
                     
                     print("Choose parrword or another try :")
                     print("+------------+      +------------+")
                     print("| 1.Confirm  |      |  2.Retry   |")
                     print("+------------+      +------------+")
                     cho=int(input("Select option :"))
                     if cho==1 :
                        print("Great! \nThank you com again")
                        break
                     elif cho==2 :
                        continue
                     else:
                        print("Invalid input ")
                        break
#================================6 Digit password ========================================
               case 2 :
                  print("\t+----------------------------+")
                  print("\t| Welcome to 6 Digit passwrod|")
                  print("\t+----------------------------+")
                  while True:
                     lock=random.randint(100000,999999)
                     input("Press Enter to generate a password :")
                     print("Password generating.....")
                     print("........")
                     print(".....")
                     print("Password generated succesfully\n")
                     print("\t+-------------------+")
                     print("\t| Password =",lock,  "|")
                     print("\t+-------------------+\n")
                     
                     print("Choose parrword or another try :")
                     print("+------------+      +------------+")
                     print("| 1.Confirm  |      |  2.Retry   |")
                     print("+------------+      +------------+")
                     cho=int(input("Select option :"))
                     if cho==1 :
                        print("Great! \nThank you com again")
                        break
                     elif cho==2 :
                        continue
                     else:
                        print("Invalid input ")
                        break
#=============================8 charchter password system ================================
               case 3 :
                  print("\t+-------------------------------+")
                  print("\t| Welcome to 8 Charcter passwrod|")
                  print("\t+-------------------------------+")
                  while True:
                     
                     input("Press Enter to generate a password :")
                     print("Password generating.....")
                     print("........")
                     print(".....")
                     lock=""
                     i=1
                     while i <=8:
                       ch = random.randint(65, 122)
                       if 91 <= ch <= 96:
                          continue
                       #print(chr(ch), end="")
                       lock=lock+chr(ch)
                       i=i+1


                     print("Password generated succesfully\n")
                     print("\t+----------------------+")
                     print("\t| Password =",lock,"|")
                     print("\t+----------------------+\n")
                     
                     print("Choose parrword or another try :")
                     print("+------------+      +------------+")
                     print("| 1.Confirm  |      |  2.Retry   |")
                     print("+------------+      +------------+")
                     cho=int(input("Select option :"))
                     if cho==1 :
                        print("Great! \nThank you com again")
                        break
                     elif cho==2 :
                        continue
                     else:
                        print("Invalid input ")
                        break
            #==================strong password generator=================         
               case 4 :
                  print("\t+-------------------------------+")
                  print("\t| Welcome to strong passwrod|")
                  print("\t+-------------------------------+")
                  while True:
                     
                     input("Press Enter to generate a password :")
                     print("Password generating.....")
                     print("........")
                     print(".....")
                     l=""
                     i=1
                     while i <=5:
                       ch = random.randint(34, 122)
                       if 91 <= ch <= 96 or 48<= ch <=64:
                           continue
                       l=l+chr(ch)
                       i=i+1
                     l1=random.randint(100,999)
                     l2=str(l1)
                     lock=l+l2
                     

                     print("Password generated succesfully\n")
                     print("\t+----------------------+")
                     print("\t| Password =",lock,"|")
                     print("\t+----------------------+\n")
                     
                     print("Choose parrword or another try :")
                     print("+------------+      +------------+")
                     print("| 1.Confirm  |      |  2.Retry   |")
                     print("+------------+      +------------+")
                     cho=int(input("Select option :"))
                     if cho==1 :
                        print("Great! \nThank you com again\n")
                        break
                     elif cho==2 :
                        continue
                     else:
                        print("Invalid input ")
                        break
               case _:
                  print("invalid choice Please read carefully")
        case 5 :
#============================luckey wheel=======================================
           print("\t+-------------------------------+")
           print("\t| Welcome to Luckey  wheel      |")
           print("\t+-------------------------------+")
           while True :
             input("Press Enter to  Spin....")
             win=random.randint(1,10)
             print(" Spining......")
             print("......")
             match win :
               case 1:
                   print("Congratulations!\n")
                   print("You Won")
                   print("Chocolate")
           
               case 2:
                   print("Congratulations!\n")
                   print("You Won")
                   print("Pizza Coupon")
           
               case 3:
                   print("Congratulations!\n")
                   print("You Won")
                   print("Free Coffee")
           
               case 4:
                   print("Congratulations!\n")
                   print("You Won")
                   print("Movie Ticket")
           
               case 5:
                   print("Congratulations!\n")
                   print("You Won")
                   print("Headphones")
         
               case 6:
                   print("Congratulations!\n")
                   print("You Won")
                   print("Free Python Book")
           
               case 7:
                   print("Congratulations!\n")
                   print("You Won")
                   print("Rs. 500 Cashback")
           
               case 8:
                   print("Better Luck Next Time!")
                   print("No Prize This Time.")
           
               case 9:
                   print("Mystery Box!")
                   print("Surprise Gift Won!")
           
               case 10:
                   print("Jackpot!")
                   print("You Won a New Bike!")
                   print("(Just Kidding)")   
             print(" ")
             print("+------------+      +------------+")
             print("| 1.Retry    |      |  2.exit    |")
             print("+------------+      +------------+")                 
             cho=int(input("Select option :"))
             if cho==1 :
                continue
             elif cho==2 :
                print("Great! \nThank you com again")
                print("====================================================")

                break
             else:
                print("Invalid input ")
                break
#==========================about project================================               
        case 6 :
           print("====================================================")
           print("====================================================")
           print("\t\tABOUT PROJECT")
           
           print("Project Name : Python Game Zone")
           print("Developed By : Ajay Lodhi")
           print("Language     : Python")
           
           print("\nDescription :")
           print("Python Game Zone is a console-based application")
           print("that contains different fun games and utilities.")
           print("The project is completely menu-driven and")
           print("developed using basic Python concepts.")
           
           print("\nGames Included :")
           print("1. Guess the Number")
           print("2. Rock Paper Scissors")
           print("3. Dice Roller")
           print("4. Password Generator")
           print("5. lucky spin")
           
           print("\nConcepts Used :")
           print("- if-else")
           print("- Nested if-else")
           print("- match-case")
           print("- Nested match-case")
           print("- while loop")
           print("- for loop")
           print("- break")
           print("- continue")
           print("- random module")
           
           print("\nVersion : 1.0")
           
           print("\n====================================================")
           print("        Thank You For Playing!")
           print("        Keep Coding... Keep Learning...")
           print("====================================================") 
        case 7 :
            break

        case _:
            print("invalid selection please read carefully \n ")
            print("====================================================") 

            continue          
    print("want to play another game \n 1.Yes\n 2.No")
    choice=int(input("Enter your choice :"))
    if choice ==1:
        continue
    elif choice==2:           
        break
    else:
        print("Invaild input\n") 
        print("====================================================") 

        continue          
print("thanks for playing visit again")
      
                   
                     
             