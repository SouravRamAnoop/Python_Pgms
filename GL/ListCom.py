# 1) Python Program to Square Each Odd Number in a List using List Comprehension

# s=[i*i for i in range(1,20) if i%2==1 ]
# print("s=",s)

#2)Python List Comprehension: Count the number of spaces in a string
# x="hello friends.welcome to the world of python"
# y=[i for i in x if i ==" " ]
# print("y=",y)
# print("number of spaces =",len(y))


#3)Create a list of all the consonants in the string
# s="Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
# b=["a","e","i","o","u","A","E","I","O","U"," "]
# x=[i for i in s if i not in b]
# z=" ".join(x)
# print(x)


#4)'''Find all of the words in a string that are less than 4 letters'''
# sentence = 'On a summer day somner smith went simming in the sun and his red skin stung'
# x=sentence.split()
# z=[i for i in x if len(i)<4]
# print(z)

# 5)''Get the index and the value as a tuple for items in the list ["hi", 4, 8.99, 'apple', ('t,b','n')].
# Result would look like [(index, value), (index, value)]

l=["hi", 4, 8.99, 'apple', ('t,b','n')]
x=[i for i in enumerate(l)]
print(x)