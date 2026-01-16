import os
os.system('cls' if os.name == 'nt' else 'clear')
import os
os.system('cls' if os.name == 'nt' else 'clear')
class Parent:
    def show(self):
        print("This is parent class")

class Child(Parent):
    def show(self):
        print("This is child class")

c = Child()
c.show()
