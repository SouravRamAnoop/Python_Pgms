# largest among list
# lst1=[10,25,16,89,76,120,245,2,800,432,255]
# lst1.sort()
# print("The largest number is",lst1[-1])
#




#count the number of string from a given string.stringlength is and fst and lst char are same
# lst2 =["sourav","srs","aba","yes","wow","srrs","ss","1221"]
# count=0
# for i in lst2:
#     if i[0] == i[-1] and len(i)>2:
#         # print(i)
#         count=count+1
# print("No.of strings are in lst2 :",count)
#




# python pgm to find common member in two strings
# lst1=["sourav","python",1234,9.5]
# lst2=["car","bus","python",2548,1234]
# count=0
# for i in lst1:
#     for j in lst2:
#         if i==j:
#          # print(i)
#          count=count+1
# print("The common members in lst1 and lst 2 are :",count)

#count unique values inside a list
list3=["bike","car","bus","car","bus","lorry","bike"]
list4=[]
count=0
for i in list3:
    if i not in list4:
        list4.append(i)
        count=count+1
print("unique values are :",count)
