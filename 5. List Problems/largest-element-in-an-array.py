from typing import List


def largest(self, arr: List[int]) -> int:
    # code here
    largest = float("-inf")

    for i in arr:
        if largest < i:
            largest = i

    return largest
