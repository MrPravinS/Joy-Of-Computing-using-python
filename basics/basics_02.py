# data types in python

# User Input

#  input()

# name = input("Whatr is your name")
# age = int(input("How old are you"))
# todayBirthday = True

# if todayBirthday:
#     print(f"Hello{name}\nYou are {age} old")
#     print("Happy Birthday")
 
# Area of Rectangle  

"""length = float(input("Enter the length"))
width = float(input("Enter the width"))
area = length * width
print(f"The area is: {area}cm")"""


# Shopping Cart Programm

"""item = input("Whta item would you like to buy: ")
price = float(input(f"What is the price of this {item}: "))

quantity = int(input("How many would you like: "))
total = price * quantity

print(f"The Item you buy {quantity} x {item}")
print(f"Total price is ${total}")"""

# Madlibs game
# word game where you create a story 
# by filling in blanks with random workds

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")

adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing'")
adjective3 = input("Enter an adjective (description): ")


print(f"Today i went to a {adjective1} zoo.")
print(f"In an exhibit, i saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}")
