#
# for i in range(65,91):
#     print(chr(i),"",end = " ")
#
# for i in range(97, 123):
#     print(chr(i), "", end=" ")

rows = int(input("Enter the row :"))
A = 65
for i in range(rows):
    for j in range(i+1):
        print(chr(A), " " , end = " ")
        A=A+1
    print()

