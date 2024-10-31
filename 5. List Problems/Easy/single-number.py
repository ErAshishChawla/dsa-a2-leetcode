from typing import List


def singleNumber(nums: List[int]) -> int:
    res = 0
    for v in nums:
        res = res ^ v
    return res
