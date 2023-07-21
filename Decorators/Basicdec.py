"""
A decorator is a design pattern in Python that allows a user to
add new functionality to an existing object without modifying its structure
"""

# def make_pretty(func):
#     def inner():
#         print("i got decorated")
#         func()
#     return inner()
#
# @make_pretty
# def ordinary():
#     print("i am ordinary ")

#2 pgm
def make_pretty(func):
    def inner():
        print("i got decorated")
        func()
    return inner()


