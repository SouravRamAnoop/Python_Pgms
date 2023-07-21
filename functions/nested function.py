#nested function
# def increment(number):
#     def inner_incremnet():
#         return number+1
#     return inner_incremnet()
#
#
# print(increment(10))

#print message
# def message(str):
#     s="you are "+ str
#     def message2():
#         print(s)
#     return message2()
#
#
# message("awsome")

# def output():
#     p="how are you guyzz?"
#     def output2():
#         print(p)
#     return output2()
#
# output()

#factorial of a number using nested function

# n = int(input("Enter the Number :"))
# def factorial(n):
#     def inner_fact():
#         fact=1
#         for i in range(1,n+1):
#             fact=fact*i
#         return fact
#     return inner_fact()
#
# print(f"Factorial of {n} =",factorial(n))

#find the odd number in the range of 1 to 50

# def outer_odd():
#     n=50
#     l=[]
#     def inner_odd():
#         for i in range(1,n,2):
#             l.append(i)
#         print(f"odd numbers =",l)
#     return inner_odd()
#
# outer_odd()

#multiplication table of a given number
# def multiply(n):
#     r=10
#     def multiply2():
#         for i in range(1,r+1):
#             print(f"{i} * {n} = {i*n}")
#     return multiply2()
# n=int(input("Enter the number :"))
# multiply(n)

#to find string is a palindrome
# s=input("Enter the string :")
# def palindrome(s):
#     print(f"String is {s}")
#     def palindrome2():
#         if s[::-1]==s[0:]:
#             print(f"{s} is palindrome")
#         else:print(f"{s} is not palindrome")
#     return palindrome2()
#
# palindrome(s)

#possitive or negative
n=int(input("Enter the number :"))
def positive(n):
    def positive2():
        if n>0:
            print(f"{n} is possitive")
        elif n<0:
            print(f"{n} is negative")
        else:print("it is zero")
    return positive2()

positive(n)






