row = int(input("Enter your row:"))
A=65
for i in range(row):
    for j in range(row):
        print(chr(A), end = " ")
        A=A+1
    print()
