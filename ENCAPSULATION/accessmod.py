""" Public Access Modifier:
-------------------------
 The members of a class that are declared public are easily accessible from any part of the program.
 All data members and member functions of a class are public by default. """


# program to illustrate public access modifier in a class
#
# class Geek:
#
#     # constructor
#     def __init__(self, name, age):
#         # public data members
#         self.geekName = name
#         self.geekAge = age
#
#     # public member function
#     def displayAge(self):
#         # accessing public data member
#         print("Age: ", self.geekAge)
#
#
# # creating object of the class
# obj = Geek("R2J", 20)
#
# # accessing public data member
# print("Name: ", obj.geekName)
#
# # calling public member function of the class
# obj.displayAge()

"""
Protected Access Modifier:
-------------------------
The members of a class that are declared protected are only accessible to a class derived from it. 
Data members of a class are declared protected by adding a single underscore ‘_’ symbol before the data member of that class. 
"""


# program to illustrate protected access modifier in a class

# # super class
# class Student:
#     # protected data members
#     _name = None
#     _roll = None
#     _branch = None
#
#     # constructor
#     def __init__(self, name, roll, branch):
#         self._name = name
#         self._roll = roll
#         self._branch = branch
#
#     # protected member function
#     def _displayRollAndBranch(self):
#         # accessing protected data members
#         print("Roll: ", self._roll)
#         print("Branch: ", self._branch)
#
#
# # derived class
# class Geek(Student):
#
#     # constructor
#     def __init__(self, name, roll, branch):
#         Student.__init__(self, name, roll, branch)
#
#     # public member function
#     def displayDetails(self):
#         # accessing protected data members of super class
#         print("Name: ", self._name)
#
#         # accessing protected member functions of super class
#         self._displayRollAndBranch()
#
#
# # creating objects of the derived class
# obj = Geek("R2J", 1706256, "Information Technology")
# # calling public member functions of the class
# obj.displayDetails()
"""
Private Access Modifier:
-----------------------
The members of a class that are declared private are accessible within the class only, 
private access modifier is the most secure access modifier. 
Data members of a class are declared private by 
adding a double underscore ‘__’ symbol before the data member of that class. """


# program to illustrate private access modifier in a class

class Geek:
    # private members
    __name = None
    __roll = None
    __branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # private member function
    def __displayDetails(self):
        # accessing private data members
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)

    # public member function
    def accessPrivateFunction(self):
        # accessing private member function
        self.__displayDetails()


# creating object
obj = Geek("R2J", 1706256, "Information Technology")

# calling public member function of the class
obj.accessPrivateFunction()
