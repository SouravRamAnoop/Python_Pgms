from functools import reduce

s=[1,2,3,4,5]
y=reduce(lambda x,y:x+y,s)
print(y)