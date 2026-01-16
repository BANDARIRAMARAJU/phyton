import os
os.system('cls' if os.name == 'nt' else 'clear')
class Grandfather:
    def land(self):
        print("Land property")

class Father(Grandfather):
    def house(self):
        print("House property")

class Son(Father):
    def bike(self):
        print("Bike property")

s = Son()
s.land()
s.house()
s.bike()


