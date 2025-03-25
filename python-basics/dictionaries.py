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