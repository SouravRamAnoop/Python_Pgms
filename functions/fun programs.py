#sum of n natural numbers
# n = 10
#
# def natural():
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i
#     print(sum)
# natural()

#to find max of three numbers

def maximum():
    n1=3
    n2=6
    n3=10
    if n1>n2:
        if n1>n3:
            print("MAX=",n1)
        else:
            print("MAX=",n3)
    else:
        print("MAX=",n2)
maximum()