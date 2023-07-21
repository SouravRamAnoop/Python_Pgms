# rows = int(input("Enter the row :"))
# a=0
# for i in range(rows):
#     for j in range(i+1):
#         print(a+1, end=" ")
#         a=a+1
#     print()
# #
# for i in range(rows):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()
#
# row=int(input("Enter the row :"))
# for i in range(1,row):
#     for j in range(-1+i,-1,-1):
#         print(2**j,end=" ")
#     print()

# row=int(input("Enter the row :"))
# for i in range(row,0,-1):
#     for j in range(0,i):
#         print("5",end=" ")
#     print()

row=int(input("Enter the row :"))
s=5
for i in range(row,0,-1):
    for j in range(0,i):
        print(s,end=" ")
    print()
    s=s-1
























