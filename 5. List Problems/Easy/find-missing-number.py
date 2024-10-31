from typing import List


def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    required_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    missing_num = required_sum - actual_sum
    return missing_num
