x = 10
print(id(x))
print(x)
x = x + 2
print(id(x))
print(x)

# mutable 
myList = [1,2,3]
print(id(myList))
print(myList)
myList.append(4)
print(id(myList))
print(myList)

myTuple = (1,3,4,5,[1,2])
myTuple = (4,5,6,7,8)
print(myTuple)

def modifyFun(n):
   return n + 3
 


# x = 11
print("Before",(5))
modifyFun(5)
print("After", (5))


def mutableObj(lst):
    lst.append(6)
    return lst

myList = [1,2,3,4]
print("Before",myList)
mutableObj(myList)
print("After",myList)
