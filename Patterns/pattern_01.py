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