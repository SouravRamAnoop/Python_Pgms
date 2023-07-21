#Swapping of two tuples
# T1=("A","B")
# T2=("34","65")
# T1,T2=T2,T1
# print("T1 =",T1)
# print("T2 =",T2)


#second largest num in list
# n=[12,24,10,58,5,7]
# n.sort()
# print("second largest number =",n[-2])

# wap to store n number of sports in tuple.Accept n from user
# n=int(input("Enter the number of elements :"))
# L1=[]
# for i in range(n):
#     s=input("Enter the elements:")
#     L1.append(s)
# tup1=tuple(L1)
# print("Tuple =",tup1)

#WAP to remove number accept from the user
Tup=(12,15,18,25,34,49,43,52,60,75)
print("Tup=",Tup)
n=int(input(("Enter the number to be delete :")))
L1=list(Tup)
if n in L1:
    L1.remove(n)
Tup=tuple(L1)
print("After deletion T1 =",Tup)

