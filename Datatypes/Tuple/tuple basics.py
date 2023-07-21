"""
Tuple
------
It is used to store multiple data items in to a single variable
Tuple is ordered,indexed,immutable and allows duplicate values
"""
tuple1=("cars","bus","bike","lorry",1,2,3,4,2,"cars",5.2,[1,2,3],(2,4,6))
# print(tuple1)
# print(type(tuple1))
# print(tuple1[1])
# print(tuple1[-1])
# print(tuple1[0:])
# print(tuple1[::-1])
# print(tuple1[1:4])
#remove
# list1=list(tuple1)
# list1.remove("lorry")
# tuple1=tuple(list1)
# print(tuple1)
#replace
# list1=list(tuple1)
# list1.insert(3,"cycle")
# tuple1=tuple(list1)
# print(tuple1)

#replace2
# list1=list(tuple1)
# list1[3]="cycle"
# tuple1=tuple(list1)
# print(tuple1)

#adding
# list1=list(tuple1)
# list1.append([10,20])
# tuple1=tuple(list1)
# print(tuple1)

#reversing a tuple
# tup2=("apple","orange","mango")
# r=tup2[::-1]
# print(r)

# s=list(tup2)
# s.reverse()
# tup2=tuple(s)
# print(tup2)

# changing tuples
# tuple1=("Apple",[10,20,30],(5,12,25))
# print(tuple1[1][1])
# tuple1 = (11,22)
# tuple2 = (10,40)
# tuple1,tuple2=tuple2,tuple1
# print("tuple1 =",tuple1)
# print("tuple2 =",tuple2)

#access 20 from tuple1
tuple1=("Apple",[10,20,30],(5,12,25),1,5,6,7)
a=tuple1[1][1]
print(a)

#convert a tuple to string
# tuple2=("s","t","r","i","n","g")
# x="".join(tuple2)
# print(x)

#index finding
# tuple2=("s","t","r","i","n","g")
# x=tuple2.index(tuple2)
# print(x)