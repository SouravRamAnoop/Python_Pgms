"""
Single inheritance
------------------
Single inheritance enables a derived class to inherit properties from a single parent class
"""

class Myclass:
    def info(self):
        print("This is from Myclass")

class Chclass(Myclass):
    def fun(self):
        print("This is from Chclass")

x=Chclass()
x.info()
x.fun()