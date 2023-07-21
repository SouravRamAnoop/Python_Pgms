#copy of sets
# s1={"sourav",20,16,}
# s2={"sandra",24}
# s3=s1.copy()
# print(s3)

#clear a set
# s1={"car","red","bike"}
# s1.clear()
# print(s1)

#using frozen set
# s1="sourav"
# s2="sourag"
# s3=frozenset(s1)
# s4=frozenset(s2)
# c=s3.intersection(s4)
# print(c)

#max and min value of a set
# s1={1,10,20,15,60}
# print("MAX =",max(s1))
# print("MIN =",min(s1))

#length of set
# s1={"car","bus","train",5,10}
# print("Length of set =",len(s1))

#a given value is present in a set
# s1={1,2,3,4,5,6,7}
# i=int(input("Enter the number :"))
# if i in s1:
#     print("The value is present in set")
#     print("value is =",i)
# else:
#     print(i,"is not present in set")

#no elements common
# s1={1,3,10,5,6}
# s2={5,6,7,4,}
# for i in s1:
#     for j in s2:
#      if i==j:
#         print("elements are common in sets")
# else:
#     print("elements are not present in sets")
# #2 method
# s1={1,2,5}
# s2={7,8,10}
# c=s1.intersection(s2)
# if c:
#     print("common numbers =",c)
# else:
#     print("common numbers are not present in sets")

#two sets have no common elements:
s1={1,2,3,4}
s2={5,6,7,8}
x=s1.isdisjoint(s2)
if x==True:
    print("Sets don't have common elements:")
else:
    print("Sets have common elements")
