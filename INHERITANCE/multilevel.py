"""
Multilevel Inheritance
----------------------
In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class.
This is similar to a relationship representing a child and a grandfathe
"""
class Grandfather:
    def ownhouse(self):
        print("Grandpa house")

class father(Grandfather):
    def ownbike(self):
        print("fathers bike")

class son(father):
    def ownbook(self):
        print("son have a book")

x=son()
x.ownhouse()
x.ownbike()
x.ownbook()