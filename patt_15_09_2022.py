n = int(input("print a digit how many times you want that pattern :"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
    