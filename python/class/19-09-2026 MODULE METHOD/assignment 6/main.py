from models import Customer
customers=[]
n=int(input("Enter number of customers:"))

for i in range(n):
    print(f"Enter details for customer {i+1}")
    customer_id=int(input("Enter customer id:"))
    customer_name=input("Enter customer name:")
    city=input("Enter city:")
    purchase_amount=int(input("Enter purchase amount:"))

    customer=Customer(customer_id,customer_name,city,purchase_amount)
    customers.append(customer)

print("\nAll Customers:")
Customer.display(customers)

city=input("\nEnter city:")

print(f"\nCustomers from {city}:")
Customer.by_city(customers,city)

print("\nCustomers with purchase amount greater than 10000:")
Customer.purchase_greater_than_10000(customers)

print("\nHighest Purchase Customer:")
Customer.highest_purchase(customers)

print("\nTotal Sales:")
Customer.total_sales(customers)

print("\nAverage Purchase Amount:")
Customer.average_purchase(customers)

customer_id=int(input("\nSearch Customer Id:"))

print("\nCustomer Found:")
Customer.search(customers,customer_id)