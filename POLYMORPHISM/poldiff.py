#Polymorphism with class methods:
# class india:
#     def capital(self):
#         print("NEW DELHI IS CAPITAL OF INDIA")
#     def language(self):
#         print("HINDI IS THE WIDELY SPEAKING LANGUAGE ")
#     def type(self):
#         print("INDIA IS A DEVELOPING COUNTRY ")
# class usa:
#     def capital(self):
#         print("WASHINGTON DC IS THE CAPITAL OF USA ")
#     def language(self):
#         print("ENGLISH IS THE WIDELY SPEAKING LANGUAGE ")
#     def type(self):
#         print("USA IS A DEVELOPED COUNTRY ")
#
# x=india()
# y=usa()
# for i in(x,y):
#     i.capital()
#     i.language()
#     i.type()

# Implementing Polymorphism with a Function
class india:
    def capital(self):
        print("NEW DELHI IS CAPITAL OF INDIA")
    def language(self):
        print("HINDI IS THE WIDELY SPEAKING LANGUAGE ")
    def type(self):
        print("INDIA IS A DEVELOPING COUNTRY ")
class usa:
    def capital(self):
        print("WASHINGTON DC IS THE CAPITAL OF USA ")
    def language(self):
        print("ENGLISH IS THE WIDELY SPEAKING LANGUAGE ")
    def type(self):
        print("USA IS A DEVELOPED COUNTRY ")

def func(obj):
    obj.capital()
    obj.language()
    obj.type()

x=india()
y=usa()

func(x)
func(y)

