"""
The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
"""
name = "Sourav"
age=24
print("%s is %d years old"%(name,age))
print('{} is {} years old'.format(name,age))
print(f'{name} is {age} years old')

s=5
y=10
print(f'There are {s*y} apples')