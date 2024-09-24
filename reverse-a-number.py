import math

def reverseNumber1(n:int) -> int:
    return int(str(n)[::-1]) 
    # TC: O(N), SC: O(1)

def reverseNumber2(n:int) -> int:
    rev = 0
    num = n
    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10
    return rev

print(reverseNumber1(12345))
print(reverseNumber2(12345))



