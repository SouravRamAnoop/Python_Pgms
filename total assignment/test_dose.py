# n=int(input("Enter the range:"))
# for i in range(1,n+1):
#     for k in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for k in range(n-i):
#         print("",end="")
#     for j in range(i):
#         print("* ",end=" ")
#     print()

n=int(input("Enter the range:"))
for i in range(n+1):
    for j in range(n+1):
        if (i==0 and j>0 and j<5) or (i==1 and j==1) or (i==1 and j==4) or (i==2 and j==1) or (i==2 and j==4):
            print("* ",end=" ")
        else:
            print(" ",end="")
        if (i==3 and j>0 and j<5) or (i==4 and j==1) or (i==4 and j==3) or (i==5 and j==1) or (i==5 and j==4) or (i==6 and j==1) or (i==6 and j==5):
            print("*",end="")
        else:
            print("",end="")
    print()



