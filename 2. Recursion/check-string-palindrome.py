def checkPalindrome(msg: str, s: int = 0) -> bool:
    e = len(msg) - s - 1
    if s >= e:
        return True
    if msg[s] != msg[e]:
        return False
    return True and checkPalindrome(msg, s + 1)


msg1 = "racecar"
msg2 = "hello"
print(checkPalindrome(msg1))
print(checkPalindrome(msg2))
