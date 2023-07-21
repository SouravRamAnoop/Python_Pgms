a = int(input("enter the 1st number :"))
b = int(input("enter the 2nd number :"))
c=input("enter the choice(+,-,*,/,**,%) = ")
if c == '+':
    print("The sum is ",a+b)
elif c == '-':
    print("difference is ",a-b)
elif c == '*':
    print("product is ",a*b)
elif c == '/':
    print("division is ",a/b)
elif c == '**':
    print("exponent is ",a**b)
elif c == '%':
    print("modulous is ",a%b)