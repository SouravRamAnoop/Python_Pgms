def search(l1, x):
    for i in range(len(l1)):
        if l1[i] == x:
            print("element is found in the index :",i)
            break
    else:
        print("not found")
l1=[12,25,33,48,85,69,12]
x=69
search(l1,x)