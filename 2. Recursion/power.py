def power(b: int, e: int) -> int:
    if e < 0:
        raise ("Invalid Input")

    if e == 0:
        return 1

    return b * power(b, e - 1)


print(power(2, 3))
