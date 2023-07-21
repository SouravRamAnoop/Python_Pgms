# SIMPLE CALCULATOR
s = int(input("Enter Your First Number : "))
y = int(input("Enter Your Second Number : "))

# Arithmetic Operations`
print("SUM = ",s + y)
print("SUB = ",s - y)
print("MUL = ",s * y)
print("DIV = ",s  / y)
print("MOD = ",s % y)
print("EXP = ",s ** y)
print("FLR_DIV = ",s // y)

#Comparison Operations
print("EQL = ",s == y)
print("LT = ",s < y)
print("GT = ",s > y)
print("LE = ",s <= y)
print("GE = ",s >= y)
print("NE = ",s != y)

#Logical Operations
print("AND = ", s > y and s < 10)
print("OR = ",s < y or y > 15)
print( "NOT = ",(not(s > y and s < 10)))
