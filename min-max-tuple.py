"""
Question: Remove duplicates from a list and create a tuple and find the minimum and maximum number
Given: sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
"""

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

print("Original list", sample_list)
print()

sample_list = list(set(sample_list))    # set(sample_list)- removes all duplicate values because sets only store unique elements
print("unique list", sample_list)       # Prints the list without duplicates

#converting list to a tuple
t = tuple(sample_list)
print("tuple ", t)

print("Minimum number is: ", min(t))
print("Maximum number is: ", max(t))