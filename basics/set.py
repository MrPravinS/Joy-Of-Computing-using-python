# Build an unordered collection of unique elements
# Elements can be of any immutable type (numbers, strings, tuples, etc.).

# 🔸 Key Properties of Sets
# Unordered: No index, no order.
# No duplicates.
# Supports set operations like union, intersection, etc.

"""set = set({4,5,6})
print(set)

my_set = {1,2,3,2}  #print only {1,2,3}
print(my_set)"""

# 📝 Assignments on Sets
# Beginner Level:
# Create a set with elements 1 to 5 and add the number 6.

"""newSet = {1,2,3,4,5}
newSet.add(6)
print(newSet)
"""
# 2 Try adding a duplicate item to a set and print it.

"""my_set = {1,2,3,2}  #print only {1,2,3}
print(my_set)"""


# 3. Remove an item using discard() and remove().

"""newSet = {1,2,3,4,5}
newSet.remove(2)  # remove 2
newSet.discard(3)  # remove 3
print(newSet)"""

# Intermediate Level:
# 4. Create two sets and perform all four operations: union, intersection, difference, symmetric difference.
#5. Count the number of unique words in a sentence using a set.

"""set1 = {1,2,3,4,5}
set2 = {2,3,5,6,7}

print(set1 | set2) # union => combine two sets
print(set1 & set2) # intersection => common element
print(set1 - set2) # differenced => in set1 but not in set2

print(set1 ^ set2)""" #symmetric difference.Elements in A or B, not both

"""name = {"I","know " ,"him","him"}
print(len(name))
# print(name.pop())  # remove random item
print(name.copy())  # Returns a copy of the set
name.clear()   # remove all items
print(name)"""

# Advanced Level:
# Write a program to find common elements in two lists using sets.

set1 = {1,2,3,4,5}
set2 = {2,3,5,6,7}

for i in set1:
    for j in set2:
        if i == j:
            print(f"Comman element in both: {i} ")
        