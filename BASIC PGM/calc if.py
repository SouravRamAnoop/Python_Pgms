# Simple calculator
print("select your operation:\n1.Addition \n2.substraction\n3.multiplication\n4.division")
ch = int(input("ENTER YOUR CHOICE :"))
if ch==1 or ch==2 or ch==3 or ch==4:
    print("Your choice is : ", ch)

    x=int(input("Enter your first Number : "))
    y=int(input("Enter your second number : "))


if ch==1:
    print(x+y)
elif ch==2:
    print(x-y)
elif ch==3:
    print(x*y)
elif ch==4:
    print(x/y)
else:
    print("You entered incorrect choice")


