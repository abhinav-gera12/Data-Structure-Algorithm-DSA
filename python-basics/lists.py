# LISTS
'''
Outline:
i) Introduction to lists
ii) Creating lists
iii) Accessing list elements
iv) Modifying list elements
v) List methods
vi) Slicing lists
vii) Iterating over lists
viii) List comprehension
ix) List comprehension with inbuild functions
x) Nested Lists
'''

'''
- Introduction to lists -> Lists are ordered, mutable collections of items. They can contain items of different data types.
'''
print("creating lists - ")
print("lists - (i)")
lst = []
print(type(list))

print("lists - (ii)")
names = ["Abhinav", "Gaurav", "Ram", "Sham"]
print(names)

print("list - (iii)")
mixed_lists = ["Abhinav", True, 1, 2.3]
print(mixed_lists)

# ACCESING LIST ELEMENTS
print("accessing the list elements - ")
fruits = ["Apple", "Banana", "Grapes", "Cherry", "Kiwi"]
print(fruits[0])
print(fruits[-1])
print(fruits[1:])
print(fruits[1:3])


# MODIFYING THE LIST ELEMENTS
print("modifying the list elements - ")
fruits[1] = "Watermelon"
print(fruits)

'''
fruits[1:] = "Watermelon"
print(fruits)
Output -> ['Apple', 'W', 'a', 't', 'e', 'r', 'm', 'e', 'l', 'o', 'n']
'''

# LIST METHODS
'''
i) Append -> Add an item to the end of the list
ii) Insert -> If you want to add an element to the particular index, then you need to specify it
iii) Remove -> To remove an element from the list and it will always remove the first occurence of an item
iv) Pop -> To remove and return the last element
v) Index -> To find the particular index of the element
vi) Count -> It counts the number of element present in the list
vii) Sort -> To sort the element alphatically, ascending order
viii) Reverse -> To reverse the list of elements
ix) Clear -> To clear and remove all the elements present in the list 
'''
print("list methods - ")
fruits.append("Orange")
print(fruits)
fruits.insert(1, "Gauva")
print(fruits)
fruits.remove("Watermelon")
print(fruits)
popped_fruits = fruits.pop()
print(popped_fruits)
print(fruits)
index = fruits.index("Cherry")
print(index)
insert = fruits.insert(2, "Gauva")
print(fruits.count("Gauva"))
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.clear()
print(fruits)

# SLICING LIST
'''
- Slicing list -> The steps to break down the list show below
'''
print("slicing list - ")
numbers = [1,2,3,4,5,6, 7, 8, 9, 10]
print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])


# ITERATING OVER LISTS
'''
- Iterating over lists -> It is a method, to use the loops and iterate to elements of the list
'''
print("iterating over list  - ")
fruits = ["Apple", "Banana", "Grapes", "Cherry", "Kiwi"]
for fruit in fruits:
    print(fruit)

numbers = [1,2,3,4,5,6, 7, 8, 9, 10]
for number in numbers:
    print(number)

'''Iteraing the list with the index values'''
for index, number in enumerate(numbers):
    print(f"index = {index} & number={number}")


# LIST COMPREHENSION
print("list comprehension - ")
'''
-List comprehension -> 
            Basic Syntax:                       [expression for item in iterable]
            Conditional Logic Syntax:           [expression for item in iterable if condition else condition]
            Nested List Comprehension:          [expression for item1 in iterable1 for item2 in iterable2]
'''
print("basic list comprehension - ")
"""
lst = []
for x in range(10):
    lst.append(x**2)
print(lst)
"""

square = [x**2 for x in range(10)]
print(square)

print("list comprehension with condition logic - ")
""""
lst = [] 
for i in range(10):
    if i%2 == 0:
        lst.append(i)
print(lst)
"""

even_numbers = [num for num in range(10) if num%2 ==0]
print(even_numbers)

print("nested list comprehension - ")
'''
pair = []
lst1 = [1,2,3,4]
lst2 = ['a', 'b', 'c', 'd']
for i in lst1:
    for j in lst2:
        pair.append([i, j])
print(pair)
'''

lst1 = [1, 2, 3, 4]
lst2 = ['a', 'b', 'c', 'd']
pair = [[i, j] for i in lst1 for j in lst2]
print(pair)


# LIST COMPREHENSION WITH THE INBUILD FUNCTIONS
words = ["hello", "world", "python", "list", "comprehension"]
lengths = [len(word) for word in words]
print(lengths)


# NESTED LISTS
'''
- Nested Lists -> Nested lists are the lists inside the lists
'''
a = [[1, 2, 3], ["a", "b", "c"], [2.14, 3.17], "Abhinav"]
for i in a:
    print(i)


# CONCLUSION
'''
- Conclusion -> List comprehension are a powerful and concise way to create lists in python. They are syntatically compact and can replace
                more verbose looping constructs. Understanding the syntax of list comprehension will help you write cleaner and more
                efficient python code.
'''