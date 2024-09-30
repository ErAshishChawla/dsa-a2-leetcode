# Brute Force
def lcm1(a: int, b: int) -> int:
    greater = max(a, b)
    smaller = min(a, b)

    for i in range(greater, greater * smaller + 1):
        if i % greater == 0 and i % smaller == 0:
            return i


def gcd(a: int, b: int) -> int:
    remainder = a % b
    if remainder == 0:
        return b
    return gcd(b, remainder)


# Optimal
def lcm2(a: int, b: int) -> int:
    return a * b // gcd(a, b)


print(lcm1(5, 10))
print(lcm2(5, 10))
