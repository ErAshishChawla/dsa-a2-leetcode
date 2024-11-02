from typing import List


def twoSum(arr: List[int], target: int) -> List[int]:
    nums_map = {}
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in nums_map:
            return [i, nums_map[complement]]
        nums_map[arr[i]] = i
