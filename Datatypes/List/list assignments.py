# wap to separate negative and positive numbers from a given list
# a=int(input("Enter the elements of list :"))
# x=[]
# for i in range(a):
#     y=int(input("Enter the elemnets :"))
#     x.append(y)
# print("x =",x)
# b = []
# c = []
# for i in x:
#     if i>0:
#         b.append(i)
#     else:
#          c.append(i)
# print("Possitive Numbers are :",b)
# print("Negative numbers are :",c)

# wap to find sum of all numbers in a list
# b=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in b:
#     sum=sum+i
# print("sum =",sum)

#largest number in list without using max()
# c=[21,14,268,900,125,5,100,2100]
#  c.sort()
# print("Largest number =",c[-1])

#second method
# c=[21,14,268,900,125,5,100,2100]
# lar=0
# for i in c:
#     if i>lar:
#         lar=i
# print("largest number =",lar)


#wap to find common members frpm two list
# a=[1,2,5,10,20,15,60]
# b=[6,10,15,17,20,2]
# c=[]
# for i in a:
#     for j in b:
#         if i==j:
#             c.append(i)
# print("common numbers are :",c)


#wap to print all even numbers from agiven list
# a=[1,20,17,16,32,25,21,38,46,27]
# even=[]
# for i in a:
#     if i%2==0:
#         even.append(i)
#         # print(even)
# print("list of even numbers are :",even)


#wap create a list of even numbers and odd numbers from a given list:
# a=[1,2,3,4,5,6,0,7,8,9,10,24,13]
# even=[]
# odd=[]
# for i in a:
#     if i==0:
#         continue
#     elif i%2==1:
#         odd.append(i)
#     else:
#         even.append(i)
# print("odd list =",odd)
# print("even list =",even)

#wap to remove repeated elements from a given list without using built-in methods
# lst1=["Let's","google","the","pineapple","photo","google","photo"]
# r=[]
# for i in lst1:
#     if i not in r:
#         r.append(i)
# print(r)


#wap to print websites suffixes(com,org,net,in) from the list
lst1=["www.zframez.com","www.wikipedia.org","www.asp.net","www.abcd.in"]
a=[]
for i in lst1:
    b= i.find(".",4)
    c=i[b:]
    a.append(c)
print(a)



