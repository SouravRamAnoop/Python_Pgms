# print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
# op=int(input("select operation:"))
#
# x = int(input("Enter first number:"))
# y = int(input("Enter second number:"))
#
# if op==1:
#     print("sum=",x+y)
# elif op==2:
#     print("differnce=",x-y)
# elif op==3:
#     print("Multiply=",x*y)
# elif op==4:
#     print("Division=",x/y)
# else:
#     print("fool...!")
row=int(input("Enter the row:"))
for i in range(row):
    for j in range(row):
        if i==0 and j<=row:
            print("* ",end="")
print()
for i in range(row):
    for j in range(row):
        if j==0 or j==row-1:
            print("* ",end="")
        else:
            print("",end="")
print()


for k in range(row):
    for m in range(row):
        if k==0 and m<=row:
            print("* ",end="")

