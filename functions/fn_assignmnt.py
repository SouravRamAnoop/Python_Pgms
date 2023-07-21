#Multiply all the numbers in a list using function
a = [12,10,10]
def multiply():
    m=1
    for i in a:
        m=m*i
    print("product =",m)


multiply()

#write a python pgm to reverse a string
# def reverse_str(s1):
#     s2=s1[-1::-1]
#     print("Reverse =",s2)
#
#
# reverse_str("1234abcd")

#factorial of a number.The function accept the number as an argument
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(f"factorial of {n} =",fact)
#
#
# factorial(5)

#program to check number is prime or not.take number as a parameter
# n=int(input("Enter the number :"))
# def prime_num(n):
#     for i in range(2,n):
#         if n%i==0:
#             print(f"{n} is not a prime number")
#             break
#     else:print(f"{n} is prime number")
#
#
# prime_num(n)


#list the even numbers between 4 and 30
# def even_num():
#   l1=[]
#   for i in range(4,30,2):
#          l1.append(i)
#   print("Even Numbers =",l1)
#
#
# even_num()

#define a function which counts vowels and consonant in a word.
# l=["a","e","i","o","u"]

# def vowel_cons(s):
#     c=0
#     x=0
#     for i in s:
#         if i in l:
#             c=c+1
#         elif i not in l:
#             x=x+1
#     print("vowels =",c)
#     print("consonant =",x)
#
# s=input("Enter the string :")
# vowel_cons(s)

#function that accept two numbers  as arguments and return the sum

# def sum(a,b):
#     c=a+b
#     return c
#
#
# print("sum =",sum(10,20))

#fuction that accepts different values as parameter and returns a list
# def lst_con(*a):
#     return list(a)
#
# print(lst_con("sourav","sandra",16,20))
#
# #function that accept dictionary as a parameter
# def dic_out(**d):
#     return d
#
# print(dic_out(name="sourav",course="python",age=25))

# def dictionary(*d):







