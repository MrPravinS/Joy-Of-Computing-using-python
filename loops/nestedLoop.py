# nested loop
rows = int(input("Enter the rows : "))
columns = int(input("Enter the columns : "))
symbols = input("Enter the symbols : ")
for x in range(rows):
    for y in range(columns):
        print(symbols,end="")
    print()