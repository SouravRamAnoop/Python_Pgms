"""
map(functions,iterables)
"""

num1=[1,2,3,4]
num2=[4,6,7,8]
res=map(lambda x,y:x+y,num1,num2)
print(list(res))