'''
(Q)-  Calculate the factorial of a number using recursion
'''
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(5))