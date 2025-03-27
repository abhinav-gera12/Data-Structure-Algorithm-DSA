'''
(Q)- Temperature conversion
'''
def convert_temperature(temp, unit):
    '''This function converts temperature between Celsius and Fahrenheit'''
    unit = unit.lower()
    if unit == "c":
        return (temp * (9/5) )+ 32        # Converting celsius to fahernheit
    elif unit == "f":
        return (temp-32) * (5/9)
    else:
        return None
    
print(convert_temperature(25, 'C'))
print(convert_temperature(77, "f"))


'''
(Q)- Password length checker
'''
def is_strong_password(password):
    '''This function checks if the password is strong or weak'''
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_-+' for char in password):
        return False
    return True
### calling the function
print(is_strong_password("WeakPwd"))
print(is_strong_password("StrongPassword@123"))
print(is_strong_password("strongpassword@123"))


'''
(Q)- Calculate the total cost of items in a shopping cart
'''
def calc_total_cost(cart):
    total_cost = 0
    for item in cart:
        total_cost = total_cost + item['price'] * item['quantity']

    return round(total_cost,3)

cart = [
    {'name':'Apple', 'price':0.5, 'quantity':4},
    {'name':'Banana', 'price':0.3, 'quantity':6},
    {'name':'Orange', 'price':0.7, 'quantity':3},
]
total_cost = calc_total_cost(cart)
print(total_cost)