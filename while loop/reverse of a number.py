n=int(input("Enter the Number :"))
reverse=0
while n!=0:
    x=n%10
    reverse=reverse*10+x
    n//=10
print("reverse of number =",reverse)

