"""
6.

NOTE: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000)
"""
n=int(input("Enter number of products :")) 
products=[] 
for i in range(n): 
    print("Enter details for product :",i+1) 
    product_id=input("Enter product id :") 
    product_name=input("Enter product name :") 
    price=int(input("Enter price :")) 
    products.append((product_id,product_name,price)) 

print("==="*20) 
print("showing details") 

cost=products[0] 
cheap=products[0] 
total=0 

for x in products: 
    print(x) 
    if x[2]>cost[2]: 
        cost=x 
    if x[2]<cheap[2]: 
        cheap=x 
    total+=x[2] 

print("==="*20) 
print("Costliest Product :") 
print(cost) 

print("==="*20) 
print("Cheapest Product :") 
print(cheap) 

print("==="*20) 
print("Average Price :") 
print(total/n) 

print("==="*20) 
print("Products Above ₹50,000 :") 
for x in products: 
    if x[2]>50000: 
       print(x)