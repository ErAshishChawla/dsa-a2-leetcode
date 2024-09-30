def checkPalindrome(s: int, e: int, msg: str) -> bool:
    if e < 0 or e >= len(msg):
        raise ("Invalid Input")

    if s < 0 or s >= len(msg):
        raise ("Invalid Input")

    if s >= e:
        return True
    if msg[s] != msg[e]:
        return False
    return True and checkPalindrome(s + 1, e - 1, msg)


msg1 = "racecar"
msg2 = "hello"
print(checkPalindrome(0, len(msg1) - 1, msg1))
print(checkPalindrome(0, len(msg2) - 1, msg2))
