import re

def is_valid_email(email):
    """This function checks if the the email is valid."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Calling the function
print(is_valid_email("test@example.com"))
print(is_valid_email("invalid-email"))