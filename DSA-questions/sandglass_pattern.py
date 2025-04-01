'''
Sandglass Pattern
Problem Description:
You are given an integer n. Your task is to return a sandglass pattern of '*', where the first row contains 2n - 1 stars and each subsequent row decreases the number of stars by 2, until the last row contains a single star. After reaching the smallest width, the pattern then continues with the same number of stars increasing back to 2n - 1. The stars in each row should be centered.

Input:
A single integer n, where 1 <= n <= 100.

Output:
A list of strings where each string represents a row in the sandglass pattern.

Example:
Input: 3
Output: ['*****', ' *** ', '  *  ', ' *** ', '*****']
Input: 4
Output: ['*******', ' ***** ', '  ***  ', '   *   ', '  ***  ', ' ***** ', '*******']

'''

def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the sandglass.
    
    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    """
    # Your code here
    if n >=1 and n <=100:
        sandglass = []
        for i in range(n):
            stars = "*" * (2 * (n-i) - 1)
            spaces = " " * i
            row = spaces + stars + spaces
            sandglass.append(row)

        for i in range(n-2, -1, -1):
            stars = "*" * (2 * (n-i) - 1)
            spaces = " " * i
            row = spaces + stars + spaces
            sandglass.append(row)
        return sandglass
    
print(generate_sandglass(4))