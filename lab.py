# Python Program to Demonstrate Data Structures and OOP Concepts

# ============================================================================
# 1. LIST OPERATIONS
# ============================================================================
print("=" * 60)
print("1. LIST OPERATIONS")
print("=" * 60)

# Create and access list elements
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)
print("Access first element:", my_list[0])
print("Access last element:", my_list[-1])

# Add list elements
my_list.append(60)
print("After append(60):", my_list)
my_list.insert(2, 25)
print("After insert(2, 25):", my_list)

# Remove list elements
my_list.remove(25)
print("After remove(25):", my_list)
removed_element = my_list.pop()
print(f"After pop(): {my_list}, Removed: {removed_element}")

# Sort list elements
numbers = [50, 30, 40, 10, 20]
numbers.sort()
print("Sorted List:", numbers)

# Reverse list elements
numbers.reverse()
print("Reversed List:", numbers)

# ============================================================================
# 2. SET OPERATIONS
# ============================================================================
print("\n" + "=" * 60)
print("2. SET OPERATIONS")
print("=" * 60)

# Create and access set elements
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Set A:", set_a)
print("Set B:", set_b)

# Union of sets
union_set = set_a.union(set_b)
print("Union (A ∪ B):", union_set)

# Intersection of sets
intersection_set = set_a.intersection(set_b)
print("Intersection (A ∩ B):", intersection_set)

# Difference of sets
difference_set = set_a.difference(set_b)
print("Difference (A - B):", difference_set)

# ============================================================================
# 3. TUPLE OPERATIONS
# ============================================================================
print("\n" + "=" * 60)
print("3. TUPLE OPERATIONS")
print("=" * 60)

# Create and access tuple
my_tuple = (10, 20, 30, 40, 50)
print("Original Tuple:", my_tuple)
print("Access first element:", my_tuple[0])
print("Access elements [1:4]:", my_tuple[1:4])

# Nested tuple
nested_tuple = (1, 2, (3, 4, 5), (6, 7))
print("Nested Tuple:", nested_tuple)
print("Access nested element [2][1]:", nested_tuple[2][1])

# Repetition of tuple
repeated_tuple = (1, 2) * 3
print("Tuple repetition (1, 2) * 3:", repeated_tuple)

# Concatenation of tuples
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
concatenated = tuple_1 + tuple_2
print("Concatenation of tuples:", concatenated)

# ============================================================================
# 4. DICTIONARY OPERATIONS
# ============================================================================
print("\n" + "=" * 60)
print("4. DICTIONARY OPERATIONS")
print("=" * 60)

# Create and access dictionary elements
student = {"name": "John", "age": 20, "grade": "A"}
print("Dictionary:", student)
print("Access 'name':", student["name"])
print("Access 'grade':", student.get("grade"))

# Update dictionary
student["age"] = 21
student["city"] = "New York"
print("After update:", student)

# Removing elements
del student["city"]
print("After deletion:", student)
student.pop("grade")
print("After pop('grade'):", student)

# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print("Merged dictionaries:", merged)

# ============================================================================
# 5. BANK ACCOUNT CLASS
# ============================================================================
print("\n" + "=" * 60)
print("5. BANK ACCOUNT CLASS")
print("=" * 60)

class BankAccount:
    """Class to represent a bank account"""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid deposit amount!")
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount}. Remaining Balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds!")
    
    def check_balance(self):
        """Check account balance"""
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")

# Test BankAccount class
account = BankAccount("ACC12345", 1000)
account.check_balance()
account.deposit(500)
account.withdraw(300)
account.check_balance()

# ============================================================================
# 6. LIBRARY CLASS
# ============================================================================
print("\n" + "=" * 60)
print("6. LIBRARY CLASS")
print("=" * 60)

class Book:
    """Class to represent a book in library"""
    
    def __init__(self, book_name, author, availability=True):
        self.book_name = book_name
        self.author = author
        self.availability = availability
    
    def checkout(self):
        """Check out a book"""
        if self.availability:
            self.availability = False
            print(f"'{self.book_name}' has been checked out.")
        else:
            print(f"'{self.book_name}' is not available.")
    
    def return_book(self):
        """Return a book"""
        self.availability = True
        print(f"'{self.book_name}' has been returned.")
    
    def display_info(self):
        """Display book information"""
        status = "Available" if self.availability else "Not Available"
        print(f"Book: {self.book_name} | Author: {self.author} | Status: {status}")

