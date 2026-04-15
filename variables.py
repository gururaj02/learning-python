a = 10
b = 20

a, b = 12, 10

a = b = 15

print(a)
print(b)


# Data Types
name = "Gururaj" # String
is_student = False # bool
age = 23 # int 
weight = 61.5 # float

print(type(name))
print(type(is_student))
print(type(weight))

is_student = "yes"
print(type(is_student))


# Type Conversion
age_float = float(age)
print(age_float)
print(type(age_float))

s = "100"
print(int(s) + age) 


# Arithmetic Operators
a = 10
b = 3
print(a + b) # Output: 13 (Addition)
print(a - b) # Output: 7 (Subtraction)
print(a * b) # Output: 30 (Multiplication)
print(a / b) # Output: 3.333... (Division)
print(a // b) # Output: 3 (Floor Division)
print(a % b) # Output: 1 (Modulus | Remainder)
print(a ** b) # Output: 1000 (Exponentiation)

print(a + b - a + b * 2 ** 3) # Output: 27 (BODMAS - Operator Precedence)