#pgm to print dictionary ,the value is squre of key
# n=int(input("Enter the Number :"))
# d1={}
# for i in range(1,n+1):
#     d1[i]=i*i
# print(d1)

#converting to list and tuple a sequence of values
# n=input("values :")
# l=n.split(",")
# t=tuple(l)
# print(l)
# print(t)

#take input as sentence and count letters and number
# s=input("Enter the sentence :")
# c=0
# d=0
# for i in s:
#     if i.isalpha():
#      c+=1
#     elif i.isdigit():
#      d+=1
# print("letters in sentence =",c)
# print("Numbers in sentence =",d)

#factorial of a given number
n=int(input("Enter the number :"))
f=1
for i in range(n,0,-1):
    f=f*n
    print(f)
print(f)