"""
Question 6: Library Book Management System


A library wants to maintain information about books. The librarian should be able to:

View book details.
Issue the book to a student.
Return the book.
Requirements

Create a class named Book with the following attributes:

book_id
title
author
status (Initially "Available")

Initialize the values using a constructor.

Create the following methods:
display_details() → Displays all book information.
issue_book() → Changes the status to "Issued".
return_book() → Changes the status to "Available".
Sample Input
Enter Book ID : B101
Enter Book Title : Python Programming
Enter Author Name : John Smith
Sample Output
------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Available

Book issued successfully.

------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Issued

Book returned successfully.

------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Available
"""
class Book:
    def __init__(self):
        self.book_id=input("Enter Book id:")
        self.title=input("Enter book titile:")
        self.author=input("Enter auther name:")
        self.status="available"
    def display(self):
        print("-------Book details-------")
        print("Book Id".ljust(17),":",self.book_id)
        print("Title".ljust(17),":",self.title)   
        print("Auther".ljust(17),":",self.author)   
        print("Status".ljust(17),":",self.status) 
    def issue_book(self):
        print("-------Book Issued succesfully-----")
        self.status="Isuued" 
        self.display()
    def return_book(self):
        print("--------returned book succesfully--------")
        self.status="available"
        self.display()     
b1=Book()
b1.display()
b1.issue_book()
b1.return_book()