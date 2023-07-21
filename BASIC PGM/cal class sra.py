class calc():
    def __init__(self,num1,num2):
       self. num1 = num1
       self.num2 = num2
    def sum(self):
        return self.num1+self.num2
        # print("sum=",self.num1+self.num2)

    def sub(self):
        return self.num1-self.num2
        # print("dif=",self.num1-self.num2)
num1 = int(input("enter your first number: "))
num2= int(input("enter your second number: "))

ob1 = calc(num1,num2)
print("sum=",ob1.sum())
print("sub",ob1.sub())





