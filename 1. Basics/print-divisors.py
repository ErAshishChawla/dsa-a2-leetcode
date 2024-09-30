import math

def printDivisors1(n) :
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end = " ")

def printDivisors2(n):
    factors = []
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if n%i == 0:
            factors.append(i)
            other_half = n // i
            if other_half != i:
                factors.append(other_half)
    return factors
        

printDivisors1(10)
print(printDivisors2(10))