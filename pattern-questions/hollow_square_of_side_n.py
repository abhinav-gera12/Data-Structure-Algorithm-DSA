'''
Hollow Square of side 'N'
Problem Description:

You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).

Input Parameters:
n (int): The size of the square (number of rows and columns).

Output:
A list of strings where each string is a row of n characters, representing a hollow square.

Example:
Input: 3
Output: ['***', '* *', '***']
 
Input: 5
Output: ['*****', '*   *', '*   *', '*   *', '*****']

'''


def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Initialize an empty list to store the rows of the hollow square
    square = []
    
    # Handle the case when n is 1 separately
    if n == 1:
        return ['*']
    
    # The first and last rows are full of '*'
    square.append('*' * n)  # First row
    
    # For the middle rows, the first and last characters are '*', rest are spaces
    for i in range(n - 2):
        square.append('*' + ' ' * (n - 2) + '*')
    
    # The last row is also full of '*'
    square.append('*' * n)  # Last row
    
    # Return the list of rows
    return square

print(generate_hollow_square(7))