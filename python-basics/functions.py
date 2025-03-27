# FUNCTIONS
'''
Outline:
i) Introduction to functions
ii) Defining functions
iii) Calling functions
iv) Default parameters
v) Variable-Length Arguments
vi) Return statement
'''

'''
- Introduction to functions -> A function is a block of code that performs a specific task. Function help in organizing code,
                                reusing code, and improving readability.
'''

# SYNTAX
def function_name(parameters):
    '''Docstring'''
    # Function body
    body = {}
    expression = {body}
    return expression

# Function
def even_or_odd(num):
    """This functions finds the number is even or odd"""
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

# Call this above function 'even_or_odd()'
even_or_odd(23)


# FUNCTION WITH THE MULTIPLE PARAMETERS
def add(a, b):
    '''This functions is used for addition of two numbers'''
    return a+b
result = add(2,4)
print(result)


# DEFAULT PARAMETERS
def greet(name="Guest"):
    print(f"Hello {name}. Welcome to the paradise.")
greet()


# VARIABLE LENGTH ARGUMENTS
### Positional Arguments
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1,2,3,4,5,6, "Abhinav")

### Keyword Arguments
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_details(name="Abhinav", age=22, country="India")

# COMBINING BOTH POSITIONAL ARGUEMENTS AND KEY-WORD ARGUMENTS
def total_function(*args, **kwargs):
    for val in args:
        print(f"Positional Argument : {val}")
    for key,value in kwargs.items():
        print(f"{key} : {value}")

total_function(1,2,3,4,5,"abc", name="Abhinav", age=22, country="India")


# RETURN STATEMENT
def multiply(a,b):
    return a*b

multiply(2,3)

### RETURN MULTIPLE VALUES FROM A FUNCTION
def div(a,b):
    return a/b, f'value of a:{a}', f'value of b:{b}'
division, a, b = div(10,5)
print(division, a, b)