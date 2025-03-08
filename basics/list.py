# Learning list in python and there methods
# Lists are used to store multiple items in a single variable.
# lists are defined as objects with the data type 'list':
# List is a collection which is ordered and changeable. Allows duplicate members.
# <class 'list'>

# myList = list(("Pravin",23,23,"Shegamwar","Ajay"))
# print((myList))

# if "Pravin" in myList:
#     print("Yes")
# else :
#     print("No")
# 


# Create a list: Write a Python program to create a list of 10 integers and print it.

# Sum of elements: Write a program to calculate the sum of all elements in a list.

newList = list([1,2,3,4,5,6,7,8,9])
# print(len(newList))
# newList[len(newList) - 1] = 3
# newList[1:3] = [10,30]

extendItem = [0,9,7,5]
#  add an item to the end of the list, use the append() method:
newList.append(30)
newList.insert(0,10)
newList.insert(1,20)
newList.extend(extendItem)  # merg list
# print(newList)
sum = 0 
# if 0 in newList :
    
# for i in range(len(newList)):
#     # print(newList[i])
#     sum += newList[i]
#     print(sum)


# list2 = [0,1,2,3,4,5]
# # print(list2[::2])  # step of 2 print index of 2 no. ex 2,4 etc

# list2.pop(2)  # remove elemnt at specific index if ther is no index remove last element

# # del delete specific index or entire list

# del list2[2]

# # clear()  empty the list  => []
# list2.clear()
# print(list2)



# numbers = [1,2,3,4,5,5,6,7,8,9, 10]
# # print(f'List : {numbers}')

# fruits = ["apple", "banana", "cherry", "mango", "orange"]

# print(fruits[0])
# print(fruits[1])
# print(fruits[-1])

# nums = [10,20,30,40]
# nums[2] = 25
# nums[1] = 15
# nums.append(60)
# print(nums)

# Remove Elements

# items = ["pen", "pencil", "eraser", "sharpener", "ruler"]

# # items.remove("eraser")
# # items.pop()
# del items[1]
# print(items)

# Check Membership
# Write a program to check if "grape" is in the list below:

# fruits = ["apple", "banana", "cherry", "mango", "orange"]

# print( "grape" in fruits)


import random
number = random.randint(1,10)
guess = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 10"))
    if guess == number:
        print("You got it")
    else:
        print("Nope , try again")