class Book:
    def __init__(self,book_id,book_name,author,price):
        self.book_id=book_id
        self.book_name=book_name
        self.author=author
        self.price=price

    def display(books):
        for book in books:
            print(book.book_id,book.book_name,book.author,book.price)

    def search(books,book_id):
        for book in books:
            if book.book_id==book_id:
                print(book.book_id,book.book_name,book.author,book.price)
                return
        print("Book not found")

    def by_author(books,author):
        for book in books:
            if book.author==author:
                print(book.book_id,book.book_name,book.price)

    def price_greater_than_500(books):
        for book in books:
            if book.price>500:
                print(book.book_name)

    def most_expensive(books):
        high=books[0]
        for book in books:
            if book.price>high.price:
                high=book
        print(high.book_name,"=",high.price)

    def average_price(books):
        total=0
        for book in books:
            total+=book.price
        average=total/len(books)
        print(f"{average:.0f}")