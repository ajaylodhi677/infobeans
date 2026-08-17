"""
QUESTION 5: LIBRARY BOOK RECORDS
================================

A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.

---

2. Display all book details.

---

3. Find and display the most expensive book.

---

4. Search books by author name.

---

5. Calculate and display the average price of all books.

---

Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 700

"""
from collections import namedtuple 
book=namedtuple("book",["book_id","title","author","price"]) 
n=int(input("Enter number of books :")) 
books=[] 
for i in range(n): 
    print("Enter details for book :",i+1) 
    book_id=input("Enter book id :") 
    title=input("Enter title :") 
    author=input("Enter author :") 
    price=int(input("Enter price :")) 
    books.append(book(book_id,title,author,price)) 

print("==="*20) 
print("showing details") 

most=books[0] 
total=0 
author_name=input("Enter Author Name :") 

for x in books: 
    print(x.book_id,x.title,x.author,x.price) 
    if x.price>most.price: 
        most=x 
    total+=x.price 

print("==="*20) 
print("Most Expensive Book :") 
print(most.book_id,most.title,most.author,most.price) 

print("==="*20) 
print("Average Book Price :") 
print(total/n) 

print("==="*20) 
print("Books Written By",author_name,":") 
for x in books: 
    if x.author.lower()==author_name.lower(): 
       print(x.book_id,x.title,x.author,x.price)