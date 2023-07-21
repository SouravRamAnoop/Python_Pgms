# list1=["ford","vento","volvo","audi",["cars","bus","lorry"],"bmw"]
# l2=list1[4][0]
# print(l2)
# print(list1[5])
# print(list1[-1])
# l4=list1[4].insert(1,"bike")
# print(list1)
# list1[4].pop(3)
# print(list1)
#want to do reverse and remove
# list1=["ford","vento","volvo","audi",["cars","bus","lorry"],"bmw"]
# list1[4].pop(2)
# print(list1)
# # list1[4].remove("cars")
# # print(list1)
# list1[4].reverse()
# print(list1)
# list1.reverse()
# print(list1)
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list =["h","i","j"]
# # list1[2][1][2].extend(sub_list)
# # print(list1)
# list1[2][1][2].insert(2,sub_list)
# print(list1)

"""
WAP to find the sum of all numbers in the list
"""
# list5=[1,2,3,4,5]
# sum=0
# for i in list5:
#     sum=sum+i
# print("Sum of all numbers in list are :",sum)

""" Remove empty strings from a list of strings
 """
# list2=["john"," ","jack","Emma"," ","Jins","Lina"]
# for i in list2:
#     if i == " ":
#         list2.remove(i)
# print(list2)
"""
 Write a python program to remove repeated elements from a given list without using built-in methods
"""
# list3=["Let's","google","the","pineapple","photo","google","photo"]
# list4=[]
# for i in list3:
#     if i not in list4:
#         list4.append(i)
# print(list4)