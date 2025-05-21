# print pattern like =
# * * * *
# * * * * 
# * * * *
# * * * *

def pattern(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()
pattern(4)


# def pattern01(n):
#     row = "* " * n
#     for _ in range(n):
#         print(row)

# pattern01(5)