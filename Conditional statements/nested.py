
x = int(input("Enter a Number :"))
if x==40:
    print("it is forty")
elif x==10:
    print("it is ten")
else:

    if x > 10:
        print("It is above ten")
        if x<40:
            print("it is also below 40")
        else:
            print("it is also above 40")
    else:
        print("it is below 10")
