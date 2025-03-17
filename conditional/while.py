# while loop = execute some code while some condition remains true
# Syntax: f"string {value:format}"

# .nf:Float with n decimal places (e.g., .2f for 2).
"""pi = 3.14445556
print(f"value of pi : {pi:.2f}") """


""""num = 42
print(f"Width: {num:5d}")     # "Width:    42" (spaces)
print(f"Zero-pad: {num:05d}") # "Zero-pad: 00042"
print(f"Left: {num:<5d}")     # "Left: 42   "
print(f"Center: {num:^5d}")   # "Center:  42 "
print(f"Hex: {num:x}")        # "Hex: 2a"
print(f"Big: {1234:,d}")      # "Big: 1,234"""""


# name = input("Enter your name")
# age = int(input("Enter your age"))
# print(f"Name: {name:>15s} and {age:<15d}")

# Price List:
# Given a list of tuples (item, price) (e.g., [("apple", 0.5), ("cake", 12.99)]), print each item:
# Item name right-aligned in a 10-character field.
# Price with 2 decimal places and a $ prefix.

"""itemList = [("apple", 0.5), ("cake", 12.99)]

for item,price in itemList:
 
   print(f"Item: {item:>10} Price: {price:.2f}")"""


# Number Converter:
# Take a number as input and print it in:
# Decimal (padded to 5 digits with zeros).
# Hexadecimal (lowercase).
# Binary.
# Example: Input 42 → Number: 00042, Hex: 2a, Binary: 101010

"""number = int(input("Enter any number"))
print(f"Decimal Padded : {number:05d}")
print(f"Decimal Padded : {number:x}")
print(f"Decimal Padded : {number:b}")
"""

# Temperature Report:
# Given a float temperature (e.g., 23.456), print it centered in a 10-character field with 1 decimal place.
# Example: "Temp: 23.5 "
"""
temp = float(input("Enter temperatur"))
print(f"Temp : {temp:^.1f}")"""

# Bonus: Budget Tracker:
# Take a total budget (e.g., 12345.67) and print it with thousand separators and 2 decimal places.
# Example: "Budget: $12,345.67"

budget = float(input("Enter your Budget"))
print(f"Budget: {budget:2,}")