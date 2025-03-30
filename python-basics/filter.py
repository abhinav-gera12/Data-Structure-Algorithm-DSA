'''
Filter : The filter function constructs an iterator from elements of an iterable for which a function returns true. It is used to
        filter out items from a list (or any other iterable) based on a condition.
'''

def even(num):
    if num %2 == 0:
        return True
    return False

a = even(24)
print(a)

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
even_list = list(filter(lambda num:num%2==0, lst))
print(even_list)


greater_than_five = list(filter(lambda num:num>5, lst))
print(greater_than_five)

# FILTER WITH THE LAMBDA FUNCTION WITH MULTIPLE CONDITIONS
even_and_greater_than_five = list(filter(lambda num:(num>5 and num %2==0), lst))
print(even_and_greater_than_five)

# FILTER FUNCTION FOR THE DICTIONARY
## Apply the filter fucntion to check the age is greater than 25 in the dictionary
people = [
    {'name':'Abhinav', 'age':22},
    {'name':'Krish', 'age':32},
    {'name':'Jack', 'age':13},
    {'name':'Denis', 'age':37},
]

def age_greater_than_25(person):
    return person['age'] > 25

new_lst = list(filter(age_greater_than_25, people))
print(new_lst)

'''
Conclusion -> The filter() function is a powerful tool for creating iterators that filter items out of an iterable based on
                a function. It is commonly used for data cleaning, filtering objects, and removing unwanted elements from lists.
                By mastering filter(), you can write more concise and efficient code for processing and manipulating collections 
                in python.
'''