class Library:
    """Class to manage library books"""
    
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        """Add a book to library"""
        self.books.append(book)
    
    def display_available_books(self):
        """Display all available books"""
        print("Available Books:")
        for book in self.books:
            if book.availability:
                book.display_info()

# Test Library class
library = Library()
book1 = Book("Python Basics", "John Doe")
book2 = Book("Data Science", "Jane Smith")
book3 = Book("Web Development", "Mike Johnson")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_available_books()
book1.checkout()
print()
library.display_available_books()
book1.return_book()

# ============================================================================
# 7. INHERITANCE - MANAGER CLASS (Multiple Inheritance)
# ============================================================================
print("\n" + "=" * 60)
print("7. INHERITANCE - MANAGER CLASS (Multiple Inheritance)")
print("=" * 60)

class Person:
    """Base class for person"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee:
    """Base class for employee"""
    
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary
    
    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Salary: ${self.salary}")

class Manager(Person, Employee):
    """Manager class inheriting from Person and Employee"""
    
    def __init__(self, name, age, employee_id, salary, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, salary)
        self.department = department
    
    def display_manager_info(self):
        """Display complete manager information"""
        self.display_person_info()
        self.display_employee_info()
        print(f"Department: {self.department}")
    
    def give_raise(self, amount):
        """Give salary raise to manager"""
        self.salary += amount
        print(f"Salary raised by ${amount}. New Salary: ${self.salary}")

# Test Manager class
manager = Manager("Alice Brown", 35, "MGR001", 80000, "IT")
manager.display_manager_info()
manager.give_raise(5000)
print(f"Updated Salary: ${manager.salary}")

# ============================================================================
# 8. POLYMORPHISM - VEHICLE CLASSES
# ============================================================================
print("\n" + "=" * 60)
print("8. POLYMORPHISM - VEHICLE CLASSES")
print("=" * 60)

class Vehicle:
    """Base class for vehicles"""
    
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    """Car subclass overriding move()"""
    
    def move(self):
        print("Driving on the road")

class Bicycle(Vehicle):
    """Bicycle subclass overriding move()"""
    
    def move(self):
        print("Pedaling on the road")

# Demonstrate polymorphism
vehicles = [Car(), Bicycle(), Vehicle()]
print("Demonstrating polymorphism:")
for vehicle in vehicles:
    vehicle.move()

# ============================================================================
# 9. USER-DEFINED MODULE - SHAPES
# ============================================================================
print("\n" + "=" * 60)
print("9. SHAPES CALCULATION")
print("=" * 60)

import math

class Shapes:
    """Class to calculate areas of different shapes"""
    
    @staticmethod
    def circle_area(radius):
        """Calculate area of circle"""
        return math.pi * radius ** 2
    
    @staticmethod
    def rectangle_area(length, width):
        """Calculate area of rectangle"""
        return length * width
    
    @staticmethod
    def triangle_area(base, height):
        """Calculate area of triangle"""
        return 0.5 * base * height

# Test shapes calculation
shapes = Shapes()

print("Circle area (radius=5):", round(shapes.circle_area(5), 2))
print("Rectangle area (length=10, width=5):", shapes.rectangle_area(10, 5))
print("Triangle area (base=8, height=6):", shapes.triangle_area(8, 6))

# User input for shape calculation
print("\n--- Shape Area Calculator ---")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = input("Select a shape (1/2/3): ")

if choice == "1":
    radius = float(input("Enter radius: "))
    area = shapes.circle_area(radius)
    print(f"Area of circle: {round(area, 2)}")
elif choice == "2":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = shapes.rectangle_area(length, width)
    print(f"Area of rectangle: {area}")
elif choice == "3":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = shapes.triangle_area(base, height)
    print(f"Area of triangle: {area}")
else:
    print("Invalid choice!")

print("\n" + "=" * 60)
print("END OF PROGRAM")
print("=" * 60)

