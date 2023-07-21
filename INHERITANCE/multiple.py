
"""
Multiple Inheritance
--------------------
When a class can be derived from more than one base class this type of inheritance is called multiple inheritances.
"""

#base 1
class Mother:
    mothername=""
    def mother(self):
        print(self.mothername)

#base 2
class Father:
    fathername=""
    def father(self):
         print(self.fathername)

#child class

class Son(Mother,Father):
    def parents(self):
        print("Father :",self.fathername)
        print("Mother :",self.mothername)

ob=Son()
ob.fathername="RAM"
ob.mothername="SEETHA"
ob.parents()
