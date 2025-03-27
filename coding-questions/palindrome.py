'''
(Q)- Check if a string is palindrome or not
Examples of palindrome - 'aba'
'''
def is_palindrome(word):
    word = word.lower()
    word = word.replace(" ", "")
    return word == word[::-1]

print(is_palindrome("abba"))
print(is_palindrome("Hello"))
print(is_palindrome("A man a plan a canal Panama"))