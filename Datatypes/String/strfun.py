# s=input("Enter Your name :")
# first=s[0]
# l=len(s)
# mid=int(l/2)
# last=l-1
# x=first+s[mid]+s[last]
# print("New string is :",x )

# s1="hello"
# s2="world"
# l=len(s1)
# x=int(l/2)
# y=s1[0:x]+s2+s1[x:]
#  print("After appending new string",y)

# str1="HeLLO World"
# lower = ""
# upper = ""
# special = ""
# for i in str1:
#     if i.islower():
#         lower=lower+i
#         print(lower)
#     elif i.upper():
#         upper=upper+i
#         print(upper)
#     else:
#         special=special+i
#         print(special)
# print("Result is :",lower+upper+special)

str1="p@#$yn26at^i5ve"
l=x=y=0
for i in str1:
    if i.isalpha():
        print(i,end =" ")
        l=l+1
    elif i.isdigit():
        print(i,end=" ")
        x=x+1
    else:
        print(i,end=" ")
        y=y+1
print("number of alphabets is",l)
print("number of digit is",x)
print("number of special characters are",y)