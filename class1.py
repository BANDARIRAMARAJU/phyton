#1. Class & Object (Basic)
import os
os.system('cls' if os.name == 'nt' else 'clear')
class Student:
    def display(self):
        print("This is a Student class")

s1 = Student()
s1.display()
