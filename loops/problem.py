# Counting Positive Numbers
# problem: Given a List of numbers, count how many are positives

# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
 
# count = 0
# for num in numbers:
#     if num > 0:
#         count += 1
# print(count)

# temperature = 10
# if temperature > 28:
#   print("Its Warm")
#   print("Drink water")
# elif temperature < 25 :
#     print("Its cold")
# else:
#     print("Dont go outside")

# ternary operator

# number = 20
# message = "Number > 10" if number > 10 else " number < 10"
# print(message)


# logical operator
 
#  And , OR , Not

# Write a Python program that checks 
# if a number is both greater than 10 and even.

# num = int(input("Enter a number"))
# if num >= 10 and (num % 2 == 0):
#     # print(num,"Number is Greater than and also a even number")
#     print(True)
# else:
#     # print(num,"Not greater than 10 and not even")
#     print(False)

# Write a Python program that checks 
# if a number is either divisible by 3 or 5.

# number = int(input("Enter a number"))

# if number % 3 == 0 or number % 5 == 0:
#     print(True)
# else :
#     print(False)


# userName = "pravin"
# if userName == "admin":
#     print(False)
# else:
#     print(True)

# Write a Python program that checks 
# if a number is between 1 and 100 (inclusive) 
# OR is a multiple of 10.


# number = 102
# if (number >= 1 and number <= 100) or number % 10 == 0:
#     print(True)
# else:
#     print(False)

# userName = "admin 1"
# password = "password123"

# if userName == "admin" and password == "password123":
#     print(True)
# else:
#     print(False)

# year = 2003
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(True)
# else:
#     print(False)

#  chaining comparision operator

# age = 17

# # if age >= 18 and age < 65:
# if 18 <= age < 65:
#     print("Eligible")
# else:
#     print("Not elgible")

if 10 == "10":   # check data type
    print(a)
elif "bag" > "apple" and "bag" > "cat":  # check unicode value b = 98 a = 97 c = 99
    print("b")
else:
    print("C")