
class check:
    def __init__(self,):
        self.n=[]
    def add(self,a):
        self.n.append(a)
    def remove(self,b):
        self.n.remove(b)
    def dis(self):
        return self.n

obj=check()

ch=1
while ch!=0:
    print("0.Exit")
    print("1.Add")
    print("2.Display")
    print("3.Delete")
    ch = int(input("Enter the choice :"))
    if ch==1:
        n = int(input("Enter the number to add :"))
        obj.add(n)
        print(obj.dis())
    elif ch==2:
        n = int(input("Enter the number to diplay :"))
        print(obj.dis())
    elif ch==3:
        n = int(input("Enter the number to remove :"))
        obj.remove(n)
        print(obj.dis())
    elif ch==0:
        print("Exiting")
    else:
        print("Invalid choice")

print()