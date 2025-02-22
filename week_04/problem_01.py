def magic_Square(n):
    # Create a 2D list initialized with 0
    magicSquare = [[0] * n for _ in range(n)]

    i, j = n // 2, n - 1  # Start position
    num = n * n  # Total numbers to place
    count = 1

    while count <= num:
        if i == -1 and j == n:  # Case when both row & column overflow
            j = n - 2
            i = 0
        else:
            if j == n:  # Column exceeds limit
                j = 0
            if i < 0:  # Row exceeds limit
                i = n - 1

        if magicSquare[i][j] != 0:  # If cell is already filled
            j -= 2
            i += 1
            continue
        else:
            magicSquare[i][j] = count
            count += 1

        i -= 1  # Move up
        j += 1  # Move right

    # Printing the magic square
    for row in magicSquare:
        print(" ".join(str(x).rjust(2) for x in row))

    print("The sum of each row/column/diagonal is:", int(n * (n**2 + 1) / 2))

# Example usage
magic_Square(3)
