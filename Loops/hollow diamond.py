row = int(input("Enter your row:"))
for i in range(0,row):
    for j in range(row-i-0):
        print(" ",end = " ")
    for k in range(0,i+1):
        if k == 0 or k == i:
            print("* ",end = " ")
        else:
            print("   ",end = " ")
    print()
for a in range(row,0,-1):
    for b in range(row-a):
        print(" ",end = " ")
    for c in range(a):
        if k == 0 or k == i-1:
             print("*", " ", end=" ")
        else:
             print("   ", end=" ")
    print()