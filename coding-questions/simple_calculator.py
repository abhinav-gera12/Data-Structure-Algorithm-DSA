'''
(Q) - Create a simple calculator to perform different operations using if, else, elif conditional statements
'''

num1 = float(input("enter your first number: "))
num2 = float(input("enter your second number: "))
operation = input("enter your operation (+, -, /, *): ")

# Perform the requested operations
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero"
else:
    result = "Invalid operation."

print(f"Result : {result}")