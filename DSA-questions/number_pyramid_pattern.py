'''
Number Pyramid Pattern
Problem Description:
You are given an integer n. Your task is to return a pyramid pattern of numbers, where each row contains increasing numbers starting from 1 up to the row number, and the pyramid is centered with leading spaces.

Input:
A single integer n, where 1 <= n <= 100.

Output:
A list of strings where each string represents a row in the pyramid pattern.

Example:
Input: 4
Output: ['   1   ', '  1 2  ', ' 1 2 3 ', '1 2 3 4']
 
Input: 3
Output: ['  1  ', ' 1 2 ', '1 2 3']

'''


def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.
    
    Parameters:
    n (int): The height of the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    """
    # Initialize an empty list to store the rows of the pyramid
    pyramid = []
    
    # Loop through each row from 1 to n
    for i in range(1, n + 1):
        # Create leading spaces for centering the numbers
        spaces = ' ' * (n - i)
        # Create a string of numbers from 1 to i, joined by spaces
        numbers = ' '.join(str(x) for x in range(1, i + 1))
        # Add the row with spaces and numbers to the pyramid
        pyramid.append(spaces + numbers + spaces)
    
    # Return the list of pyramid rows
    return pyramid

print(generate_number_pyramid(4))