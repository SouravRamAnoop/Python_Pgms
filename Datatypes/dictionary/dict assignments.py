#1.convert two list in to dictionary
# l1=["name","age","course"]
# l2=["sourav",25,"python"]
# dict1={}
# i=0
# while i<3:
#     a=l1[i]
#     b=l2[i]
#     c={a:b}
#     dict1.update(c)
#     i+=1
# print(dict1)
#2.merging of two dictionaries

# dict1={"name":"sourav",
#        "age":25,
#        "course":"python"}
# dict2={"item":"woods",
#        "qty":25,}
# dict1.update(dict2)
# print(dict1)

#3.print the value of key "history from below dict"
# sampleDict={"class":{"student":{"name":"mike","marks":{
#     "physics":70,"history":80 }}}}
# a=sampleDict["class"]["student"]["marks"]["history"]
# print("value =",a)

#4.initialize dictionaries with default values
# r=int(input("Enter the no.of key-value pair :"))
# d1={}
# for i in range(r):
#     key=input("Enter the key :")
#     value=input("Enter the value :")
#     d1.setdefault(key,value)
# print(d1)

#5.create dictionary by extracting the keys from a given dictionary
# d1={"a":1,"b":2,"c":3}
# d2={}
# for i in d1:
#     d2.setdefault(i)# c=d1.fromkeys(a,b)
# print(d2)

# method 2
# ---------
# d1 = {"a": 1, "b": 2, "c": 3}
# a=d1.keys()
# b=0
# print(c)

#6.delete a list of keys from a dictionary
# d1={"item":"bat","qty":2,"rate":3000}
# l1=["item","qty"]
# for i in l1:
#     d1.pop(i)
# print(d1)

#7.check if a value is exists in a dictionary
# d1={"item":"bat","price":800,"shop":"SRA"}
# x=input(("Enter your value :"))
# for i in d1:
#     if x==d1.get(i):
#         print(f"{x} is exists")
#         break
# else:
#     print(f"{x} is not exists")

#8.rename key of dictionary
#
# d1={"name":"sourav","age":25,"course":"python"}
# d1["AGE"]=d1.pop("age")
# print(d1)

#get the key of minimum values from dict
# d1 = {"a": -2, "b": 2, "c": 3,"d":1}
# a=d1.values()
# b=min(a)
# print(b)

sampleDict={"class":{"student":{"name":"mike","marks":{
   "physics":70,"history":80 }}}}
a=sampleDict.keys()
print(a)
