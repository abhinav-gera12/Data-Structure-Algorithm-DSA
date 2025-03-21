# CONDITIONAL STATEMENTS (if, else and elif)

'''
Outline:
i) Introduction to conditional statement
ii) If statement
iii) Else statement
iv) Elif statement
v) Nested conditional statement
vi) Common error and best practices
'''

'''
- Introduction to conditional statement -> Those statements, where we need to check some conditions to be satsified. And if 
                                            satisfied, we need to execute the indented block under if-else statements. 
                                            If false, we don't want to execute the flow and we can skip the if-else indentation
                                            part flow from the code on runtime.
'''

'''
- if statement -> It evaluates the statement and executes the block of code within it, if the condition is true. 
'''

# IF CONDITION
age = 20
print("if conditional statement - ")
if age >= 18:
    print(f"line no: 27, age is greater than or equal to 18, and you are eligible for the vote as per your age {age}")

'''
- else statement -> It executes the block of code if the condition in the if statement is returned false
'''
# ELSE CONDITION
print("else conditional statement - ")
age = 16
if age >= 18:
    print(f"line no: 35, age is greater than or equal to 18, and you are eligible for the vote as per your age {age}")
else:
    print(f"line no: 35, age is smaller than or not equal to 18 and you are not eligible for the vote as per your age {age}")

'''
- elif statement -> It allows you to check multiple conditions and it stands for "else if" 
'''
print("else conditional statement - ")
age = 17
if age <= 13:
    print(f"line no: 46, you are a child and your age is {age}")
elif age < 18:
    print(f"line no: 48, you are a teenager and your age is {age}")
else:
    print(f"line no: 46, you are an adult and your age is {age}")

'''
- Nested conditional statements -> You can place one or more if, elif, else statements inside another if, elif or else to create
                                    nested conditional statements
'''
# NESTED CONDITIONAL STATEMENTS
'''
- CREATE A PROGRAM WHICH TELLS THE NUMBER IS POSITIVE, NEGATIVE OR EVEN OR ODD OR ZERO
'''
number = int(input("Enter one number: "))
print(f"The number you entered is {number}")
if number == 0:
    print("Number is zero")
elif (number > 0) and (number % 2 == 0):
    print("It is a positive even number")
elif (number < 0) and (number % 2 == 0):
    print("It is negative even number")
elif (number > 0) and (number % 2 != 0):
    print("It is positive odd number")
else:
    print("It is negative odd number")