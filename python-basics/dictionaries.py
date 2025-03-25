# DICTIONARIES

'''
Outline:
i) Introduction to dictionaries
ii) Creating dictionaries
iii) Accessing dictionary elements
iv) Modifying dictionary elements
v) Dictionary methods
vi) Iterating over dictionaries
vii) Nested Dictionary
viii) Dictionary comprehensions
'''

# INTRODUCTION TO DICTIONARIES
'''
- Introduction to dictionaries -> These are unordered collections of items. They stored data in key-value pairs. Keys must be
                                    unique and immutable (e.g. strings, tupeles, numbers), while values can be of any type.
                                    Single key is always being used instead of multiple keys, otherwise it will superimposed
                                    new key with the new value.
'''

# CREATING DICTIONARIES
print("create an empty dictionary - ")
empty_dict = {}
print(type(empty_dict))
print(empty_dict)
empty_dict = dict()
print(empty_dict)

student = {'name':'Abhinav', 'age':22, 'grade':24}
print(student)

'''
Error -> 
student = {'name':'Abhinav', 'age':22, 'name':24}
print(student)
Output -> {'name':24, 'age':22}
'''


# ACCESING DICTIONARY ELEMENTS
print('accesing dictionary element - ')
student = {'name':'Abhinav', 'age':22, 'grade':'A'}
print(student['name'])
print(student['age'])
print(student['grade'])

## ACCESING THE VALUES WITH THE 'get()' method
print(student.get('name'))
print(student.get('last_name')) # It will not raise an error, if the key is not present and return - None
print(student.get('last_name', 'Not available')) # We can give the key value as default if key is not present


# MODIFYING DICTIONARY ELEMENTS
'''
- Modifying dictionary elements -> Dictionaries are mutuable, so you can add, remove and update the elements. All in all,
                                    your key should be unique.
'''
print('modifying dictionary elements - ')
studnet = {"name":"Abhinav", "age": 22, "grade": "A"}
student['age'] = 33         ## updated the value
student['address'] = 'AB Colony'    ## insert a new key and value
print(student)
del student['grade']        ## delete the key-value pair from the original dictionary
print(student)


# DICTIONARY METHODS
print('dictionary methods - ')
keys = student.keys()
print(keys)
values = student.values()
print(values)
items = student.items()
print(items)

## SHALLOW COPY
'''
- SHALLOW COPY -> It provides the different memory allocation to the variable, so if we change one of the variable, it doesn't reflect
                    the other variable's memory address
'''
student_copy = student
print(student)
print(student_copy)

student['name'] = 'Abhinav2'
print(student)
print(student_copy)         ## It will also reflect the new value, so it will reflect the same values which are present in the dict

student['name'] = 'Abhinav Gera'
student_copy1 = student.copy()
print(student)
print(student_copy)
print(student_copy1)

student['name'] = 'Abhinav Gera 2'
print(student)
print(student_copy)
print(student_copy1)


# ITERATING OVER DICTIONARIES
'''
- Iterating over dictionaries -> You can use the loops to iterate over dictionaries, keys, values and items
'''
print('iterating over dictionaries - ')
## iterating over keys
student = {"name":'Abhinav', 'age':22, 'grade':'A'}
for keys in student.keys():
    print(keys)
## iterating over values
for values in student.values():
    print(values)
## iterating over key-value pairs
for key, value in student.items():
    print(f'{key} : {value}')


# NESTED DICTIONARIES
'''
- Nested dictionaries -> A dictionary inside of another dictionary
'''
print('nested dictionary - ')
students = {
    "student1": {'name':'Abhinav', 'age':32},
    'student2': {'name':'Krish', 'age':15}
}
print(students)

# ACCESS NESTED DICTIONARIES ELEMENTS
print(students['student2']['name'])

# ITERATING OVER NESTED DICTIONARIES
for student_id, student_info in students.items():
    print(f'{student_id} : {student_info}')
    for key, value in student_info.items():
        print(f"{key} : {value}")


# DICTIONARY COMPREHENSION
squares = {x:x**2 for x in range(1,6)}
print(squares)

squares_even = {x:x**2 for x in range(1,10) if x%2==0}
print(squares_even)