from array import *

#variable_name would be the name of the array.
#The typecode specifies what kind of elements would be stored in the array
#variable_name = array(typecode,[elements])

array1 = array('i', [10,20,30,40,50])

#Accessing Array Element
for x in array1:
   print(x)

# 2 using index numbers
# from array import *
#
# array1 = array('i', [10, 20, 30, 40, 50])
#
# print(array1[0])
#
# print(array1[2])

#delete operation
# from array import *
#
# array1 = array('i', [10,20,30,40,50])
#
# array1.remove(40)
#
# for x in array1:
#    print(x)