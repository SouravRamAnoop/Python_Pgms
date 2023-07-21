"""
"""
#Polymorphism with Inheritance
class Vehicle:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price

    def show(self):
        print("Details :",self.name,self.color,self.price)

    def max_speed(self):
        print("max speed is 150")

    def change_gear(self):
        print("vehicle change 6 gear")

class Car(Vehicle):
    def price_info(self):
        print(f"{self.price}")
    def max_speed(self):
        print("max speed of car is 200")

    def change_gear(self):
        print("car can change 7 gear")

car=Car("bmw","red",2500000)
car.show()
car.price_info()
car.max_speed()
car.change_gear()