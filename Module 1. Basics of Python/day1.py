# -*- coding: utf-8 -*-
"""Day1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qtoUtvWsGEmeDbIZFrLSZcLK7K1sDgYE
"""

print("HELLO WORLD !!")

# Integer Variable
x = 5
print(x)

# Float Variable
y = 5.5
print(y)

# Arthemtic Opertaor on these two variable
print(x + y)
print(x - y)
print(x * y)
print(x / y)

# Comparison Operator on these two variable
print(x > y)
print(x < y)
print(x == y)
print(x != y)

# String Variable
name = "John"
print(name)
name2 = 'Mohan'
print(name2)
var2 = "324344"
print(var2)

# Boolen Variable
is_student = True
print(is_student)
is_teacher = False
print(is_teacher)

# All variables together
age = 34
height = 5.4
name = "John"
is_student = True
print("Age:",age)
print("Height:",height)
print("Name:",name)
print("Is Student:",is_student)

"""### Data Types:
**Introduce basic data types in Python:**

- int: for integers
- float: for decimal numbers
- str: for text (strings)
- bool: for True/False
"""

type(is_student)

# Checking data types
print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

# Operators

a = 10
b = 3

# Addition
print("Addition:",a + b)

# Substraction
print("Substraction:",a - b)

# Multiplication
print("Multiplication:",a * b)

# Division
print("Division:",a / b)

# Floor Division
print("Floor Division:",a // b)

# Modulus
print("Modulus:",a % b)

# Comparison Operators:

x = 20
y = 4

# Equal to
print(x == y)  # Output: False

# Not equal to
print(x != y)  # Output: True

# Greater than
print(x > y)  # Output: True

# Less than
print(x < y)  # Output: False

# Greater than or equal to
print(x >= y)  # Output: True

# Less than or equal to
print(x <= y)  # Output: False

var1 = 10
var2 = "john"
var3 = True

print(type(var1))
print(type(var2))
print(type(var3))

# Input From User
name = input("Enter your name: ")
age= int(input("Enter your age: "))
print("Your name is",name,"and your age is",age)

type(age)

age1 = 34

type(age1)

# Input From User (Defining Data Type)
name = input("Enter your name: ")
age= int(input("Enter your age: "))
print("Your name is",name,"and your age is",age)

type(age)

# Input From User to apply arthematic opertors
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition:",a + b)
print("Substraction:",a - b)
print("Multiplication:",a * b)
print("Division:",a / b)

# Input from user as string data type values to apply arthematic opertors
a = input("Enter first number: ")
b = input("Enter second number: ")
print("Addition:",a + b)
#print("Substraction:",a - b)