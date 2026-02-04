class Library:
    def __init__(self,book_name,author, available = True):
        self.book_name = book_name
        self.author = author
        self.available = available

    def check_out(self):
        if self.available:
            self.available = False
            print(f"{self.book_name} has been checked out")
        else:
            print(f"{self.book_name} is currently  not available")

    def return_book(self):
        self.available = True
        print(f"{self.book_name} has been returned now available")

    def display(self):
        status = "Available" if self.available else "Not Available"
        print(f"Book name : {self.book_name} Author: {self.author} Status: {status}")

book1 = Library("Python", "Guido van rossum")
book2 = Library("Java", "James Gosling")

book1.check_out()
book1.display()
book1.return_book()
book1.display()
 
book2.check_out()
book2.display()
book2.return_book()
book2.display()
