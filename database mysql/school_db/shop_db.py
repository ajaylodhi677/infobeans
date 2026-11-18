"""
ASSIGNMENT 3 – PRODUCT MANAGEMENT SYSTEM

Q1. Create a database named shop_db and use the database.

Q2. Create a table named product with:
- product_id – INT, PRIMARY KEY, AUTO_INCREMENT
- product_name – VARCHAR(50)
- category – VARCHAR(50)
- brand – VARCHAR(50)
- price – INT
- quantity – INT

Q3. Insert the following 10 product records:

product_name | category | brand | price | quantity
Laptop | Electronics | Dell | 55000 | 10
Smartphone | Electronics | Samsung | 25000 | 15
Keyboard | Accessories | Logitech | 1500 | 25
Mouse | Accessories | HP | 800 | 30
Monitor | Electronics | LG | 18000 | 12
Headphones | Accessories | Sony | 3000 | 20
Printer | Electronics | Canon | 12000 | 8
Tablet | Electronics | Lenovo | 22000 | 14
Webcam | Accessories | Logitech | 2500 | 18
Speaker | Accessories | JBL | 4500 | 16

Q4. Display the structure of the product table using DESC.

Q5. Display all records from the product table.
"""
create database shop_db;
use shop_db;
create table product(product_id int primary key auto_increment,
product_name varchar(50),
category varchar(50),
brand varchar(50),
price int,
quantity int);

insert into product(product_name,category,brand,price,quantity)
values('laptop','electronics','dell',55000,10),
('smartphone','electronics','samsung',25000,15),
('keyboard','accesories','logitech',1500,25),
('mouse','accesories','hp',800,30),
('moniter','elecrtronics','lg',18000,12),
('headphones','accessories','sony',3000,20),
('printer','accesories','sony',12000,8),
('tablet','electrinics','lenovo',22000,14),
('webcom','accesories','logitech',25000,18),
('speaker','accesories','jbl',4500,16);

desc product;
select * from product;