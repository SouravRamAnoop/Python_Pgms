"""
Hierarchical Inheritance
--------------------------
When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance.
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

ob1=Car()
ob1.car_info("BMW")
ob1.info()

ob2=Truck()
ob2.truck_info("MAHINDRA")
ob2.info()