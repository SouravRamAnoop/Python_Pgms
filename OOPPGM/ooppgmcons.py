# class Car:
#     name=" "
#     model=" "
#
# car1 = Car()
# Car2 = Car()
#
# car1.name="Vento"
# car1.model=2015
#
# Car2.name="KIA"
# Car2.model=2022
#
# print(f"{car1.name} is {car1.model} model car")
# print(f"{Car2.name} is {Car2.model} model car")


class car:
    def __init__(self,name,model):
        self.name=name
        self.model=model

    def __str__(self):
        return f"{self.name}({self.model})"

car1=car("vento",2015)
print(car1)
print(f"{car1.name} is {car1.model} model car")