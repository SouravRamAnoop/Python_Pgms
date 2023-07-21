row = int(input("Enter the row :"))
for i in range(row):
    for j in range(row):
        if i==0 or i==row-1:
            print("* ",end="")
        elif j==0 or j==row-1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()