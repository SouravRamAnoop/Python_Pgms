#wap using function create and print a list where the values are squre of numbers between 1 and 30(both included)
# def squre():
#     l1=[]
#     for i in range(1,31):
#         l1.append(i**2)
#     print("L1 =",l1)
# squre()

#uppercase and lowercase letters in a string
# s=input("Enter the string:")
# def Upper_lower(s):
#     u=0
#     l=0
#     for i in s:
#         if i.isupper():
#             u=u+1
#         elif i.islower():
#             l=l+1
#     print(f"Uppercase ={u}")
#     print(f"Lowercase ={l}")
#
# Upper_lower(s)

#PALINDROME OR NOT
# def palindrome(s):
#     y=s.lower()
#     if y[0:]==y[::-1]:
#         print(f"{s} is palindrome")
#     else:
#         print(f"{s} is not palindrome")
# s=input("Enter the string :")
# palindrome(s)

#unique elements
# def unique(l):
#     u=[]
#     for i in l:
#         if i in u:
#             continue
#         else:
#             u.append(i)
#     print("unique elements =",u)
# l=["apple","banana","apple",1,10,1]
# unique(l)

# to check whether a number is perfect or not
# n=int(input("Enter the number :"))
# def perfrct(n):
#     c=0
#     for i in range(1,n):
#       if n%i==0:
#           c=c+i
#     if n==c:
#         print(f"{n} is perfect number")
#     else:
#         print(f"{n} is not aperfect number ")
#
# perfrct(n)



