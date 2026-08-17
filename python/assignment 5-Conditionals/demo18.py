unit1 = int(input("enter unit1 stocks")) 
unit2 = int(input("enter unit2 stocks")) 
unit3 = int(input("enter unit3 stocks")) 
unit4 = int(input("enter unit4 stocks")) 
unit5 = int(input("enter unit5 stocks"))
unit6 = int(input("enter unit6 stocks"))

if unit1>=unit2:
   if unit1>=unit3:
      if unit1>=unit4:
         if unit1>=unit5:
            if unit1>=unit6:
               print("highest stock: ",unit1)
            else:
               print("highest stock: ",unit6)
         else:
            if unit5>=unit6:
               print("highest stock: ",unit5)
            else:
               print("highest stock: ",unit6)
      else:
         if unit4>=unit5:
            if unit4>=unit6:
               print("highest stock: ",unit4)
            else:
               print("highest stock: ",unit6)
         else:
            if unit5>=unit6:
               print("highest stock: ",unit5)
            else:
               print("highest stock: ",unit6)   
   else:
      if unit3>=unit4:
         if unit3>=unit5:
            if unit3>=unit6:
               print("highest stock: ",unit3)
            else:
               print("highest stock: ",unit6)
         else:
            if unit5>=unit6:
               print("highest stock: ",unit5)
            else:
               print("highest stock: ",unit6)
      else:
         if unit4>=unit5:
            if unit4>=unit6:
               print("highest stock: ",unit4)
            else:
               print("highest stock: ",unit6)
         else:
            if unit5>=unit6:
               print("highest stock: ",unit5)
            else:
               print("highest stock: ",unit6) 

else:
   if unit2>=unit3:
      if unit2>=unit4:
         if unit2>=unit5:
            if unit2>=unit6:
                print("highest stock: ",unit2) 
            else:
                print("highest stock: ",unit6) 
         else:
            if unit5>=unit6:
               print("highest stock: ",unit5)
            else:
               print("highest stock: ",unit6) 
      else:
         if unit4>=unit5:
            if unit4>=unit6:
               print("highest stock: ",unit4)
            else:
               print("highest stock: ",unit6)
         else:
            if unit5>=unit6:
               print("highest stock: ",unit5)
            else:
               print("highest stock: ",unit6)
   else:
      if unit3>=unit4:
         if unit3>=unit5:
            if unit3>=unit6:
               print("highest stock: ",unit3)
            else:
               print("highest stock: ",unit6)
         else:
            if unit5>=unit6:
               print("highest stock: ",unit5)
            else:
               print("highest stock: ",unit6)
      else:
         if unit4>=unit5:
            if unit4>=unit6:
               print("highest stock: ",unit4)
            else:
               print("highest stock: ",unit6)
         else:
            if unit5>=unit6:
               print("highest stock: ",unit5)
            else:
               print("highest stock: ",unit6)   