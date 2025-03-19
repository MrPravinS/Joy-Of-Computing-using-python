#print("Hi! How are you ?")

# for i in range(5):
#     print("Hey Pravin !",i)

#for i in range(11):
#    print(i ,"* 2 =", i * 2 )

# sum = 0
# for i in range(6):
#     # if(i % 2 == 0):
#        sum += i
#        print("First",i,"numbers, When added, gives",sum)

# num = int(input("enter any number for multiplication table"))
# for i in range(11):
#     print(num,"*", i,"=", i * num)

# print("Hello Everyone, we are starting")

"""n = 1
c = 1
while(c == 1):
    print("Token number",n,"my please come in")
    c = int(input("continue?(0/1)"))
    n = n + 1
print("Thank you, this is the end of our day")
"""

# Basic Syntax

# for item in sequence:
#     # Code block (indented)
#     print(item)


# words = "pravin"
# arr = []
# for word in words:
#     print(word)
#     arr.append(word)
# print("-".join(arr))

# range(start,end)

# range(start, stop, step):

"""for i in range(0,10,2):
    print(i)
"""
"""fruits = ["apple", "banana", "cherry"]
for fruit in enumerate(fruits):
    print(fruit)"""

# Assignment: For Loop Practice

# Tasks
# Print Multiples:
# Use a for loop with range() to print multiples of 5 from 5 to 50.
# Example: 5 10 15 20 25 30 35 40 45 50

"""for i in range(11):
    print(f"5 x {i} = {i * 5}")"""

# Reverse String:
# Take a user-input string and print it reversed using a for loop over its characters.
# Example: Input "hello" → Output "olleh"


# my_list = [0, 1, 2, 3, 4]
# for i in range(len(my_list) - 1, -1, -1):  use to reversed string
#     print(my_list[i])


"""string = input("Enter any string")
reversedStr = []
for i in reversed (string):
    # print(reversedStr + i)
     reversedStr.append(i)
print("".join(reversedStr))"""



# Given a list of numbers (e.g., [1, 2, 3, 4, 5]), use a for loop to calculate and print their sum.
# Example: Output 15

"""sum = 0
for num in range(51):
    sum += num
print(sum)"""

# Count the number of vowels in a given string.
vowels = ["a","e","i","o","u"]

count = 0
# strs = input("Enter Any String")
# for word in strs:
#     # if word.find(vowels):
#        count+=1  
#     print(word)\


def removeDuplicates(nums):
        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k+=1
                print(nums[k])

        return k
print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))