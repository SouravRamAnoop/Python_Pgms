#
# num1 = int(input("Enter your fisrt number :"))
# num2 = int(input("Enter Your second number :"))
# num3 = int(input("Enter your third number :"))
#
# if num1>num2 and num1>num3 :
#     print(num1," is greater")
# elif num1==num2 and num1>num3:
#     print(num1,"&",num2,"are greater")
# elif num1==num3 and num3>num2:
#     print(num1,"&",num3,"are greater")
# elif num2==num3 and num2>num1:
#     print(num2, "&", num3, "are greater")
# elif num2>num1 and num2>num3 :
#     print(num2,"is greater")
# else:
#     print(num3,"is greater")

# mark = int(input("Enter your mark :"))
# if mark>100 or mark<0:
#     print("not valid")
# elif mark>=80 and mark<=100:
#     print("A Grade")
# elif mark>=60:
#     print("B Grade")
# elif mark >= 50:
#     print("C Grade")
# elif mark >= 45:
#     print("D Grade")
# elif mark>=25:
#     print("E Grade")
# else:
#     print("F Grade")

n = int(input("ENTER A NUMBER :"))

if n>10 and n>40 :
    print(n,"is above 10 and above 40")
    if n > 10 and n < 40:
        print(n, "is above 10 and below 40")
        if n < 10 and n < 40:
            print(n, "is below 10 and below 40")
            if n == 10 and n == 40:
                print("it is",n)
else:print("invalid")





