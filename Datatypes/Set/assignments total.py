#counting vowels
# str1="education"
# set1={"a","e","i","o","u"}
# count=0
# for i in str1:
#     if i in set1:
#         count=count+1
# print("No.of vowels =",count)

#common letter in two input strings
# a="race"
# b="care"
# count=0
# for i in a:
#     for j in b:
#       if i==j:
#           count=count+1
# print("common letters =",count)

#common letter in strings
# a="face"
# b="race"
# set1=set(a)
# set2=set(b)
# c=set1.intersection(set2)
# print("common letters =",c)

#python pgm to print letter in fst string not on second
# str1="python"
# str2="django"
# set1=set(str1)
# set2=set(str2)
# x=set1.difference(set2)
# print(x)

#python pgm to displays which letters are present in both strings
# a="python"
# b="django"
# s1=set(a)
# s2=set(b)
# s3=s1.union(s2)
# print("letters present in both strings are")
# for i in s3:
#     print(i,end=" ")

#python pgm to display which letters are in the two strings but not in both
# a="sourav"
# b="sourag"
# s1=set(a)
# s2=set(b)
# c=s1.symmetric_difference(s2)
# print(c)

#intersection of sets
# s1={"apple","orange","banana","cherry"}
# s2={"cherry","watermelon","banana"}
# s3=s1.intersection(s2)
# print(s3)

# union of sets
# s1={"orange","white","green"}
# s2={"red","yellow","white","blue"}
# s3=s1.union(s2)
# print(s3)

#set difference
# a={"red",10,"car",20}
# b={"car",20}
# c=a.difference(b)
# print(c)

#symmetric difference
# a={"red","green","yellow","bike"}
# b={"red","green","yellow","car"}
# c=a.symmetric_difference(b)
# print(c)

#check is a set is subset of another set
# s1={1,2,3}
# s2={1,2,3,4}
# s3=s1.issubset(s2)
# if s3==True:
#     print(s1,"is subset of",s2)
# else:
#     print(s1,"is not subset of",s2)

s1={1,2,4,8}
s2={7,10,}
# s1.intersection_update(s2)
# print(s1)
# s1.difference_update(s2)
# print(s1)
# s1.symmetric_difference_update(s2)
# print(s1)
c=s1.isdisjoint(s2)
print(c)
# c=s1.issuperset(s2)
# print(c)