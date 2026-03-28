""" AIM: crate a class Animal and call it with method move() with method overriding in class Dog() and Bird()  """
class Animal:
    def move(self):
        print("Animals move.")

class Dog:
    def move(self):
        print("Dog run on the ground.")

class Bird:
    def move(self):
        print("Bird fly in the sky.")

animal = [Animal(), Dog(), Bird()]
for a in animal:
    a.move()

