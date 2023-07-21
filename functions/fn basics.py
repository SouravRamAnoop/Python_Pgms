"""
Function
--------
function in a python is a block of codes.It is run only it is called

Parameters
----------
it is the variable that listed inside the parentheses of python

Arguments
---------
Arguments are values that are transferring to the function at the time of function call
"""
# def message():

#     print("HAI WORLD")
# message()

#default value
# def my_function(country="norway"):
#     print("The country is :",country)
# my_function()
# my_function("india")
# my_function("USA")

#LIST OF ITEMS IN FUNCTION

def  fooditems(food):
    for x in food:
        print(x)

s=["biriyani","rice","dosha","alfarm"]
fooditems(s)