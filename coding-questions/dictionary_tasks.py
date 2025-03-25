'''
(Q)- Use a dictionary to count the frequency of the elements in the list
'''
numbers = [1,2,3,3,3,4,4,4,4,5]
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1
print(frequency)


'''
(Q)- Merge two dictionaries into one
'''
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)