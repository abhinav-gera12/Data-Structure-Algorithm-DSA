# OPERATORS

'''
Outline:
i) Introduction to operators
ii) Arithmetic Operators - Addition, Subtraction, Multiplication, Division, Floor Division, Modulus, Exponentiation
iii) Comparision Operators - Equal to, Not equal to, Greather than, Less than, Greater than or equal to, Less than or equal to
iv) Logical Operators - AND, OR, NOT
'''

'''
- Introduction to operators -> Python operators are special symbols used to perform specific operations on one or more operands, 
                                which can be variables, values, or expressions.
'''

# ARITHMETIC OPERATORS
print("Arithmetic operators: ")
a = 10
b = 5
add_result = a + b              # Addition
sub_result = a - b              # Subtraction
mul_result = a * b              # Multiplication
div_result = a/b                # Division
floor_div_result = a // b       # Floor Division
modulus_result = a % b          # Modulus
exp_result = a ** b             # Exponentiation

print(add_result)
print(sub_result)
print(mul_result)
print(div_result)
print(floor_div_result)
print(modulus_result)
print(exp_result)


# COMPARISION OPERATORS
print("Comparision Operators: ")
print("Equal to operators(==) - ")
a = 10
b = 10
equal_to = (a==b)                                               # Equal to
print(f'line no 37: equal to {equal_to}')
str1 = "Abhinav"
str2 = "abhinav"
equal_to_str = (str1==str2)                                     # Equal to
print(f'line no 41: equal to {equal_to_str}')

print("Not equal to operators(!=) - ")
not_equal_to_str = (str1 != str2)                               # Not equal to
print(f'line no 45: not equal to {not_equal_to_str}')

not_equal_to = (a != b)                                         # Not equal to
print(f'line no 48: not equal to {not_equal_to}')

print("Greater than (>) - ")
num1 = 45
num2 = 55
greater_than = (num1 > num2)                                    # Greater than
print(f'line no 54: greater than {greater_than}')

print("Greater than (>=) - ")
greater_than_equal_to = (num1 >= num2)                          # Greater than equal to
print(f'line no 58: greater than equal to {greater_than_equal_to}')

print("Less than (<) - ")
less_than = (num1 < num2)                                       # Less than
print(f"line no 62: less than {less_than}")

print("Less than (<=) - ")
less_than_equal_to = (num1 <= num2)                             # Less than equal to 
print(f"line no 66: less than {less_than_equal_to}")


# LOGICAL OPERATORS
'''
- AND Operator -> Every condition checks and every condition should be true
'''
print("And Operator - ")
X = True
Y = True
and_result = X and Y                                            # And operator
print(f"line no 82: and operator {and_result}")

'''
- OR Operator -> Only once condition should be satisified and it returns true afterwards;
'''
print("OR Operator - ")
X = True
Y = False
or_result = X or Y                                              # Or operator
print(f"line no 91: or operator {or_result}")

'''
- NOT Opeartor -> Every condition which is true, should returns opposite of that
'''
print("NOT Operator - ")
X = True
not_result = not X                                              # Not operator
print(f"line no 99: not operator {not_result}")