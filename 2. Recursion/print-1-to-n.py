# Backtracking without index variable
def printN(N):
    if N == 0:
        return
    printN(N - 1)
    print(N)


# With the help of a index variable
def printN2(i, N):
    if i > N:
        return
    print(i)
    printN2(i + 1, N)


# Backtracking with index variable
def printN3(i, N):
    if i < 1:
        return
    printN3(i - 1, N)
    print(i)


printN(5)
print()
printN2(1, 5)
print()
printN3(5, 5)
