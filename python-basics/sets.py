# --------------------------------------------------------
# SETS
# --------------------------------------------------------

'''
- Sets -> Sets are built-in data types in Python used to store collections of unique elements. They are unordered, meaning that
          elements do not follow a specific order (indexing), and they do not allow duplicate elements. Sets are useful for
          membership tests, eliminating duplicate entities, and performing mathematical set operations like union, intersection,
          difference, and symmetric difference.
'''

'''
Outline:
i) Create a set
ii) Basic set operations -> (add, remove, discard, pop, boolean value to check element is present in the set)
iii) Mathematical operations -> (union, intersection, difference, symmetric difference)
iv) Subset
v) Superset
'''

# --------------------------------------------------------
# CREATE A SET
# --------------------------------------------------------

my_set = {1, 2, 3, 4 ,5}
print(my_set)  # Output will be {1, 2, 3, 4, 5}
print(type(my_set))  # Output will be <class 'set'>

empty_set = set()
print(empty_set)  # Output will be set()
print(type(empty_set))  # Output will be <class 'set'>

my_new_set = set([1, 2, 3, 4, 5, 5, 6, 7, 7, 7])
print(my_new_set)  # Output will be {1, 2, 3, 4, 5, 6, 7}

# --------------------------------------------------------
# BASIC SET OPERATIONS
# --------------------------------------------------------

# ADDING AN ELEMENT
my_new_set.add(10)
print(my_new_set)  # Output will be {1, 2, 3, 4, 5, 6, 7, 10}

# REMOVING AN ELEMENT
my_new_set.remove(7)
print(my_new_set)  # Output will be {1, 2, 3, 4, 5, 6, 10}

# REMOVING ELEMENT WITHOUT RAISING ERROR IF NOT FOUND (USING DISCARD)
my_new_set.discard(9)  # No error even if 9 is not present in the set
print(my_new_set)  # Output will be {1, 2, 3, 4, 5, 6, 10}

# RETURNING AND REMOVING THE FIRST ELEMENT (POP)
popped_element = my_new_set.pop()
print(popped_element)  # Output will be an arbitrary element from the set
print(my_new_set)  # Remaining elements of the set after popping one

# SET MEMBERSHIP TEST
print(11 in my_new_set)  # Output will be False or True

# --------------------------------------------------------
# MATHEMATICAL OPERATIONS
# --------------------------------------------------------

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

# UNION METHOD
union = set1.union(set2)
print(union)  # Output will be {1, 2, 3, 4, 5, 6, 7, 8, 9}

# INTERSECTION
intersection = set1.intersection(set2)
print(intersection)  # Output will be {4, 5, 6}

# INTERSECTION UPDATE
set1.intersection_update(set2)
print(set1)  # Output will be {4, 5, 6}

# RESET set1 for further operations
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

# DIFFERENCE
differnece_set_1 = set1.difference(set2)
print(differnece_set_1)  # Output will be {1, 2, 3}

differnece_set_2 = set2.difference(set1)
print(differnece_set_2)  # Output will be {7, 8, 9}

# DIFFERENCE UPDATE
set1.difference_update(set2)
print(set1)  # Output will be {1, 2, 3}

# RESET set1 and set2 for further operations
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

# SYMMETRIC DIFFERENCE
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)  # Output will be {1, 2, 3, 7, 8, 9}

# SYMMETRIC DIFFERENCE UPDATE
set1.symmetric_difference_update(set2)
print(set1)  # Output will be {1, 2, 3, 7, 8, 9}

# --------------------------------------------------------
# SETS METHODS
# --------------------------------------------------------

# IS SUBSET
print(set1.issubset(set2))  # Output will be True or False

# IS SUPERSET
print(set1.issuperset(set2))  # Output will be True or False