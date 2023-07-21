
# r=int(input("Enter the range :"))
#
# for i in range(r,0,-2):
#     for j in range(r-i):
#         print(" ",end="")
#     for k in range(i):
#         print("* ",end="")
#     print()

#
# r=int(input("Enter the range :"))
# for i in range(1,r+1):
#     for j in range(r-i):
#         print(" ",end="")
#     for k in range(i):
#         print(k+1,end=" ")
#     print()

#last element in a list

# s=[1,2,3,2,6]
# print(f'last element = {s[-1]}')

#area of triangle
# b=int(input("Enter the base of triangle :"))
# h=int(input("enter the height of triangle :"))
#
# Area = (b*h)/2
# print(f"Area of Triangle = {Area}")


# def find_pairs(arr, target_sum):
#     pairs = []
#     n = len(arr)
#
#     for i in range(n):
#         for j in range(i+1, n):
#             if arr[i] + arr[j] == target_sum:
#                 pairs.append((arr[i], arr[j]))
#
#     return pairs
#
#
# arr = [2, 3, 4, 5, 6]
# target = 9
#
# result = find_pairs(arr, target)
#
# # Print the pairs
# if result:
#     print(f"Pairs that give a sum of {target}:")
#     for pair in result:
#         print(pair)
# else:
#     print(f"No pairs found that give a sum of {target}.")


# my_list = [
#     {'name': 'John', 'age': 25},
#     {'name': 'Alice', 'age': 20},
#     {'name': 'Bob', 'age': 30}
# ]
#
# # Sort the list by the 'age' value in each dictionary
# sorted_list = sorted(my_list, key=lambda x: x['age'])
#
# # Print the sorted list
# for item in sorted_list:
#     print(item)



# movies=[
# {"language":"malayalam","name":"2018","rating":5,"year":2023,"genres":["mystery"]},
# {"language":"malayalam","name":"aadujeevitahm","rating":5,"year":2023,"genres":["fiction","drama"]},
# {"language":"malayalam","name":"neymar","rating":4,"year":2023,"genres":["action","comedy","romance"]},
# {"language":"malayalam","name":"sunny","rating":4,"year":2022,"genres":["drama","thriller"]},
# {"language":"malayalam","name":"12th man","rating":3,"year":2022,"genres":["drama","thriller"]},
# {"language":"thamil","name":"vikram","rating":5,"year":2022,"genres":["action","thriller"]},
# {"language":"thamil","name":"jai bhim","rating":5,"year":2021,"genres":["mystery","crime"]},
# {"language":"hindi","name":"pathaan","rating":5,"year":2023,"genres":["action","thriller"]},
# ]
#
# for i in movies:
#     print(i["name"])
#
# for i in movies:
#     if "mystery" in i["genres"]:
#         print(i["name"])
# #
# for i in movies:
#     if i["rating"] == 5:
#         print(i["name"])

# for i in movies:
#     if i["year"] == 2023:
#         print(i["name"])

#
# sort_movie = sorted(movies,key=lambda x:x["rating"],reverse=True)
# for i in sort_movie:
#     print(i["name"])


# for i in movies:
#     if i["language"] == "malayalam":
#         print(i["name"])


#fibanocci
#
# n=int(input("Enter the Number :"))
# a,b=0,1
#
# while b<n:
#     a,b=b,a+b
#
# if b==n:
#     print(f"{n} is fibanocci number")
#
# else:
#     print(f"{n} is not fibanocci number")


#series
# r=int(input("Enter the range :"))
# n1=0
# n2=1
# print(n1)
# print(n2)
# for i in range(r):
#     n3=n1+n2
#     print(n3)
#     n1=n2
#     n2=n3

# r=int(input("Enter the range :"))
# for i in range(r,0,-1):
#     for j in range(0,r-i):
#         print(" ",end="")
#     for k in range(i):
#         print("* ", end="")
#     print()
#
# for i in range(1,r+1):
#     for j in range(0,r-i):
#         print(" ",end="")
#     for k in range(i):
#         print("* ", end="")
#     print()
#
# import array
#
# arr1=array.array('i',[2,3,4,5])
# arr2=array.array('i',[4,3,6,7])
# l=len(arr1)
# for i in range(l):
#     for j in range(l):
#         if arr1[i]==arr2[j]:
#             print(f"common elements  are {arr1[i]}")

# import array
#
# arr1=array.array('i',[2,3,4,5])
# arr2=array.array('i',[4,3,6,7])
#
# s1=set(arr1)
# s2=set(arr2)
# s3=s1.intersection(s2)
# print(s3)

#armstrong
# n=int(input("Enter the number :"))
# l=len(str(n))
# num=n
# res=0
#
# for i in range(l):
#     m=n%10
#     res=res+m**l
#     n=n//10
#
# if num==res:
#     print(f"{num} is armstrong number")
# else:
#     print(f"{num} is not armstrong number")


# def pairs(arr,sum):
#
#     l=len((arr))
#     print(l)
#     lst=[]
#
#     for i in range(l):
#         for j in range(i+1,l):
#             if arr[i]+arr[j]==sum:
#                 lst.append((arr[i],arr[j]))
#     return lst
# arr=[1,2,3,4,6,7,10]
# sum=9
# result=pairs(arr,sum)
#
# if result:
#     for i in result:
#         print(i)

# r=int(input("Enter the range :"))
# for i in range(r,0,-1):
#     for j in range(r-i):
#         print(" ",end="")
#     for k in range(i):
#         print("* ",end="")
#     print()

# import random
# s=random.randrange(1,100)
# print(s)

