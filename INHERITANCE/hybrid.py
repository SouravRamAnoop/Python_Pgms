"""
Hybrid Inheritance
------------------
Inheritance consisting of multiple types of inheritance is called hybrid inheritance.
"""
class Vehicle:
    def info(self):
        print("This is Vehicle")

class Car(Vehicle):
    def car_info(self,name):
        print("car name is ",name)

class Truck(Vehicle):
    def truck_info(self,name):
        print("truck name is :",name)

class Sportscar(Car,Vehicle):
    def spo_car_info(self):
        print("inside the sports car class")

ob1=Sportscar()
ob1.info()
ob1.car_info("VOLVO")
ob1.spo_car_info()

ob2=Truck()
ob2.info()
ob2.truck_info("Mahindra")