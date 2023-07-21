#A Company decided to give bonus of 5% to employees to if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary = int(input("Enter your salary :"))
year = int(input("Enter your year of service :"))
if year > 5:
    print("You are eligible for bonus ")
    bonus = salary * 5 /100
    print("Your bonus is =",bonus)
    print("Your Net Salary is =", salary + bonus)
else:
    print("You are not eligible for bonus")
