
num1 = int(input("Enter your fisrt number :"))
num2 = int(input("Enter Your second number :"))
num3 = int(input("Enter your third number :"))

if num1>num2 and num1>num3 :
    print("num1 is greater")
elif num2>num1 and num2>num3 :
    print(" num2 is greater")
elif num3>num1 and num3>num2:
    print(" num3 is greater")
elif num1==num2==num3:
    print("All are equal")
else:
    if num1==num2 and num1>num3:
        print("num1 and num2 is greater")
    if num1==num3 and num1>num2:
        print(" num1 and num3 is greater")
    if num2==num3 and num2>num1:
        print("num2 and num3 is greater")

