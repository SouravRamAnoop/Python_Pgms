
row =int(input("Enter the rows :"))
# for i in range(1,row+1):
#     for j in range(row-i):
#         print(" ",end =" ")
#     for k in range(i):
#         print("*  ",end=" ")
#     print()
for a in range(row-1,0,-1):
    for b in range(row-a):
        print(" ",end =" ")
    for c in range(a):
        print("*  ",end=" ")
    print()