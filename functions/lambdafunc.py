"""
Lambda Function
---------------
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
"""

# x=lambda a: a+10
#
# print(x(5))
#
# y=lambda b,c,d: b+c*d
#
# print(y(10,2,3))
#
# z= lambda :print("Sourav")
# z()
#
# f= lambda c:print(c)
# f("sra")

#sort a list of dictionary using lamda
# a=[("english",88),("maths",77),("hindi",90)]
# a.sort(key=lambda a:a[0])
# print(a)

# s=[{"name":"sourav"},{"age":25},{"course":"python"}]
# s.sort(s,key=lambda s:s[0])
# print(s)
"""
extract year,month,date and time using lamba
2022-01-15 09.03.32
"""
# import datetime
#
# now=datetime.datetime.now()
# print(now)
# year=lambda x:x.year
# month=lambda x:x.month
# day=lambda x:x.day
# t=lambda x:x.time()

# print(year(now))
# print(month(now))
# print(day(now))
# print(t(now))

# def num(n):
#     return lambda a:a*n
#
# x=num(7)
# print(x(6))

def cube(y):
	return y*y*y


lambda_cube = lambda y: y*y*y


# using function defined
# using def keyword
print("Using function defined with `def` keyword, cube:", cube(5))

# using the lambda function
print("Using lambda function, cube:", lambda_cube(5))
