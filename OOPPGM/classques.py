
class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

emp=Employee("James",122,25000)

print(f"{emp.name} job id is {emp.id} and salary is {emp.salary}")
