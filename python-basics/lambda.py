'''
Lambda Function: These are the small anonyomous functions defined using the lambda keyword. They can have any number of arguments but only
                one expression. They are commonly used for short operations or as arguments to higher-order functions.
'''

# SYNTAX
# lambda arguments : expression

addition = lambda a, b: a+b
print(type(addition))
print(addition(5,6))

even = lambda num: num%2==0
print(even(13))
print(even(14))
