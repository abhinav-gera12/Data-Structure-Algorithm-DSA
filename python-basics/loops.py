# LOOPS

'''
Outline:
i) Introduction to loops
ii) For loop -> (iterating over a range), (iterating over a string)
iii) while loop
iv) Loop control statements -> break, continue, pass
v) Nested loops
'''

'''
- Introduction to loops -> It's a concept of repeatedly executing a block of code based on a condition or a sequence. Loops allow
                            you to automate repetitive tasks, making your code more efficient and reducing redundancy. There are
                            two main types of loops - for loop and while loop
'''

# FOR LOOP
'''
- For Loop -> It iterates over a sequence of items
'''
'''
- range -> It is a function which gives the sequence of numbers (start, end, step)
'''
print("for loop - (i)")
for i in range(10):
    print(i)

print("for loop - (ii)")
for i in range (2, 10):
    print(i)
 
print("for loop - (iii)")
for i in range(3, 31, 3):
    print(i, end= " ")
print("\n")

# FOR LOOP WITH STRING
print("for loop with string functionality - ")
for i in "Abhinav Gera":
    print(i, end = " ")
print("\n")


# WHILE LOOP
'''
- While loop -> It continues to execute as long as the condition is True.
'''
print("while loop -")
count = 0
while count < 5:
    print(count)
    count = count + 1