#product of two numbers using recursion
def product(a,b):
    if a==1or b==1:
        return a
    else:
        p=a+product(a,b-1)
        return p

print("product =",product(10,2))

#reverse of a string using recursion
#
def reverse(str):
    if len(str)==0:
        return str
    else:
        x=reverse(str[1:])+str[0]
        print(x)
        return x
str=input("Enter the string :")
print(reverse(str))