# TUPLES

'''
- Outline: 
i) Introduction to tuples
ii) Creating tuples
iii) Accessing tuple elements
iv) tuple operations
v) Immutable nature of tuples
vi) Tuple methods
vii) Packing and unpacking tuples
viii) Nested tuples
'''

# INTRODUCTION TO TUPLES
'''
- Introduction to tuples -> Tuples are ordered collections of items that are immutable. They are similar to lists, but their 
                            immutability makes them different.
'''

# CREATING A TUPLE
print('creating a tuple - ')
empty_tuple = ()
print(empty_tuple,'\n', type(empty_tuple))
tpl = tuple()
print(tpl, '\n', type(type))

numbers = tuple([1, 2, 3, 4, 5])
print(numbers)

mixed_tuple = (1, 2.3, 'str', True)
print(mixed_tuple)

# ACCESING TUPLE ELEMENTS
print('accesing tuple elements - ')
print(numbers[0])
print(numbers[-1])
print(numbers[0:4])
print(numbers[::-1])


# TUPLE OPERATIONS
numbers = (1, 2, 3, 4, 5, 6)
mixed_tuple = (1, 2.3, True, 'str')
concatenation = numbers + mixed_tuple
print(concatenation)
mixed_tuple = mixed_tuple * 3
print(mixed_tuple)


# IMMUTABLE NATURE OF TUPLES
''' we cannot change the items present in the tuple 
like : 
tpl = (1, 2, 3, 4, 5)
tpl[1]= 'Krish'
print(tpl)
'''

# TUPLE METHODS
print(numbers.count(1))
print(numbers.index(3))

# PACKING AND UNPACKING TOOL
## PACKING :
packed_tuple = 1, "Hello", 3.
print(packed_tuple)

## UNPACKING :
a, b, c = packed_tuple
print(a, b, c)


# Unpacking with  '*'
numbers = (1, 2, 3, 4, 5, 6)
first, *middle, last = numbers
print(first)
print(middle)
print(last)

# NESTED TUPLE
nested_tuple = ((1,2,3), (4,5,6), (7,8, 9))
print(nested_tuple[1][1:2])


# ITERATING OVER NESTED TUPLES
for sub_tuple in nested_tuple:
    for items in sub_tuple:
        print(items, end=" ")
print()

'''
- Conclusion -> Tuples are versatile and useful in many real-world scenarios where an immutable and ordered collection of
                item is required. They are commonly used in data structures, function arguments, and return values, and as
                dictionary keys. Understanding how to leverage tuples effectively can improve the efficiency and readability
                of your python code.
'''