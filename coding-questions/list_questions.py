'''
(Q)- Create a To Do List to keep tracks of the tasks
'''
to_do_list = ["Buy groceries", 'Clean the house', 'Pay bills']

# Adding to the task
to_do_list.append("Schedule meeting")
to_do_list.append("Go for a run")

# Remove the particular task
to_do_list.remove('Clean the house')

# Checking the task in the list
if "Pay bills" in to_do_list:
    print("Don't forget to pay the utility bills")

print("To do list remiaining")
for task in to_do_list:
    print(f"- {task}")


'''
(Q)- Organizing the student grades
- Create a list to store and calculate average grades for students
'''
# Organizing the student grades
grades = [85, 92, 78, 90, 88]

# Adding a new grade
grades.append(95)

# Calculating the average grade
average_grade = sum(grades) / len(grades)
print(f"Average Grade : {average_grade:.2f}")

# Finding the highest and lowest grades
highest_grades = max(grades)
lowest_grades = min(grades)
print(f"Highest Grade: {highest_grades}")
print(f"Lowest Grade: {lowest_grades}")


'''
(Q)- Managing an inventory
- Use a list to manage inventory items in a store
'''
# Managing an inventory
inventory = ["apple", "banana", "orange", "grapes"]

# Adding a new item in an inventory
inventory.append('strawberries')

# Removing an item that is out of stock
inventory.remove('banana')

# Checking if an item is in stock
item = "oranges"
if item in inventory:
    print(f"{item} are in stock.")
else:
    print(f"{item} are out of stock.")

# Printing the inventory
print("Inventory List")
for item in inventory:
    print(f"- {item}")


'''
(Q)- Collecting user feedback
- Use a list to collect and analyze user feedback.
'''

# Collecting user feedback
feedback = ["Great service!", "Very Satisfied", "Could be better", "Excellent experience"]

# Adding new feedback
feedback.append("Not happy with the service")

# Counting specific feedback
positive_feedback_count = sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower() or "satisfied" in comment.lower())
print(f"Feedback Count - {positive_feedback_count}")

print("User Feedback:")
for comment in feedback:
    print(f"- {comment}")