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

def calaculator(num1,num2, operator):
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
calaculator(16,3,"%")  # modulo operator for remainder