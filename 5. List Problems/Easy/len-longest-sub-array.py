from typing import List


def lenOfLongestSubArray(arr: List[int], k: int):
    # Brute force approach
    max_len = 0
    for i in range(0, len(arr) - 1):
        total = 0
        total_len = 0
        for j in range(i, len(arr)):
            total += arr[j]
            total_len += 1
            if total == k:
                max_len = max(max_len, total_len)
                break
            elif total > k:
                break
    return max_len


arr = [10, 5, 2, 7, 1, 9]
k = 15
print(lenOfLongestSubArray(arr, k))
