for i in range(7):
    for j in range(4-i-1):
        print(" ", end="")
    for j in range(i+1):
        print(" ","*", end="")
    for j in range(5-i-2):
        print(" ", end="")
    print()
    