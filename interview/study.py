# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
#
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
#
# p1 = Person("John", 36)
# p1.myfunc()

#fibnocii
# n1=0
# n2=1
# print(n1)
# print(n2)
# for i in range(1,10):
#     n3=n1+n2
#     print(n3)
#     n1=n2
#     n2=n3

#primenumber
# r=int(input("Enter the range :"))
# for i in range(2,r+1):
#     for j in range(2,i):
#       if i%j==0:
#         break
#     else:
#         print(i)

#2
# n=int(input("Enter the number :"))
# for i in range(2,n):
#     if n%i==0:
#         print("NOT PRIME")
#         break
# else:
#     print("PRIME")

#armstrong
# n=int(input("Enter the number :"))
# num=n
# l=len(str(n))
# a=0
# for i in range(0,l):
#     x=n%10
#     a=a+x**l
#     n=n//10
# if a==num:
#     print("armstrong")
# else:
#     print("not armstrong")

#anagrams
# s=input("Enter the string1 :")
# y=input("Enter the string2 :")
# if sorted(s)==sorted(y):
#     print("anagram")
# else:
#     print("not anagram")

# a=100
# b=20
# c=50
# if a>b and a>c:
#     print("a")
# elif b>a and b>c:
#     print("b")
# else:
#     print("c")

# s=input("Enter the string:")
# l1=[]
# c=0
# for i in s:
#     if i not in "aeiou":
#         l1.append(i)
#         c+=1
# print(l1)
# print(f"c={c}")

# s=["apple","banana","1","cherry"]
# x=" ".join(s)
# print(x)

# n=int(input("Enter the number :"))
# s=0
# for i in range(1,n+1):
#     s=s+i
# print(f"fact={s}")

# n1=int(input("Enter the number :"))
# n2=int(input("Enter the number :"))
# gcd=0
# for i in range(1,min(n1,n2)+1):
#     if n1%i==0 and n2%i==0:
#         gcd=i
# print(gcd)

# r=int(input("Enter the range :"))
# for i in range(r,0,-1):
#     for j in range(0,r-i):
#         print(" ",end="")
#     for j in range(0,i):
#         print("* ",end="")
#     print()
# r=5
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# r=5
# n=1
# for i in range(1,r+1):
#     for j in range(0,i):
#         print(n,end=" ")
#         n=n+1
#     print()
r=5
s=5
# for i in range(0,r+1):
#     for j in range(i,-1,-1):
#         print(2**j,end=" ")
#     # s=s-1
#     print()

# c=input("Enter a character :")
# l=["a","e","i","o","u"]
# g=c.lower()
# if g in l:
#     print("vowel")
# else:
#     print("not vowel")
# n=34558
# rev=0
# while n>0:
#     x=n%10
#     rev=rev*10+x
#     n=n//10
# print(rev)

# r=5
# n=1
# for i in range(1,r+1,2):
#     for j in range(i):
#         print(n,end=" ")
#         n=n+1
#     print()

# r=6
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for k in range(i-1,0,-1):
#         print(k,end=" ")
#     print()

# r=5
# n=1
# for i in range(0,r):
#     for j in range(0,i+1):
#         print(n,end=" ")
#     n=n+2
#     print()

# r=5
# for i in range(1,r+1):
#     for j in range(0,r-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end="")
#     print()

# r=5
# for i in range(r,0,-1):
#     # for j in range(0,r-i):
#     #     print(" ",end="")
#     for j in range(0,i):
#         print("* ",end="")
#     print()

# r=5
# for i in range(1,r+1):
#     for j in range(0,r-i):
#         print(" ",end=" ")
#     for j in range(0,i):
#         print("* ",end="")
#     print()

# r=5
# for i in range(0,r):
#     for j in range(0,i+1):
#         print("* ",end="")
#     print()
# for i in range(r-1,0,-1):
#     for j in range(0,i):
#         print("* ",end="")
#     print()

# r=5
# for i in range(1,r+1):
#     for k in range(0,r-i):
#         print(" ",end="")
#     for j in range(0,i):
#         print("* ",end="")
#     print()
# for i in range(r-1,0,-1):
#     for k in range(0,r-i):
#         print(" ",end="")
#     for j in range(0,i):
#         print("* ",end="")
#     print()

# r=int(input("Enter the range :"))
# sum=0
# for i in range(1,r+1):
#     sum=sum+i**2
# print(sum)
# l1=[1,2,3,4]
# l1[0],l1[-1]=l1[-1],l1[0]
# print(l1)
# l1=[]
# for i in range(-4,9):
#     if i<0:
#        l1.append(i)
# print(l1)

# s="i am sourav"
# x=s.split()
# print(s)
# for i in x:
#     print(i)
num = str(input("Enter the number :"))
print(int(num,17))