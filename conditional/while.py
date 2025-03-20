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

"""budget = float(input("Enter your Budget"))
print(f"Budget: {budget:2,}")"""

"""i = 1
while i <= 5:
    print("Hello")
    if i == 2:
        break
    i+=1
print("end")"""

"""i = 1
while i <= 5:
    if i == 2:
        continue
    i+=1
    print(f"hello {i}")
print("end")"""


# Compound Interest Calculator

"""
A=Px(1+r/n) ^ n * t


Where:
A = Final Amount (Total amount after interest)
P = Principal (Initial amount)
r = Annual interest rate (in decimal, e.g., 10% = 0.10)
n = Number of times interest is compounded per year
t = Time in years"""

# Compound Interest (CI) = A - P



# make a shopping cart

# foods = []
# prices = []
# total = 0

# while True:
#     food = input("Buy Food (q for quit): ")
#     if food == "q":
#         break
#     else:
#         price = float(input("Enter price of specific food: "))
#         foods.append(food)
#         prices.append(price)

# print("---------Your Cart-------")
# for food in foods:
#     print (f"{food}",end=" ")


# for money in prices:
#     total += money
# print(f"Total price is : ${total}")

def moveZeros(nums):
    count = 0
    for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count+=1
    while count < len(nums):
            nums[count] = 0
            count+=1
    return nums
nums = [1,2,0,4,3,0,5,0]
print(moveZeros(nums))