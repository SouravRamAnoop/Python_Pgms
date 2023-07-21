import os
# file1=r"C:\Users\ASUS\PycharmProjects\PYTHONPROJECT1\file handling\sample.txt"
# if os.path.isfile(file1):
#     print(f"It is exist")
# else:
#     print("it is not exist")
#
# if os.path.isfile("sample2.txt"):
#     print("It is exist")
# else:
#     print("it is not exist")

#size of a file
# a=os.path.getsize("sample.txt")
# b=os.path.getsize("file_assignments.py")
# print(a)
# print(b)

#delete a lines from a file
# f=open("sample.txt","a")
# # lines=f.readlines()
# f.truncate()
# f.close()
#
# f=open("sample.txt","r")
# print(f.read())
# f=open("demofile.txt","w")
# f.write("hai all.how are you\nall the best")
# f.close()
#
# with open(r"demofile.txt","r+") as fp:
    # lines=fp.readlines()
    # fp.seek(1)
    # fp.truncate(20)
    #
    # print(fp.writelines(lines[0:]))

#search for a string in text file
# s="sourav"
# f=open("sra.txt","w")
# f.write(s)
# f.close()
# f=open("sra.txt","r")
# f5=f.read()
# f6=list(f5)
# "".join(f6)
# print(f6)
# # print(f5)
#
# for i in f5:
#     print(i)
#     if i in s:
#         print("present")

word="sourav"
with open("sra.txt","r") as fp:
   lines= fp.readlines()

   for i in lines:
       if i.find(word) != -1:
           print("it is present")
