#Calculator

class Calculator:
    def addition(self):
        print(a+b)

    def substraction(self):
        print(a-b)

    def multiplication(self):
        print(a*b)

    def division(self):
        print(a/b)

a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))

ob=Calculator()
ch=int(input("Enter the choice :"))

if ch>0:
    print("1)Addition")
    print("2)Substraction")
    print("3)Multiplication")
    print("4)Division")

if ch==1:
    ob.addition()
elif ch==2:
    ob.substraction()
elif ch==3:
    ob.multiplication()
elif ch==4:
    ob.division()