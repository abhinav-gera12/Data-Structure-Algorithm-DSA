# VARIABLES

'''
Variables ->    These are the fundamental elements in programming used to store data that can be referenced and manipulated
                in a program. In python, variables are created when you assign a value to them, and they do not need explicit
                declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable.
'''

'''
Outline:
- Introduction to variables
- Declaraing and assigning variables
- Naming conventions
- Understanding the type variables
- Type checking and conversion
- Dynamic typing
'''

# DECLARING AND ASSIGNING THE VARIABLES
name = "Abhinav"
age = 32
height = 5.8
is_working = True

# Use the f-string format to print the values
print(f""" name = {name}\n age = {age}\n height = {height}\n is working = {is_working}""")


# NAMING CONVENTIONS
'''
- Variable name should be descriptive
- They must start with a letter or '_' and contain letters, numbers, and underscores
- Variable names are case sensitive
'''
first_name = "Abhinav"
last_name = "Gera"

'''
- Invalid variable names
2age = 30
first-name = "Abhi"
@name = "Abhi"
'''

'''
- Case Sensitive
name = "Abhinav"
Name = "Abhinav"
Both 'name' and 'Name' are different
(name ≠ Name)
'''

'''
- Understanding variable types
Python is dynamically typed language, the type of the variable is determined at the runtime
age = 25 (int)
height = 6.1 (float)
name = "Abhinav" (str)
is_working = True (bool)
'''

'''
- Type checking and conversion
age = 22
type(age) == int
age_str = str(age)     -> type(age) == str (it converts variable from int to str) -> "22"
age_int = int(age)     -> type(age) == int (it converts variable from str to int) -> 22
age_float = float(age) -> type(age) == float (it converts variable from int to float) -> 22.0

name = "Abhinav"
int(name)               -> It will raises an error as it doesn't contain any int value

height = 6.1
type(height) == float
age_str = str(height)   -> type(height) == str (it converts variable from float to str) --> "6.1"
age_int = int(height)   -> type(height) == int (it converts variable from float to int) --> 6
'''

# DYNAMIC TYPING
'''
- Python allows the type of a variable to change as the program executes

var = 10
print(var, type(var)) --> 10 int

var = "Hello"
print(var, type(var)) --> Hello str

var = 3.14
print(var, type(var)) --> 3.14 float
'''

# INPUT
age = input("What is your age? ")
print(age)                                  # 22
print(type(age))                            # str

# Type caste
age = int(input("What is your age? "))
print(age)                                  # 22
print(type(age))                            # int 

# Create a simple calculator
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1/num2

print("Sum: ", sum)
print("Difference: ", difference)
print("Product: ", product)
print("Quotient: ", quotient)