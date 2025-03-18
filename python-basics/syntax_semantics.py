# SYNTAX AND SEMANTICS

'''
Outline:
i) Single line comments and multiline comments
ii) Definition of syntax and semantics
iii) Basic syntax rules in python
iv) Understanding the semantic rules in python
'''

'''
Syntax ->   It refers to the set of rules that defines the comibination of symbols that are considered to be correctly 
            structured programs in a language. In simpler terms, syntax is about the correct arrangement of words and symbols
            in a code.
'''

'''
Semantics ->    It refers to the meaning or the interpretation of the symbols, characters, and commands in a language. 
                It is about what the code supposed to do when it runs.
'''

# BASIC SYNTAX RULES IN PYTHON
## CASE SENSTIVITITY -- Python is a case sensitive language
name = "Abhinav"
Name = "Arun"

"""
Both variables 'name' or 'Name' are different identifier because the names are different from each other as per the 
case sensitivity
"""

# INDENTATION
'''
Indentation ->  Python uses indentation to define the blocks of code. Consistent use of spaces (commonly 4) or a tabis required.
                It is being used to define the structure and hierarchy of the code. Unlike many other programming languages
                that uses {} to delimit the blocks of code. It uses indetantion to determine the groups of statements.
                This means that all the statements are within the block must be indented at the same level.
'''

age = 32
if age > 18:
    print(f"Age is greater than 18")


# COMMENTS
'''
"#" ->  Using the hashtag, will provide you the single line comments
""" """ -> using the quotes for three times at the beginning or at the end, will work as the multi-line comments
"\" ->  black slash being used for the line continuation
'''

# MULTIPLE STATEMENTS ON A SINGLE LINE
x=5;    y=10;   z=x+y
print(f'z = {z}')            # z = 15


# UNDERSTAND THE SEMANTICS IN PYTHON
'''
1) Variable Assignment -> 
    age = 32            # It will check the variable is an integer value
    name = Abhinav      # It will check the variable is a string value

2) Checking the type of the variable: use type() function
    type(age) ->        It will return the value int
    type(name) ->       It will return the value str
'''