# Parameterized Recursion
def sum1(n: int, sum: int):
    if n < 1:
        print(sum)
        return
    sum1(n - 1, sum + n)


# Functional Recursion:
def sum2(n: int):
    # Handles the -ve and 0 case
    if n < 0:
        raise ("Invalid Input")

    # Base Case
    if n == 0:
        return 0

    return n + sum2(n - 1)


# # Backtracking:
def sum3(i: int, n: int, sum: int):
    if i > n:
        return sum
    return sum3(i + 1, n, sum + i)


sum1(5, 0)
print(sum2(5))
# print(sum2(-10))
print(sum3(1, 5, 0))

print(sum2(995))
