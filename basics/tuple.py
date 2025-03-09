# Tuples in python
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable, allow duplicate values.

# thisTupel = ("Pravin","Ajay","Vijay","Pravin")
# print(len (thisTupel))

# One item tuple, remember the comma:

# myTuple = ("pravin")
# print( type (myTuple))  # data type = <class str>

# myTuple = ("pravin",)   # give (,) for one item
# print( type (myTuple))  # data type = <class tuple>

tuples = ("aj",1,True,5)
# print(tuples[-2])
# tuples[2] = "AJay"   => gives error bcs tuple is immutable
# for i in range(len(tuples)):
#     print(tuples[i])


#  Tuple Methods 
# count(): Counts occurrences.
# numbers = (1,2,3,4,5,2,3,4,4)
# print(numbers.count(1))


# index(): Finds first occurrence.
# print(numbers.index(3))


# students = [("Alex",87),("Bob",23),("cathy",60)]

# for student in students:
#     name,grade = student   # destructure
#     if grade > 80:
#         print(f"{name} scored: {grade}")


# Assignment: Tuple Practice
# Objective
# You’ll write a program using tuples to manage a small "inventory system" for a store. It’ll involve creating tuples, looping through them, unpacking, and doing some basic logic—all stuff we’ve touched on.

inventory = [
    ("apple",0.50,10),
    ("banana",0.75,8),
    ("orange",1.25,5),
    ("mango",1.50,3)
    ]

def show_inventory(items):
    # Your code here
    for fruit in inventory:
        print(fruit)

def total_value(items):
    # Your code here
    sum = 0
    for item in items:
       fruit,price,qty  = item
       sum += price * qty
    return sum
        

def expensive_items(items):
    # Your code here\

     expensive = []
     for fruit,price,qty in inventory:
         if price > 1.00:
            expensive.append(fruit)
     return expensive

def restock(item, amount):
    # Your code here
    name,price,qty = item
    return (name,price,qty + amount)

show_inventory(inventory)
print(f"Total inventory value: ${total_value(inventory):.2f}")
print(f"Expensive items: {expensive_items(inventory)}")
new_item = restock(inventory[0], 5)
print(f"Restocked apple: {new_item}")