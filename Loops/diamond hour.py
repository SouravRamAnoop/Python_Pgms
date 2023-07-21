rows = int(input("Enter your rows :"))
for i in range(rows,0,-1):
    for j in range(rows-i):
     print(" ",end = " ")
    for k in range(i):
     print("*"," ", end = " ")
    print()
for a in range(1,rows+1):
    for c in range(rows-a):
        print(" ",end = " ")
    for b in range(a):
        print("*", " ", end = " ")
    print()
