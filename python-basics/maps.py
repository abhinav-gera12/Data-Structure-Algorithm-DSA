'''
MAP() - This function applies a given function to all the items in an input list (or any other iterable) and returns a map
        object (an iterator). This is particularly useful for transforming data in a list comprehensively.
'''

num = [1,2,3,4,5,6,7,8,9,10]
def square(num):
    lst = []
    for i in num:
        lst.append(i**2)
    return lst

print(square(num))

# Now using the above logic with the map function
numbers = list(map(lambda x: x**2, num))
print(numbers)

# MULTIPLE ITERABLES
numbers1 = [1,2,3]
numbers2 = [4,5,6]
added_numbers = list(map(lambda x,y: x+y, numbers1, numbers2))
print(added_numbers)


# MAP TO CONVERT A LIST OF STRINGS TO INTEGERS
str_numbers = ['1', '2', '3', '4']
int_numbers = list(map(int, str_numbers))
print(int_numbers)


words = ['apple', 'banana', 'cherry', 'guava']
upper_word = list(map(str.upper, words))
print(upper_word)


# ONE MORE EXAMPLE ON DICTIONARY
def get_name(person):
    return person['name']
people = [
    {'name':'Abhinav', 'age':22},
    {'name':'Krish', 'age':32}
]
names = list(map(get_name, people))
print(names)

'''
Conclusion -> The map() function is a powerful tool for applying transformation to iterable data structures. It can be used with
                regular functions, lambda functions, and even multiple iterables, providing a versatile approach to data processing
                in python. By understanding and utilizing map(), you write more efficient and readable code.
'''