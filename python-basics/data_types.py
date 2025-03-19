# DATA TYPES

'''
- Outline:
i) Introduction to data types
ii) Importance of data types
iii) Basic data types (integer, float-point numbers, strings, booleans)
iv) Advanced data types (List, tuple, dictionaries, sets)
v) Type conversion
'''

'''
- Definition -> Data types are a classification of data which tell the compiler or interpreter how the programmer intends to use
                the data
             -> They determine the type of operations that can be performed on the data, the values that the data can take, and
                the amount of memory needed to store the data.
'''

'''
- Importance of data types in programming:
    Explanation -> Data types ensure that data is stored in an efficient way.
                -> They help in performing correct operations on data.
                -> Proper use of data types can prevent errors and bugs in the program
'''

# INTEGERS
age = 22
print("Age data type: ", type(age))

# FLOATING-POINT NUMBER
height = 5.11
print("Height data type: ", type(height))

# STRING
name = "Abhinav"
print("Name data type: ", type(name))

# BOOLEAN
is_working = True
print("Is working? : ", type(is_working))

# COMMON ERRORS
'''
result = "Hello" + 5        (can only concatenate 'str' to 'str' not 'int')
- Fix the issue above:
    result = "Hello" + str(5)
    print(result, type(str))        -> (Hello5, str)
'''