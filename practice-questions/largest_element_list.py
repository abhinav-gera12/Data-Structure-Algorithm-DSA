'''
Largest Element in a List
Find the Largest Element in a List
Write a Python function that finds and returns the largest element in a given list of integers.

Parameters:
numbers (List of integers): The input list containing integers.

Returns:
An integer representing the largest element in the input list.

Example:
Input: numbers = [3, 8, 2, 10, 5]
Output: 10
Input: numbers = [-5, -10, -2, -1, -7]
Output: -1

'''

def find_largest(numbers):
    # Check if the list is empty
    if not numbers:
        return None  # or raise an exception, depending on requirements
 
    # Initialize the largest number as the first element
    largest = numbers[0]
    
    # Iterate through the list starting from the second element
    for num in numbers[1:]:
        # If we find a number larger than our current largest, update largest
        if num > largest:
            largest = num
    
    # Return the largest number found
    return largest

print("Calling the first function")
print(find_largest([3, 8, 2, 10, 5]))
 
# Alternative solution using built-in max() function:
def find_largest(numbers):
    return max(numbers) if numbers else None

print("Calling the second function")
print(find_largest([3, 8, 2, 10, 5]))
