"""
Euclid algo

1. Calculate remainder of a/b
2. If remainder is 0, return b
3. Else, continue dividing b/remainder until remainder is 0
"""


def gcd(a, b):
    remainder = a % b
    if remainder == 0:
        return b
    return gcd(b, remainder)


print(gcd(5, 10))
