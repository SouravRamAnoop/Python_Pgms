# # palindrome or not
# str1= input("Enter the string :")
# if str1[0:]==str1[::-1]:
#     print(str1,"is a palindrome")
# else:
#     print("It is not palindrome")

#vowels count in astring
s=input("Enter a string :")
vowels = 0
for i in s:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        vowels = vowels+1
print("vowels = ",vowels)

