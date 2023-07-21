# CROSS PATTERN
# row =8
# for i in range(row+1):
#     for j in range(row+1):
#         if i==j or i+j==8:
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()

# CROSS NUMBER PRINTING
# row = int(input("Enter the row :"))
# for i in range(row,0,-1):
#     for j in range(row-i):
#         print(" ",end="")
#     for k in range(i,0,-1):
#         if k==1 or k==i:
#             print(row-i+1,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
# for i in range(1,row):
#     for j in range(row-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         if k==0 or k==i:
#             print(row-i,end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# pgmfor heart pattern
# row=int(input("Enter the row:"))
# for x in range(row,0,-2):
#     if x==10 or x==8:
#         continue
#     for y in range(0,int(x/2)):
#         print(" ",end="")
#     for z in range(0,row-x+1):
#         print("*",end="")
#     for a in range(0,x-1):
#         print(" ",end="")
#     for b in range(0,row-x+1):
#         print("*",end="")
#     print()
# for i in range(row,0,-1):
#     for k in range(0,row-i+1):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()

# name first letter printing
for i in range(7):
    for j in range(5):
        if (i == 0 and j > 0) or (i == 1 and j == 0) or (i == 2 and j == 0) or (i == 3 and j > 0):
            print("*",end="")
        else:
            print(" ",end="")
        if (i == 4 and j == 4) or (i == 5 and j == 4) or (i == 6 and j < 4):
            print("*", end="")
        else:
            print(" ", end="")
    print()



