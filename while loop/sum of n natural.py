"""
While loop
To repeat a block of code repeatedly,
as long as the condition is true
"""
# i=1
# while i<=10:
#     print(i)
#     i+=1

# i=10
# while i>=1:
#     print(i)
#     i-=1

#
# num=int(input("enter the number:"))
# sum=0
# i=1
# while i<=num:
#     sum+=i
#     i+=1
# print(sum)

# i=1
# while i<=10:
#     if i%2==0:
#        print(i)
#     i+=1

# n=int(input("Enter the number :"))
# while n>0:
#     if n%2==0:
#        print("It is a even number")
#        break
#     elif n%2==1:
#         print("It ia odd number")
#         break
# else:
#     print

# n=int(input("Enter the Number :"))
# while n>0:
#     x=n//10
#     z =n%10
#
#     print(z,x)
#     break


n=int(input("Enter the Number :"))
reverse=0
temp=n
while temp!=0:
    x=temp%10
    reverse=reverse*10+x
    temp//=10
print("reverse of number=",reverse)







