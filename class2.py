#2. Constructor (__init__)
import os
os.system('cls' if os.name == 'nt' else 'clear')

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print("Name:", self.name)
        print("Roll:", self.roll)

s1 = Student("Ramaraju", 101)
s1.show()
