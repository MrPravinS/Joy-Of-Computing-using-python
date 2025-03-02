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
# o add an item to the end of the list, use the append() method:
newList.append(30)
newList.insert(0,10)
newList.insert(1,20)
newList.extend(extendItem)
print(newList)
sum = 0 
# if 0 in newList :
    
# for i in range(len(newList)):
#     # print(newList[i])
#     sum += newList[i]
#     print(sum)
