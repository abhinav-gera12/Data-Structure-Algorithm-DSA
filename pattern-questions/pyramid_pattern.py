'''
Pyramid Pattern
Problem Description:
You are given an integer n. Your task is to return a pyramid pattern of '*' where each side has n rows, represented as a list of strings. The pyramid is centered, with 1 star in the first row, 3 stars in the second row, and so on, increasing by 2 stars per row until the base row has 2n - 1 stars.

Input:
A single integer n, where 1 <= n <= 100.

Output:
A list of strings where each string contains stars ('*') centered, forming a pyramid shape. Each row has an increasing number of stars, with appropriate spaces for centering.

Example:
Input: 3
Output: ['  *  ', ' *** ', '*****']
Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']

'''

def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    # Your code here
    if n >= 1 and n <=100:
        pyramid = []
        for i in range(n, 0, -1):
            stars = "*" * (2 * i + 1)
            spaces = " " * (n - i -1)
            row = spaces + stars + spaces
            pyramid.append(row)
        return pyramid 

print(generate_pyramid(3))