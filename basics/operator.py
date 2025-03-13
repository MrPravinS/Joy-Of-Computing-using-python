#  Addition a + b

# num1 = 25
# num2 = 20
# # num3 = num1 + num2
# # print(num3)
 

# # Subtraction

# a = num1 - num2
# print(a)

# # multilication

# c = num1 * num2
# print(c)

# # division

# d = num1 / num2
# print(d)


# # remainder  => gives remainder

# e = num1 % num2
# print(e)



#  simple calculator

"""def calaculator(num1,num2, operator):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print(num1 % num2)

calaculator(2,3,"+")   # addition
calaculator(5,3,"-")   # sub
calaculator(2,3,"*")   # multiplication
calaculator(15,3,"/")  # division
calaculator(16,3,"%")  """# modulo operator for remainder


x = 3

# result = round(x)   #=> gives rounded value near the integer like 3.14 => 3 and 3.89 => 4

# result = abs(x)  # return the absolute value of the integer
# result = pow(3,2)  # return the exponential value value like sqaure cube based given args
# result = max(3,6.0,6) # return maximum value based on args
# result = max(1.1,1.10)

# import math
# result = math.pi
# result = math.e

# result = math.sqrt(4)  gives square root
x = 12.99
# result = math.ceil(x)   number always rounded greater number

# result = math.floor(x)  => return always lower number
# print(result)

# cicumference of the circle  => formula = 2pir
import math
# def circumferenceOfCircle(r):
#     return 2 * math.pi * r
# print(circumferenceOfCircle(3))

# radius = float(input("Enter the radius of the circle"))

# circumference = 2 * math.pi * radius

# print(f"Cicumference of the circle is {round(circumference,2)}")

# areaOfCircle = math.pi * pow(radius,2)

# print(f"The Area of the circle is {round(areaOfCircle,2)}cm")

# hypotaneous of the triangle

a = float(input("Enter Side A: "))
b = float(input('Enter Side B: '))

c = math.sqrt(pow(a,2)+pow(b,2))

print(f"Side C is: {round(c,2)}")