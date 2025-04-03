'''
Sum of List Elements
Problem Description
Sum of List Elements

Write a Python function that calculates the sum of all elements in a given list of integers.

Parameters:
numbers (List of integers): The input list containing integers.

Returns:
An integer representing the sum of all elements in the input list.

Example:
Input: numbers = [1, 2, 3, 4, 5]
Output: 15
Input: numbers = [10, -5, 7, 8, -2]
Output: 18
'''

def sum_list(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    
    return sum

print(sum_list([1,2,3,4,5]))