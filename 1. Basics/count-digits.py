import math

def countDigits1(n:int) -> int:
    # Bruteforce Approach
    return len(str(n))

def countDigits2(n:int) -> int:
    # Brute Force Approach
    c = 0
    num = n
    while num > 0:
        c +=1
        num = num // 10

    return c

def countDigits3(n:int) -> int:
    # Optimized Approach
    if n ==0 or n ==1:
        return 1
    return int(math.floor(math.log10(n))+1)

print(countDigits1(12345))
print(countDigits2(12345))
print(countDigits3(12345))
print(countDigits3(1))
