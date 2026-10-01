from main import Payment,UPIPayment,CreditCardPayment,DebitCardPayment,NetBankingPayment,WalletPayment
Payments=[]
while True:
    print("""========================================
       ONLINE PAYMENT SYSTEM
========================================

1. Make Payment
2. View Payment Details
3. Exit
    """)
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            CustomerName=input("Enter customer name:")
            orderid=int(input("Enter order id:"))
            orderamount=int(input("Enter order amount:"))
            print("""
            Select Payment Method

1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet
            """)
            select=int(input("Select your payment mode:"))
            match select:
                case 1 :
                    upiid=int(input("Enter upi id:"))
                    pin=int(input("Enter upi pin :"))
                    fees=int(input("Enter processing fees:"))
                    upi=UPIPayment(CustomerName,orderid,orderamount,upiid,pin,fees)
                    upi.calculate_processing_fee()
                    upi.generate_receipt()
                    Payments.append(upi)
                case 2 :
                    cardno=int(input("Enter credit card number:"))    
                    name=input("Enter card holder name:")
                    cvv=int(input("Enter CVV:"))
                    expdate=input("Enter expiry date:")
                    fees=int(input("Enter processing fees:"))
                    credit=CreditCardPayment(CustomerName,orderid,orderamount,cardno,name,cvv,expdate,fees)
                    credit.calculate_processing_fee()
                    credit.generate_receipt()
                    Payments.append(credit)
                case 3 :
                    cardno=int(input("Enter debit card number:"))    
                    name=input("Enter card holder name:")
                    cvv=int(input("Enter CVV:"))
                    expdate=input("Enter expiry date:")
                    fees=int(input("Enter processing fees:"))  
                    debit=DebitCardPayment(CustomerName,orderid,orderamount,cardno,name,cvv,expdate,fees)
                    debit.calculate_processing_fee()
                    debit.generate_receipt()
                    Payments.append(debit)
                    
                case 4: 
                    bname=input("Enter bank name:")
                    acc=int(input("Enter account numbver:"))
                    cid=int(input("Enter customerr id:"))
                    fees=int(input("Enter processing fees:"))
                    net=NetBankingPayment(CustomerName,orderid,orderamount,bname,acc,cid,fees)
                    net.calculate_processing_fee()
                    net.generate_receipt()
                    Payments.append(net)
                case 5:
                    wname=input("Enter Wallet name:") 
                    mob=int(input("Enter wallet number:"))  
                    pin=int(input("Enter wallet pin:"))
                    fees=int(input("Enter processing fees:"))
                    wallet=WalletPayment(CustomerName,orderid,orderamount,wname,mob,pin,fees) 
                    wallet.calculate_processing_fee()
                    wallet.generate_receipt()
                    Payments.append(wallet)
                case _:
                    print("Invalid choice :")    
        case 2:
            id=int(input("Enter order id:"))
            found=False
            for p in Payments:
                if p.orderid==id:
                    print("Order ID:",p.orderid)
                    print("Customer Name:",p.CustomerName)
                    print("Payment Method:",type(p).__name__)
                    print("Order Amount:",p.orderamount)
                    print("Processing Fee:",p.processingfee)
                    print("Final Amount:",p.orderamount+p.processingfee)
                    found=True
                    break
            if found==False:
                print("Payment record not found.")
        case 3:
            print("thanks you for using online banking system")  
            break            