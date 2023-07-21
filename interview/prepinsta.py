#reverse a number
#x=int(input("Enter the number:"))
# y=str(x)
# z=y[::-1]
# print("Reversed number is",int(z))

# x=int(input("Enter the number:"))
# y=str(x)
# l1=[]
# for i in range(len(y)):
#     z=x%10
#     l1.append(z)
#     x=x//10
# print("Reversed number is",l1)
#
# num = int(input("Enter the Number:"))
# temp = num
# reverse = 0
# while num > 0:
#     remainder = num % 10
#     reverse = (reverse * 10) + remainder
#     num = num // 10
# print(reverse)

# print("The Given number is {} and Reverse is {}".format(temp, reverse))

#fibonacci series
# r=int(input("enter the range:"))
# n1=0
# n2=1
# print(n1)
# print(n2)
# for i in range(1,r+1):
#     n3=n1+n2
#     print(n3)
#     n1=n2
#     n2=n3

#greatest common devisor
# x=int(input("Enter the first number:"))
# y=int(input("Enter the second number:"))
# z=0
# if x>y :
#     small=x
# else:
#     small=y
# for i in range(1,small+1):
#     if x%i==0 and y%i==0:
#         z=i
# print("GCD=",z)

#finding perfect number
# n=int(input("Enter the number :"))

# z=0
# for i in range(1,n):
#     if n%i==0:
#         z=z+i
#         print(z)
# if n==z:
#     print(f"{n} is a prfect number")
# else:
#     print(f"{n} is not a perfect number")

#anagram or not
# x="earth"
# y="heart"
# if sorted(x)==sorted(y):
#     print(f"{x} and {y} are anagrams")
# else:
#     print("not")


#palindrome or not
# x=input("Enter the string :")
# s=x.lower()
# if s==s[::-1]:
#     print(f"{s} is palindrome")
# else:
#     print("It is not palindrome")

#freequency of characters
# #take user input
# String = input('Enter the string :')
# #take character input
# Character = input('Enter character :')
# #initiaalize int variable to store frequency
# frequency = 0
# #use count function to count frequency of character
# frequency = String.count(Character)
# #count function is case sencetive
# #so it print frequency of Character according to given Character
# print(str(frequency) + ' is the frequency of given character')

#replacing substring
#
# string=input("Enter String :\n")
# str1=input("Enter substring which has to be replaced :\n")
# str2=input("Enter substring with which str1 has to be replaced :\n")
# string=string.replace(str1,str2)
# print("String after replacement")
# print(string)

#leap year or not
# year=int(input("Enter the year :\n"))
# if (year%400==0) or (year%4==0 and year%100!=0):
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")

#find non repeating characters in a string

# s=input("Enter a string :")
# for i in s:
#     count = 0
#     for j in s:
#         if i==j:
#             count+=1
#         if count>1:
#             break
#     if count==1:
#         print(i,end="")

# def changeArr(input1):
#     newArray = input1.copy()
#     newArray.sort()
#     print(newArray)
#     print(input1)
#     for i in range(len(input1)):
#         for j in range(len(newArray)):
#             if input1[i] == newArray[j]:
#                 input1[i] = j + 1;
#                 break;

# Driver Code
# arr = [100, 2, 70, 12, 90]
# changeArr(arr)
# # Print the array elements
# print(arr)

#factorial of a number
# n=int(input("Enter the number :"))
# f=1
# for i in range(1,n+1):
#     f=f*i
# print(f)

# import math
# n=math.factorial(5)
# print(n)

#armstrong number
# n=int(input("Enter the number :"))
# l=len(str(n))
# num=n
# a=0
# for i in range(0,l):
#     x=n%10
#     a=a+x**l
#     n=n//10
#     print(a)
# if num==a:
#     print("armstrong")

# reverse
# n=int(input("Enter the number :"))
# l=len(str(n))
# rev=0
# for i in range(l):
#     x=n%10
#     rev=rev*10+x
#     n=n//10
# print(rev)

#sum of n natural numbers
# n=int(input("Enter the number :"))
# s=0
# for i in range(1,n+1):
#     s=s+i
# print(s)

#using recursion

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# print(factorial(5))


# num = int(input("Enter number:"))
# binary_val = num
# decimal_val = 0
# base = 1
# while num > 0:
#     rem = num % 10
#     decimal_val = decimal_val + rem * base
#     print(decimal_val)
#     num = num // 10
#     base = base * 2
#
# print("Binary Number is {} and Decimal Number is {}".format(binary_val, decimal_val))

# n=int(input("Enter the number :"))
# binaryval=n
# decimalval=0
# base=1
# while n>0:
#     rem=n%10
#     decimalval=decimalval+rem*base
#     n=n//10
#     base=base*2
# print("binary number is {} and decimal number is {}".format(binaryval,decimalval))

# pattern
# r=int(input("Enter the range :"))
# for i in range(1,r+1):
#     for j in range(0,r-i):
#         print(" ",end="")
#     for k in range(i):
#         print("* ",end="")
#     print()
# for l in range(r-1,0,-1):
#     for m in range(0,r-l):
#         print(" ",end="")
#     for n in range(l):
#         print("* ",end="")
#     print()

# s="python"
# x=""
# for i in s:
#     x+=i
#     print(x)

#ascii
# n=65
# r=int(input("Enter the range :"))
# for i in range(1,r+1):
#     for k in range(0,r-i):
#         print(" ",end="")
#     for j in range(i):
#         asc=chr(n)
#         print(asc,end=" ")
#         n+=1
#     print()
# #pattern
# r=5
# l=10
# e=l
# for i in range(1,r+1):
#     e=l
#     for j in range(i):
#       print(e,end=" ")
#       e-=2
#     print("\r")

#pattern
# r=int(input("Enter the range:"))
# for i in range(0,r+1):
#     for j in range(r-i,0,-1):
#         print(j,end=" ")
#     print()

#pattern
# r=int(input("Enter the range:"))
# for i in range(1,r,2):
#     for j in range(0,i):
#         print(i,end=" ")
#     print()

#class
# l=int(input("Enter the length :"))
# b=int(input("Enter the width :"))
# class area:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def rec_area(self):
#         return self.l * self.b
#
# ob=area(l,b)
#
# print(ob.rec_area())

# class message:
#     def __init__(self,s):
#         self.s=s
#     def prnt(self):
#         print(f"name is {self.s}")
#
# x=message("sourav")
# x.prnt()

class sra:
    def __init__(self,v,t):
        self.v=v
        self.t=t

    def mothername(self):
        print(f"Mother name is {self.v}")

    def fathername(self):
        print(f"Father name is {self.t}")

class ramsan(sra):
    def __init__(self,v,t):
        super().__init__(v,t)

ob=ramsan("sandra","sourav")
ob.mothername()
ob.fathername()

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#
#   def printname(self):
#     print(self.firstname, self.lastname)
#
# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)
#
# x = Student("Mike", "Olsen")
# x.printname()

