"""
Question: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
Given:
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
"""

first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", first_set)           #printing bith the sets to see what's inside them
print("Second Set ", second_set)
print()                                  #to add a break in line

print("First set is subset of second set -", first_set.issubset(second_set))  #This checks if all items in first set are also in second set
print("Second set is subset of First set -", second_set.issubset(first_set)) #This checks the reverse are all items in second set also in first set?
print()

print("First set is Super set of second set - ", first_set.issuperset(second_set))
print("Second set is Super set of First set - ", second_set.issuperset(first_set))
print()

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("First Set ", first_set)
print("Second Set ", second_set)