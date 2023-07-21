"""1.	The Rectangle Class
A class called Rectangle, which models a rectangle with a length and a width (in float),
is designed as shown in the following class diagram. Write the Rectangle class.
 Attribute : length , width
Methods :
Rectangle()
Rectangle(length:float, width:float)
getLength()
getWidth()
getArea()
getPerimeter()
"""
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#
#     def get_length(self):
#         print(f"length ={self.length}")
#
#     def get_width(self):
#         print(f"Width ={self.width}")
#
#     def get_Area(self):
#         print(f"Area={self.length * self.width}")
#
#     def get_perimeter(self):
#         print(f"Perimeter ={2*(self.length+self.width)}")

# r=Rectangle(5.5,3.2)
# r.get_length()
# r.get_width()
# r.get_Area()
# r.get_perimeter()


"""
2.	The Employee Class
A class called Employee, which models an employee with an ID, name and salary,
 is designed as shown in the following class diagram. 
 The method raiseSalary(percent) increases the salary by the given percentage. Write the Employee class.

Attributes:
Id :int
Firstname:string
Lastname:string
Salary:int   """

# class Employee:
#     def __init__(self,id,firstname,lastname,salary):
#         self.id=id
#         self.firstname=firstname
#         self.lastname=lastname
#         self.salary=salary
#
#     def get_id(self):
#         print(f"id={self.id}")
#
#     def get_Firstname(self):
#         print(f"Fname= {self.firstname}")
#
#     def get_Lastname(self):
#         print(f"Lname= {self.lastname}")
#
#     def get_Name(self):
#         print(f"{self.firstname + self.lastname}")
#
#     def get_salary(self):
#         print(f"salary= {self.salary}")
#
#     def get_Annualsalary(self):
#         print(f"Annualsal={self.salary*12}")
#
#     def raisesalary(self,percentage):
#         sal=(self.salary*percentage/100)
#         New_sal=self.salary+(self.salary*percentage/100)
#         print(f"increased amount ={sal}")
#         print(f"New Salary ={New_sal}")
#
#     def toString(self):
#         print(f"Employee[id={self.id} ,Name={self.firstname+self.lastname} ,Salary={self.salary}]")

# e1=Employee(1,"Sourav","Ram",50000)
# e1.get_id()
# e1.get_Firstname()
# e1.get_Lastname()
# e1.get_Name()
# e1.get_salary()
# e1.get_Annualsalary()
# e1.raisesalary(20)
# e1.toString()
"""
3.	The Date Class
A class called Date, which models a calendar date, is designed as shown in the following class diagram. Write the Date class.
"""
class Date:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year

    def get_day(self):
        print(f"date={self.day}")

    def get_month(self):
        print(f"month={self.month}")

    def get_year(self):
        print(f"year={self.year}")

    def set_day(self,d):
        self.day=d

    def set_month(self,m):
        self.month=m

    def set_year(self,y):
        self.year=y

    def set_date(self,d,m,y):
        self.day=d
        self.month = m
        self.year=y
        # print({})
    def toString(self):
        print(f"date={self.day/self.month/self.year}")




d=Date(20,4,1998)
d.get_day()
d.get_month()
d.get_year()
d.set_day(16)
d.set_month(7)
d.set_year(1998)
d.set_date(16,7,1998)
d.toString()


