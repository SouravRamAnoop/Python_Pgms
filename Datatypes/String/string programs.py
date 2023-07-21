#Remove special symbols / puntuation from a string
str1="/*jon is 2developer & music director"
# for i in str1:
#     if i.isalpha() or i==" ":
#         print(i,end="")

# To find two strings are Anagrams or not
# str1=input("Enter the string1 :")
# str2=input("Enter the string2 :")
# print(sorted(str1))
# print(sorted(str2))
# if sorted(str1)==sorted(str2):
#     print(f"{str1} and {str2} are Anagram")
# else:print(f"{str1} and {str2} are not Anagram")

#To find the length of a string without using alibrary function
# name=input("Enter the string :")
# count=0
# for i in name:
#     count=count+1
# print("length of the string is :",count)

#To check if a string is palindrome or not
# str1 =input("Enter the string :")
# if str1[0:] == str1[::-1]:
#     print(str1,"is palindrome")
# else:
#     print("It is not palindrome")

#Write a python code to remove all the repeating letters from a each words of a given sentence
str3=input("Enter the string :")
str2 = str3.split()
lst1=[]
print(str2)
for i in str2:
    str1=""
    for j in i:
        if j not in str1:
            str1=str1+j
    lst1.append(str1)
print(lst1)
    # print(lst1)
lst2=" ".join(lst1)
print(lst2)






