# Function in python
#  use 4 spaces per indentation level
# declaration 
# def funName(parameter):
   #code
# funcName(args) ,fun call
'''
def squareOfNumber(n):
    return n ** 2 

result = squareOfNumber(3)
print(result)
'''

'''
Write a func that takews mutipl;e parameters and return their sum
'''

# def sumOfTwoNumbers(num1,num2):
#     return num1 + num2

# ans = sumOfTwoNumbers(2,3)
# print(ans)

# polymorphism in python 
#  takes number as well as string and multipy with another number

# def multiply(a,b):
#     return a * b

# print(multiply(2,2))
# print(multiply(5,"a"))
# print(multiply("b",2))

# create a fun that returns both area and circumference of the circle given its radius

# import math
# def areaAndCircumference(radius):
#     areaOfCircle = round(math.pi * (radius ** 2),2)
#     cicumferenceOfCircle = round(2 * math.pi* radius,2)
#     return areaOfCircle, cicumferenceOfCircle
# a, c = areaAndCircumference(2)

# print("Area: ",a,"Cicumference: ", c)
# print(areaAndCircumference(2))


# default parameter

# def defualtPara(name="Pravin"):
#      return "Hello, "+name+" !"
# print(defualtPara())


#  lambda function
#  varName = lambda varName : code

# cube = lambda x : x ** 3
# print(cube(2))

#  *args  => take multiple args and perform task and create a tuple = (args)

# def sumAll(*args):
#     # print(args)
#     for i in args:
#         print(i * 3)
#     return sum(args)
# print(sumAll(2,3,4))

# **kwargs
# def keyValuePair(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")
# keyValuePair(name="pravin",age=23)
# keyValuePair(name="ajay",age=22)



# def varName(**kwargs):
#         for key, value in kwargs.items():
#                 print(f"{key}: {value}")
# varName(name="pravin",age=133)


# def keyValue(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")
# keyValue(age=133,lastname="shegamwar")

def factorial(n):
    if n == 0 :
        return 1
    else:

        return n * factorial(n - 1)
print(factorial(3))
print(factorial(4))
print(factorial(5))