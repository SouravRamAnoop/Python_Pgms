"""
LIST COMPREHENSION
------------------
It offers a shorter syntax when you want to create a new list based on the values of an existing list
l=[expression for item in iterable if condition==true]

# """
# l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# e=[]
# o=[]
# for i in l:
#     if i%2==0:
#         e.append(i)
#     else:
#         o.append(i)
# print(f"e={e}")
# print(f"o={o}")


# l1=[i for i in range(1,20) if i%2==0 else ]
# l2=[i for i in range(1,20) if i%2==1]

# l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#
# l1=[(i,"even" if i%2==0 else "odd") for i in l]
# print(l1)
#
# s=["apple","orange","banana","kiwi","grapes"]
# s1=[x for x in s if "a" in x]
# print(s1)

l=[2,3,4,5,6,7,8,9,10,11,12,13,14,15]
s=[(i,"not prime" if i%j==0 else "prime") for i in l for j in range(2,i)]
print(s)


"List of numbers is divisble by 3"
# s=[2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# s2=[]
# for i in s:
#     if i%3==0:
#         s2.append(i)
# print("s2=",s2)

#using list comprehension
# s=[2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# s1=[i for i in s if i%3==0 ]
# print("s1=",s1)

