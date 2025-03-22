'''
(Q)- REMOVE THE DUPLICATES FROM A LIST
# The task is to remove duplicates from the given list of elements and keep only unique values.
'''
lst = [1, 2, 3, 3, 3, 4, 4, 5]  # Original list with duplicates
lst = list(set(lst))  # Converting the list to a set removes duplicates, then converting it back to a list
print("List after removing duplicates:", lst)  # Output will be [1, 2, 3, 4, 5]

'''
# COUNTING THE UNIQUE WORDS IN A TEXT
# The task is to count how many unique words are there in the given text.
'''

text = "In this tutorial we are discussing about the sets"  # Given string of text
words = text.split()  # Splitting the string into words based on spaces

# Convert the list of words to a set to get the unique words
unique_words = set(words)  
print("Unique words in the text:", unique_words)  # Output will be a set of unique words like {'about', 'are', 'discussing', 'sets', 'we', 'In', 'the', 'this', 'tutorial'}

# Print the count of unique words
print("Number of unique words:", len(unique_words))  # Output will be 9
