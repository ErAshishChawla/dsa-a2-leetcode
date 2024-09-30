def printN(i: int, n: int):
    if i > n:
        return
    print("Ashish")
    printN(i + 1, n)


printN(1, 5)
