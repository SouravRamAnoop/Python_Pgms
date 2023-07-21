
# r = int(input("Enter a range :"))
# for i in range(2,r+1):
#
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#             print(f"{i} is prime number")

# n=int(input("Enter the number :"))
#
# for i in range(2,n):
#     if n%i==0:
#         print(f"{n} is not prime number ")
#         break
# else:
#     print(f"{n} is prime")

#fibanacci series
# r=int(input("Enter the range:"))
# n1=0
# n2=1
# print(n1)
# print(n2)
# for i in range(r+1):
#     n3=n1+n2
#     print(n3)
#     n1=n2
#     n2=n3

#factorial of a number
#
# n=int(input("Enter the number:"))
# f=1
# for i in range(1,n+1):
#     f=f*i
# print(f"factorial of {n} is {f}")

#palindrome or not
# s1=input("Enter the string 1 :")
# s=s1.lower()
# if s == s[::-1]:
#     print(f"{s1} is palindrome")
# else:
#     print(f"{s1} is not palindrome")

#odd or even

# n=int(input("Enter the number :"))
#
# if n%2==0 and n!=0:
#     print(f"{n} is even number")
# elif n%2==1:
#     print(f"{n} odd number")
# else:
#     print("It is zero")

#max value
# n1=int(input("Enter the first number :"))
# n2=int(input("Enter the second number :"))
# n3=int(input("Enter the third number :"))
#
# if n1>n2 and n1>n3:
#     print(f"{n1} is greatest number")
# elif n2>n1 and n2>n3:
#     print(f"{n2} is greatest number")
# else:
#     print(f"{n3} is greatest number")

#sum of n natural number
# n=int(input("Enter the number :"))
# s=0
# for i in range(n+1):
#     s=s+i
# print(f"sum of natural number is {s}")

#pattern
r=int(input("Enter the range:"))
for i in range(0,r+1):
    for j in range(r):
        print(" ",end=" ")
    for k in range(i):
        print("* ",end=" ")
    print()