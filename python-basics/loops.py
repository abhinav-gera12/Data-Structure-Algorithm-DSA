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

print("while loop - (ii)")
count = 0
while count <= 20:
    if count%2 == 0:
        print(count)
        count = count + 1
    else:
        count = count + 1


# LOOP CONTROL STATEMENTS
# BREAK
'''
- break -> The break statements exists the loop prematurely 
'''
print("break statement - ")
for i in range(0,10):
    if i == 5:
        break
    print(i)

# CONTINUE
'''
- continue -> The continue statement skips the current iteration and continues with the next
'''
print("continue statement - ")
for i in range(0, 10):
    if i % 2 == 0:
        continue
    print(i)

# PASS
'''
- pass -> The pass statement is a null statement and it does nothing.
'''
print('pass statement - ')
for i in range(5):
    if i == 2:
        print(f"the number is {i}")
        pass
    else:
        print(i)


# NESTED LOOOPS:
'''
- Nested Loops -> It means inside a loop, we are defining another loop which will specifically iterate more elements in the loop.
'''
print("nested loops (i) - ")
for i in range(5):
    for j in range(3):
        print(f'i = {i} and j = {j}')


# CONCLUSION
'''
- Conclusion -> Loops are powerful constructs in Python that allow you to execute a block of code multiple times. By understanding,
                and using for loop and while loops, along with loop control statements like break, continue and pass; you can handle
                a wide range of programming tasks efficiently.
'''