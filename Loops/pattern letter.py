n =input("Enter a Name :")
char = len(n)
for i in range(1,char+1):
     for j in range(i):
         print(n[j], end = " ")
     print()