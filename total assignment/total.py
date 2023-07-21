# #wap to reverse a number
# a=int(input("Enter the number :"))
# b=str(a)
# c=b[-1::-1]
# print(f"Reverse of {a} =",int(c))

#check two strings are anagram
# a="race"
# b="care"
# if sorted(a)==sorted(b):
#     print(a,"and",b, "are anagrams")

#strings are paliandrome or not
# a=input("Enter the first string:")
# if a[-1::-1]==a[0:]:
#     print(a,"is palindrome")
# else:
#     print("it is not palindrome")

#leap year or not
# x=int(input("Enter the year :"))
# if x%4!=0:
#     print(f"{x} is not a leap year")
# elif x%100!=0:
#     print(f"{x} is a leap year")
# elif x%400!=0:
#     print(f"{x} is not leap year")
# else:
#     print(f"{x} is leap year")

#gcd from 2 numbers
# x=int(input("Enter the first number:"))
# y=int(input("Enter the second number :"))
# gcd=1
# for i in range(1,min(x,y)+1):
#     if x%i==0 and y%i==0:
#      gcd=i
# print(f"greatest common divisor of {x} and {y} =",gcd)

#vowel or consonant
# l=input("Enter a charcter:")
# if "a" or "e" or "i" or "o" or "u" in l:
#     print(f"{l} is a vowel")
# elif "h" or "r" or "w" or "y" in l:
#     print(f"{l} is sometimes consonant")
# else:
#     print(f"{l} is a consonant")

#vowel or consonant
# l=input("Enter a charcter:")
# a=["a","e","i","o","u"]
# b=["h","r","w""y"]
# for i in a:
#     if i in l:
#      print(f"{l} is a vowel")
#      break
# else:
#     print(f"{l} is a consonant")

#armstrong or not
# n=int(input("Enter the number :"))
# l=len(str(n))
# b=0
# c=n
# for i in range(l):
#     a=n%10
#     b=b+a**l
#     n=n//10
# if b==c:
#     print(f"{c} is armstrong")
# else:
#     print(f"{c} is not armstrong")

# s="abacus"
# d=s
# for i in s:
#     if i in d:
#         print(i)

