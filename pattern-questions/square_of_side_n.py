'''
Square of side 'N'
Problem Description: You are given an integer n. Your task is to return a square pattern of size n x n made up of the character '*', represented as a list of strings.

Input Parameters:
n (int): The size of the square (number of rows and columns).

Output:
A list of strings where each string is a row of n characters.

Example:
Input: 3
Output: ['***', '***', '***']

Input: 5
Output: ['*****', '*****', '*****', '*****', '*****']

'''

def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    Parameters:
    n (int): The size of the square.
    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    # Initialize an empty list to store the rows of the square
    square = []
    
    # Loop n times to generate each row
    for i in range(n):
        # Create a row of '*' of length n and append it to the list
        square.append('*' * n)
    
    # Return the list of rows
    return square

print(generate_square(7))