#3. Single Inheritance
import os
os.system('cls' if os.name == 'nt' else 'clear')
class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()
