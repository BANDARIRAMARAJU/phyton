#7. Polymorphism (Same Function Name)
import os
os.system('cls' if os.name == 'nt' else 'clear')
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

for animal in (Dog(), Cat()):
    animal.sound()
