# last element in a list

# s=[1,2,3,2,6]
# print(f'last element = {s[-1]}')

#area of triangle
# b=int(input("Enter the base of triangle :"))
# h=int(input("enter the height of triangle :"))
#
# Area = (b*h)/2
# print(f"Area of Triangle = {Area}")
#
# def common_elements(arr1, arr2):
#     set1 = set(arr1)
#     set2 = set(arr2)
#     elements = set1.intersection(set2)
#     return list(elements)
#
#
# array1 = [10, 20, 3, 40, 5]
# array2 = [40, 5, 6, 3, 8]
# result = common_elements(array1, array2)
# print(f'common elements = {result}')


# r=int(input("Enter the range :"))

# for i in range(1,r+1,2):
#     for j in range(r-i):
#         print(" ",end="")
#     for k in range(i):
#         print("* ",end="")
#     print()


# import random
#
# my_list = [1, 2, 3, 4, 5]
#
# random_item = random.choice(my_list)
# print(random_item)

#pattern luminar


# s="luminar"
# x=""
# for i in s:
#     x+=i
#     print(x,)

movies=[
{"language":"malayalam","name":"2018","rating":5,"year":2023,"genres":["mystery"]},
{"language":"malayalam","name":"aadujeevitahm","rating":5,"year":2023,"genres":["fiction","drama"]},
{"language":"malayalam","name":"neymar","rating":4,"year":2023,"genres":["action","comedy","romance"]},
{"language":"malayalam","name":"sunny","rating":4,"year":2022,"genres":["drama","thriller"]},
{"language":"malayalam","name":"12th man","rating":3,"year":2022,"genres":["drama","thriller"]},
{"language":"thamil","name":"vikram","rating":5,"year":2022,"genres":["action","thriller"]},
{"language":"thamil","name":"jai bhim","rating":5,"year":2021,"genres":["mystery","crime"]},
  {"language":"hindi","name":"pathaan","rating":5,"year":2023,"genres":["action","thriller"]},
]

# for i in movies:
#     print(i["name"])

# for i in movies:
#     if "mystery" in i["genres"]:
#         print(i["name"])
#
# for i in movies:
#     if i["rating"] == 5:
#         print(i["name"])

# for i in movies:
#     if i["year"] == 2023:
#         print(i["name"])


# sort_movie = sorted(movies,key=lambda x:x["rating"])
# sort_movie.reverse()
# for i in sort_movie:
#     print(i["name"])


# for i in movies:
#     if i["language"] == "malayalam":
#         print(i["name"])


#Interview pattern

# r=int(input("Enter the range :"))
#
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print(i*j,end=" ")
#     print()


#leap year pgm
# year=int(input("Enter the year:"))
#
# if year % 400==0 or (year % 100!=0 and year % 4==0):
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")


#no of elements of list
# l=[1,2,3,4,5]
# c=0
# for i in l:
#     c=c+1
# print(f"No of elements = {c}")

#second method
# s=[1,2,3,4,5]
# length=len(s)
# print(f"No of elements = {length}")

#pair
# def find_sum_pairs(arr, target_sum):
#     pairs = []
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == target_sum:
#                 pairs.append((arr[i], arr[j]))
#
#     return pairs
#
#
# arr = [2, 3, 4, 5, 6]
# target_sum = 9
# result = find_sum_pairs(arr, target_sum)
#
# print("Pairs which give sum =", target_sum, ":", result)

#fibonacci or not
def is_fibonacci_number(num):
    if num == 0 or num == 1:
        return True

    # Check if the number is a Fibonacci number
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
        if b == num:
            return True

    return False

# Test the function
number = int(input("Enter a number: "))
is_fibonacci = is_fibonacci_number(number)

if is_fibonacci:
    print(number, "is a Fibonacci number.")
else:
    print(number, "is not a Fibonacci number.")
