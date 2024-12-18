from typing import List


def rearrangeBySign(arr: List[int]):
    n = len(arr)
    res = [0] * n

    next_neg = 1
    next_pos = 0

    for i in arr:
        if i < 0:
            res[next_neg] = i
            next_neg += 2
        else:
            res[next_pos] = i
            next_pos += 2

    return res
