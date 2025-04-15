"""
write a program that calculates the average student height from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
The average height can be calculated by adding all the heights together and dividing by the total number of heights.
e.g. 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
There are a total of 7 heights in student_heights
1146 ÷ 7 = 163.71428571428572
Average height rounded to the nearest whole number = 164
Important You should not use the sum() or len() functions in your answer.
"""

# Student Height Average Calculator without using sum() or len()

# Step 1: Prompt the user to enter the heights
print("Enter the student heights separated by spaces (e.g. 180 124 165 173 189 169 146):")

# Step 2: Take input from user and split it into a list
student_heights = input().split()

# Step 3: Convert all string elements to integers
for i in range(len(student_heights)):
    student_heights[i] = int(student_heights[i])

# Step 4: Initialize counters for total height and number of students
total_height = 0
total_students = 0

# Step 5: Manually loop through the list to calculate totals
for height in student_heights:
    total_height += height
    total_students += 1

# Step 6: Calculate average height (rounded to nearest whole number)
average_height = round(total_height / total_students)

# Step 7: Print the results
print(f"\nTotal height of all students: {total_height}")
print(f"Total number of students: {total_students}")
print(f"Average height (rounded): {average_height}")
