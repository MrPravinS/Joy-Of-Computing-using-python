# conditional => A one line shortcut for the if-elsestatement (terneryu operator)

# x if condition else y

num = 50

# # print("Positive" if num  > 0 else "Negative")

# result = "Even" if num % 2 == 0 else "Odd"
# print(result)

# a = 4
# b = 10

# maxValue = a if a > b else b
# minValue = a if a < b else b
# print(minValue)
# print(maxValue)

"""x = 15
result = "high" if x > 10 else "low" 
print(result)"""

"""x = 7
y = 12
result = "x is greater" if x > y else "y is greater" if y > x else x and y are equal"
print(result) """

# Write a ternary operator to check if a number is divisible by both 2 and 3. If it is, print "Divisible by 6"; otherwise, print "Not divisible by 6".

"""number = float(input("Enter any number"))

result = "Divisible by 6 " if number % 2 == 0 and number % 3 == 0 else "Not Divisible by 6"
print(result)"""

# Real-World Scenarios
# Discount Calculator
# Use the ternary operator to calculate the discount for a product:

# If the price is greater than 100, apply a 10% discount.

# Otherwise, apply a 5% discount.

price = float(input("Price of the product"))

discountsForTen = (10 / 100) * price
disCountForFive = (5/100) * price

discount = discountsForTen if price > 100 else disCountForFive
print(discount)