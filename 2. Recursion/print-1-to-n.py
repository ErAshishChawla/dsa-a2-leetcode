def printN(N):
    if N == 0:
        return
    printN(N - 1)
    print(N)


def printN2(i, N):
    if i > N:
        return
    print(i)
    printN2(i + 1, N)


printN(5)
