"""wap which will return true if the two given integer values are equal or
their sum or difference is 5"""
# x=int(input("Enter the first number:"))
# y=int(input("Enter the second number :"))
# def check(x,y):
#     if x==y or x+y==5 or x-y==5:
#         return True
#     return -1
# print(check(x,y))

#accept integer ,compute the value n+nn+nnn
# x=int(input("Enter the number :"))
# z=0
# a=0
# for i in range(1,6):
#     z=(z*10)+x
#     a=a+z
# print(a)

#filter a possitive numbers from a list

# x=filter(lambda x:x%2==1,[10,25,19,27,24])
# for i in x:
#     print(i)

#sum of first n primenumbers
# r=int(input("Enter the range:"))
# z=0
# for i in range(2,r+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         z=z+i
#         print(i)
# print(z)

# n=int(input("Enter the number:"))
# for i in range(2,n):
#     if n%i==0:
#         break
# else:
#     print(f"{n} is a prime number")

# from array import *
# s=array("i",[10,20,30])
# s.append(40)
# print(list(s))

# print(s)

#pattern
# x="python"
# s=""
# for i in x:
#     s=s+i
#     print(s)

#pattern
# asciinumber = 65
# for i in range(0,7):
#     for j in range(0,i+1):
#         character=chr(asciinumber)
#         print(character,end=" ")
#         asciinumber+=1
#     print()

# s="sourav"
# l=list(s)
# l.reverse()
# s="".join(l)
# print(s)

# s="apple"
# z=""
# for i in s:
#     z=i+z
# print(z)

#pattern

# r=int(input("Enter the range :"))
# for i in range(0,r):
#     for j in range(0,r-i):
#         print(j,end=" ")

#     print()

#pattern


#pattern
n=1
for i in range(1,6):
    for j in range(0,i):
        print(n,end=" ")
        n=n+1
    print()
