'''
(Q)- Determine the ticket pricing based on the age and whether the person is a student.
Ticket pricing based on the age and the student status.
'''

age = int(input("enter your age: "))
is_student = input("Are you a student? (yes or no): ").lower()

# Determine the ticket price
if age < 5:
    price = "Free"
elif age <= 12:
    price = "$10"
elif age <= 17:
    if is_student == 'yes':
        price = "$12"
    else:
        price = "$15"
elif age <= 64:
    if is_student == 'yes':
        price = "$18"
    else:
        price = "$20"
else:
    price = "$21"

print(f"Ticket price is : {price}")