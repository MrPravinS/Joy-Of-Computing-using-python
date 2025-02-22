# magic square problem
#sum of every row, column and diagonal is the same

def magic_Square(n):

    magicSqaure = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicSqaure.append(l)

    for i in range(n):
        for j in range(n):
            print(magicSqaure[i][j], end=" ")
        print()
magic_Square(3)