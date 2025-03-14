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

"""price = float(input("Price of the product"))

discountsForTen = (10 / 100) * price
disCountForFive = (5/100) * price

discount = discountsForTen if price > 100 else disCountForFive
print(discount)"""

# User Role Assigner
# Write a program that assigns a user role based on their age:
# If the age is less than 18, assign "Minor".
# If the age is between 18 and 65, assign "Adult".
# If the age is greater than 65, assign "Senior".
"""
age = int(input("Enter Your Age"))

roleAssign = "Minor" if age < 18 else "Adult" if age >= 18 and age <= 65 else "Senior"

print(roleAssign)
"""

# Password Strength Checker
# Use the ternary operator to check the strength of a password:
# If the password length is greater than 8, print "Strong".
# Otherwise, print "Weak".

"""password = input("Enter your Password")

strengthCheaker = "Strong" if len(password) >= 8 else "Weak"
print(strengthCheaker)"""


# Temperature Checker
# Write a program that uses the ternary operator to check the temperature:
# If the temperature is greater than 30, print "Hot".
# If the temperature is between 20 and 30, print "Warm".
# Otherwise, print "Cold".

"""temperature = float(input("Enter temperature"))

checkTemp = "Hot" if temperature > 30 else "Warm" if temperature >= 20 and temperature <= 30 else "Cold"

print(checkTemp)"""


# Ternary in a Loop
# Write a loop that iterates through a list of numbers and uses the ternary operator to print "Even" or "Odd" for each number.

"""newList = (10,2,3,4,8,6)

for i in newList:
    # print(i)
     evenOdd = "even" if i % 2 == 0 else "Odd"
     print(evenOdd)"""