'''
Problem Description:
You are given two integers, n and m. Your task is to return a rectangle pattern of '*', where n represents the number of rows (length) and m represents the number of columns (breadth).

Input:
Two integers n and m, where 1 <= n, m <= 100.

Output:
A list of strings where each string represents a row of the rectangle pattern.

Example:
Input: n = 4, m = 5
Output: ['*****', '*****', '*****', '*****']

Input: n = 3, m = 2
Output: ['**', '**', '**']

'''
def generate_rectangle(n, m):
    """
    Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.
    
    Parameters:
    n (int): The number of rows in the rectangle.
    m (int): The number of columns in the rectangle.
    
    Returns:
    list: A list of strings where each string represents a row of the rectangle pattern.
    """
    # Initialize an empty list to store the rows of the rectangle
    rectangle = []
    
    # Loop through each row from 1 to n
    for i in range(n):
        # Create a row with m stars
        row = '*' * m
        # Add the row to the rectangle list
        rectangle.append(row)
    
    # Return the list of rectangle rows
    return rectangle

generate_rectangle(3,2)